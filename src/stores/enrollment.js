import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { useAuthStore } from './auth.js';
import { useToastStore } from './toast.js';

export const useEnrollmentStore = defineStore('enrollment', () => {
    const authStore = useAuthStore();
    const toastStore = useToastStore();

    const isLoading = ref(false);
    const isSubmitting = ref(false);
    const auditData = ref(null);
    const selectedCourseIds = ref([]);
    const registrationSlip = ref(null);
    const activeTab = ref('registration'); // 'registration' | 'slip' | 'history'

    const student = computed(() => auditData.value?.student || null);
    const session = computed(() => auditData.value?.session || '2026/2027');
    const semester = computed(() => auditData.value?.semester || 'First Semester');
    const hasMandatoryCarryovers = computed(() => auditData.value?.hasMandatoryCarryovers || false);
    const mandatoryCarryovers = computed(() => auditData.value?.mandatoryCarryovers || []);
    const availableCourses = computed(() => auditData.value?.availableCourses || []);
    const currentEnrollments = computed(() => auditData.value?.currentEnrollments || []);
    const creditPolicy = computed(() => auditData.value?.creditPolicy || { minUnits: 15, maxUnits: 24, carryoverUnits: 0, advisableMaxUnits: 21 });
    const aiAdvisory = computed(() => auditData.value?.aiAdvisory || null);

    // Set of mandatory carryover course IDs
    const carryoverIdSet = computed(() => new Set(mandatoryCarryovers.value.map(c => c.id)));

    // Check if course is a locked carryover
    const isCarryoverLocked = (courseId) => {
        return carryoverIdSet.value.has(courseId);
    };

    // Dictionary of all courses by ID for quick lookup
    const allCoursesMap = computed(() => {
        const map = new Map();
        for (const c of mandatoryCarryovers.value) map.set(c.id, c);
        for (const c of availableCourses.value) map.set(c.id, c);
        return map;
    });

    // Reactive calculations
    const selectedCourses = computed(() => {
        return selectedCourseIds.value
            .map(id => allCoursesMap.value.get(id))
            .filter(Boolean);
    });

    const totalSelectedUnits = computed(() => {
        return selectedCourses.value.reduce((sum, c) => sum + (c.creditUnits || 0), 0);
    });

    const carryoverUnits = computed(() => {
        return selectedCourses.value
            .filter(c => carryoverIdSet.value.has(c.id))
            .reduce((sum, c) => sum + (c.creditUnits || 0), 0);
    });

    const regularUnits = computed(() => totalSelectedUnits.value - carryoverUnits.value);

    const isUnderload = computed(() => totalSelectedUnits.value < (creditPolicy.value?.minUnits || 15));
    const isOverload = computed(() => totalSelectedUnits.value > (creditPolicy.value?.maxUnits || 24));
    
    const allCarryoversSelected = computed(() => {
        for (const coId of carryoverIdSet.value) {
            if (!selectedCourseIds.value.includes(coId)) return false;
        }
        return true;
    });

    const canSubmit = computed(() => {
        return (
            selectedCourseIds.value.length > 0 &&
            !isUnderload.value &&
            !isOverload.value &&
            allCarryoversSelected.value &&
            !isSubmitting.value
        );
    });

    // Ensure all mandatory carryovers are always included
    const enforceCarryoverSelection = () => {
        const currentSet = new Set(selectedCourseIds.value);
        for (const coId of carryoverIdSet.value) {
            currentSet.add(coId);
        }
        selectedCourseIds.value = Array.from(currentSet);
    };

    // Toggle course selection
    const toggleCourse = (course) => {
        if (isCarryoverLocked(course.id)) {
            toastStore.warning(
                `Senate Regulation Lock: ${course.code} is a mandatory carryover from a previous level and cannot be unselected.`,
                'Mandatory Carryover Enforced'
            );
            return;
        }

        const idx = selectedCourseIds.value.indexOf(course.id);
        if (idx >= 0) {
            selectedCourseIds.value.splice(idx, 1);
        } else {
            // Check potential overload
            const nextUnits = totalSelectedUnits.value + (course.creditUnits || 0);
            if (nextUnits > (creditPolicy.value?.maxUnits || 24)) {
                toastStore.warning(
                    `Adding ${course.code} (${course.creditUnits} Units) would bring total units to ${nextUnits}, exceeding the 24-unit ceiling!`,
                    'Credit Unit Limit Exceeded'
                );
                return;
            }
            selectedCourseIds.value.push(course.id);
        }
    };

    // API: Fetch Audit
    const fetchAudit = async (studentId = null) => {
        isLoading.value = true;
        try {
            const token = authStore.token;
            const queryParams = new URLSearchParams({
                session: session.value,
                semester: semester.value
            });
            if (studentId) queryParams.append('student_id', studentId);

            const res = await fetch(`http://127.0.0.1:8000/api/v1/enrollment/audit?${queryParams.toString()}`, {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.detail || 'Failed to retrieve enrollment audit.');
            }

            const data = await res.json();
            auditData.value = data;

            // Initialize selections:
            // 1. If existing active enrollments exist, populate those
            if (data.currentEnrollments && data.currentEnrollments.length > 0) {
                selectedCourseIds.value = data.currentEnrollments.map(e => e.courseId);
            } else {
                // Otherwise populate with recommended courses
                selectedCourseIds.value = [...(data.aiAdvisory?.recommendedCourseIds || [])];
            }

            // Always enforce that mandatory carryovers are selected
            enforceCarryoverSelection();

            return data;
        } catch (err) {
            console.error('[EnrollmentStore] Audit error:', err);
            toastStore.error(err.message || 'Could not load enrollment audit.');
            throw err;
        } finally {
            isLoading.value = false;
        }
    };

    // API: Submit Registration
    const submitRegistration = async () => {
        if (!canSubmit.value) {
            if (!allCarryoversSelected.value) {
                toastStore.error('All mandatory carryover courses must be registered first!');
            } else if (isUnderload.value) {
                toastStore.warning(`Minimum allowable course load is ${creditPolicy.value?.minUnits} units.`);
            } else if (isOverload.value) {
                toastStore.error(`Maximum allowable course load is ${creditPolicy.value?.maxUnits} units.`);
            }
            return;
        }

        isSubmitting.value = true;
        try {
            const token = authStore.token;
            const res = await fetch('http://127.0.0.1:8000/api/v1/enrollment/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    session: session.value,
                    semester: semester.value,
                    courseIds: selectedCourseIds.value
                })
            });

            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.detail || 'Course registration submission failed.');
            }

            const result = await res.json();
            toastStore.success(result.message || 'Course registration completed successfully!');
            
            // Refresh audit & switch to slip view
            await fetchSlip();
            activeTab.value = 'slip';
            await fetchAudit();
            return result;
        } catch (err) {
            console.error('[EnrollmentStore] Registration error:', err);
            toastStore.error(err.message || 'Failed to complete registration.');
            throw err;
        } finally {
            isSubmitting.value = false;
        }
    };

    // API: Fetch Registration Slip
    const fetchSlip = async () => {
        try {
            const token = authStore.token;
            const res = await fetch('http://127.0.0.1:8000/api/v1/enrollment/slip', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.detail || 'Failed to fetch registration slip.');
            }

            const data = await res.json();
            registrationSlip.value = data;
            return data;
        } catch (err) {
            console.error('[EnrollmentStore] Slip fetch error:', err);
            throw err;
        }
    };

    // API: Drop Course
    const dropCourse = async (courseId) => {
        try {
            const token = authStore.token;
            const res = await fetch(`http://127.0.0.1:8000/api/v1/enrollment/drop/${courseId}`, {
                method: 'DELETE',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.detail || 'Cannot drop course.');
            }

            const data = await res.json();
            toastStore.success(data.message || 'Course dropped successfully.');
            await fetchAudit();
            await fetchSlip();
            return data;
        } catch (err) {
            console.error('[EnrollmentStore] Drop course error:', err);
            toastStore.error(err.message || 'Failed to drop course.');
            throw err;
        }
    };

    return {
        isLoading,
        isSubmitting,
        auditData,
        selectedCourseIds,
        registrationSlip,
        activeTab,
        student,
        session,
        semester,
        hasMandatoryCarryovers,
        mandatoryCarryovers,
        availableCourses,
        currentEnrollments,
        creditPolicy,
        aiAdvisory,
        selectedCourses,
        totalSelectedUnits,
        carryoverUnits,
        regularUnits,
        isUnderload,
        isOverload,
        allCarryoversSelected,
        canSubmit,
        isCarryoverLocked,
        toggleCourse,
        enforceCarryoverSelection,
        fetchAudit,
        submitRegistration,
        fetchSlip,
        dropCourse
    };
});

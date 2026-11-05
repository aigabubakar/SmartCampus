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
    const activeTab = ref('registration'); // 'registration' | 'slip'
    const allAccreditedCourses = ref([]);
    const searchQuery = ref('');
    const selectedCategoryFilter = ref('All'); // 'All' | 'Core' | 'Elective'
    const isInterDeptModalOpen = ref(false);

    // Underload Concession & Waiver State
    const underloadReason = ref('');
    const underloadNotes = ref('');

    const student = computed(() => auditData.value?.student || null);
    const session = computed(() => auditData.value?.session || '2026/2027');
    const semester = computed(() => auditData.value?.semester || 'First Semester');
    const hasMandatoryCarryovers = computed(() => auditData.value?.hasMandatoryCarryovers || false);
    const mandatoryCarryovers = computed(() => auditData.value?.mandatoryCarryovers || []);
    const availableCourses = computed(() => auditData.value?.availableCourses || []);
    const currentEnrollments = computed(() => auditData.value?.currentEnrollments || []);
    const creditPolicy = computed(() => auditData.value?.creditPolicy || { minUnits: 15, maxUnits: 24, carryoverUnits: 0, advisableMaxUnits: 21 });
    const aiAdvisory = computed(() => auditData.value?.aiAdvisory || null);

    const underloadReasonsList = computed(() => {
        return creditPolicy.value?.underloadReasons || [
            'Final Year / Graduating Clearance (Completing Remaining Degree Requirements)',
            'Academic Adviser Prescribed Workload Pacing (GPA Recovery & Counseling)',
            'Medical / Compassionate Concession (Senate Certified)',
            'Special Academic Accommodation / Approved Part-Time Load',
            'Senate Special Exemption'
        ];
    });

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
        for (const c of allAccreditedCourses.value) {
            if (!map.has(c.id)) map.set(c.id, c);
        }
        return map;
    });

    // Reactive list of currently selected courses in docket
    const selectedCourses = computed(() => {
        return selectedCourseIds.value
            .map(id => allCoursesMap.value.get(id))
            .filter(Boolean);
    });

    // Fresh courses in docket added by student (excluding mandatory carryovers)
    const freshSelectedCourses = computed(() => {
        return selectedCourses.value.filter(c => !carryoverIdSet.value.has(c.id));
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
        if (selectedCourseIds.value.length === 0 || isSubmitting.value) return false;
        if (!allCarryoversSelected.value) return false;
        if (isOverload.value) return false;
        // Underload situation requires justification reason
        if (isUnderload.value) {
            return !!underloadReason.value && underloadReason.value.trim().length > 0;
        }
        return true;
    });

    // Ensure all mandatory carryovers are always included and locked
    const enforceCarryoverSelection = () => {
        const currentSet = new Set(selectedCourseIds.value);
        for (const coId of carryoverIdSet.value) {
            currentSet.add(coId);
        }
        selectedCourseIds.value = Array.from(currentSet);
    };

    // Add a fresh course to docket
    const addCourse = (course) => {
        if (selectedCourseIds.value.includes(course.id)) {
            toastStore.info(`${course.code} is already in your registration docket.`);
            return;
        }

        const nextUnits = totalSelectedUnits.value + (course.creditUnits || 0);
        if (nextUnits > (creditPolicy.value?.maxUnits || 24)) {
            toastStore.warning(
                `Cannot add ${course.code} (${course.creditUnits} Units). Current load is ${totalSelectedUnits.value} units; adding this course would exceed the 24-unit ceiling!`,
                'Credit Limit Exceeded'
            );
            return;
        }

        selectedCourseIds.value.push(course.id);
        toastStore.success(`Added ${course.code}: ${course.title} (${course.creditUnits} Units) to docket.`);
    };

    // Remove a fresh course from docket
    const removeCourse = (courseId) => {
        if (isCarryoverLocked(courseId)) {
            toastStore.warning(
                `Senate Regulation Lock: Mandatory carryover courses cannot be removed from your docket.`,
                'Mandatory Carryover Locked'
            );
            return;
        }

        const idx = selectedCourseIds.value.indexOf(courseId);
        if (idx >= 0) {
            const course = allCoursesMap.value.get(courseId);
            selectedCourseIds.value.splice(idx, 1);
            if (course) {
                toastStore.info(`Removed ${course.code} from docket.`);
            }
        }
    };

    // Toggle course selection
    const toggleCourse = (course) => {
        if (selectedCourseIds.value.includes(course.id)) {
            removeCourse(course.id);
        } else {
            addCourse(course);
        }
    };

    // Clear only fresh courses (preserves mandatory carryovers)
    const clearFreshCourses = () => {
        selectedCourseIds.value = Array.from(carryoverIdSet.value);
        toastStore.info('Cleared fresh courses. Mandatory carryovers remain locked in docket.');
    };

    // Quick add AI recommended core courses
    const quickAddRecommendedCore = () => {
        const recommendedIds = auditData.value?.aiAdvisory?.recommendedCourseIds || [];
        let addedCount = 0;
        let currentLoad = totalSelectedUnits.value;

        for (const id of recommendedIds) {
            if (!selectedCourseIds.value.includes(id)) {
                const c = allCoursesMap.value.get(id);
                if (c && currentLoad + c.creditUnits <= 24) {
                    selectedCourseIds.value.push(id);
                    currentLoad += c.creditUnits;
                    addedCount++;
                }
            }
        }
        if (addedCount > 0) {
            toastStore.success(`Batch-added ${addedCount} recommended core modules to docket.`);
        } else {
            toastStore.info('All recommended core modules are already in your docket.');
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
            // If existing active enrollments exist in DB, load them
            if (data.currentEnrollments && data.currentEnrollments.length > 0) {
                selectedCourseIds.value = data.currentEnrollments.map(e => e.courseId);
            } else {
                // By default, start with ONLY mandatory carryovers so student can add fresh ones!
                selectedCourseIds.value = (data.mandatoryCarryovers || []).map(c => c.id);
            }

            // Always enforce that mandatory carryovers are selected
            enforceCarryoverSelection();

            // Fetch all accredited courses for search
            await fetchAllAccreditedCourses();

            return data;
        } catch (err) {
            console.error('[EnrollmentStore] Audit error:', err);
            toastStore.error(err.message || 'Could not load enrollment audit.');
            throw err;
        } finally {
            isLoading.value = false;
        }
    };

    // API: Fetch All Accredited University Courses
    const fetchAllAccreditedCourses = async (search = '', level = 'All Levels', department = 'All Departments') => {
        try {
            const queryParams = new URLSearchParams();
            if (search) queryParams.append('search', search);
            if (level && level !== 'All Levels') queryParams.append('level', level);
            if (department && department !== 'All Departments') queryParams.append('department', department);

            const res = await fetch(`http://127.0.0.1:8000/api/v1/enrollment/all-courses?${queryParams.toString()}`);
            if (res.ok) {
                const courses = await res.json();
                allAccreditedCourses.value = courses;
                return courses;
            }
        } catch (err) {
            console.warn('[EnrollmentStore] Error fetching all courses:', err);
        }
        return [];
    };

    // API: Submit Registration
    const submitRegistration = async () => {
        if (!canSubmit.value) {
            if (!allCarryoversSelected.value) {
                toastStore.error('Mandatory carryover courses must be registered first!');
            } else if (isUnderload.value && !underloadReason.value) {
                toastStore.warning(
                    `Your selected load (${totalSelectedUnits.value} Units) is below 15 units. Please select an Academic Underload Concession reason to submit.`,
                    'Underload Concession Required'
                );
            } else if (isOverload.value) {
                toastStore.error(`Maximum allowable course load is ${creditPolicy.value?.maxUnits} units. Please remove excess courses.`);
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
                    courseIds: selectedCourseIds.value,
                    underloadReason: isUnderload.value ? underloadReason.value : null,
                    underloadNotes: isUnderload.value ? underloadNotes.value : null
                })
            });

            if (!res.ok) {
                const err = await res.json();
                throw new Error(err.detail || 'Course registration submission failed.');
            }

            const result = await res.json();
            if (result.isUnderload) {
                toastStore.success(
                    `Course registration submitted under Senate Underload Concession [${result.underloadConcession?.concessionReference}].`,
                    'Underload Concession Approved'
                );
            } else {
                toastStore.success(result.message || 'Course registration completed successfully!');
            }
            
            // Switch to official slip view
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

    // API: Reset Docket
    const resetDocket = async () => {
        try {
            const token = authStore.token;
            const res = await fetch('http://127.0.0.1:8000/api/v1/enrollment/reset', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });

            if (res.ok) {
                const result = await res.json();
                toastStore.info(result.message || 'Docket reset to mandatory carryover only.');
                await fetchAudit();
                activeTab.value = 'registration';
            }
        } catch (err) {
            console.error('[EnrollmentStore] Reset error:', err);
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

    return {
        isLoading,
        isSubmitting,
        auditData,
        selectedCourseIds,
        registrationSlip,
        activeTab,
        allAccreditedCourses,
        searchQuery,
        selectedCategoryFilter,
        isInterDeptModalOpen,
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
        freshSelectedCourses,
        totalSelectedUnits,
        carryoverUnits,
        regularUnits,
        isUnderload,
        isOverload,
        allCarryoversSelected,
        canSubmit,
        underloadReason,
        underloadNotes,
        underloadReasonsList,
        isCarryoverLocked,
        addCourse,
        removeCourse,
        toggleCourse,
        clearFreshCourses,
        quickAddRecommendedCore,
        enforceCarryoverSelection,
        fetchAudit,
        fetchAllAccreditedCourses,
        submitRegistration,
        resetDocket,
        fetchSlip
    };
});

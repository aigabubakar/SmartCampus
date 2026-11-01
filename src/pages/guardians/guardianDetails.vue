<template>
    <Sidebar />
    <main class="dashboard-main">
        <Navbar />
        <div class="dashboard-main-body">
            <Breadcrumb @open-login-details="openSidebar" />

            <div class="mt-24">
                <GuardianInfoCard :guardian="guardian" />
            </div>

            <div class="mt-16">
                <GuardianStudents :students="students" />
            </div>
        </div>
        <Footer />
        <LoginDetailsSidebar :isOpen="isSidebarOpen" :guardian="guardian" @close="closeSidebar" />
    </main>
    <ThemeCustomizer />
</template>

<script>
import { ref } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/guardians/guardianDetails/Breadcrumb.vue';
import GuardianInfoCard from '@/components/guardians/guardianDetails/GuardianInfoCard.vue';
import GuardianStudents from '@/components/guardians/guardianDetails/GuardianStudents.vue';
import LoginDetailsSidebar from '@/components/guardians/guardianDetails/LoginDetailsSidebar.vue';

// Assets
import guardianImg from '@/assets/images/thumbs/teacher-details-img.png';
import studentImg1 from '@/assets/images/thumbs/guardian-img1.png';
import studentImg2 from '@/assets/images/thumbs/guardian-img2.png';
import profileImg from '@/assets/images/thumbs/student-details-img.png'; // Using this for login side bar profile as per HTML

export default {
    name: "GuardianDetails",
    components: {
        Sidebar,
        Navbar,
        Footer,
        ThemeCustomizer,
        Breadcrumb,
        GuardianInfoCard,
        GuardianStudents,
        LoginDetailsSidebar
    },
    setup() {
        const isSidebarOpen = ref(false);

        const guardian = ref({
            id: 'AD1256589',
            name: 'Marvin McKinney',
            image: guardianImg,
            type: 'Father',
            phone: '+1 21541214',
            occupation: 'N/A',
            address: '8502 Preston Rd. Inglewood, Maine 98380',
            joinDate: '10 Nov 2006',
            email: 'guardian@example.com',
            password: '15445@#AC' // In a real app, do not expose password like this
        });

        const students = ref([
            {
                name: 'Robert Fox',
                image: studentImg1,
                relation: 'Father',
                phone: '+19854 65642',
                email: 'father@example.com'
            },
            {
                name: 'Brooklyn Simmons',
                image: studentImg2,
                relation: 'Mother',
                phone: '+19854 65642',
                email: 'mother@example.com'
            }
        ]);

        const openSidebar = () => {
            isSidebarOpen.value = true;
        };

        const closeSidebar = () => {
            isSidebarOpen.value = false;
        };

        return {
            isSidebarOpen,
            guardian,
            students,
            openSidebar,
            closeSidebar
        };
    }
}
</script>

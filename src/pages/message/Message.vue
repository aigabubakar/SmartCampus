<template>
  <div>
    <Sidebar />

    <main class="dashboard-main">
    <Navbar />
      <div class="dashboard-main-body">
        <Breadcrumb />

        <div class="mt-24">
          <div class="chat-wrapper">
            <ChatSidebar :users="users" :activeUserId="activeUserId" @select-user="handleUserSelect" />
            
            <ChatArea 
              v-if="activeUserId" 
              :activeUser="activeUser" 
              :messages="currentMessages" 
              @send-message="handleSendMessage"
            />
          </div>
        </div>
      </div>

      <Footer />
    </main>
    <ThemeCustomizer />
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import Sidebar from '@/components/layout/Sidebar.vue';
import Navbar from '@/components/layout/Navabar.vue';
import Footer from '@/components/layout/Footer.vue';
import ThemeCustomizer from '@/components/layout/ThemeCustomizer.vue';
import Breadcrumb from '@/components/message/Breadcrumb.vue';
import ChatSidebar from '@/components/message/ChatSidebar.vue';
import ChatArea from '@/components/message/ChatArea.vue';

export default {
  name: "Message",
  components: {
    Sidebar,
    Navbar,
    Footer,
    ThemeCustomizer,
    Breadcrumb,
    ChatSidebar,
    ChatArea
  },
  setup() {
    const activeUserId = ref(1);

    const users = ref([
      { id: 1, name: 'Kathryn Murphy', image: 'assets/images/chat/11.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
      { id: 2, name: 'James Michael', image: 'assets/images/chat/3.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
      { id: 3, name: 'Russell Lucas', image: 'assets/images/chat/4.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
      { id: 4, name: 'Caleb Bradley', image: 'assets/images/chat/5.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
      { id: 5, name: 'Bobby Roy', image: 'assets/images/chat/6.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
      { id: 6, name: 'Vincent Liam', image: 'assets/images/chat/7.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
      { id: 7, name: 'Randy Mason', image: 'assets/images/chat/8.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
      { id: 8, name: 'Albert Wayne', image: 'assets/images/chat/9.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
      { id: 9, name: 'Elijah Willie', image: 'assets/images/chat/10.png', lastMessage: "hey! there i'm...", time: '12:30 PM', unreadCount: 8 },
    ]);

    const messages = ref({
      1: [ // Messages for user 1
         { text: "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters.", time: "6.30 pm", isMyMessage: false },
         { text: "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters.", time: "6.30 pm", isMyMessage: true },
         { text: "The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default.Contrary to popular belief, Lorem Ipsum is not simply random text is the model text for your company.", time: "6.30 pm", isMyMessage: false },
      ]
    });

    const activeUser = computed(() => users.value.find(u => u.id === activeUserId.value));
    const currentMessages = computed(() => messages.value[activeUserId.value] || []);

    const handleUserSelect = (id) => {
      activeUserId.value = id;
      // Mark as read, etc.
      const user = users.value.find(u => u.id === id);
      if(user) user.unreadCount = 0;
      
      if (!messages.value[id]) {
          messages.value[id] = [];
      }
    };

    const handleSendMessage = (text) => {
      if (!messages.value[activeUserId.value]) {
        messages.value[activeUserId.value] = [];
      }
      messages.value[activeUserId.value].push({
        text,
        time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        isMyMessage: true
      });
    };

    return {
      users,
      activeUserId,
      activeUser,
      currentMessages,
      handleUserSelect,
      handleSendMessage
    };
  }
}
</script>

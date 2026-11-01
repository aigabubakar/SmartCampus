<template>
  <div class="chat-main card">
    <div class="chat-sidebar-single active" v-if="activeUser">
      <div class="img">
        <img :src="activeUser.image" alt="image">
      </div>
      <div class="info">
        <h6 class="text-md mb-0">{{ activeUser.name }}</h6>
        <p class="mb-0">Available</p>
      </div>
      <div class="action d-inline-flex align-items-center gap-3">
        <div class="btn-group">
          <button type="button" class="text-primary-light text-xl" data-bs-toggle="dropdown" data-bs-display="static" aria-expanded="false">
            <iconify-icon icon="tabler:dots-vertical"></iconify-icon>
          </button>
          <ul class="dropdown-menu dropdown-menu-lg-end border">
            <li>
              <button class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2" type="button">
                <iconify-icon icon="mdi:clear-circle-outline"></iconify-icon>
                Clear All
              </button>
            </li>
            <li>
              <button class="dropdown-item rounded text-secondary-light bg-hover-neutral-200 text-hover-neutral-900 d-flex align-items-center gap-2" type="button">
                <iconify-icon icon="ic:baseline-block"></iconify-icon>
                Block
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div class="chat-message-list">
      <div 
        v-for="(msg, index) in messages" 
        :key="index" 
        class="chat-single-message" 
        :class="msg.isMyMessage ? 'right' : 'left'"
      >
        <img v-if="!msg.isMyMessage" :src="activeUser.image" alt="image" class="avatar-lg object-fit-cover rounded-circle">
        <div class="chat-message-content">
          <p class="mb-3">{{ msg.text }}</p>
          <p class="chat-time mb-0">
            <span>{{ msg.time }}</span>
          </p>
        </div>
      </div>
    </div>

    <form class="chat-message-box" @submit.prevent="sendMessage">
      <input type="text" name="chatMessage" placeholder="Write message" v-model="newMessage">
      <div class="chat-message-box-action">
        <button type="button" class="text-xl">
          <iconify-icon icon="ph:link"></iconify-icon>
        </button>
        <button type="button" class="text-xl">
          <iconify-icon icon="solar:gallery-linear"></iconify-icon>
        </button>
        <button type="submit" class="btn btn-sm btn-primary-600 radius-8 d-inline-flex align-items-center gap-1">
          Send
          <iconify-icon icon="f7:paperplane"></iconify-icon>
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: "ChatArea",
  props: {
    activeUser: {
      type: Object,
      default: null
    },
    messages: {
      type: Array,
      default: () => []
    }
  },
  emits: ['send-message'],
  setup(props, { emit }) {
    const newMessage = ref('');

    const sendMessage = () => {
      if (newMessage.value.trim()) {
        emit('send-message', newMessage.value);
        newMessage.value = '';
      }
    };

    return {
      newMessage,
      sendMessage
    };
  }
}
</script>

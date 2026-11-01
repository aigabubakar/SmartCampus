<template>
  <div class="chat-sidebar card">
    <div class="px-24 py-16">
      <form class="navbar-search d-block">
        <input type="text" class="bg-transparent w-100" name="search" placeholder="Search" v-model="searchQuery">
        <iconify-icon icon="ion:search-outline" class="icon"></iconify-icon>
      </form>
    </div>
    <div class="chat-all-list">
      <div 
        v-for="(user, index) in users" 
        :key="index" 
        class="chat-sidebar-single" 
        :class="{ active: user.id === activeUserId }" 
        @click="$emit('select-user', user.id)"
      >
        <div class="img">
          <img :src="user.image" alt="image">
        </div>
        <div class="info">
          <h6 class="text-sm mb-1">{{ user.name }}</h6>
          <p class="mb-0 text-xs">{{ user.lastMessage }}</p>
        </div>
        <div class="action text-end">
          <p class="mb-0 text-neutral-400 text-xs lh-1">{{ user.time }}</p>
          <span v-if="user.unreadCount > 0" class="w-16-px h-16-px text-xs rounded-circle bg-warning-main text-white d-inline-flex align-items-center justify-content-center">
            {{ user.unreadCount }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  name: "ChatSidebar",
  props: {
    users: {
      type: Array,
      required: true
    },
    activeUserId: {
      type: Number,
      default: null
    }
  },
  emits: ['select-user'],
  setup() {
    const searchQuery = ref('');

    return {
      searchQuery
    };
  }
}
</script>

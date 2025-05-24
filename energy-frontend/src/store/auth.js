import { defineStore } from 'pinia'
import axios from 'axios'
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: localStorage.getItem('token') || null
  }),
  actions: {
    async login(email, password) {
      const response = await axios.post(`${API_BASE_URL}/api-token-auth/`, { username: email, password })
      this.token = response.data.token
      localStorage.setItem('token', this.token)
    },
    logout() {
      this.token = null
      localStorage.removeItem('token')
    }
  }
})

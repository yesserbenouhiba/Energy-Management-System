import axios from 'axios'
import { useAuthStore } from './store/auth'
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

const api = axios.create({
  baseURL: `${API_BASE_URL}/api`
})

api.interceptors.request.use(config => {
  const auth = useAuthStore()
  if (auth.token) {
    config.headers.Authorization = `Token ${auth.token}`
  }
  return config
})

export default api

import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../pages/Dashboard.vue'
import Login from '../pages/Login.vue'
import SocieteList from '../pages/SocieteList.vue'
import SocieteDetail from '../pages/SocieteDetail.vue'
import QuotationManagement from '../pages/QuotationManagement.vue'
import ContractManagement from '../pages/ContractManagement.vue'


const routes = [
  { path: '/', component: Dashboard },
  { path: '/login', component: Login },
  { path: '/societes', component: SocieteList },
  { path: '/societes/:id', component: SocieteDetail },
  { path: '/quotations', component: QuotationManagement },
  { path: '/contracts', component: ContractManagement },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

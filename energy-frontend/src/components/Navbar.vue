<!-- Navbar Component (components/Navbar.vue) -->
<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm">
    <div class="container">
      <!-- Brand/Logo -->
      <router-link class="navbar-brand fw-bold" to="/">
        <i class="fas fa-bolt me-2"></i>
        Energy Manager
      </router-link>

      <!-- Mobile toggle button -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Navigation items -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav me-auto">
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: isActive('/') }"
              to="/"
            >
              <i class="fas fa-tachometer-alt me-1"></i>
              Dashboard
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: isActive('/societes') }"
              to="/societes"
            >
              <i class="fas fa-building me-1"></i>
              Companies
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: isActive('/contracts') }"
              to="/contracts"
            >
              <i class="fas fa-file-contract me-1"></i>
              Contracts
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              class="nav-link"
              :class="{ active: isActive('/quotations') }"
              to="/quotations"
            >
              <i class="fas fa-quote-left me-1"></i>
              Quotations
            </router-link>
          </li>
        </ul>

        <!-- User menu -->
        <ul class="navbar-nav">
          <li class="nav-item dropdown" v-if="auth.token">
            <a
              class="nav-link dropdown-toggle d-flex align-items-center"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              <div class="bg-light rounded-circle p-1 me-2">
                <i class="fas fa-user text-primary"></i>
              </div>
              {{ auth.user?.username || "User" }}
            </a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li>
                <a class="dropdown-item text-danger" href="#" @click="logout">
                  <i class="fas fa-sign-out-alt me-2"></i>Logout
                </a>
              </li>
            </ul>
          </li>
          <li class="nav-item" v-else>
            <router-link class="nav-link" to="/login">
              <i class="fas fa-sign-in-alt me-1"></i>
              Login
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "../store/auth";

const route = useRoute();
const router = useRouter();
const auth = useAuthStore();

// Function to check if current route is active
const isActive = (path) => {
  if (path === "/") {
    return route.path === "/";
  }
  return route.path.startsWith(path);
};

// Logout function
const logout = async () => {
  try {
    await auth.logout();
    router.push("/login");
  } catch (error) {
    console.error("Logout failed:", error);
  }
};
</script>

<style scoped>
.navbar-nav .nav-link {
  transition: all 0.3s ease;
  border-radius: 0.375rem;
  margin: 0 0.25rem;
  position: relative;
}

.navbar-nav .nav-link:hover {
  background-color: rgba(255, 255, 255, 0.1);
  transform: translateY(-1px);
}

.navbar-nav .nav-link.active {
  background-color: rgba(255, 255, 255, 0.2);
  font-weight: 600;
}

.navbar-nav .nav-link.active::after {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 50%;
  transform: translateX(-50%);
  width: 60%;
  height: 2px;
  background-color: #fff;
  border-radius: 1px;
}

.dropdown-menu {
  border: none;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  border-radius: 0.5rem;
}

.dropdown-item {
  padding: 0.5rem 1rem;
  transition: all 0.2s ease;
}

.dropdown-item:hover {
  background-color: #f8f9fa;
  transform: translateX(4px);
}
</style>

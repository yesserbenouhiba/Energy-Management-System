<template>
  <div class="min-vh-100 d-flex align-items-center bg-light">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-md-6 col-lg-4">
          <div class="card border-0 shadow">
            <div class="card-body p-4">
              <div class="text-center mb-4">
                <div
                  class="bg-primary bg-opacity-10 rounded-circle d-inline-flex p-3 mb-3"
                >
                  <i class="fas fa-user text-primary fa-2x"></i>
                </div>
                <h2 class="fw-bold text-dark">Welcome Back</h2>
                <p class="text-muted">Please sign in to your account</p>
              </div>

              <form @submit.prevent="login">
                <div class="mb-3">
                  <label for="username" class="form-label">Username</label>
                  <div class="input-group">
                    <span class="input-group-text bg-light border-end-0">
                      <i class="fas fa-user text-muted"></i>
                    </span>
                    <input
                      v-model="username"
                      type="text"
                      class="form-control border-start-0 ps-0"
                      id="username"
                      placeholder="Enter your username"
                      required
                    />
                  </div>
                </div>

                <div class="mb-4">
                  <label for="password" class="form-label">Password</label>
                  <div class="input-group">
                    <span class="input-group-text bg-light border-end-0">
                      <i class="fas fa-lock text-muted"></i>
                    </span>
                    <input
                      v-model="password"
                      type="password"
                      class="form-control border-start-0 ps-0"
                      id="password"
                      placeholder="Enter your password"
                      required
                    />
                  </div>
                </div>

                <button
                  type="submit"
                  class="btn btn-primary w-100 py-2 fw-semibold"
                >
                  <i class="fas fa-sign-in-alt me-2"></i>Sign In
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "../store/auth";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const auth = useAuthStore();
const router = useRouter();

const login = async () => {
  try {
    await auth.login(username.value, password.value);
    router.push("/");
  } catch (error) {
    alert("Login failed");
  }
};
</script>

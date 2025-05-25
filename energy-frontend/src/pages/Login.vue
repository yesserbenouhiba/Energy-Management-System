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

              <!-- General Error Alert -->
              <div v-if="generalError" class="alert alert-danger d-flex align-items-center mb-3" role="alert">
                <i class="fas fa-exclamation-triangle me-2"></i>
                <div>{{ generalError }}</div>
              </div>

              <form @submit.prevent="login">
                <div class="mb-3">
                  <label for="username" class="form-label">Username</label>
                  <div class="input-group">
                    <span class="input-group-text bg-light border-end-0" :class="{ 'border-danger': errors.username }">
                      <i class="fas fa-user" :class="errors.username ? 'text-danger' : 'text-muted'"></i>
                    </span>
                    <input
                      v-model="username"
                      type="text"
                      class="form-control border-start-0 ps-0"
                      :class="{ 'border-danger': errors.username, 'is-invalid': errors.username }"
                      id="username"
                      placeholder="Enter your username"
                    />
                  </div>
                  <div v-if="errors.username" class="invalid-feedback d-block">
                    <i class="fas fa-exclamation-circle me-1"></i>{{ errors.username }}
                  </div>
                </div>

                <div class="mb-4">
                  <label for="password" class="form-label">Password</label>
                  <div class="input-group">
                    <span class="input-group-text bg-light border-end-0" :class="{ 'border-danger': errors.password }">
                      <i class="fas fa-lock" :class="errors.password ? 'text-danger' : 'text-muted'"></i>
                    </span>
                    <input
                      v-model="password"
                      type="password"
                      class="form-control border-start-0 ps-0"
                      :class="{ 'border-danger': errors.password, 'is-invalid': errors.password }"
                      id="password"
                      placeholder="Enter your password"
                    />
                  </div>
                  <div v-if="errors.password" class="invalid-feedback d-block">
                    <i class="fas fa-exclamation-circle me-1"></i>{{ errors.password }}
                  </div>
                </div>

                <button
                  type="submit"
                  class="btn btn-primary w-100 py-2 fw-semibold"
                  :disabled="isLoading"
                >
                  <span v-if="isLoading">
                    <i class="fas fa-spinner fa-spin me-2"></i>Signing In...
                  </span>
                  <span v-else>
                    <i class="fas fa-sign-in-alt me-2"></i>Sign In
                  </span>
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
import { ref, reactive, watch } from "vue";
import { useAuthStore } from "../store/auth";
import { useRouter } from "vue-router";

const username = ref("");
const password = ref("");
const auth = useAuthStore();
const router = useRouter();
const isLoading = ref(false);
const generalError = ref("");

// Reactive errors object
const errors = reactive({
  username: "",
  password: ""
});

// Clear errors when user starts typing
watch(username, () => {
  if (errors.username) errors.username = "";
  if (generalError.value) generalError.value = "";
});

watch(password, () => {
  if (errors.password) errors.password = "";
  if (generalError.value) generalError.value = "";
});

// Validation function
const validateForm = () => {
  let isValid = true;
  
  // Reset errors
  errors.username = "";
  errors.password = "";
  generalError.value = "";

  // Validate username
  if (!username.value.trim()) {
    errors.username = "Username is required";
    isValid = false;
  } else if (username.value.trim().length < 3) {
    errors.username = "Username must be at least 3 characters";
    isValid = false;
  }

  // Validate password
  if (!password.value.trim()) {
    errors.password = "Password is required";
    isValid = false;
  }

  return isValid;
};

const login = async () => {
  // Validate form first
  if (!validateForm()) {
    return;
  }

  isLoading.value = true;
  
  try {
    await auth.login(username.value.trim(), password.value);
    router.push("/");
  } catch (error) {
    // Handle different types of errors
    if (error.response && error.response.status === 400) {
      generalError.value = "Username or password is incorrect. Please try again.";
    } else if (error.response && error.response.status === 401) {
      generalError.value = "Username or password is incorrect. Please try again.";
    } else if (error.response && error.response.status === 422) {
      generalError.value = "Invalid credentials provided.";
    } else if (!error.response) {
      generalError.value = "Network error. Please check your connection and try again.";
    } else {
      generalError.value = "Login failed. Please try again.";
    }
  } finally {
    isLoading.value = false;
  }
};
</script>
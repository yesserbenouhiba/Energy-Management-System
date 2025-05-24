<template>
  <div>
    <Navbar />
    <div class="container mt-4">
      <div class="row">
        <div class="col-12">
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="text-primary">
              <i class="fas fa-building me-2"></i>Company List
            </h1>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-12">
          <div class="card border-0 shadow-sm">
            <div class="card-body p-0">
              <div v-if="societes && societes.length > 0">
                <div
                  v-for="(s, index) in societes"
                  :key="s.id"
                  class="border-bottom last:border-0"
                >
                  <router-link
                    :to="`/societes/${s.id}`"
                    class="d-block p-4 text-decoration-none text-dark hover-bg-light transition"
                  >
                    <div class="d-flex align-items-center">
                      <div class="flex-shrink-0">
                        <div
                          class="bg-primary bg-opacity-10 rounded-circle p-2"
                        >
                          <i class="fas fa-building text-primary"></i>
                        </div>
                      </div>
                      <div class="flex-grow-1 ms-3">
                        <h5 class="mb-0 fw-semibold">{{ s.nom }}</h5>
                        <small class="text-muted">Click to view details</small>
                      </div>
                      <div class="flex-shrink-0">
                        <i class="fas fa-chevron-right text-muted"></i>
                      </div>
                    </div>
                  </router-link>
                </div>
              </div>
              <div v-else class="text-center py-5">
                <div class="text-muted">
                  <i class="fas fa-building fa-3x mb-3 opacity-50"></i>
                  <h4>No companies found</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import Navbar from "../components/Navbar.vue";
import api from "../axios";

const societes = ref([]);

onMounted(async () => {
  const res = await api.get("/societes/");
  societes.value = res.data;
});
</script>

<style scoped>
.hover-bg-light:hover {
  background-color: #f8f9fa !important;
}

.transition {
  transition: all 0.2s ease-in-out;
}

.last\:border-0:last-child {
  border-bottom: none !important;
}

.last\:pb-0:last-child {
  padding-bottom: 0 !important;
}

.last\:mb-0:last-child {
  margin-bottom: 0 !important;
}

.min-vh-100 {
  min-height: 100vh;
}
</style>

<template>
  <div>
    <Navbar />
    <div class="container mt-4">
      <div class="row">
        <div class="col-12">
          <h2 class="mb-4 text-primary">
            <i class="fas fa-tachometer-alt me-2"></i>Dashboard
          </h2>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-md-6">
          <div class="card border-0 shadow-sm h-100">
            <div class="card-body d-flex align-items-center">
              <div class="flex-shrink-0">
                <div class="bg-primary bg-opacity-10 rounded-circle p-3">
                  <i class="fas fa-file-contract text-primary fa-2x"></i>
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="card-title text-muted mb-1">Active Contracts</h5>
                <h2 class="fw-bold text-primary mb-0">{{ activeContracts }}</h2>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-6">
          <div class="card border-0 shadow-sm h-100">
            <div class="card-body d-flex align-items-center">
              <div class="flex-shrink-0">
                <div class="bg-warning bg-opacity-10 rounded-circle p-3">
                  <i class="fas fa-clock text-warning fa-2x"></i>
                </div>
              </div>
              <div class="flex-grow-1 ms-3">
                <h5 class="card-title text-muted mb-1">Pending Quotations</h5>
                <h2 class="fw-bold text-warning mb-0">
                  {{ pendingQuotations }}
                </h2>
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

const activeContracts = ref(0);
const pendingQuotations = ref(0);

const fetchDashboardMetrics = async () => {
  try {
    const response = await api.get("/dashboard-metrics/");
    activeContracts.value = response.data.active_contracts;
    pendingQuotations.value = response.data.pending_quotations;
  } catch (error) {
    console.error("Failed to fetch dashboard metrics", error);
  }
};

onMounted(() => {
  fetchDashboardMetrics();
});
</script>

<template>
  <div>
    <Navbar />
    <div class="container mt-4" v-if="societe">
      <div class="row">
        <div class="col-12">
          <div class="card border-0 shadow-sm mb-4">
            <div class="card-header bg-primary text-white">
              <h2 class="card-title mb-0">
                <i class="fas fa-building me-2"></i>{{ societe.nom }}
              </h2>
            </div>
            <div class="card-body">
              <div class="row">
                <div class="col-md-6">
                  <div class="d-flex align-items-center mb-3">
                    <i class="fas fa-envelope text-primary me-3"></i>
                    <div>
                      <strong class="text-muted">Email:</strong>
                      <div>{{ societe.email }}</div>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="d-flex align-items-center mb-3">
                    <i class="fas fa-phone text-primary me-3"></i>
                    <div>
                      <strong class="text-muted">Téléphone:</strong>
                      <div>{{ societe.telephone }}</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row g-4">
        <div class="col-lg-6">
          <div class="card border-0 shadow-sm h-100">
            <div class="card-header bg-warning text-dark">
              <h4 class="card-title mb-0">
                <i class="fas fa-bolt me-2"></i>Electric Meters
              </h4>
            </div>
            <div class="card-body">
              <div
                v-if="
                  societe.compteurelec_set &&
                  societe.compteurelec_set.length > 0
                "
              >
                <div
                  v-for="elec in societe.compteurelec_set"
                  :key="elec.id"
                  class="border-bottom pb-3 mb-3 last:border-0 last:pb-0 last:mb-0"
                >
                  <div class="row align-items-center">
                    <div class="col-8">
                      <h6 class="fw-bold mb-1">{{ elec.numCompteur }}</h6>
                      <small class="text-muted">{{
                        elec.optionTarifaire
                      }}</small>
                    </div>
                    <div class="col-4 text-end">
                      <span class="badge bg-warning text-dark">
                        {{ elec.puissance }} kW
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <div v-else class="text-center text-muted py-4">
                <i class="fas fa-info-circle me-2"></i>No electric meters found
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-6">
          <div class="card border-0 shadow-sm h-100">
            <div class="card-header bg-info text-white">
              <h4 class="card-title mb-0">
                <i class="fas fa-fire me-2"></i>Gas Meters
              </h4>
            </div>
            <div class="card-body">
              <div
                v-if="
                  societe.compteurgaz_set && societe.compteurgaz_set.length > 0
                "
              >
                <div
                  v-for="gaz in societe.compteurgaz_set"
                  :key="gaz.id"
                  class="border-bottom pb-3 mb-3 last:border-0 last:pb-0 last:mb-0"
                >
                  <div class="row align-items-center">
                    <div class="col-8">
                      <h6 class="fw-bold mb-1">{{ gaz.numCompteur }}</h6>
                    </div>
                    <div class="col-4 text-end">
                      <span class="badge bg-info">
                        {{ gaz.consommation }} m³
                      </span>
                    </div>
                  </div>
                </div>
              </div>
              <div v-else class="text-center text-muted py-4">
                <i class="fas fa-info-circle me-2"></i>No gas meters found
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
import { useRoute } from "vue-router";
import Navbar from "../components/Navbar.vue";
import api from "../axios";

const route = useRoute();
const societe = ref(null);

onMounted(async () => {
  const res = await api.get(`/societes/${route.params.id}/`);
  societe.value = res.data;
});
</script>

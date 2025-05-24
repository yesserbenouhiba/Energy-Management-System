<template>
  <div>
    <Navbar />
    <div class="container py-4">
      <!-- Page Header -->
      <div class="row">
        <div class="col-12">
          <div class="d-flex justify-content-between align-items-center mb-4">
            <h2 class="text-primary mb-0">
              <i class="fas fa-quote-left me-2"></i>Quotation Management
            </h2>
            <div class="badge bg-primary fs-6">
              {{ quotations.length }} Total Quotations
            </div>
          </div>
        </div>
      </div>

      <!-- Create / Edit Form -->
      <div class="row mb-4">
        <div class="col-12">
          <div class="card border-0 shadow-sm">
            <div class="card-header bg-gradient-primary text-white">
              <h5 class="card-title mb-0">
                <i
                  class="fas fa-{{ isEditing ? 'edit' : 'plus-circle' }} me-2"
                ></i>
                {{ isEditing ? "Update" : "Create" }} Quotation
              </h5>
            </div>
            <div class="card-body p-4">
              <form @submit.prevent="handleSubmit">
                <div class="row g-3">
                  <!-- Type -->
                  <div class="col-md-6">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-tag text-primary me-1"></i>Type
                    </label>
                    <select v-model="form.type" class="form-select" required>
                      <option value="" disabled>Select type</option>
                      <option value="GAZ">GAZ</option>
                      <option value="ELEC">ELEC</option>
                    </select>
                  </div>

                  <!-- Status -->
                  <div class="col-md-6">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-flag text-primary me-1"></i>Status
                    </label>
                    <select v-model="form.status" class="form-select" required>
                      <option value="Pending">Pending</option>
                      <option value="Validated">Validated</option>
                    </select>
                  </div>

                  <!-- Societe -->
                  <div class="col-md-6">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-building text-primary me-1"></i>Company
                    </label>
                    <select v-model="form.societe" class="form-select" required>
                      <option value="" disabled>Select company</option>
                      <option v-for="s in societes" :key="s.id" :value="s.id">
                        {{ s.nom }}
                      </option>
                    </select>
                  </div>

                  <!-- Compte -->
                  <div class="col-md-6">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-user-circle text-primary me-1"></i
                      >Account
                    </label>
                    <select v-model="form.compte" class="form-select" required>
                      <option value="" disabled>Select account</option>
                      <option v-for="c in comptes" :key="c.id" :value="c.id">
                        Account #{{ c.id }}
                      </option>
                    </select>
                  </div>

                  <!-- Num Compteur -->
                  <div class="col-12">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-barcode text-primary me-1"></i>Meter
                      Number
                    </label>
                    <div class="input-group">
                      <span class="input-group-text bg-light">
                        <i class="fas fa-hashtag text-muted"></i>
                      </span>
                      <input
                        v-model="form.numCompteur"
                        type="text"
                        class="form-control"
                        placeholder="Enter meter number"
                        required
                      />
                    </div>
                  </div>
                </div>

                <div class="d-flex justify-content-end mt-4 pt-3 border-top">
                  <button type="submit" class="btn btn-primary me-2 px-4">
                    <i
                      class="fas fa-{{ isEditing ? 'save' : 'plus' }} me-2"
                    ></i>
                    {{ isEditing ? "Update" : "Create" }}
                  </button>
                  <button
                    v-if="isEditing"
                    type="button"
                    class="btn btn-outline-secondary px-4"
                    @click="resetForm"
                  >
                    <i class="fas fa-times me-2"></i>Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>

      <!-- Quotations List -->
      <div class="row">
        <div class="col-12">
          <div class="card border-0 shadow-sm">
            <div class="card-header bg-light border-bottom">
              <div class="d-flex justify-content-between align-items-center">
                <h5 class="card-title mb-0">
                  <i class="fas fa-list-alt text-primary me-2"></i>Quotations
                  List
                </h5>
              </div>
            </div>
            <div class="card-body p-0">
              <div class="table-responsive">
                <table class="table table-hover mb-0">
                  <thead class="table-light">
                    <tr>
                      <th class="ps-4">#</th>
                      <th><i class="fas fa-tag me-1"></i>Type</th>
                      <th><i class="fas fa-building me-1"></i>Company</th>
                      <th><i class="fas fa-user-circle me-1"></i>Account</th>
                      <th><i class="fas fa-barcode me-1"></i>Meter Number</th>
                      <th><i class="fas fa-flag me-1"></i>Status</th>
                      <th class="text-center">Actions</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr
                      v-for="(q, index) in quotations"
                      :key="q.id"
                      class="align-middle"
                    >
                      <td class="ps-4 fw-semibold text-muted">
                        {{ index + 1 }}
                      </td>
                      <td>
                        <div class="fw-semibold">{{ q.type }}</div>
                      </td>
                      <td>
                        <div class="fw-semibold">{{ q.societe.nom }}</div>
                      </td>
                      <td>
                        <span
                          class="badge bg-secondary bg-opacity-10 text-secondary"
                        >
                          #{{ q.compte.id }}
                        </span>
                      </td>
                      <td>
                        <code class="text-dark bg-light px-2 py-1 rounded">{{
                          q.numCompteur
                        }}</code>
                      </td>
                      <td>
                        <div class="fw-semibold">{{ q.status }}</div>
                      </td>
                      <td class="text-center">
                        <button
                          class="btn btn-sm btn-outline-primary"
                          @click="editQuotation(q)"
                          title="Edit quotation"
                        >
                          <i class="fas fa-edit me-1"></i> Edit
                        </button>
                      </td>
                    </tr>
                    <tr v-if="quotations.length === 0">
                      <td colspan="7" class="text-center py-5">
                        <div class="text-muted">
                          <i class="fas fa-inbox fa-3x mb-3 opacity-50"></i>
                          <h5>No quotations available</h5>
                          <p class="mb-0">
                            Create your first quotation using the form above
                          </p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
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

const quotations = ref([]);
const societes = ref([]);
const comptes = ref([]);

const form = ref({
  id: null,
  type: "",
  societe: null,
  compte: null,
  numCompteur: "",
  status: "Pending",
});

const isEditing = ref(false);

const fetchQuotations = async () => {
  try {
    const res = await api.get("/demandes-cotation/");
    quotations.value = res.data;
  } catch (err) {
    console.error("Failed to fetch quotations", err);
  }
};

const fetchSocietes = async () => {
  try {
    const res = await api.get("/societes/");
    societes.value = res.data;
  } catch (err) {
    console.error("Failed to fetch societes", err);
  }
};

const fetchComptes = async () => {
  try {
    const res = await api.get("/comptes/");
    comptes.value = res.data;
  } catch (err) {
    console.error("Failed to fetch comptes", err);
  }
};

const handleSubmit = async () => {
  try {
    if (isEditing.value) {
      await api.put(`/demandes-cotation/${form.value.id}/`, form.value);
    } else {
      await api.post("/demandes-cotation/", form.value);
    }
    resetForm();
    fetchQuotations();
  } catch (err) {
    console.error("Failed to submit form", err);
  }
};

const editQuotation = (quotation) => {
  form.value = {
    id: quotation.id,
    type: quotation.type,
    societe: quotation.societe.id,
    compte: quotation.compte.id,
    numCompteur: quotation.numCompteur,
    status: quotation.status,
  };
  isEditing.value = true;

  // Scroll to form
  window.scrollTo({ top: 0, behavior: "smooth" });
};

const resetForm = () => {
  form.value = {
    id: null,
    type: "",
    societe: null,
    compte: null,
    numCompteur: "",
    status: "Pending",
  };
  isEditing.value = false;
};

onMounted(() => {
  fetchQuotations();
  fetchSocietes();
  fetchComptes();
});
</script>

<style scoped>
.bg-gradient-primary {
  background: linear-gradient(135deg, #0d6efd 0%, #0056b3 100%);
}

.table th {
  font-weight: 600;
  font-size: 0.875rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.table td {
  vertical-align: middle;
}

.form-select:focus,
.form-control:focus {
  border-color: #0d6efd;
  box-shadow: 0 0 0 0.2rem rgba(13, 110, 253, 0.25);
}

.btn {
  transition: all 0.2s ease;
}

.btn:hover {
  transform: translateY(-1px);
}

.card {
  transition: all 0.3s ease;
}

.table-hover tbody tr:hover {
  background-color: rgba(13, 110, 253, 0.05);
}

code {
  font-size: 0.875rem;
}

.badge {
  font-size: 0.75rem;
  font-weight: 500;
}
</style>

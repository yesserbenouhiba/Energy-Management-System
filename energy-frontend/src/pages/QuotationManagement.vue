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

      <!-- Error Alert -->
      <div class="row mb-4" v-if="errorMessage">
        <div class="col-12">
          <div class="alert alert-danger alert-dismissible fade show" role="alert">
            <i class="fas fa-exclamation-triangle me-2"></i>
            <strong>Error:</strong> {{ errorMessage }}
            <button type="button" class="btn-close" @click="clearError" aria-label="Close"></button>
          </div>
        </div>
      </div>

      <!-- Success Alert -->
      <div class="row mb-4" v-if="successMessage">
        <div class="col-12">
          <div class="alert alert-success alert-dismissible fade show" role="alert">
            <i class="fas fa-check-circle me-2"></i>
            {{ successMessage }}
            <button type="button" class="btn-close" @click="clearSuccess" aria-label="Close"></button>
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
              <form @submit.prevent="handleSubmit" novalidate>
                <div class="row g-3">
                  <!-- Type -->
                  <div class="col-md-6">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-tag text-primary me-1"></i>Type
                      <span class="text-danger">*</span>
                    </label>
                    <select 
                      v-model="form.type" 
                      class="form-select" 
                      :class="{ 'is-invalid': errors.type }"
                      required
                    >
                      <option value="" disabled>Select type</option>
                      <option value="GAZ">GAZ</option>
                      <option value="ELEC">ELEC</option>
                    </select>
                    <div v-if="errors.type" class="invalid-feedback">
                      {{ errors.type }}
                    </div>
                  </div>

                  <!-- Status -->
                  <div class="col-md-6">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-flag text-primary me-1"></i>Status
                      <span class="text-danger">*</span>
                    </label>
                    <select 
                      v-model="form.status" 
                      class="form-select" 
                      :class="{ 'is-invalid': errors.status }"
                      required
                    >
                      <option value="">Select status</option>
                      <option value="Pending">Pending</option>
                      <option value="Validated">Validated</option>
                    </select>
                    <div v-if="errors.status" class="invalid-feedback">
                      {{ errors.status }}
                    </div>
                  </div>

                  <!-- Societe -->
                  <div class="col-md-6">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-building text-primary me-1"></i>Company
                      <span class="text-danger">*</span>
                    </label>
                    <select 
                      v-model="form.societe" 
                      class="form-select" 
                      :class="{ 'is-invalid': errors.societe }"
                      :disabled="loadingStates.societes"
                      required
                    >
                      <option value="" disabled>
                        {{ loadingStates.societes ? 'Loading companies...' : 'Select company' }}
                      </option>
                      <option v-for="s in societes" :key="s.id" :value="s.id">
                        {{ s.nom }}
                      </option>
                    </select>
                    <div v-if="errors.societe" class="invalid-feedback">
                      {{ errors.societe }}
                    </div>
                    <div v-if="societes.length === 0 && !loadingStates.societes" class="form-text text-warning">
                      <i class="fas fa-exclamation-triangle me-1"></i>
                      No companies available. Please add companies first.
                    </div>
                  </div>

                  <!-- Compte -->
                  <div class="col-md-6">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-user-circle text-primary me-1"></i>Account
                      <span class="text-danger">*</span>
                    </label>
                    <select 
                      v-model="form.compte" 
                      class="form-select" 
                      :class="{ 'is-invalid': errors.compte }"
                      :disabled="loadingStates.comptes"
                      required
                    >
                      <option value="" disabled>
                        {{ loadingStates.comptes ? 'Loading accounts...' : 'Select account' }}
                      </option>
                      <option v-for="c in comptes" :key="c.id" :value="c.id">
                        Account #{{ c.id }}
                      </option>
                    </select>
                    <div v-if="errors.compte" class="invalid-feedback">
                      {{ errors.compte }}
                    </div>
                    <div v-if="comptes.length === 0 && !loadingStates.comptes" class="form-text text-warning">
                      <i class="fas fa-exclamation-triangle me-1"></i>
                      No accounts available. Please add accounts first.
                    </div>
                  </div>

                  <!-- Num Compteur -->
                  <div class="col-12">
                    <label class="form-label fw-semibold">
                      <i class="fas fa-barcode text-primary me-1"></i>Meter Number
                      <span class="text-danger">*</span>
                    </label>
                    <div class="input-group">
                      <span class="input-group-text bg-light">
                        <i class="fas fa-hashtag text-muted"></i>
                      </span>
                      <input
                        v-model="form.numCompteur"
                        type="text"
                        class="form-control"
                        :class="{ 'is-invalid': errors.numCompteur }"
                        placeholder="Enter meter number"
                        required
                      />
                      <div v-if="errors.numCompteur" class="invalid-feedback">
                        {{ errors.numCompteur }}
                      </div>
                    </div>
                  </div>
                </div>

                <div class="d-flex justify-content-end mt-4 pt-3 border-top">
                  <button 
                    type="submit" 
                    class="btn btn-primary me-2 px-4"
                    :disabled="isSubmitting"
                  >
                    <span v-if="isSubmitting" class="spinner-border spinner-border-sm me-2" role="status"></span>
                    <i v-else class="fas fa-{{ isEditing ? 'save' : 'plus' }} me-2"></i>
                    {{ isSubmitting ? 'Processing...' : (isEditing ? 'Update' : 'Create') }}
                  </button>
                  <button
                    v-if="isEditing"
                    type="button"
                    class="btn btn-outline-secondary px-4"
                    @click="resetForm"
                    :disabled="isSubmitting"
                  >
                    <i class="fas fa-times me-2"></i>Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>

      <!-- Loading State -->
      <div class="row" v-if="loadingStates.quotations">
        <div class="col-12">
          <div class="card border-0 shadow-sm">
            <div class="card-body text-center py-5">
              <div class="spinner-border text-primary mb-3" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
              <h5>Loading quotations...</h5>
            </div>
          </div>
        </div>
      </div>

      <!-- Quotations List -->
      <div class="row" v-else>
        <div class="col-12">
          <div class="card border-0 shadow-sm">
            <div class="card-header bg-light border-bottom">
              <div class="d-flex justify-content-between align-items-center">
                <h5 class="card-title mb-0">
                  <i class="fas fa-list-alt text-primary me-2"></i>Quotations List
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
                        <div class="fw-semibold">{{ q.societe?.nom || 'N/A' }}</div>
                      </td>
                      <td>
                        <span
                          class="badge bg-secondary bg-opacity-10 text-secondary"
                        >
                          #{{ q.compte?.id || 'N/A' }}
                        </span>
                      </td>
                      <td>
                        <code class="text-dark bg-light px-2 py-1 rounded">{{
                          q.numCompteur
                        }}</code>
                      </td>
                      <td>
                        <span class="badge" :class="getStatusBadgeClass(q.status)">
                          {{ q.status }}
                        </span>
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
const isSubmitting = ref(false);
const errorMessage = ref("");
const successMessage = ref("");

const errors = ref({});

const loadingStates = ref({
  quotations: false,
  societes: false,
  comptes: false
});

const validateForm = () => {
  errors.value = {};
  
  if (!form.value.type) {
    errors.value.type = "Type is required";
  }
  
  if (!form.value.status) {
    errors.value.status = "Status is required";
  }
  
  if (!form.value.societe) {
    errors.value.societe = "Company is required";
  }
  
  if (!form.value.compte) {
    errors.value.compte = "Account is required";
  }
  
  if (!form.value.numCompteur || form.value.numCompteur.trim() === "") {
    errors.value.numCompteur = "Meter number is required";
  }
  
  return Object.keys(errors.value).length === 0;
};

const fetchQuotations = async () => {
  try {
    loadingStates.value.quotations = true;
    clearError();
    const res = await api.get("/demandes-cotation/");
    quotations.value = res.data;
  } catch (err) {
    console.error("Failed to fetch quotations", err);
    errorMessage.value = "Failed to load quotations. Please try again.";
  } finally {
    loadingStates.value.quotations = false;
  }
};

const fetchSocietes = async () => {
  try {
    loadingStates.value.societes = true;
    const res = await api.get("/societes/");
    societes.value = res.data;
  } catch (err) {
    console.error("Failed to fetch societes", err);
    errorMessage.value = "Failed to load companies. Please try again.";
  } finally {
    loadingStates.value.societes = false;
  }
};

const fetchComptes = async () => {
  try {
    loadingStates.value.comptes = true;
    const res = await api.get("/comptes/");
    comptes.value = res.data;
  } catch (err) {
    console.error("Failed to fetch comptes", err);
    errorMessage.value = "Failed to load accounts. Please try again.";
  } finally {
    loadingStates.value.comptes = false;
  }
};

const handleSubmit = async () => {
  if (!validateForm()) {
    return;
  }

  try {
    isSubmitting.value = true;
    clearError();
    clearSuccess();
    
    if (isEditing.value) {
      await api.put(`/demandes-cotation/${form.value.id}/`, form.value);
      successMessage.value = "Quotation updated successfully!";
    } else {
      await api.post("/demandes-cotation/", form.value);
      successMessage.value = "Quotation created successfully!";
    }
    
    resetForm();
    fetchQuotations();
  } catch (err) {
    console.error("Failed to submit form", err);
    
    if (err.response?.data) {
      // Handle server validation errors
      if (typeof err.response.data === 'object') {
        errors.value = err.response.data;
      } else {
        errorMessage.value = err.response.data.message || "Failed to save quotation. Please check your input.";
      }
    } else {
      errorMessage.value = "Network error. Please check your connection and try again.";
    }
  } finally {
    isSubmitting.value = false;
  }
};

const editQuotation = (quotation) => {
  form.value = {
    id: quotation.id,
    type: quotation.type,
    societe: quotation.societe?.id || null,
    compte: quotation.compte?.id || null,
    numCompteur: quotation.numCompteur,
    status: quotation.status,
  };
  isEditing.value = true;
  errors.value = {};
  clearError();
  clearSuccess();

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
  errors.value = {};
  clearError();
  clearSuccess();
};

const clearError = () => {
  errorMessage.value = "";
};

const clearSuccess = () => {
  successMessage.value = "";
};

const getStatusBadgeClass = (status) => {
  switch (status) {
    case 'Validated':
      return 'bg-success';
    case 'Pending':
      return 'bg-warning text-dark';
    default:
      return 'bg-secondary';
  }
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

.btn:hover:not(:disabled) {
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

.alert {
  border: none;
  border-radius: 0.5rem;
}

.form-text.text-warning {
  font-size: 0.875rem;
}

.is-invalid {
  border-color: #dc3545;
}

.invalid-feedback {
  display: block;
}

.spinner-border-sm {
  width: 1rem;
  height: 1rem;
}
</style>
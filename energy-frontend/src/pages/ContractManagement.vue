<template>
  <div>
    <Navbar />

    <div class="container mt-5">
      <!-- Page Header -->
      <div class="d-flex justify-content-between align-items-center mb-4">
        <h2 class="text-primary mb-0">
          <i class="fas fa-file-contract me-2"></i>
          {{ isEditing ? "Modifier un contrat" : "Ajouter un contrat" }}
        </h2>
        <div class="badge bg-primary fs-6">
          {{ contracts.length }} Total Contrats
        </div>
      </div>

      <!-- Error Alert -->
      <div class="row mb-4" v-if="errorMessage">
        <div class="col-12">
          <div class="alert alert-danger alert-dismissible fade show" role="alert">
            <i class="fas fa-exclamation-triangle me-2"></i>
            <strong>Erreur:</strong> {{ errorMessage }}
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

      <!-- Contract Form -->
      <div class="card border-0 shadow-sm mb-5">
        <div class="card-header bg-gradient-primary text-white">
          <h5 class="card-title mb-0">
            <i class="fas fa-{{ isEditing ? 'edit' : 'plus-circle' }} me-2"></i>
            {{ isEditing ? "Modifier" : "Créer" }} un contrat
          </h5>
        </div>
        <div class="card-body p-4">
          <form @submit.prevent="handleSubmit" novalidate class="row g-3">
            <!-- Société -->
            <div class="col-md-6">
              <label class="form-label fw-semibold">
                <i class="fas fa-building text-primary me-1"></i>Société
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
                  {{ loadingStates.societes ? 'Chargement des sociétés...' : 'Choisir une société' }}
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
                Aucune société disponible. Veuillez d'abord ajouter des sociétés.
              </div>
            </div>

            <!-- Fournisseur -->
            <div class="col-md-6">
              <label class="form-label fw-semibold">
                <i class="fas fa-truck text-primary me-1"></i>Fournisseur
                <span class="text-danger">*</span>
              </label>
              <input
                v-model="form.fournisseur"
                type="text"
                class="form-control"
                :class="{ 'is-invalid': errors.fournisseur }"
                placeholder="Nom du fournisseur"
                required
              />
              <div v-if="errors.fournisseur" class="invalid-feedback">
                {{ errors.fournisseur }}
              </div>
            </div>

            <!-- Num Compteur -->
            <div class="col-md-6">
              <label class="form-label fw-semibold">
                <i class="fas fa-barcode text-primary me-1"></i>Numéro du compteur
                <span class="text-danger">*</span>
              </label>
              <input
                v-model="form.numCompteur"
                type="text"
                class="form-control"
                :class="{ 'is-invalid': errors.numCompteur }"
                placeholder="Numéro du compteur"
                required
              />
              <div v-if="errors.numCompteur" class="invalid-feedback">
                {{ errors.numCompteur }}
              </div>
            </div>

            <!-- Statut -->
            <div class="col-md-6">
              <label class="form-label fw-semibold">
                <i class="fas fa-flag text-primary me-1"></i>Statut
                <span class="text-danger">*</span>
              </label>
              <select 
                v-model="form.status" 
                class="form-select"
                :class="{ 'is-invalid': errors.status }"
                required
              >
                <option value="">Sélectionner le statut</option>
                <option value="Pending">En attente</option>
                <option value="Active">Actif</option>
                <option value="Cancelled">Annulé</option>
              </select>
              <div v-if="errors.status" class="invalid-feedback">
                {{ errors.status }}
              </div>
            </div>

            <!-- Date début fourniture -->
            <div class="col-md-6">
              <label class="form-label fw-semibold">
                <i class="fas fa-calendar-plus text-primary me-1"></i>Date début de fourniture
                <span class="text-danger">*</span>
              </label>
              <input
                v-model="form.dateDebutFourniture"
                type="date"
                class="form-control"
                :class="{ 'is-invalid': errors.dateDebutFourniture }"
                :max="form.dateFinFourniture || undefined"
                required
              />
              <div v-if="errors.dateDebutFourniture" class="invalid-feedback">
                {{ errors.dateDebutFourniture }}
              </div>
            </div>

            <!-- Date fin fourniture -->
            <div class="col-md-6">
              <label class="form-label fw-semibold">
                <i class="fas fa-calendar-minus text-primary me-1"></i>Date fin de fourniture
                <span class="text-danger">*</span>
              </label>
              <input
                v-model="form.dateFinFourniture"
                type="date"
                class="form-control"
                :class="{ 'is-invalid': errors.dateFinFourniture }"
                :min="form.dateDebutFourniture || undefined"
                required
              />
              <div v-if="errors.dateFinFourniture" class="invalid-feedback">
                {{ errors.dateFinFourniture }}
              </div>
            </div>

            <div class="col-12 d-flex justify-content-end mt-4 pt-3 border-top">
              <button 
                type="submit" 
                class="btn btn-primary me-2 px-4"
                :disabled="isSubmitting"
              >
                <span v-if="isSubmitting" class="spinner-border spinner-border-sm me-2" role="status"></span>
                <i v-else class="fas fa-{{ isEditing ? 'save' : 'plus' }} me-2"></i>
                {{ isSubmitting ? 'Traitement...' : (isEditing ? 'Modifier' : 'Ajouter') }}
              </button>
              <button
                type="button"
                class="btn btn-outline-secondary px-4"
                @click="resetForm"
                :disabled="isSubmitting"
                v-if="isEditing"
              >
                <i class="fas fa-times me-2"></i>Annuler
              </button>
            </div>
          </form>
        </div>
      </div>

      <!-- Loading State -->
      <div class="card border-0 shadow-sm" v-if="loadingStates.contracts">
        <div class="card-body text-center py-5">
          <div class="spinner-border text-primary mb-3" role="status">
            <span class="visually-hidden">Chargement...</span>
          </div>
          <h5>Chargement des contrats...</h5>
        </div>
      </div>

      <!-- Contracts List -->
      <div class="card border-0 shadow-sm" v-else>
        <div class="card-header bg-light border-bottom">
          <h5 class="card-title mb-0">
            <i class="fas fa-list-alt text-primary me-2"></i>Liste des contrats
          </h5>
        </div>
        <div class="card-body p-0">
          <div class="table-responsive">
            <table class="table table-hover mb-0">
              <thead class="table-light">
                <tr>
                  <th class="ps-4">#</th>
                  <th><i class="fas fa-building me-1"></i>Société</th>
                  <th><i class="fas fa-truck me-1"></i>Fournisseur</th>
                  <th><i class="fas fa-barcode me-1"></i>N° Compteur</th>
                  <th><i class="fas fa-calendar-plus me-1"></i>Début</th>
                  <th><i class="fas fa-calendar-minus me-1"></i>Fin</th>
                  <th><i class="fas fa-flag me-1"></i>Statut</th>
                  <th class="text-center">Actions</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="contracts.length === 0" class="align-middle">
                  <td colspan="8" class="text-center py-5">
                    <div class="text-muted">
                      <i class="fas fa-inbox fa-3x mb-3 opacity-50"></i>
                      <h5>Aucun contrat disponible</h5>
                      <p class="mb-0">
                        Créez votre premier contrat en utilisant le formulaire ci-dessus
                      </p>
                    </div>
                  </td>
                </tr>
                <tr v-for="(contract, index) in contracts" :key="contract.id" class="align-middle">
                  <td class="ps-4 fw-semibold text-muted">{{ index + 1 }}</td>
                  <td>
                    <div class="fw-semibold">{{ contract.societe?.nom || 'N/A' }}</div>
                  </td>
                  <td>
                    <div class="fw-semibold">{{ contract.fournisseur }}</div>
                  </td>
                  <td>
                    <code class="text-dark bg-light px-2 py-1 rounded">{{ contract.numCompteur }}</code>
                  </td>
                  <td>
                    <span class="badge bg-info bg-opacity-10 text-info">
                      {{ formatDate(contract.dateDebutFourniture) }}
                    </span>
                  </td>
                  <td>
                    <span class="badge bg-warning bg-opacity-10 text-warning">
                      {{ formatDate(contract.dateFinFourniture) }}
                    </span>
                  </td>
                  <td>
                    <span class="badge" :class="getStatusBadgeClass(contract.status)">
                      {{ getStatusLabel(contract.status) }}
                    </span>
                  </td>
                  <td class="text-center">
                    <button
                      class="btn btn-sm btn-outline-primary"
                      @click="editContract(contract)"
                      title="Modifier le contrat"
                    >
                      <i class="fas fa-edit me-1"></i> Modifier
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
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

const contracts = ref([]);
const societes = ref([]);
const isEditing = ref(false);
const isSubmitting = ref(false);
const errorMessage = ref("");
const successMessage = ref("");

const errors = ref({});

const loadingStates = ref({
  contracts: false,
  societes: false
});

const form = ref({
  id: null,
  societe: null,
  fournisseur: "",
  numCompteur: "",
  dateDebutFourniture: "",
  dateFinFourniture: "",
  status: "Pending",
});

const validateForm = () => {
  errors.value = {};
  
  if (!form.value.societe) {
    errors.value.societe = "La société est requise";
  }
  
  if (!form.value.fournisseur || form.value.fournisseur.trim() === "") {
    errors.value.fournisseur = "Le fournisseur est requis";
  }
  
  if (!form.value.numCompteur || form.value.numCompteur.trim() === "") {
    errors.value.numCompteur = "Le numéro du compteur est requis";
  }
  
  if (!form.value.dateDebutFourniture) {
    errors.value.dateDebutFourniture = "La date de début est requise";
  }
  
  if (!form.value.dateFinFourniture) {
    errors.value.dateFinFourniture = "La date de fin est requise";
  }
  
  if (!form.value.status) {
    errors.value.status = "Le statut est requis";
  }
  
  // Validate date range
  if (form.value.dateDebutFourniture && form.value.dateFinFourniture) {
    const startDate = new Date(form.value.dateDebutFourniture);
    const endDate = new Date(form.value.dateFinFourniture);
    
    if (startDate >= endDate) {
      errors.value.dateFinFourniture = "La date de fin doit être postérieure à la date de début";
    }
  }
  
  return Object.keys(errors.value).length === 0;
};

const fetchContracts = async () => {
  try {
    loadingStates.value.contracts = true;
    clearError();
    const res = await api.get("/ventepro/");
    contracts.value = res.data;
  } catch (err) {
    console.error("Erreur lors du chargement des contrats", err);
    errorMessage.value = "Impossible de charger les contrats. Veuillez réessayer.";
  } finally {
    loadingStates.value.contracts = false;
  }
};

const fetchSocietes = async () => {
  try {
    loadingStates.value.societes = true;
    const res = await api.get("/societes/");
    societes.value = res.data;
  } catch (err) {
    console.error("Erreur lors du chargement des sociétés", err);
    errorMessage.value = "Impossible de charger les sociétés. Veuillez réessayer.";
  } finally {
    loadingStates.value.societes = false;
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
      await api.put(`/ventepro/${form.value.id}/`, form.value);
      successMessage.value = "Contrat modifié avec succès !";
    } else {
      await api.post("/ventepro/", form.value);
      successMessage.value = "Contrat créé avec succès !";
    }
    
    resetForm();
    fetchContracts();
  } catch (err) {
    console.error("Erreur lors de l'envoi du formulaire", err);
    
    if (err.response?.data) {
      // Handle server validation errors
      if (typeof err.response.data === 'object') {
        errors.value = err.response.data;
      } else {
        errorMessage.value = err.response.data.message || "Erreur lors de l'enregistrement du contrat. Vérifiez vos données.";
      }
    } else {
      errorMessage.value = "Erreur de réseau. Vérifiez votre connexion et réessayez.";
    }
  } finally {
    isSubmitting.value = false;
  }
};

const editContract = (contract) => {
  form.value = {
    id: contract.id,
    societe: contract.societe?.id || null,
    fournisseur: contract.fournisseur,
    numCompteur: contract.numCompteur,
    dateDebutFourniture: contract.dateDebutFourniture,
    dateFinFourniture: contract.dateFinFourniture,
    status: contract.status,
  };
  isEditing.value = true;
  errors.value = {};
  clearError();
  clearSuccess();
  window.scrollTo({ top: 0, behavior: "smooth" });
};

const resetForm = () => {
  form.value = {
    id: null,
    societe: null,
    fournisseur: "",
    numCompteur: "",
    dateDebutFourniture: "",
    dateFinFourniture: "",
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
    case 'Active':
      return 'bg-success';
    case 'Pending':
      return 'bg-warning text-dark';
    case 'Cancelled':
      return 'bg-danger';
    default:
      return 'bg-secondary';
  }
};

const getStatusLabel = (status) => {
  switch (status) {
    case 'Active':
      return 'Actif';
    case 'Pending':
      return 'En attente';
    case 'Cancelled':
      return 'Annulé';
    default:
      return status;
  }
};

const formatDate = (dateString) => {
  if (!dateString) return 'N/A';
  
  try {
    return new Date(dateString).toLocaleDateString('fr-FR', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  } catch (error) {
    return dateString;
  }
};

onMounted(() => {
  fetchContracts();
  fetchSocietes();
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
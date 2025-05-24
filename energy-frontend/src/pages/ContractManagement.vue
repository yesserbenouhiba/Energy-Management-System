<template>
  <div>
    <Navbar />

    <div class="container mt-5">
      <h2 class="mb-4">
        {{ isEditing ? "Modifier un contrat" : "Ajouter un contrat" }}
      </h2>

      <form @submit.prevent="handleSubmit" class="row g-3">
        <!-- Société -->
        <div class="col-md-6">
          <label class="form-label">Société</label>
          <select v-model="form.societe" class="form-select" required>
            <option value="" disabled>Choisir une société</option>
            <option v-for="s in societes" :key="s.id" :value="s.id">
              {{ s.nom }}
            </option>
          </select>
        </div>

        <!-- Fournisseur -->
        <div class="col-md-6">
          <label class="form-label">Fournisseur</label>
          <input
            v-model="form.fournisseur"
            type="text"
            class="form-control"
            placeholder="Nom du fournisseur"
            required
          />
        </div>

        <!-- Num Compteur -->
        <div class="col-md-6">
          <label class="form-label">Numéro du compteur</label>
          <input
            v-model="form.numCompteur"
            type="text"
            class="form-control"
            placeholder="Compteur"
            required
          />
        </div>

        <!-- Date début fourniture -->
        <div class="col-md-6">
          <label class="form-label">Date début de fourniture</label>
          <input
            v-model="form.dateDebutFourniture"
            type="date"
            class="form-control"
            required
          />
        </div>

        <!-- Date fin fourniture -->
        <div class="col-md-6">
          <label class="form-label">Date fin de fourniture</label>
          <input
            v-model="form.dateFinFourniture"
            type="date"
            class="form-control"
            required
          />
        </div>

        <!-- Statut -->
        <div class="col-md-6">
          <label class="form-label">Statut</label>
          <select v-model="form.status" class="form-select" required>
            <option value="Pending">Pending</option>
            <option value="Active">Active</option>
            <option value="Cancelled">Cancelled</option>
          </select>
        </div>

        <div class="col-12">
          <button type="submit" class="btn btn-primary">
            {{ isEditing ? "Modifier" : "Ajouter" }}
          </button>
          <button
            type="button"
            class="btn btn-secondary ms-2"
            @click="resetForm"
            v-if="isEditing"
          >
            Annuler
          </button>
        </div>
      </form>

      <hr class="my-5" />

      <h2 class="mb-4">Liste des contrats</h2>
      <div class="table-responsive">
        <table class="table table-bordered align-middle text-center">
          <thead class="table-light">
            <tr>
              <th>#</th>
              <th>Société</th>
              <th>Fournisseur</th>
              <th>Numéro Compteur</th>
              <th>Début</th>
              <th>Fin</th>
              <th>Statut</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-if="contracts.length === 0">
              <td colspan="8">Aucun contrat trouvé.</td>
            </tr>
            <tr v-for="(contract, index) in contracts" :key="contract.id">
              <td>{{ index + 1 }}</td>
              <td>{{ contract.societe.nom }}</td>
              <td>{{ contract.fournisseur }}</td>
              <td>{{ contract.numCompteur }}</td>
              <td>{{ contract.dateDebutFourniture }}</td>
              <td>{{ contract.dateFinFourniture }}</td>
              <td>{{ contract.status }}</td>
              <td>
                <button
                  class="btn btn-sm btn-outline-primary"
                  @click="editContract(contract)"
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
</template>

<script setup>
import { ref, onMounted } from "vue";
import Navbar from "../components/Navbar.vue";
import api from "../axios";

const contracts = ref([]);
const societes = ref([]);
const isEditing = ref(false);

const form = ref({
  id: null,
  societe: null,
  fournisseur: "",
  numCompteur: "",
  dateDebutFourniture: "",
  dateFinFourniture: "",
  status: "Pending",
});

const fetchContracts = async () => {
  try {
    const res = await api.get("/ventepro/");
    contracts.value = res.data;
  } catch (err) {
    console.error("Erreur lors du chargement des contrats", err);
  }
};

const fetchSocietes = async () => {
  try {
    const res = await api.get("/societes/");
    societes.value = res.data;
  } catch (err) {
    console.error("Erreur lors du chargement des sociétés", err);
  }
};

const handleSubmit = async () => {
  try {
    if (isEditing.value) {
      await api.put(`/ventepro/${form.value.id}/`, form.value);
    } else {
      await api.post("/ventepro/", form.value);
    }
    resetForm();
    fetchContracts();
  } catch (err) {
    console.error("Erreur lors de l'envoi du formulaire", err);
  }
};

const editContract = (contract) => {
  form.value = {
    id: contract.id,
    societe: contract.societe.id,
    fournisseur: contract.fournisseur,
    numCompteur: contract.numCompteur,
    dateDebutFourniture: contract.dateDebutFourniture,
    dateFinFourniture: contract.dateFinFourniture,
    status: contract.status,
  };
  isEditing.value = true;
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
};

onMounted(() => {
  fetchContracts();
  fetchSocietes();
});
</script>

<style scoped>
.table th,
.table td {
  vertical-align: middle;
}
</style>

<template>
  <div m="5">
    <b-col lg="6" class="my-1">
      <b-form-group
          label="Filter"
          label-for="filter-input"
          label-cols-sm="3"
          label-align-sm="right"
          label-size="sm"
          class="mb-0"
      >
        <b-form-select
            size="sm"
            v-model="filter"
            :options="specialtiesChoices"
        >
          <template #first>
            <b-form-select-option :value="null">-- Please select an option --</b-form-select-option>
          </template>
        </b-form-select>
      </b-form-group>
    </b-col>
    <b-table
        striped
        hover
        :current-page="currentPage"
        :per-page="perPage"
        :items="items"
        :fields="fields"
        :filter="filter"
        :filter-included-fields="filterOn"
        @filtered="onFiltered"
    >
    </b-table>
    <b-row>
      <b-col sm="1" md="1" class="my-1">
        <b-form-group class="mb-0">
          <b-form-select
              id="per-page-select"
              v-model="perPage"
              :options="pageOptions"
              size="sm"
          ></b-form-select>
        </b-form-group>
      </b-col>

      <b-col offset="7" sm="4" md="4" class="my-1">
        <b-pagination
            v-model="currentPage"
            :total-rows="totalRows"
            :per-page="perPage"
            :limit=3
            align="right"
            size="sm"
            class="my-0"
            last-number
        ></b-pagination>
      </b-col>
    </b-row>
  </div>
</template>

<script>
const api_url = 'http://127.0.0.1:8000/api/';
const kols_api_url = api_url + 'kols/'

const axios = require("axios");
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

export default {
  name: 'Kols',
  data() {
    return {
      // Note 'isActive' is left out and will not appear in the rendered table
      fields: [
        {
          key: 'full_name',
          label: 'Name, credential',
          sortable: true
        },
        {
          key: 'specialty',
          sortable: false
        },
      ],
      items: [
        {full_name: 'Larsen', specialty: 'Shaw'},
        {full_name: 'Geneva', specialty: 'Wilson'},
        {full_name: 'Jami', specialty: 'Carney'}
      ],
      filter: null,
      filterOn: [],
      specialtiesChoices: [],
      totalRows: 1,
      currentPage: 1,
      perPage: 5,
      pageOptions: [5, 10, 50, 100],
    }
  },
  beforeMount() {
    this.getSpecialties();
    this.getKols();
  },
  methods: {
    getKols() {
      axios.get(kols_api_url)
          .then(result => {
            this.items = result.data;
            this.totalRows = this.items.length;
          })
    },
    getSpecialties() {
      axios.get(kols_api_url + 'specialties/')
          .then(result => this.specialtiesChoices = result.data.specialties)
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length
      this.currentPage = 1
    }
  }
}
</script>

<style scoped>

</style>
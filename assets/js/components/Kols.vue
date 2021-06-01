<template>
  <div>
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
          </b-form-select>
        </b-form-group>
    </b-col>
    <b-table
        striped
        hover
        :items="items"
        :fields="fields"
        :filter="filter"
        :filter-included-fields="filterOn"
    >
    </b-table>
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
    }
  },
  computed: {
      sortOptions() {
        // Create an options list from our fields
        return this.fields
          .filter(f => f.sortable)
          .map(f => {
            return { text: f.label, value: f.key }
          })
      }
  },
  beforeMount(){
    this.getSpecialties();
    this.getKols();
  },
  methods: {
    getKols(){
      axios.get(kols_api_url)
          .then(result => this.items=result.data)
    },
    getSpecialties(){
      axios.get(kols_api_url + 'specialties/')
          .then(result => this.specialtiesChoices=result.data.specialties)
    },
  }
}
</script>

<style scoped>

</style>
<template>
  <div>
    <!--  KOLS ACTIONS  -->
    <div align="right">
      <b-button class="mr-1">Delete HCP</b-button>
      <b-button class="mr-1">Button 2</b-button>
      <b-button class="mr-1">Button 3</b-button>
      <b-button class="mr-1">Button 4</b-button>
      <b-button>Button 3</b-button>
    </div>
    <!--  END KOLS ACTIONS  -->

    <!--  FILTERS  -->
    <b-row>
      <b-col lg="3" class="my-1">
        <b-form-group class="mb-0">
          <b-input-group size="sm">
            <b-form-input
                id="filter-input"
                v-model="filters.search"
                type="search"
                placeholder="Type to Search"
            ></b-form-input>
          </b-input-group>
        </b-form-group>
      </b-col>

      <b-col lg="2" class="my-1">
        <b-form-group
            class="mb-0"
        >
          <b-form-select
              size="sm"
              v-model="filters.specialty"
              :options="specialtiesChoices"
          >
            <template #first>
              <b-form-select-option :value="null">
                Specialty filter
              </b-form-select-option>
            </template>
          </b-form-select>
        </b-form-group>
      </b-col>
    </b-row>
    <!--  END FILTERS  -->

    <!--  TABLE  -->
    <b-table
        striped
        hover
        :current-page="currentPage"
        :per-page="perPage"
        :items="filtered"
        :fields="fields"
        :filter-included-fields="filterOn"
        selectable
        :select-mode="selectMode"
        @row-selected="onRowSelected"
    >
      <template #cell(selected)="{ rowSelected }">
        <template v-if="rowSelected">
          <span aria-hidden="true">&check;</span>
          <span class="sr-only">Selected</span>
        </template>
        <template v-else>
          <span aria-hidden="true">&nbsp;</span>
          <span class="sr-only">Not selected</span>
        </template>
      </template>
    </b-table>
    <!--  END TABLE  -->


    <!-- PAGINATION  -->
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
    <!-- END PAGINATION  -->
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
          key: "selected",
          label: "",
          sortable: false,
        },
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
      filters: {
        search: null,
        specialty: null
      },
      selectMode: 'multi',
      selected: [],
      filterOn: [],
      specialtiesChoices: [],
      totalRows: 1,
      currentPage: 1,
      perPage: 5,
      pageOptions: [5, 10, 50, 100],
    }
  },

  computed: {
    filtered() {
      const filtered = this.items.filter(item => {
        return Object.keys(this.filters).every(function (key) {
          const filterValue = this.filters[key];
          if (filterValue === null || filterValue === '') {
            return true
          }
          if (key === 'search') {
            return Object.values(item).some(element => String(element).includes(filterValue))
          }
          return String(item[key]).includes(filterValue);
        }.bind(this))
      })

      if (filtered.length > 0) {
        this.totalRows = filtered.length
        this.currentPage = 1
        return filtered
      }

      return [{
        full_name: '',
        specialty: ''
      }]
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

    onRowSelected(items) {
      this.selected = items
    },
  }
}
</script>

<style scoped>

</style>
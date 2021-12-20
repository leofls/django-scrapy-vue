<template>
  <div id="app">
    <form @submit.prevent="submitForm">
      <div class="form-group row">
        <input
          type="text"
          class="form-control col-3 mx-2"
          placeholder="Author"
          v-model="quote.author"
        />
        <!-- <input type="text" class="form-control col-4 mx-2" placeholder="text"> -->
        <textarea
          class="form-control col-7 mx-2"
          name="text"
          placeholder="Texto"
          id=""
          rows="1"
          v-model="quote.text"
        ></textarea>

        <button class="btn btn-success col">Enviar</button>
      </div>
    </form>
    <h4 class="text-center text-muted">Dê 2 cliques para selecionar uma citação e editar  </h4>
    <table class="table">
      <thead>
        <tr>
          <th width="150px">Autor</th>
          <th>Texto</th>
          <th width="60px">Excluir</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="quote in quotes"
          :key="quote.id"
          @dblclick="$data.quote = quote"
        >
          <td>{{ quote.author }}</td>
          <td>{{ quote.text }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteQuote(quote)">X</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      quote: {},
      quotes: [],
    };
  },
  async created() {
    await this.getQuotes();
  },
  methods: {
    submitForm() {
      if (this.quote.id === undefined) {
        this.createQuote();
      } else {
        this.editQuote();
      }
    },
    async getQuotes() {
      var response = await fetch("http://localhost:8000/api/quotes/");
      this.quotes = await response.json();
    },
    async createQuote() {
      await this.getQuotes();

      await fetch("http://localhost:8000/api/quotes/", {
        method: "post",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.quote),
      });

      await this.getQuotes();
    },
    async editQuote() {
      await this.getQuotes();

      await fetch(`http://localhost:8000/api/quotes/${this.quote.id}/`, {
        method: "put",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.quote),
      });

      await this.getQuotes();
      this.quote = {};
    },
    async deleteQuote(quote) {
      
      if(confirm("Deseja realmente deletar?")){
        await this.getQuotes();

        await fetch(`http://localhost:8000/api/quotes/${quote.id}/`, {
          method: "delete",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(this.quote),
        });

        await this.getQuotes();
        this.quote = {};
      }
      
    },
  },
 
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

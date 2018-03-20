<template>
  <div id="app">
    <app-header>
    </app-header>
    <app-score-table></app-score-table>
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import ScoreTable from './components/ScoreTable.vue'

export default {
  name: 'App',
  components: {
    appHeader: Header,
    appScoreTable: ScoreTable,
    appFooter: Footer
  }
}
</script>

<style>
</style>

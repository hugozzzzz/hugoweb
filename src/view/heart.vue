<template>
  <div class="container">
    <div class="heart"></div>
  </div>
</template>

<script>
  export default {
    components: {},
    data() {
      return {

      };
    },
    computed: {},
    watch: {},
    methods: {},
    created() {},
    mounted() {},
    beforeCreate() {},
    beforeMount() {},
    beforeUpdate() {},
    updated() {},
    beforeDestroy() {},
    destroyed() {},
    activated() {},
  }

</script>
<style scoped>
  .container {
    margin: 0 auto;
    width: 300px;
    height: 300px;
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    background-image: radial-gradient(#FFC0CB, #FF8888);
    border: 4px solid rgba(255, 0, 0, 0.9);
    border-radius: 10%;
  }

  .heart {
    width: 100px;
    height: 100px;
    background-color: #FF6347;
    position: relative;
    animation: beat 0.6s infinite;
  }

  .heart:before,
  .heart:after {
    content: "";
    position: absolute;
    width: 100px;
    height: 100px;
    background-color: #FF6347;
    border-radius: 50%;
  }

  .heart:before {
    left: 50px;
  }

  .heart:after {
    top: -50px;
    left:0px;
  }

  @keyframes beat {
    0% {
      transform: scale(1) rotate(-45deg);
    }

    40% {
      transform: scale(1.1) rotate(-45deg);
    }

    55% {
      transform: scale(1.3) rotate(-30deg);
    }

    70% {
      transform: scale(1.1) rotate(-45deg);
    }

    85% {
      transform: scale(1.3) rotate(-60deg);
    }

    100% {
      transform: scale(1) rotate(-45deg);
    }
  }

</style>

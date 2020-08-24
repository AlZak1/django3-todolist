new Vue({
  el:'#orders_app',
  data:{
    orders: []
  },
  created: function(){
    const vm = this;
    axios.get('/api/todos/')
    .then(function (response){
    vm.orders = response.data
    })
  }

}

)

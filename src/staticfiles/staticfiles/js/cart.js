console.log("Hello WORLD")
console.log("Hello WORLD")
var updateBtns =[]

 updateBtns= document.getElementsByClassName('update-cart')

for (var i = 0; i <updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        console.log('USER:', user)

        if (user == 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(productId, action)
        }
    })
}

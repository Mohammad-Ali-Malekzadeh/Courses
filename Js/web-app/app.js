console.log(uuid())

let products = []

const filters = {
    searchItem: '',
    availableProducts: false
}

if (localStorage.getItem('products') !== null) {
    products = JSON.parse(localStorage.getItem('products'))
}

renderProducts(products, filters)

document.querySelector('#search-products').addEventListener('input', function(e) {
    filters.searchItem = e.target.value
    renderProducts(products, filters)
})

document.querySelector('#add-product-form').addEventListener('submit', function(e) {
    e.preventDefault()
    products.push({
        id: uuid(),
        title: e.target.elements.productTitle.value,
        exist: true
    })
    renderProducts(products, filters)
    saveProducts(products)
    e.target.elements.productTitle.value = ''
})

document.querySelector('#available-products').addEventListener('change', function(e) {
    filters.availableProducts = e.target.checked
    renderProducts(products, filters)
})
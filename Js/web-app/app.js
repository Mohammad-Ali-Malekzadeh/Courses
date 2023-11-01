let products = []

const filters = {
    searchItem: '',
    availableProducts: false
}

if (localStorage.getItem('products') !== null) {
    products = JSON.parse(localStorage.getItem('products'))
}

const renderProducts = function(products, filters) {
    
    let filteredProducts = products.filter(function(item) {
        return item.title.toLowerCase().includes(filters.searchItem.toLowerCase())
    })
    filteredProducts = filteredProducts.filter(function(item) {
        if(filters.availableProducts) {
            return item.exist
        } else {
            return true
        }
    })
    document.querySelector('#products').innerHTML = ''
    filteredProducts.forEach(function(item) {
        const productEl = document.createElement('p')
        productEl.textContent = item.title
        document.querySelector('#products').appendChild(productEl)
    })
}

renderProducts(products, filters)

document.querySelector('#search-products').addEventListener('input', function(e) {
    filters.searchItem = e.target.value
    renderProducts(products, filters)
})

document.querySelector('#add-product-form').addEventListener('submit', function(e) {
    e.preventDefault()
    products.push({
        title: e.target.elements.productTitle.value,
        exist: true
    })
    renderProducts(products, filters)
    localStorage.setItem('products', JSON.stringify(products))
    e.target.elements.productTitle.value = ''
})

document.querySelector('#available-products').addEventListener('change', function(e) {
    filters.availableProducts = e.target.checked
    renderProducts(products, filters)
})
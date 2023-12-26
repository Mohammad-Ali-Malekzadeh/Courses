const getSaveProducts = function () {
    const productJSON = localStorage.getItem('products')
    if (productJSON !== null) {
        products = JSON.parse(productJSON)
    }
}

const saveProducts = function (products) {
    localStorage.setItem('products', JSON.stringify(products))
}

const removeProducts = function (id) {
    const productIndex = products.findIndex(function (item) {
        return item.id == id
    })
    if (productIndex > -1) {
        products.splice(productIndex, 1)
    }
}

const toggleProduct = function (id, exist) {
    const productIndex = products.findIndex(function (item) {
        return item.id == id
    })
    products[productIndex].exist = !exist
}

const renderProducts = function (products, filters) {

    let filteredProducts = products.filter(function (item) {
        return item.title.toLowerCase().includes(filters.searchItem.toLowerCase())
    })
    filteredProducts = filteredProducts.filter(function (item) {
        if (filters.availableProducts) {
            return item.exist
        } else {
            return true
        }
    })
    document.querySelector('#products').innerHTML = ''
    filteredProducts.forEach(function (item) {
        document.querySelector('#products').appendChild(createProductDOM(item))
    })
}

const createProductDOM = function (product) {
    const productEl = document.createElement('div')
    const checkbox = document.createElement('input')
    const productItem = document.createElement('a')
    const removeButton = document.createElement('button')

    checkbox.setAttribute('type', 'checkbox')
    checkbox.checked = !product.exist
    productEl.appendChild(checkbox)
    checkbox.addEventListener('change', function (e) {
        toggleProduct(product.id ,e.target.checked)
        saveProducts(products)
        renderProducts(products, filters)
    })

    productItem.textContent = product.title
    productItem.setAttribute('href', `./edit-product.html#${product.id}`)
    productEl.appendChild(productItem)

    removeButton.textContent = 'Remove'    
    productEl.appendChild(removeButton)
    removeButton.addEventListener('click', function () {
        removeProducts(product.id)
        saveProducts(products)
        renderProducts(products, filters)
    })

    return productEl
}
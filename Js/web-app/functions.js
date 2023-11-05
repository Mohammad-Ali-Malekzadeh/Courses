const getSaveProducts = function () {
    const productJSON = localStorage.getItem('products')
    if (productJSON !== null) {
        products = JSON.parse(productJSON)
    }
}

const saveProducts = function (products) {
    localStorage.setItem('products', JSON.stringify(products))
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
    const productItem = document.createElement('span')
    const removeButton = document.createElement('button')

    checkbox.setAttribute('type', 'checkbox')
    productEl.appendChild(checkbox)

    productItem.textContent = product.title
    productEl.appendChild(productItem)

    removeButton.textContent = 'Remove'    
    productEl.appendChild(removeButton)

    return productEl
}
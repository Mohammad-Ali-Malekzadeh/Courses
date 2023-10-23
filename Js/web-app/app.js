/* const product = {
    title: 'Book',
    price: 79
}

const productJSON = JSON.stringify(product)

localStorage.setItem('product', productJSON) */

const productJSON = localStorage.getItem('product')

const product = JSON.parse(productJSON)

console.log(`Title: ${product.title} - Price: ${product.price}`)
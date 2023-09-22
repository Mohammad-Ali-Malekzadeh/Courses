document.querySelector('#add-product-form').addEventListener('submit', (e) => {
    e.preventDefault()
    console.log(e.target.elements.ProductTitle.value)
    e.target.elements.ProductTitle.value = ''
})
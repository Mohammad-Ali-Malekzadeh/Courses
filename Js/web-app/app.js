const paragraphs = document.querySelectorAll('p')
let findWord = paragraphs.forEach((item) => {
    if (item.textContent.toLowerCase().includes('js')) {
        item.remove()
    }
})

console.log(findWord)
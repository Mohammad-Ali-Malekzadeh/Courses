let backdrop = document.querySelector('.backdrop')
let modal = document.querySelector('.modal')
let selectPlanBTN = document.querySelectorAll('.plan button')
let modalCloseBTN = document.querySelector('.modal__action--neagative')

for (let i = 0; i < selectPlanBTN.length; i++) {
    selectPlanBTN[i].addEventListener('click', () => {
        modal.style.display = 'block'
        backdrop.style.display = 'block'
    })
}

modalCloseBTN.addEventListener('click', () => {
    modal.style.display = 'none'
    backdrop.style.display = 'none'
})
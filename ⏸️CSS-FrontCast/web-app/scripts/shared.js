let backdrop = document.querySelector('.backdrop')
let modal = document.querySelector('.modal')
let selectPlanBTN = document.querySelectorAll('.plan button')
let modalCloseBTN = document.querySelector('.modal__action--neagative')

for (let i = 0; i < selectPlanBTN.length; i++) {
    selectPlanBTN[i].addEventListener('click', () => {
        modal.classList.add('open')
        backdrop.classList.add('open')
    })
}

modalCloseBTN.addEventListener('click', () => {
    modal.classList.remove('open')
    backdrop.classList.remove('open')
})
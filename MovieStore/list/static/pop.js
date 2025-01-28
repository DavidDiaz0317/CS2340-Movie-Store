const modal = document.querySelector('.modalContainer');
const openModal = document.querySelector('.open');
const closeModal = document.querySelector('.close');

openModal.addEventListener('click', () => {
    modal.showModal();
})
closeModal.addEventListener('click', () => {
    modal.close();
} )
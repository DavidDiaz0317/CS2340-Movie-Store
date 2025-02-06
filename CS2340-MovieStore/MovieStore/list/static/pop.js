document.addEventListener("DOMContentLoaded", function () {


    const modal = document.querySelector('.modal');

    const closeModal = document.querySelector('.close-button');
    const openModals = document.querySelectorAll(".open_button");

    const modalTitle = document.getElementById("modal-title");
    const modalPlot = document.getElementById("modal-plot");
    const modalDirector = document.getElementById("modal-director");
    const modalGenre = document.getElementById("modal-genre");
    const modalImage = document.getElementById("modal-image");
    const modalYear = document.getElementById("modal-year");

    const searchInput = document.getElementById("search-field");
    const searchButton = document.getElementById("search-button");

    if (openModals && closeModal && modal) {

        openModals.forEach(button => {
            button.addEventListener("click", function () {

                const movieTitle = this.getAttribute("data-title");
                const moviePlot = this.getAttribute("data-plot");
                const movieDirector = this.getAttribute("data-director");
                const movieGenre = this.getAttribute("data-genre");
                const moviePosterUrl = this.getAttribute("data-poster");
                const movieYear = this.getAttribute("data-year")

                modalTitle.textContent = movieTitle;
                modalPlot.textContent = `Plot: ${moviePlot}`;
                modalDirector.textContent = `Director: ${movieDirector}`;
                modalGenre.textContent = `Genre: ${movieGenre}`;
                modalImage.src = moviePosterUrl;
                modalImage.alt = `Poster for ${movieTitle}`;
                modalYear.textContent = `Year : ${movieYear}`;

                modal.showModal();
                modalImage.focus();
            })
        })

        closeModal.addEventListener("click", () => {
            modal.close();
        })


        searchButton.addEventListener("click", function () {
            const search = searchInput.value.trim().toLowerCase();
            if (!search) return;

            let found = false;

            openModals.forEach(button => {
                const title = button.getAttribute("data-title").toLowerCase();
                if (title.includes(search)) {
                    button.click();
                    found = true;
                }
            })
            if (!found) {
                alert("No movie found for: " + search);
            }
        })
        searchInput.addEventListener('keydown', function (event) {
            if (event.key === 'Enter') {
                event.preventDefault();
                searchButton.click();
            }
});
    } else {
        console.error("JS error");
    }
});
(function() {

    const btnDelete = document.querySelectorAll(".btnDelete")

    btnDelete.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmation = confirm('¿Seguro que desea eliminar?');
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });

})();
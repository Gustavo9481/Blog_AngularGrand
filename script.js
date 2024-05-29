
document.addEventListener('DOMContentLoaded', (event) => {
    const menuButton = document.getElementById('menuButton');
    const dropdownMenu = document.getElementById('dropdownMenu');

    menuButton.addEventListener('click', () => {
        if (dropdownMenu.classList.contains('show')) {
            dropdownMenu.classList.remove('show');
            setTimeout(() => {
                dropdownMenu.style.display = 'none';
            }, 200); // Tiempo en milisegundos que coincide con la duración de la animación
        } else {
            dropdownMenu.style.display = 'flex';
            setTimeout(() => {
                dropdownMenu.classList.add('show');
            }, 10); // Un pequeño retraso para permitir que el display: flex se aplique antes de la animación
        }
    });
});

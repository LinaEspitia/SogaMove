document.addEventListener("DOMContentLoaded", function() {
    const menu = document.getElementById('menu');
    const menuContent = document.getElementById('menu-content');

    menuContent.style.display = 'none';

    menu.addEventListener('click', function(event) {
        // Alternar la visibilidad del menú
        menuContent.style.display = menuContent.style.display === 'block' ? 'none' : 'block';
        event.stopPropagation();
    });

    document.addEventListener('click', function() {

        menuContent.style.display = 'none';
    });


    menuContent.addEventListener('click', function(event) {
        event.stopPropagation();
    });
});

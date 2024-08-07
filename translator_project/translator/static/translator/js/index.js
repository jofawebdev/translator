document.addEventListener('DOMContentLoaded', function() {
    var logoutLink = document.getElementById('logoutLink');
    var lastScrollTop = 0;

    window.addEventListener('scroll', function() {
        var scrollTop = window.pageYOffset || document.documentElement.scrollTop;

        if (scrollTop > lastScrollTop) {
            // Scrolling Down
            logoutLink.classList.add('hidden');
        } else {
            // Scrolling Up
            logoutLink.classList.remove('hidden');
        }
        lastScrollTop = scrollTop;
    });
});
document.addEventListener('DOMContentLoaded', function () {
    if (typeof Swiper === 'undefined') {
        return;
    }

    const heroEl = document.querySelector('.hero-swiper');
    if (heroEl) {
        new Swiper('.hero-swiper', {
            loop: true,
            autoplay: {
                delay: 5500,
                disableOnInteraction: false,
            },
            effect: 'fade',
            fadeEffect: { crossFade: true },
            speed: 900,
            pagination: {
                el: '.hero-swiper-pagination',
                clickable: true,
            },
            navigation: {
                prevEl: '.hero-swiper-prev',
                nextEl: '.hero-swiper-next',
            },
        });
    }

    const blogEl = document.querySelector('.blog-swiper');
    if (blogEl) {
        new Swiper('.blog-swiper', {
            loop: true,
            autoplay: {
                delay: 6000,
                disableOnInteraction: false,
            },
            speed: 700,
            spaceBetween: 24,
            slidesPerView: 1,
            breakpoints: {
                640: { slidesPerView: 2 },
                1024: { slidesPerView: 3 },
            },
            navigation: {
                prevEl: '.blog-swiper-prev',
                nextEl: '.blog-swiper-next',
            },
        });
    }
});

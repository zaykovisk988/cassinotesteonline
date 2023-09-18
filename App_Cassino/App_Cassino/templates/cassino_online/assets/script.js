
var slideIndex = 0;

function showSlides() {
    var slides = document.getElementsByClassName("slide");
    for (var i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].classList.add("active");
    setTimeout(showSlides, 2000); // Muda a imagem a cada dois segundos
}

showSlides();
var games = document.getElementsByClassName('game');
var scrollLeft = document.getElementById('scrollLeft');
var scrollRight = document.getElementById('scrollRight');
var index = 0;

function updateDisplay() {
    for (var i = 0; i < games.length; i++) {
        if (i >= index && i < index + 5) {
            games[i].style.display = 'block';
        } else {
            games[i].style.display = 'none';
        }
    }
}

scrollLeft.addEventListener('click', function () {
    if (index > 0) {
        index--;
        updateDisplay();
    }
});

scrollRight.addEventListener('click', function () {
    if (index < games.length - 5) {
        index++;
        updateDisplay();
    }
});

updateDisplay();
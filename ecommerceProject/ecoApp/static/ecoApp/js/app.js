// Initialize the carousel with JavaScript

document.addEventListener("DOMContentLoaded", function () {
  let myCarousel = document.getElementById("carouselExampleCaptions");
  let carousel = new bootstrap.Carousel(myCarousel, {
    interval: 2000, //2 seconds
  });
});

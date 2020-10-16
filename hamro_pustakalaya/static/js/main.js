//init dynamic year
$("#year").text(new Date().getFullYear());

// Decreases sticky menu backgorund opacity
window.addEventListener("scroll", function () {
  if (window.scrollY > 50) {
    document.querySelector("#nav-section").style.opacity = 0.8;
  } else {
    document.querySelector("#nav-section").style.opacity = 1;
  }
});

//init slick slider
$(".autoplay").slick({
  dots: true,
  infinite: true,
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
  arrows: false,
  mobileFirst: true,
});

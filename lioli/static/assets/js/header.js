$(window).scroll(function () {
  if ($(this).scrollTop() > 50) {
    $(".navbar").addClass("scrolled");
  } else {
    $(".navbar").removeClass("scrolled");
  }
});


/**Momentum Scroll**/
$("html").easeScroll();
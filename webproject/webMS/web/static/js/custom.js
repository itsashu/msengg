// PRELOADER JS
$(window).load(function(){
    $('.preloader').fadeOut(1000); // set duration in brackets    
});


// jQuery to collapse the navbar on scroll //
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});


/* HTML document is loaded. DOM is ready. 
-------------------------------------------*/
$(function(){

  // ------- WOW ANIMATED ------ //
  wow = new WOW(
  {
    mobile: false
  });
  wow.init();


  // HIDE MOBILE MENU AFTER CLIKING ON A LINK
  $('.navbar-collapse a').click(function(){
        $(".navbar-collapse").collapse('hide');
    });


  // HOME BACKGROUND SLIDESHOW
  $(function(){
    jQuery(document).ready(function() {
    $('#home').backstretch([
       "static/images/home-bg-slideshow1.jpg", 
       "static/images/home-images/index.jpg",
       "static/images/home-images/index1.jpg",
       //"static/images/home-images/index2.jpg",
       "static/images/home-images/index3.jpg",
       "static/images/home-images/index4.jpg",
       "static/images/home-images/index5.jpg",
        ],  {duration: 2000, fade: 750});
    });
  })

});


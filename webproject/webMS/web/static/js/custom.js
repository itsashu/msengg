
// ISOTOPE FILTER
jQuery(document).ready(function($){

  if ( $('.iso-box-wrapper').length > 0 ) { 

      var $container  = $('.iso-box-wrapper'), 
        $imgs     = $('.iso-box img');

      $container.imagesLoaded(function () {

        $container.isotope({
        layoutMode: 'fitRows',
        itemSelector: '.iso-box'
        });

        $imgs.load(function(){
          $container.isotope('reLayout');
        })

      });

      //filter items on button click

      $('.filter-wrapper li a').click(function(){

          var $this = $(this), filterValue = $this.attr('data-filter');

      $container.isotope({ 
        filter: filterValue,
        animationOptions: { 
            duration: 750, 
            easing: 'linear', 
            queue: false, 
        }                
      });             

      // don't proceed if already selected 

      if ( $this.hasClass('selected') ) { 
        return false; 
      }

      var filter_wrapper = $this.closest('.filter-wrapper');
      filter_wrapper.find('.selected').removeClass('selected');
      $this.addClass('selected');

        return false;
      }); 

  }

});


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


  // NIVO LIGHTBOX
  $('.iso-box-section a').nivoLightbox({
        effect: 'fadeScale',
    });


  // HOME BACKGROUND SLIDESHOW
  $(function(){
    jQuery(document).ready(function() {
    $('#home').backstretch([
       "images/home-bg-slideshow1.jpg", 
       "images/home-bg-slideshow2.jpg",
        ],  {duration: 2000, fade: 750});
    });
  })
  
  // CAROSEL
  'use strict';

var carousel = function carousel(options) {

    var _carousel = {

        paused: false,

        stopped: false,

        options: {
            speed: 3000,
            acceleration: 5,
            reverse: false,
            selector: '.c-carousel',
            slidesSelector: '.c-carousel__slides',
            leftArrowSelector: '.c-carousel__arrow--left',
            rightArrowSelector: '.c-carousel__arrow--right'
        },

        init: function init() {
            var options = arguments.length <= 0 || arguments[0] === undefined ? {} : arguments[0];

            // Copy options to this.options
            for (var prop in options) {
                if (!options.hasOwnProperty(prop)) break;
                this.options[prop] = options[prop];
            }

            // Cache nodes
            var carousel = document.querySelector(options.selector || this.options.selector);
            var slides = this._slides = carousel.querySelector(this.options.slidesSelector);
            this._leftArrow = carousel.querySelector(this.options.leftArrowSelector);
            this._rightArrow = carousel.querySelector(this.options.rightArrowSelector);

            // Multiply speed value by the number of slides
            this.options.speed = this.options.speed * slides.children.length;

            // Set slides container width
            this.width = slides.offsetWidth;

            // Repeat elements
            slides.innerHTML = slides.innerHTML + slides.innerHTML + slides.innerHTML;

            this._registerEvents();
            this._animate();
        },
        _registerEvents: function _registerEvents() {
            var _this = this;

            var speed = this.options.speed;
            var reverse = this.options.reverse;

            this._rightArrow.addEventListener('mouseover', function () {
                _this.options.speed = speed / _this.options.acceleration;
                _this.options.reverse = false;
            });
            this._rightArrow.addEventListener('mouseleave', function () {
                _this.options.speed = speed;
                _this.options.reverse = reverse;
            });
            this._leftArrow.addEventListener('mouseover', function () {
                _this.options.speed = speed / _this.options.acceleration;
                _this.options.reverse = true;
            });
            this._leftArrow.addEventListener('mouseleave', function () {
                _this.options.speed = speed;
                _this.options.reverse = reverse;
            });

            // Pause when cursor is over carousel
            this._slides.addEventListener('mouseover', this.pause.bind(this));
            this._slides.addEventListener('mouseleave', this.start.bind(this));

            // Pause when cursor is over carousel
            window.addEventListener('resize', function () {
                _this.width = _this._slides.offsetWidth;
            });
        },
        pause: function pause() {
            this.paused = true;
        },
        start: function start() {
            this.paused = false;
        },
        stop: function stop() {
            this.stopped = true;
        },
        _animate: function _animate() {
            var _this2 = this;

            var slides = this._slides;
            var oneThird = slides.lastElementChild.getBoundingClientRect().right / 3;
            var framesCount = 0;
            var step = 0;
            var posX = 0;

            var animate = function animate() {
                if (!_this2.paused) {

                    framesCount = _this2.options.speed * 60 / 1000;
                    step = oneThird / framesCount;

                    posX += _this2.options.reverse ? step : -step;

                    slides.style.transform = 'translateX(' + posX + 'px)';

                    if (_this2.options.reverse) {
                        if (posX >= _this2.width - oneThird) {
                            posX = _this2.width - oneThird * 2;
                        }
                    } else {
                        if (Math.abs(posX) >= oneThird * 2) {
                            posX = -oneThird;
                        }
                    }
                }
                !_this2.stopped && requestAnimationFrame(animate);
            };
            animate();
        }
    };

    _carousel.init(options);

    return _carousel;
};

window.onload = function () {
    return carousel({
        selector: '.c-carousel'
    });
};

});


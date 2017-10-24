function loadImage($img) {
    if (!$img[0].hasAttribute('src')) {
        $img.attr('src', $img.data('src'));
    }

    $img.closest('.js-slideshow-slide').removeClass('is-loading'); 
}

function loadNextImage($slideshow) {
    // load the next unloaded image
    var $nextImgToLoad = $slideshow.find('img:not([src])').first();
    if ($nextImgToLoad.length) {
      loadImage($nextImgToLoad);
    };
}

function loadRemainingImages($slideshow) {
  var $imgs = $slideshow.find('img:not([src])');
  if ($imgs.length) {
    $imgs.each(function(){
      loadImage($(this));
    });
  }
}

function slideshowNext() {
    var $allSlides = $('.js-slideshow-slide');
    var $hiddenSlides = $('.js-slideshow-slide.is-hidden');
    var $visibleSlides = $('.js-slideshow-slide:not(.is-hidden)');
    var $prevButton = $('.js-slideshow-prev');

    var isFirstSlide = $hiddenSlides.length == 0;
    var isLastSlide = $visibleSlides.length == 1;

    if (!isFirstSlide && !isLastSlide) {
        var $slideToHide = $hiddenSlides.last().next();
        $slideToHide.addClass('is-hidden');
        $prevButton.prop('disabled', false);
    } else if (isFirstSlide) {
        var $slideToHide = $allSlides.first();
        $slideToHide.addClass('is-hidden');
        $prevButton.prop('disabled', false);
    } else if (isLastSlide) {
        $allSlides.removeClass('is-hidden');
        $prevButton.prop('disabled', true);
    }

    if (!isLastSlide) {
        var $slideToShow = $slideToHide.next();
        $slideToShow.addClass('is-loading');
        loadImage($slideToShow.find('img'));
    }
    
    loadNextImage($('.js-images'));
    
}

function slideshowPrev() {
    var $hiddenSlides = $('.js-slideshow-slide.is-hidden');
    var isFirstSlide = $hiddenSlides.length == 0;
    var $prevButton = $('.js-slideshow-prev');
    
    if (!isFirstSlide) {
        $prevSlide = $hiddenSlides.last();
        $prevSlide.removeClass('is-hidden');
        $prevSlide.addClass('is-loading');
        loadImage($prevSlide.find('img'));
    }

    if ($hiddenSlides.length == 1) {
        $prevButton.prop('disabled', true);
    }
}

$(document).ready(function(){

    loadNextImage($('.js-images'));

    $('body').on('click', '.js-modal-show', function(){
        $('.js-modal').removeClass('is-hidden');
        $('.js-modal').addClass('is-expanded');

        $('.js-slideshow-slide').removeClass('is-hidden');

        var $target = $('#' + $(this).data('target'));

        var $prevSlides = $target.prevAll();
        var $prevButton = $('.js-slideshow-prev');

        if ($prevSlides.length) {
            $target.prevAll().addClass('is-hidden');
            $prevButton.prop('disabled', false);
        } else {
            $prevButton.prop('disabled', true);
        }
        
        $target.addClass('is-loading');
        loadImage($target.find('img'));
        loadNextImage($('.js-images'));
    });

    $('body').on('click', '.js-modal-close', function(){
        $('.js-modal').addClass('is-hidden');
        $('.js-modal').removeClass('is-expanded');
    });

    $('body').on('click', '.js-slideshow-next', slideshowNext);

    $('body').on('click', '.js-slideshow-prev', slideshowPrev);

    //implmement touch events with hammer.js
    //var slideContainer = document.getElementById('js-slideshow');

    // create a simple instance
    // by default, it only adds horizontal recognizers
    //var hammerit = new Hammer(slideContainer);

    // listen to events...
    //hammerit.on('swipeleft', slideshowNext);
    //hammerit.on('swiperight', slideshowPrev);
});
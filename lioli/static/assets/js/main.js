    $(window).on('load', function() {
        $('#status').delay(1000).fadeOut();
        $('#preloader').delay(1000).fadeOut('slow');
        $("body").fadeIn("slow");
    })
    $(window).scroll(function() {
        if ($(this).scrollTop() > 50) {
            $(".navbar").addClass("scrolled");
        } else {
            $(".navbar").removeClass("scrolled");
        }
        // if ($(window).scrollTop() > 300) {        
        //     $(".product-filter").addClass("product-filter-scrolled");
        // } else {
        //     $(".product-filter").removeClass("product-filter-scrolled");
        // }
    });
    $.fn.isInViewport = function() {
        var elementTop = $(this).offset().top;
        var elementBottom = elementTop + $(this).outerHeight();

        var viewportTop = $(window).scrollTop();
        var viewportBottom = viewportTop + $(window).height();

        return elementBottom > viewportTop && elementTop < viewportBottom;
    };

    $(window).on('resize scroll', function() {
        if ($(window).scrollTop() > 800) {
            if ($('#product-cta').isInViewport()) {
                $("#product-filter").removeClass("product-filter-scrolled");
                $("#product-filter").addClass("product-filter-bottom-scrolled");
            } else {
                $("#product-filter").addClass("product-filter-scrolled");
                $("#product-filter").removeClass("product-filter-bottom-scrolled");
            }

            $(".mobile-filter").addClass("mobile-filter-scrolled");

        } else {
            $("#product-filter").removeClass("product-filter-scrolled");
            $(".mobile-filter").removeClass("mobile-filter-scrolled");
        }
    });
    if($(window).width() > 762){
         /**Aos**/
    $(function() {
        AOS.init({
            duration: 1200,
        });
    });

    $(window).on("load", function() {
        AOS.refresh();
    }); 
    }
    else{
        $(function() {
            AOS.init({
                duration: 500,
            });
        });
    
        $(window).on("load", function() {
            AOS.refresh();
        }); 
    }

   


    /**Momentum Scroll**/
    // $("html").easeScroll();

    const video = document.getElementById("video");
    const circlePlayButton = document.getElementById("circle-play-b");

    function togglePlay() {
        if (video.paused || video.ended) {
            video.play();
        } else {
            video.pause();
        }
    }

    circlePlayButton.addEventListener("click", togglePlay);
    video.addEventListener("playing", function() {
        circlePlayButton.style.opacity = 0;
    });
    video.addEventListener("pause", function() {
        circlePlayButton.style.opacity = 1;
    });

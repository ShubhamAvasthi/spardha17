$(document).ready(function(){
//Navbar Fade in after section
  $(".navbar-custom").hide(); //Hide the navigation bar first
    $(window).scroll(function () {  
        if (isScrolledAfterElement("#about")) { 
            $('.navbar-custom').fadeIn();  
        } else {
            $('.navbar-custom').fadeOut(); 
        }
    });
//Navbar Fade Done
$("#top_bg").slideshow(3,6000);
$("#about").parallax("50%",-0.2);
});

//Function that returns true if the window has scrolled beyond the given element
function isScrolledAfterElement(elem) {
    var $elem = $(elem);
    var $window = $(window);

    var docViewTop = $window.scrollTop();
    var docViewBottom = docViewTop + $window.height()/1.5;

    var elemTop = $elem.offset().top;

    return elemTop <= docViewBottom;
}
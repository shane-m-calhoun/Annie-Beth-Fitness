// Select all links with hashes
$('a[href*="#"]')
  // Remove links that don't actually link to anything
  .not('[href="#"]')
  .not('[href="#0"]')
  .click(function(event) {
    // On-page links
    if (
      location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
      && 
      location.hostname == this.hostname
    ) {
      // Figure out element to scroll to
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      // Does a scroll target exist?
      if (target.length) {
        // Only prevent default if animation is actually gonna happen
        event.preventDefault();
        $('html, body').animate({
          scrollTop: target.offset().top
        }, 1000, function() {
          // Callback after animation
          // Must change focus!
          var $target = $(target);
          $target.focus();
          if ($target.is(":focus")) { // Checking if the target was focused
            return false;
          } else {
            $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
            $target.focus(); // Set focus again
          };
        });
      }
    }
  });




function myFunction() {
    var x = document.getElementById("more-content");
    var y = document.getElementById("section-a");
    if (x.style.display === "none") {
        x.style.display = "block";
        y.style.height = "auto"
    } else {
        x.style.display = "none";
        y.style.height = $(window).height();
    }
}










$showcaseHeight = $('#showcase').height();
$aHeight = $('#section-a').height();
$bHeight = $('#section-b').height();
$cHeight = $('#section-c').height();
$(document).ready(function(){
    if ($(window).height() > $showcaseHeight + 55){
      $('#showcase').css('height', $(window).height());
    }else {
      $('#showcase').css('height', $showcaseHeight + 55);
    }

    $('#strike').css('top', $('#showcase').height()-55);

    if ($(window).width() > 849){
      if ($(window).height() > $aHeight){
        $('#section-a').css('height', $(window).height());
      }else{
        $('#section-a').css('height', 'auto');
      }
      if ($(window).height() > $bHeight){
        $('#section-b').css('height', $(window).height());
      }else{
        $('#section-b').css('height', 'auto');
      }
      if ($(window).height() > $cHeight){
        $('#section-c').css('height', $(window).height());
      }else{
        $('#section-c').css('height', 'auto');
      }
      
      $('#blog').css('height', $('#section-b').height()-$('.blog-subscribe').height());
    }
});
$(window).resize(function(){
    if ($(window).height() > $showcaseHeight + 55){
      $('#showcase').css('height', $(window).height());
    }else {
      $('#showcase').css('height', $showcaseHeight + 55);
    }

    $('#strike').css('top', $('#showcase').height()-55);

    if ($(window).width() > 849){
      if ($(window).height() > $aHeight){
        $('#section-a').css('height', $(window).height());
      }else{
        $('#section-a').css('height', 'auto');
      }
      if ($(window).height() > $bHeight){
        $('#section-b').css('height', $(window).height());
      }else{
        $('#section-b').css('height', 'auto');
      }
      if ($(window).height() > $cHeight){
        $('#section-c').css('height', $(window).height());
      }else{
        $('#section-c').css('height', 'auto');
      }
      
      $('#blog').css('height', $('#section-b').height()-$('.blog-subscribe').height());
    }else {
      $('#section-a').css('height', 'auto');
      $('#section-b').css('height', 'auto');
      $('#blog').css('height', 'auto');
      $('#section-c').css('height', 'auto');
    }
});
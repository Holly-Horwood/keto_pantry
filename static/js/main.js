// Changes nav colour on scroll - Code courtesy of System 22 I.T. Solutions https://www.youtube.com/watch?v=AM-GT_0Uu5w
$(window).scroll(function() {
    $('nav').toggleClass('scroll', $(this).scrollTop() > 10);
    });
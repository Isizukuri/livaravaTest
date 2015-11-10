$(document).ready(function() {
    $(".year_input").hide();
    $(".author_input").hide();
    $('.year_toggle').click(function() {
        $(".year_select").fadeOut(400, function() {
            $(".year_input").fadeIn(400, function() {})
        });
        $('.year_toggle').fadeOut(400);
    });

    $('.author_toggle').click(function() {
        $(".author_select").fadeOut(400, function() {
            $(".author_input").fadeIn(400, function() {})
        });
        $('.author_toggle').fadeOut(400);
    });
});

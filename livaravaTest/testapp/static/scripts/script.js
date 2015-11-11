$(document).ready(function() {
    $(".year_input").hide();
    $(".author_input").hide();
    $('.year_toggle').click(function() {
        $(".year_select").fadeOut(400, function() {
            $(".year_select").remove();
            $("#year").after("<input type='text' class='form-control year_input' placeholder='Введіть рік написання' name='year'>");
            $(".year_input").fadeIn(400, function() {});
        });
        $('.year_toggle').fadeOut(400);
    });

    $('.author_toggle').click(function() {
        $(".author_select").fadeOut(400, function() {
            $(".author_select").remove();
            $("#author").after("<input type='text' class='form-control author_input' placeholder='Введіть автора' name='author'>");
            $(".author_input").fadeIn(400, function() {});
        });
        $('.author_toggle').fadeOut(400);
    });

    $(".like").click(function() {
            var id = $(this).attr("verse-name");
            var parameters = {'id': id};
            $.post("/", parameters, function(data) {
                /*
                $(this).html("<div style='float: right;' class='like' verse-name='{{verse.name}}'>
                Мені подобається <img src='http://cliparts.co/cliparts/kiM/nnL/kiMnnL8yT.svg' style='width:30px%;height:30px;'>"+data+
            "</div>");*/
            });  		
        });
});


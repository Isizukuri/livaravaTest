$(document).ready(function() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        };
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

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
        var parameters = {
            'id': id
        };
        $.post("/like/", parameters, function(data) {
            tag = '.'+data.tag
            $(tag).html(data.likes);
        });
    });
});

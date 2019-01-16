let LazyLoadEvent = function (is_enable, action) {
    $(window).scroll(function () {
        if (is_enable()) {
            if ($(document).scrollTop() + $(window).height() >= $(document).height()) {
                action();
            }
        }
    });
};
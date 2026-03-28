$(document).ready(function () {

    $('.eye-btn').on('click', function () {

        var inputId = $(this).data('target');
        var input = $('#' + inputId);

        var eyeShow = $(this).find('.eye-show');
        var eyeHide = $(this).find('.eye-hide');

        if (input.attr('type') === 'password') {
            input.attr('type', 'text');
            eyeShow.hide();
            eyeHide.show();
        } else {
            input.attr('type', 'password');
            eyeShow.show();
            eyeHide.hide();
        }

    });

});
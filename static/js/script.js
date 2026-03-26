
$(document).ready(function () {

    var modal = $('#modalAlertTaskAdded');

    // Check if modal exists
    if (modal.length) {

        var modal = new bootstrap.Modal($modal[0]);
        modal.show();

        // Hide after 3 seconds
        setTimeout(function () {
            modal.hide();
        }, 3000);
    }

});

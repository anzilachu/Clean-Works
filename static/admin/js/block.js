$("#FilUploader, #FilUploader2").change(function () {
    var fileExtension = ['jpg', 'jpeg', 'jfif', 'pjpeg', 'pjp', 'png'];
    if ($.inArray($(this).val().split('.').pop().toLowerCase(), fileExtension) == -1) {
        alert("Only formats allowed: " + fileExtension.join(', '));
        $(this).val('');
    }
});
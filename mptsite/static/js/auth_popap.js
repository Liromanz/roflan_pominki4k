const authModal = $('#authModal');

authModal.on('show.bs.modal', function (event) {
    $('body').addClass('no-scroll');
});

authModal.on('hidden.bs.modal', function (event) {
    $('body').removeClass('no-scroll');
});


$(document).ready(function() {
    const dropdown = $('#comboDropdown');
    const input = $('#comboInput');
    const dropdownItems = $('.dropdown-item');

    $(this).on('click', function (event) {
        if (!$(event.target).closest('#comboInput, #comboDropdown').length) {
            dropdown.removeClass('show');
        }
    });

    input.on('click', function () {
        console.log(dropdown.hasClass('show'))
        if (!dropdown.hasClass('show')){
            dropdownItems.each(function() {
                $(this).show();
            });
            setTimeout(function() {
                dropdown.addClass('show');
            }, 10);
            input.val('');
        }
    });

    input.on('input', function() {
        dropdown.addClass('show');
        let filter = $(this).val().toLowerCase();
        dropdownItems.each(function() {
            const itemContent = $(this).text().toLowerCase();
            if (itemContent.includes(filter))
                $(this).show();
            else
                $(this).hide();
        });
    });

    dropdownItems.each(function () {
        $(this).on('click', function () {
            const content = $(this).text();
            input.val(content);
            dropdown.removeClass('show');
        });
    });
});
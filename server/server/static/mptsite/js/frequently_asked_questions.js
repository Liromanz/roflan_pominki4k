const listDropdownContent = Array.from(document.getElementsByClassName('dropdown-content'))
Array.from(document.getElementsByClassName('custom-dropdown-toggle'))
    .forEach((btn, index) => {
        btn.addEventListener("click", function ()
        {
            this.classList.toggle('collapsed');
            listDropdownContent[index].classList.toggle('show');
        });
    });


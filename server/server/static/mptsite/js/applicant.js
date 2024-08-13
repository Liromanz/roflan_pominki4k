const containers = Array.from(document.getElementsByClassName('subsections'))
Array.from(document.getElementsByClassName('section-button'))
    .forEach((btn, index) =>
        btn.addEventListener('click', function ()
        {
            const listCollapsedButton = Array.from(document.querySelectorAll('.section-button.collapsed'));
            if (!listCollapsedButton.includes(btn)){
                listCollapsedButton.forEach(element => element.classList.toggle('collapsed'));
                containers.forEach(element => element.classList.remove('show'));
            }
            this.classList.toggle('collapsed');
            containers[index].classList.toggle('show');
        })
    )
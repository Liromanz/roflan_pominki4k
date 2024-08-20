const containers = Array.from(document.getElementsByClassName('subsections'));
const buttons = Array.from(document.getElementsByClassName('section-button'));

const originalPositions = containers.map(container => ({
    container: container,
    parent: container.parentNode,
    nextSibling: container.nextElementSibling
}));

const targetParent = document.getElementById('container-content');

buttons.forEach((btn, index) => {
    btn.addEventListener('click', function () {
        let viewportWidth = window.innerWidth;
        const listCollapsedButton = Array.from(document.querySelectorAll('.section-button.collapsed'));

        if (!listCollapsedButton.includes(btn)) {
            listCollapsedButton.forEach(element => element.classList.toggle('collapsed'));
            containers.forEach(element => element.classList.remove('show'));
        }

        this.classList.toggle('collapsed');
        containers[index].classList.toggle('show');

        if (viewportWidth > 992) {
            if (containers[index].parentNode !== targetParent) {
                Array.from(targetParent.children).forEach(child => {
                    const original = originalPositions.find(pos => pos.container === child);
                    if (original) {
                        original.parent.insertBefore(child, original.nextSibling);
                    }
                });
                targetParent.appendChild(containers[index]);
            }
        } else {
            containers.forEach(element => {
                const original = originalPositions.find(pos => pos.container === element);
                if (element.parentNode === targetParent && original) {
                    original.parent.insertBefore(element, original.nextSibling);
                }
            });
        }
    });
});

const observer = new MutationObserver(() => {
    const elements = [
        {
            leftArrow: document.getElementById("left-arrow"),
            rightArrow: document.getElementById("right-arrow"),
            container: document.getElementById("card-container"),
            card: document.getElementById("card")
        },
        {
            leftArrow: document.getElementById("l-arrow"),
            rightArrow: document.getElementById("r-arrow"),
            container: document.getElementById("news-card-container"),
            card: document.getElementById("news-card")
        }
    ];

    elements.forEach(({ leftArrow, rightArrow, container, card }) => {
        if (leftArrow && rightArrow && container && card) {
            const width = card.offsetWidth;
            const gap = getGapValue(container);

            leftArrow.addEventListener("click", () => {
                container.scrollBy({
                    left: (width + gap) * -1,
                    behavior: "smooth",
                });
            });

            rightArrow.addEventListener("click", () => {
                container.scrollBy({
                    left: (width + gap),
                    behavior: "smooth",
                });
            });
        }
    });
});

const getGapValue = (container) => {
    const containerStyles = window.getComputedStyle(container);
    let gap = containerStyles.getPropertyValue("gap");

    if (!gap.includes("px")) {
        const tmpDiv = document.createElement("div");
        tmpDiv.style.width = gap;
        document.body.appendChild(tmpDiv);
        gap = window.getComputedStyle(tmpDiv).width;
        document.body.removeChild(tmpDiv);
    }

    return Number(gap.replace("px", ""));
}

const config = { subtree: true, childList: true };
observer.observe(document, config);

const observer = new MutationObserver(() => {
    const leftArrow = document.getElementById("left-arrow");
    const rightArrow = document.getElementById("right-arrow");
    const cardContainer = document.getElementById("card-container");

    const card = document.getElementById("card");
    const width = card.offsetWidth;
    const height = card.offsetHeight;

    const cardContainerStyles = window.getComputedStyle(cardContainer);
    let gap = cardContainerStyles.getPropertyValue("gap");

    if (!gap.includes("px")) {
        const tmpDiv = document.createElement("div");
        tmpDiv.style.width = gap;
        document.body.appendChild(tmpDiv);
        gap = window.getComputedStyle(tmpDiv).width;
        document.body.removeChild(tmpDiv);
    }

    gap = Number(gap.replace("px", ""))

    leftArrow.addEventListener("click", () => {
        cardContainer.scrollBy({
            left: (width + gap) * -1,
            behavior: "smooth",
        });
    });

    rightArrow.addEventListener("click", () => {
        cardContainer.scrollBy({
            left: (width + gap),
            behavior: "smooth",
        });
    });
})

const config = {subtree: true, childList: true}; 

observer.observe(document, config);
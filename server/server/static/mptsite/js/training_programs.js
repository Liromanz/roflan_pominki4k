const observer = new MutationObserver(() => {
    const leftArrow = document.getElementById("left-arrow");
    const rightArrow = document.getElementById("right-arrow");
    const cardContainer = document.getElementById("card-container");

    const lArrow = document.getElementById("l-arrow");
    const rArrow = document.getElementById("r-arrow");
    const newsCardContainer = document.getElementById("news-card-container");

    const card = document.getElementById("card");
    const width = card.offsetWidth;

    const newsCard = document.getElementById("news-card");
    const newsWidth = newsCard.offsetWidth;

    const cardContainerStyles = window.getComputedStyle(cardContainer);
    const newsCardContainerStyles = window.getComputedStyle(newsCardContainer);
    let gap = cardContainerStyles.getPropertyValue("gap");
    let newsGap = newsCardContainerStyles.getPropertyValue("gap");

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

    lArrow.addEventListener("click", () => {
        newsCardContainer.scrollBy({
            left: (width + gap) * -1,
            behavior: "smooth",
        });
    });

    rArrow.addEventListener("click", () => {
        newsCardContainer.scrollBy({
            left: (width + gap),
            behavior: "smooth",
        });
    });
})

const config = {subtree: true, childList: true};
observer.observe(document, config);
const calendarMobile = document.getElementById("calendar-mobile");

const dayMonthFormater = new Intl.DateTimeFormat(locale, { day: 'numeric', month: 'numeric' });
const weekdayFormater = new Intl.DateTimeFormat(locale, { weekday: 'long' });

let selectIndex = null;
let startIndexMobile = null;
let endIndexMobile = null;

const updateSelect = (selectedIndex) => {
    const allDays = document.querySelectorAll('#calendar-mobile button');
    allDays.forEach((day) => {
        const currentIndex = day.dataset.index;

        if (currentIndex === selectedIndex) {
            day.classList.add('selected');
        } else {
            day.classList.remove('selected');
        }
    });
}

const addEventMobile = (btn) => {
    btn.addEventListener('click', () => {
        const currentIndex = btn.dataset.index;
        selectIndex = currentIndex;
        updateSelect(selectIndex);
    });
}

const createBtn = (currentDate) => {
    const dayBtn = document.createElement('button');

    dayBtn.dataset.index = idFormatter.format(currentDate);
    dayBtn.classList.add('d-flex', 'align-items-center', 'flex-column', 'p-2');

    const dateText = document.createElement('h4');
    dateText.textContent = dayMonthFormater.format(currentDate);
    dayBtn.appendChild(dateText);

    const weekdayText = document.createElement('p');
    weekdayText.textContent = weekdayFormater.format(currentDate);
    dayBtn.appendChild(weekdayText);
    addEventMobile(dayBtn);
    return dayBtn;
}

const renderTwoMonth = (startOfDay) => {
    for (let i = 0; i < 70; i++) {
        const currentDate = new Date(startOfDay.getFullYear(), startOfDay.getMonth(), startOfDay.getDate() + i);
        const dayBtn = createBtn(currentDate);
        calendarMobile.appendChild(dayBtn);
    }
};

let currentDate = new Date();
startIndexMobile = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() - 40)
endIndexMobile = new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() + 29)
renderTwoMonth(startIndexMobile);

selectIndex = idFormatter.format(currentDate);
const todayButtonElement = Array.from(document.querySelectorAll('#calendar-mobile button')).find(btn => btn.dataset.index === selectIndex);
todayButtonElement.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
todayButtonElement.classList.add('selected')

calendarMobile.addEventListener('scroll', () => {
    if (calendarMobile.scrollLeft + calendarMobile.clientWidth >= calendarMobile.scrollWidth * 0.9) {
        for (let i = 1; i <= 30; i++) {
            endIndexMobile = new Date(endIndexMobile.getFullYear(), endIndexMobile.getMonth(), endIndexMobile.getDate()+1);
            const endBtn = createBtn(endIndexMobile);
            calendarMobile.appendChild(endBtn);
        }
    }

    if (calendarMobile.scrollLeft <= calendarMobile.clientWidth * 0.1) {
        for (let i = 1; i <= 30; i++) {
            startIndexMobile = new Date(startIndexMobile.getFullYear(), startIndexMobile.getMonth(), startIndexMobile.getDate()-1);
            const endBtn = createBtn(startIndexMobile);
            calendarMobile.prepend(endBtn);
        }
    }
});
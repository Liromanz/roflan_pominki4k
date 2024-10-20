const calendarMobile = document.getElementById("calendar-mobile");

const dayMonthFormater = new Intl.DateTimeFormat(locale, { day: 'numeric', month: 'numeric' });
const weekdayFormater = new Intl.DateTimeFormat(locale, { weekday: 'long' });

let selectIndex = null; // Изначально null, чтобы не было выбранного элемента

const updateSelect = (selectedIndex) => {
    const allDays = document.querySelectorAll('#calendar-mobile button');
    allDays.forEach((day) => {
        const currentIndex = day.dataset.index;

        if (currentIndex === selectedIndex) {
            console.log(currentIndex);
            day.classList.add('selected'); // Добавляем класс только для выбранного дня
        } else {
            day.classList.remove('selected'); // Убираем класс с остальных
        }
    });
}

const addEventMobile = (btn) => {
    btn.addEventListener('click', () => {
        const currentIndex = btn.dataset.index;
        selectIndex = currentIndex;
        console.log(selectIndex);
        updateSelect(selectIndex);
    });
}

const renderTwoMonth = (startOfDay) => {
    for (let i = 0; i < 60; i++) {
        const currentDate = new Date(startOfDay.getFullYear(), startOfDay.getMonth(), startOfDay.getDate() + i);
        const dayBtn = document.createElement('button');

        dayBtn.dataset.index = idFormatter.format(currentDate); // Установите index один раз
        dayBtn.classList.add('d-flex', 'align-items-center', 'flex-column', 'p-2');

        const dateText = document.createElement('h4');
        dateText.textContent = dayMonthFormater.format(currentDate);
        dayBtn.appendChild(dateText);

        const weekdayText = document.createElement('p');
        weekdayText.textContent = weekdayFormater.format(currentDate);
        dayBtn.appendChild(weekdayText);
        addEventMobile(dayBtn);

        calendarMobile.appendChild(dayBtn);
    }
};

let currentDate = new Date();
renderTwoMonth(new Date(currentDate.getFullYear(), currentDate.getMonth(), currentDate.getDate() - 30));

selectIndex = idFormatter.format(currentDate);
const todayButtonElement = Array.from(document.querySelectorAll('#calendar-mobile button')).find(btn => btn.dataset.index === selectIndex);
todayButtonElement.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });
todayButtonElement.classList.add('selected')
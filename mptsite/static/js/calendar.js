const calendar = document.getElementById("calendar");
const currentMonthYear = document.getElementById("currentMonth");
const prevWeekBtn = document.getElementById("prevWeek");
const nextWeekBtn = document.getElementById("nextWeek");

let today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();
let firstWeek = new Date();
let lastWeek = new Date();

const locale = 'ru-RU';
const monthFormatter = new Intl.DateTimeFormat(locale, { month: 'long' });
const idFormatter = new Intl.DateTimeFormat(locale, { day: "numeric", month: "numeric", year: "numeric" });

let isSelecting = false;
let startIndex = null;
let endIndex = null;

const parseDate = (dateString) => {
    const [day, month, year] = dateString.split('.').map(Number);
    return new Date(year, month - 1, day);
}

const updateSelection = () => {
    const allDays = document.querySelectorAll('.calendar-days button');
    const start = parseDate(startIndex);
    const end = parseDate(endIndex);
    allDays.forEach((day, index) => {
        const currentIndex = day.dataset.index;
        const current = parseDate(currentIndex);

        if (current >= Math.min(start, end) && current <= Math.max(start, end)) {
            day.classList.add('selected');
        } else {
            day.classList.remove('selected');
        }

    });
}

const addEvent = (btn) => {
    btn.addEventListener('click', (e) => {
            const currentIndex = e.target.dataset.index;
            if (!isSelecting) {
                isSelecting = true;
                startIndex = currentIndex;
                endIndex = startIndex;
                updateSelection();
            } else {
                endIndex = currentIndex;
                isSelecting = false;
                updateSelection();
            }
        });

        btn.addEventListener('mouseenter', (e) => {
            if (isSelecting) {
                endIndex = e.target.dataset.index;
                updateSelection();
            }
        });
}

const getMonday = (date) => {
    const day = date.getDay();
    const diff = (day === 0 ? -6 : 1) - day;
    return new Date(date.setDate(date.getDate() + diff));
};

const renderWeek = (startOfWeek, month) => {
    const weekContainer = document.createElement("div");
    weekContainer.classList.add("week");
    for (let i = 0; i < 7; i++) {
        const currentDate = new Date(startOfWeek.getFullYear(), startOfWeek.getMonth(), startOfWeek.getDate() + i);
        const dayBtn = document.createElement("button");
        dayBtn.textContent = currentDate.getDate();
        dayBtn.dataset.index = idFormatter.format(currentDate);
        addEvent(dayBtn);
        if (currentDate.getMonth() === month) {
            dayBtn.classList.add('day');
        } else {
            dayBtn.classList.add('day', 'another-month-day');
        }

        weekContainer.appendChild(dayBtn);
    }

    calendar.appendChild(weekContainer);
    return weekContainer;
};

const renderInitialWeeks = (month, year) => {
    calendar.innerHTML = "";
    const firstDayOfMonth = new Date(year, month, 1);
    let firstMonday = getMonday(firstDayOfMonth);
    firstWeek = firstMonday;
    lastWeek = new Date(firstWeek.getFullYear(), firstWeek.getMonth(), firstWeek.getDate()+43);

    for (let i = 0; i < 6; i++) {
        renderWeek(new Date(firstMonday.getFullYear(), firstMonday.getMonth(), firstMonday.getDate() + i * 7), currentMonth);
    }

    const monthStr = monthFormatter.format(new Date(year, month));
    currentMonthYear.textContent = `${monthStr.charAt(0).toUpperCase() + monthStr.slice(1)}`;
};

const deleteWeek = (index) => {
    const weeks = document.querySelectorAll('.calendar-days div');
    weeks[index].remove();
}

const updateMonthNext = (week) => {
    if (23 <= week.getDate() ) {
        currentMonth++;
        const monthStr = monthFormatter.format(new Date(week.getFullYear(), week.getMonth()));
        currentMonthYear.textContent = `${monthStr.charAt(0).toUpperCase() + monthStr.slice(1)}`;
        const allDays = document.querySelectorAll('.calendar-days button');

        allDays.forEach(day => {
            if (parseDate(day.dataset.index).getMonth() === week.getMonth()){
                day.classList.remove('another-month-day');
            } else {
                day.classList.add('another-month-day');
            }
        });
    }
}

const updateMonthPrevious = (week) => {
    if (8 >= week.getDate()) {
        currentMonth--;
        const monthStr = monthFormatter.format(new Date(week.getFullYear(), week.getMonth()));
        currentMonthYear.textContent = `${monthStr.charAt(0).toUpperCase() + monthStr.slice(1)}`;
        const allDays = document.querySelectorAll('.calendar-days button');

        allDays.forEach(day => {
            if (parseDate(day.dataset.index).getMonth() <= week.getMonth()){
                day.classList.remove('another-month-day');
            } else {
                day.classList.add('another-month-day');
            }
        });
    }
}

const addNextWeek = () => {
    const week = getMonday(new Date(lastWeek.getFullYear(), lastWeek.getMonth(), lastWeek.getDate() + 1));
    renderWeek(week, currentMonth);
    updateMonthNext(week);
    lastWeek = new Date(lastWeek.getFullYear(), lastWeek.getMonth(), lastWeek.getDate() + 7);
    firstWeek = new Date(firstWeek.getFullYear(), firstWeek.getMonth(), firstWeek.getDate() + 7);
};

const addPreviousWeek = () => {
    const week = getMonday(new Date(firstWeek.getFullYear(), firstWeek.getMonth(), firstWeek.getDate() - 1));
    const weekContainer = renderWeek(week, currentMonth);
    updateMonthPrevious(week);
    calendar.prepend(weekContainer);
    firstWeek = new Date(firstWeek.getFullYear(), firstWeek.getMonth(), firstWeek.getDate() - 7);
    lastWeek = new Date(lastWeek.getFullYear(), lastWeek.getMonth(), lastWeek.getDate() - 7);
};

prevWeekBtn.addEventListener("click", () => {
    addPreviousWeek();
    deleteWeek(6);
});

nextWeekBtn.addEventListener("click", () => {
    addNextWeek();
    deleteWeek(0);
});

renderInitialWeeks(currentMonth, currentYear);

const highlightCurrentWeek = () => {
    const allDays = document.querySelectorAll('.calendar-days button');
    let startOfWeek = getMonday(today);
    startOfWeek = new Date(startOfWeek.getFullYear(), startOfWeek.getMonth(), startOfWeek.getDate());
    allDays.forEach(day => {
        const dayDate = parseDate(day.dataset.index);
        if (dayDate >= startOfWeek && dayDate < new Date(startOfWeek.getFullYear(), startOfWeek.getMonth(), startOfWeek.getDate() + 7)) {
            day.classList.add('selected');
        }
    });
};

highlightCurrentWeek();
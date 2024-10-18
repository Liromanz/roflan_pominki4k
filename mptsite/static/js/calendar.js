const calendar = document.getElementById("calendar");
const currentMonthYear = document.getElementById("currentMonthYear");
const prevMonthBtn = document.getElementById("prevMonth");
const nextMonthBtn = document.getElementById("nextMonth");

let today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();

const locale = 'ru-RU';
const monthFormatter = new Intl.DateTimeFormat(locale, { month: 'long' });
const alertFormatter = new Intl.DateTimeFormat(locale, {day: "numeric", month: "numeric", year: "numeric"});

let isSelecting = false;
let startIndex = null;
let endIndex = null;

const getWeek = (date) => {
    const startOfYear = new Date(date.getFullYear(), 0, 1);
    const pastDays = (date - startOfYear) / (1000 * 60 * 60 * 24);
    return Math.ceil((pastDays + startOfYear.getDay()) / 7);
}

const renderCalendar = (month, year) => {
    calendar.innerHTML = "";

    const monthStr = monthFormatter.format(new Date(year, month));
    currentMonthYear.textContent  = monthStr.charAt(0).toUpperCase() + monthStr.slice(1);

    let firstDay = new Date(year, month).getDay() || 7;
    let daysInMonth = new Date(year, month + 1, 0).getDate();

    let prevMonthDays = new Date(year, month, 0).getDate();
    let daysToShowFromPrevMonth = firstDay - 1;
    const currentWeek = getWeek(new Date(year, month, today.getDate()))

    for (let i = daysToShowFromPrevMonth; i > 0; i--) {
        const dayBtn = document.createElement("button");
        dayBtn.textContent = prevMonthDays - i + 1;
        dayBtn.classList.add("day", "prev-month-day");
        dayBtn.dataset.index = alertFormatter.format(new Date(year, month-1, prevMonthDays - i + 1));

        addEvent(dayBtn);
        calendar.appendChild(dayBtn);
    }

    for (let day = 1; day <= daysInMonth; day++) {
        const dayBtn = document.createElement("button");
        dayBtn.textContent = day;
        dayBtn.classList.add("day");
        const date = new Date(year, month, day);
        dayBtn.dataset.index = alertFormatter.format(date);

        if (getWeek(new Date(year, month, day)) === currentWeek) {
            dayBtn.classList.add("selected");
        }

        addEvent(dayBtn);
        calendar.appendChild(dayBtn);
    }

    const remainingCells = 42 - calendar.childNodes.length;
    for (let i = 1; i <= remainingCells; i++) {
        const dayBtn = document.createElement("button");
        dayBtn.textContent = i;
        dayBtn.classList.add("day", "next-month-day");
        dayBtn.dataset.index = alertFormatter.format(new Date(year, month+1, i));


        addEvent(dayBtn);
        calendar.appendChild(dayBtn);
    }
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

const parseDate = (dateString) => {
    const [day, month, year] = dateString.split('.').map(Number);
    return new Date(year, month - 1, day);
}

const updateSelection = () => {
    const allDays = document.querySelectorAll('.calendar-days button');
    allDays.forEach((day, index) => {
        const currentIndex = day.dataset.index;
        const start = parseDate(startIndex);
        const end = parseDate(endIndex);
        const current = parseDate(currentIndex);

        if (current >= Math.min(start, end) && current <= Math.max(start, end)) {
            day.classList.add('selected'); // Диапазон
        } else {
            day.classList.remove('selected');
        }

    });
}

renderCalendar(currentMonth, currentYear);

prevMonthBtn.addEventListener("click", () => {
    currentMonth--;
    if (currentMonth < 0) {
        currentMonth = 11;
        currentYear--;
    }
    renderCalendar(currentMonth, currentYear);
});

nextMonthBtn.addEventListener("click", () => {
    currentMonth++;
    if (currentMonth > 11) {
        currentMonth = 0;
        currentYear++;
    }
    renderCalendar(currentMonth, currentYear);
});
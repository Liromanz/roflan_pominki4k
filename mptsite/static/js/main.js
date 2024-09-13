fetch("../main-page/header_top.html")
    .then(response => response.text())
    .then(data => {
        document.getElementById('first-header').innerHTML = data;
    });

fetch('../main-page/second_header.html')
	.then(response => response.text())
	.then(data => {
		document.getElementById('second-header').innerHTML = data
	})

fetch('../main-page/about_MPT.html')
	.then(response => response.text())
	.then(data => {
		document.getElementById('block-about-MPT').innerHTML = data
	})

fetch('../main-page/training_program.html')
	.then(response => response.text())
	.then(data => {
		document.getElementById('block-training-program').innerHTML = data
	})

fetch('../main-page/footer.html')
	.then(response => response.text())
	.then(data => {
		document.getElementById('integrade-footer').innerHTML = data
	})

fetch('../main-page/map_block.html')
	.then(response => response.text())
	.then(data => {
		document.getElementById('block-map').innerHTML = data
	})

fetch('../main-page/frequently_asked_questions.html')
	.then(response => response.text())
	.then(data => {
		document.getElementById('block-frequently-asked-questions').innerHTML = data
	})

fetch('../main-page/news.html')
	.then(response => response.text())
	.then(data => {
		document.getElementById('block-news').innerHTML = data
	})

fetch('../main-page/applicant.html')
	.then(response => response.text())
	.then(data => {
		document.getElementById('block-applicant').innerHTML = data
	})
/*function adjustMainContainer() {
    const mainElement = document.querySelector('main');
    if (window.innerWidth > 1920) {
        mainElement.classList.add('container');
    } else {
        mainElement.classList.remove('container');
    }
}*/

// Запуск функции при загрузке страницы
//window.addEventListener('DOMContentLoaded', adjustMainContainer);

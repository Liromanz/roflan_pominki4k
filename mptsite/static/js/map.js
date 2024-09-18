const map = document.getElementById("map");
document.getElementById("Nahim").onclick = function () {
  map.innerHTML = ""; // очищаем содержимое перед вставкой
  const script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = 'https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A46dd7db97ed8957810a25f1c0ceb7fc9924d769dc2c0ac9f5fc75dbc78f5845d&amp;width=100%&amp;height=100%&amp;lang=ru_RU&amp;scroll=false';
  map.appendChild(script); // добавляем новый скрипт
};
document.getElementById('Nezhka').onclick = function(){
  map.innerHTML = "";
  const script = document.createElement('script');
  script.type = 'text/javascript';
  script.src = "https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Ad5b54d2099ccb83cbc84369977fca7c6a336a522f49d1396f3e311f2e9951bcf&amp;width=567&amp;height=500&amp;lang=ru_RU&amp;scroll=true"
  map.appendChild(script);
}
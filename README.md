# rating_API
<h1> Назначение </h1>
	<p>API предназначена для создания возможности получения данных о рейтинге учеников в формате <a href="https://www.json.org/">JSON</a></p>
	<h2>Алгоритм работы c API</h2>
	<ol>
		<li>
			<p>Работники ответственные за составление рейтинга заполняют таблицу в формате .xlsx</p>
		</li>
		<li>
			<p>После заполнения они загружают таблицу в специальную форму на сайте</p>
			<img src="https://downloader.disk.yandex.ru/preview/152af14f11e03b6aebc6e8d95b07ebd23d22042b609cff292cb34a30eca0e3c4/5c46f18b/enDafUgLP-2oQnEhpocgdBnaAV_VHvKrPF4X3aTxrmVuH1FV30yr58IrsX9jEnvC4EcUnlZSz0xtgOcMU6enLw%3D%3D?uid=0&filename=1.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&size=807x892">
<img src="https://4.downloader.disk.yandex.ru/preview/66d3adb2d9e6f85bd9774dc48a3ea9052a420e89a6dffdefa75467d39ed9709e/inf/H5vpbfuBuS39EiQH7y7UB_C7_IWiaY1HmAREL8v40xK9Q1bxNmuda4Ul5KYWUXz6wNpHmSmoUgE5TcOAkNxLNQ%3D%3D?uid=20109010&filename=2019-01-22_08-48-55%20%282%29.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&tknv=v2&size=787x892">
		</li>
		<li>
			<p>Далее, ретинг доступен по get-запросу с двумя параметрами 1) ФИО 2) ключ (секретный ключ для ограничения доступа к сайту). Запрос осуществлется сайтом "Лидер"</p>
		</li>
	</ol>

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
			<img src="http://i63.tinypic.com/sku6io.png">
			<img src="http://i66.tinypic.com/2zfk9d2.png">
		</li>
		<li>
			<p>Далее, ретинг доступен по get-запросу с двумя параметрами 1) ФИО 2) ключ (секретный ключ для ограничения доступа к сайту). Запрос осуществлется сайтом "Лидер"</p>
			<img src="http://i63.tinypic.com/j7yyc7.png">
		</li>
	</ol>
<h2> Примеры запросов </h2>
<h3> Запрос на языке Python </h3>

```python
import requests
payload = {'name':'Петров Петр Петрович', 'key':'key'}
r = requests.get('http://ratingapi.pythonanywhere.com/rating', params = payload)
```


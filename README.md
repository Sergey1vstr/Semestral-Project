# Semestral-Project
V.0.0
В рамках курсовой создается скрипт для поиска новых статей по заданной тематике
Что должен принимать на вход:
1. Ключевые слова;
2. Частоту срабатывания (раз в день, месяц, неделю, каждую третью пятницу и т.д.)
3. Авторов

Что должен отдавать:
Список статей с авторами, названием, журналом, ссылкой и DOI


V.0.1 - Сыроватый код сам себя не доработает
Возможности:
1. Парсит HTML сайта ScienceDirect.com
2. Ищет статьи по ключевым словам
3. Выдает первые пять результатов со страницы, которые содержат:
    - Список авторов
    - Название статьи
    - Название журнала
    - Ссылку на статью

Принципы работы:
1. Отправка запроса с помощью requests.sessions
2. Использование HTTP заголовков
3. Парсинг с помощью BeautifulSoup

Проблемы к решению:
1. Унификация скрипта: автоматическая вставка headers или аторизация на сайте, использование Selenium
2. Вывод статей в более удобный формат для чтения (отдельный документ)
3. Вывод DOI, аннотации (переход по ссылкам на статью и их парсинг)
4. Сделать окно для ввода, чтоб не залезать в сам код для запуска
5. Повышение количества запросов в обход блокировки (установить таймаут)

В далеком будущем:
1. Увеличение количества сайтов

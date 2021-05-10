# -*- coding: utf-8 -*-

# Импортируем модуль errors
from urllib.error import HTTPError
# Импортируем "прекрасный суп"
from bs4 import BeautifulSoup as bs
import requests as req

#------------------------------------------------------------------------------------------------------------------

# Функция для вытаскивания со страницы элементов, содержащих всю информацию о статье
def get_me_some_info(url):
    s = req.Session()
    heads = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
         "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
    try: # Посылаем запрос с помощью Сессионс, притворяясь человеком
        html = s.get(url, headers=heads)
    except HTTPError as e:
        return "Ошибка HTTP. Проверь URL адрес, либо у тебя нет права доступа"
    # Если запрос удачный, работаем с "супом"
    try:
        HTML_Code = bs(html.text, features="html.parser")
        result_holders = HTML_Code.findAll("div", {"class":"issue-item_metadata"})
        return result_holders
    except:
        return "Ошибка! В верстке могло что-то поменяться, залезай на страницу и проверяй."


#------------------------------------------------------------------------------------------------------------------

# Функция адреса. Позволяет выбирать ключевые слова, количество искомых статей и даты
def search(KeyWords, page_size, earliest_date=None, latest_date=None):
    """
    KeyWords : list
        A list of keywords that you need to search for articles, e.g. ["mesophase","carbon"]

    page_size : str
        The size of page == the number of results shown in one page
        Possible values: 20, 50, 100

    earliest_date : str, default=None
        The earliest date to search for articles from
        The format is as follows: 4 digits for year, 2 digits for month and two digits for day - "20210407"
        NOTE!!! If earliest_date is given, the argument "latest_date" must be given too

    latest_date : str, optional, default=None
        The date articles are searched to
        The format is as follows: 4 digits for year, 2 digits for month and two digits for day - "20210407"
    """
    search_page = "https://pubs.acs.org/action/doSearch?AllField="
    kw_position = 0
    while kw_position <= len(KeyWords) - 1:
        search_page += KeyWords[kw_position] + "+"
        kw_position += 1
    search_page += "&startPage=0"
    if earliest_date != None and latest_date != None:
        search_page += "&Earliest=%5B" + earliest_date + "+TO+" + latest_date + "%5D"
    else:
        pass
    search_page += "&pageSize=" + page_size
    return search_page

#------------------------------------------------------------------------------------------------------------------

# Функция поиска названий статей
def extract_titles(info_holders):
    titles_list = list()
    for result in info_holders:
        if result.h2 != None:
            article_name = result.h2.get_text()
        else:
            article_name = "N/A"
        titles_list.append(article_name)
    return titles_list

#------------------------------------------------------------------------------------------------------------------

# Функция поиска названий журналов или сборников (книг)
def extract_journals(info_holders):
    journals_and_books = list()
    for result in info_holders:
        if result.find("span", {"class": "issue-item_chapter_bookTitle"}) != None:
            j_title = result.find("span", {"class": "issue-item_chapter_bookTitle"}).get_text() + ", " + "Book title"
        elif result.find("span", {"class": "issue-item_jour-name"}) != None:
            j_title = result.find("span", {"class": "issue-item_jour-name"}).get_text() + ", " + "Jour. title"
        else:
            j_title = "N/A"
        journals_and_books.append(j_title)
    return journals_and_books

#------------------------------------------------------------------------------------------------------------------

# Функция поиска списка авторов
def extract_authors(info_holders):
    authors = list()
    for result in info_holders:
        if result.ul != None:
            j_authors = result.ul.get_text()
        else:
            j_authors = "N/A"
        authors.append(j_authors)
    return authors

#------------------------------------------------------------------------------------------------------------------

# Функция поиска цифрового идентификатора
def extract_doi(info_holders):
    doi_list = list()
    for result in info_holders:
        if result.h2.a != None:
            doi = result.h2.a.get("href")
        else:
            doi = "N/A"
        doi_list.append(doi)
    return doi_list

#------------------------------------------------------------------------------------------------------------------

# Функция поиска даты статьи
def extract_years(info_holders):
    years = list()
    for result in info_holders:
        if result.find("span", {"class": "issue-item_year"}) != None:
            year = result.find("span", {"class": "issue-item_year"}).get_text()
        else:
            year = "N/A"
        years.append(year)
    return years

#------------------------------------------------------------------------------------------------------------------

# Функция поиска выпуска
def extract_issues(info_holders):
    issues = list()
    for result in info_holders:
        if result.find("span", {"class": "issue-item_vol-num"}) != None:
            vol = result.find("span", {"class": "issue-item_vol-num"}).get_text()
        else:
            vol = "N/A"
        if result.find("span", {"class": "issue-item_issue-num"}) != None:
            iss = result.find("span", {"class": "issue-item_issue-num"}).get_text()
        else:
            iss = "N/A"
        issues.append(["Volume " + vol, "Issue " + iss])
    return issues

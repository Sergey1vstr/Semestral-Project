# -*- coding: utf-8 -*-

# TODO: make the input of user data possible through GUI

import pandas as pd
from pandas import ExcelWriter
from webscrap import webscrap, design
from PyQt5 import QtWidgets
import sys

class WebScrapperApp(QtWidgets.QMainWindow, design.Ui_ACSWebScrapper):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.execute_parsing)
        self.KwLine.editingFinished.connect(self.prepare_kwords)
        self.EarlDateLine.editingFinished.connect(self.prepare_date_early)
        self.LateDateLine.editingFinished.connect(self.prepare_date_late)

    # Готовит для парсера ключевые слова
    def prepare_kwords(self):
        return self.KwLine.text().split(",")

    # готовит для парсера параметр количества статей
    def prepare_size(self):
        return self.NumEdit.currentText()

    # Готовит для парсера дату начала
    def prepare_date_early(self):
        return self.EarlDateLine.text()

    # Готовит для парсера дату окончания
    def prepare_date_late(self):
        return self.LateDateLine.text()

    # Функция, срабатывающая при нажатии "Export...", делает всю важную работу
    # Собирает аргументы для парсера,
    def execute_parsing(self):
        kwords = self.prepare_kwords()

        size = self.prepare_size()

        early = self.prepare_date_early()

        late = self.prepare_date_late()

        webpage = webscrap.search(kwords, size, early, late)
        arts = webscrap.get_me_some_info(webpage)
        titles = webscrap.extract_titles(arts)
        journs = webscrap.extract_journals(arts)
        auths = webscrap.extract_authors(arts)
        dois = webscrap.extract_doi(arts)
        dates = webscrap.extract_years(arts)
        issues = webscrap.extract_issues(arts)
        df = pd.DataFrame(columns=["Article Head", "Authors", "Journal or book title", "Year", "Issue", "DOI"])
        df["Article Head"] = titles
        df["Authors"] = auths
        df["Journal or book title"] = journs
        df["Year"] = dates
        df["Issue"] = issues
        df["DOI"] = dois
        with ExcelWriter('Articles.xlsx') as writer:
            df.to_excel(writer)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = WebScrapperApp()  # Создаём объект класса WebScrapperApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

#------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    main()

    # Ask the user to enter the parameters
    #kwords = input("Enter keywords without spaces (Example: mesophase,carbon): ")
    #size = input("Enter number of articles (20,50 or 100): ")
    #early = input("Enter the earliest date to search from (optional, example: 20052020): ")
    #late = input("Enter the earliest date to search to (optional, example: 21052020): ")

    #kwords = kwords.split(",")

# ------------------------------------------------------------------------------------------------------------------

    # Start parsing
    #webpage = webscrap.search(kwords,size,early,late)
    #arts = webscrap.get_me_some_info(webpage)

    #titles = webscrap.extract_titles(arts)
    #journs = webscrap.extract_journals(arts)
    #auths = webscrap.extract_authors(arts)
    #dois = webscrap.extract_doi(arts)
    #dates = webscrap.extract_years(arts)
    #issues = webscrap.extract_issues(arts)

#------------------------------------------------------------------------------------------------------------------

    # Make a more representative form for articles

    #df = pd.DataFrame(columns=["Article Head", "Authors", "Journal or book title", "Year", "Issue", "DOI"])
    #df["Article Head"] = titles
    #df["Authors"] = auths
    #df["Journal or book title"] = journs
    #df["Year"] = dates
    #df["Issue"] = issues
    #df["DOI"] = dois

# ------------------------------------------------------------------------------------------------------------------

    # Write everything into an excel
    # TODO: Сделать возможность записи в разные эксели, либо в один с исключением дублирующихся статей
    #with ExcelWriter('Articles.xlsx') as writer:
        #df.to_excel(writer)

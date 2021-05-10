import pandas as pd
from pandas import ExcelWriter
from webscrap import webscrap

#------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    # Ask the user to enter the parameters
    kwords = input("Enter keywords without spaces (Example: mesophase,carbon): ")
    size = input("Enter number of articles (20,50 or 100): ")
    early = input("Enter the earliest date to search from (optional, example: 20052020): ")
    late = input("Enter the earliest date to search to (optional, example: 21052020): ")

    kwords = kwords.split(",")

# ------------------------------------------------------------------------------------------------------------------

    # Start parsing
    webpage = webscrap.search(kwords,size,early,late)
    arts = webscrap.get_me_some_info(webpage)

    titles = webscrap.extract_titles(arts)
    journs = webscrap.extract_journals(arts)
    auths = webscrap.extract_authors(arts)
    dois = webscrap.extract_doi(arts)
    dates = webscrap.extract_years(arts)
    issues = webscrap.extract_issues(arts)

#------------------------------------------------------------------------------------------------------------------

    # Make a more representative form for articles
    df = pd.DataFrame(columns=["Article Head", "Authors", "Journal or book title", "Year", "Issue", "DOI"])
    df["Article Head"] = titles
    df["Authors"] = auths
    df["Journal or book title"] = journs
    df["Year"] = dates
    df["Issue"] = issues
    df["DOI"] = dois

# ------------------------------------------------------------------------------------------------------------------

    # Write everything into an excel
    # TODO: Сделать возможность записи в разные эксели, либо в один с исключением дублирующихся статей
    with ExcelWriter('Articles.xlsx') as writer:
        df.to_excel(writer)

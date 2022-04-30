import wikipedia
from rich.console import Console
from rich.table import Table


def getWiki(query):
    try:
        return wikipedia.search(query)
    except:
        return "No results found."


def createTable():
    table = Table(title="Select an Article")
    table.add_column("#", justify="left", style="dark_orange")
    table.add_column("Article", justify="left", style="cyan")
    return table


def selectArticle(wikiList):
    table = createTable()
    for i in range(len(wikiList)):
        table.add_row(str(i), wikiList[i])
    console = Console()
    console.print(table)
    selection = input("Select article: ")
    try:
        return wikiList[int(selection)]
    except:
        return "Invalid selection."


def printSummary(article, sentences):
    try:
        summary = wikipedia.summary(article, sentences)
        print(summary)
    except:
        print("No summary found.")


def main():
    search = input("Search: ")
    wikiList = getWiki(search)
    article = selectArticle(wikiList)
    sentences = input("Number of sentences: ")
    printSummary(article, sentences)


if __name__ == '__main__':
    main()

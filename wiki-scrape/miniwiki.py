from bs4 import BeautifulSoup
from requests import get
import string

# scrapes the title, first sentence, and first image of a wikipedia page


def main():
    # prompt user for a wiki page
    q = input("Which Wikipedia article? ")
    url_q = add_underscores(q)

    # get wikipedia page
    page = get("https://en.wikipedia.org/wiki/" + url_q)

    # parse html
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find('h1', id='firstHeading').get_text()
    # get image in table
    img = soup.find('table').find('img').get('src')
    if not img:
        img = "No available image"

    body = soup.find('div', class_='mw-parser-output')
    if not body:
        print("No Wikipedia page available for " + q)
        return 1

    # get first 5 p tags in body
    body_text = body.find_all('p', limit=5)

    print("Title: " + title)
    print("Description: " + first_sentence(body_text, q.split(" ")[0]))
    print("Img URL: " + img[2:len(img)])

# return the first sentence containing a keyword in a block of tags


def first_sentence(b, q):
    # for each tag in a block of tags
    for p in b:
        sentences = p.get_text().split(".")
        # for each sentence of text in a tag
        for s in sentences:
            if q.lower() in s.lower():
                return s
    return b[0].get_text().split(".")[0]


def add_underscores(s):
    return s.replace(" ", "_")


if __name__ == "__main__":
    main()

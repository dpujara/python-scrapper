from bs4 import BeautifulSoup
from requests import get

# practice scraping the local HTML file alice.html
def main():
    # open alice.html as read-only and read
    f = open('dhaval.html', 'r')
    s = f.read()

    # use BeautifulSoup to parse the HTML file
    soup = BeautifulSoup(s,'html.parser')

    # print out the HTML page with BeautifulSoup's prettify function
    print(soup.prettify())

if __name__ == "__main__":
    main()

from bs4 import BeautifulSoup

html = open('links.html' , 'r')
data = html.read()

soup = BeautifulSoup(data )

links = soup.find_all('a' , {"class":"a-link-normal a-text-normal"})

all_links = []
for link in links:
    unformated = link["href"]
    formated = "https://amazon.in"+unformated
    print(formated)
    all_links.append(formated)
    print("\n\n")

for link in all_links:
    with open('links','a') as f:
        f.write(link+"\n")
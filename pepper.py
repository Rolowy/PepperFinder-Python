from bs4 import BeautifulSoup
import request

def forek(param):
    for x in param:
        print(x)


res = request.get('https://www.pepper.pl/grupa/za-darmo')
soup = BeautifulSoup(res.content, "html.parser")

pepperlistname = []
pepperlisturl = []

#print(soup)

for match in soup.find_all('div', class_='gridLayout-item threadCardLayout--card'):
    pepper_name = match.find('a', class_='cept-tt thread-link linkPlain thread-title--card').text;
    pepperlistname.append(pepper_name)
    pepper_url = match.find('a', class_='cept-dealBtn').get('href');
    pepperlisturl.append(pepper_url)

forek(pepperlistname)
forek(pepperlisturl)

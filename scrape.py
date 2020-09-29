import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

link = soup.select(".storylink")
link2 = soup2.select(".storylink")
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_link = link + link2
mega_subtext = subtext + subtext2


def sorted_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(link, subtext):
    hn = []
    for idx, item in enumerate(link):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})
    return sorted_by_votes(hn)


pprint.pprint(create_custom_hn(mega_link, mega_subtext))

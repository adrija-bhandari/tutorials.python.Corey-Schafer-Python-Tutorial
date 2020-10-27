from bs4 import BeautifulSoup
import vyConsoleEscapes as vsc
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('cms_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])

i = 0

for article in soup.find_all('article'):
    i += 1

    headline = article.h2.a.text

    print(i, vsc.format(headline, fgColor='yellow'))

    summary = article.find('div', class_='entry-content').p.text
    print(summary)

    iframe = article.find('iframe', class_='youtube-player')

    if not iframe:
        continue

    vid_src = iframe['src']

    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://www.youtube.com/watch?v={vid_id}'
    print(vsc.format(yt_link, fgColor='red'))

    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
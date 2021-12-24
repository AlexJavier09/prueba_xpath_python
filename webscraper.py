import requests
import lxml.html as html 
import os 
import datetime

HOME_URL = 'https://www.tvn-2.com/'

X_PATH_LINK_TO_ARTICLE = '//h2[@class = "headline"]/a[@class = "lnk"]/@href'
X_PATH_TITLE = '//header[@class = "pg-head"]/h1[@class = "pg-bkn-headline"]/text()'
X_PATH_SUMMARY = '//div[@class = "teaser"]/b/p/text()'
X_PATH_BODY = '//div[@class = "gdu u14 pg-body mce-body"]/p[@class = "mce"]/text()'


def parse_notice(link , notice):
    try:
        reponse = requests.get(link)
        if response.status == 200:
            notice = response.content.decode('utf-8')
            parsed = html.fromstring(notice)
            
            try:
                title = parsed.xpath(X_PATH_TITLE)[0]
                title = title.replace('\"','')
                summary = parsed.xpath(X_PATH_SUMMARY)[0]
                body = parsed.xpath(X_PATH_BODY)
            except IndexError:
                return
            
            with open(f'{today}/{title}.txt', 'w', encoding='utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(body)
                    f.write('\n')
                
        else:
            raise ValueError(f'Error : {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        reponse = requests.get(HOME_URL)
        if reponse.status_code == 200:
            home = reponse.content.decode('utf-8')
            parsed = html.fromstring(home)
            link_to_notices = parsed.xpath(X_PATH_LINK_TO_ARTICLE)
            # print(link_to_notices)
            
            today = datetime.date.today().strftime('%d-%m-%Y')
            if not os.path.isdir(today):
                os.mkdir(today)
                
            for link in link_to_notices:
                parse_notice(link, today)
                
        else:
            raise ValueError(f'Error:{response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()
    
    
if __name__ == '__main__':
    run()

import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
import datetime
import time
from itertools import count
from urllib.request import urlopen


def get_request_url(year, month, enc='utf-8'):
    url = "https://www.melon.com/chart/search/list.htm"
    Cookie = 'PCID=15762297218523292758610; PC_PCID=15762297218523292758610; POC=WP10'
    classCd = "KPOP"
    if year >=2004:
        if year > 2004:
            classCd = "DP0000"
        elif month > 10:
            classCd = "DP0000"
    headers = {
        'Cookie': Cookie,
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                       '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36')
    }
    parameters = urllib.parse.urlencode({'chartType' : 'MO',
        'age' : (year-(year%10)),
        'year' : year,
        'mon' : "0"+str(month) if month<10 else str(month),
        'classCd' : classCd,
        'moved' : 'Y'
    })
    parameters = parameters.encode(enc)
    try:
        html = urllib.request.Request(url, headers=headers)
        data = urllib.request.urlopen(html,parameters).read()
        try:
            ret = data.decode(enc)
        except UnicodeDecodeError as ue:
            ret = data.decode(enc, 'replace')
        return ret
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getMellon(result):

    for year in range(2000, 2019+1):
        for month in range(1, 12+1):
            response = get_request_url(year, month)
            soup = bs(response,'html.parser')
            tbody = soup.find('tbody', attrs={'id': 'chartListObj'})
            rank = 1
            for tr_tag in tbody.findAll('tr'):
                for td_tag in tr_tag.find('td'):
                    result_song_id = td_tag.find('input').get('value')
                    result.append([rank]+[year]+["%s"%str(month) if month<10 else str(month)]+[result_song_id])
                    rank += 1
            print("===== %d년 %s월 완료 ===== " %(year, str("0"+str(month)) if month<10 else str(month)))
    table = pd.DataFrame(result, columns=['rank','year','month', 'song_id'])
    table.to_csv("C:/Users/jay/Desktop/school/2019-2/DataCrawling/DataCrawl/melon/melon_ranking.csv", encoding="cp949",
                 mode='w', index=True)
    time.sleep(5)


def main():
    result =[]
    print("START")
    getMellon(result)


if __name__ == '__main__':
    main()

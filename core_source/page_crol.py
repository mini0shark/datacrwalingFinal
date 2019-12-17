import pandas as pd
import datetime
import urllib.request
from bs4 import BeautifulSoup as bs
import time

start_year = 2016
end_year = 2016 + 1
cut_month = 3
cut_year = 2016
"""
cut_month = 12
cut_year = 2016
"""


def get_pandas(year, month):
    csv_test = pd.read_csv(
        'C:/Users/jay/Desktop/school/2019-2/DataCrawling/DataCrawl/melon/melon_ranking%d_%s.csv' % (
            year, str("0" + str(month)) if month < 10 else str(month)),
        names=['year', 'month', 'ranking', 'song_id'], header=None)
    return csv_test


def get_request_url(songId):
    URL = "https://www.melon.com/song/detail.htm?songId=%s" % songId
    # Cookie = 'PCID=15762297218523292758610; PC_PCID=15762297218523292758610; POC=WP10'
    # Cookie = 'PCID=15762376554090846986981; PC_PCID=15762376554090846986981; POC=WP10'
    # 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    # '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
    Cookie = 'PCID=15762385157528253091433; PC_PCID=15762385157528253091433; POC=WP10'
    Cookie = 'PCID=15762390647668013071402; PC_PCID=15762390647668013071402; POC=WP10'
    Cookie = 'PCID=15762405792953612590711; PC_PCID=15762405792953612590711; POC=WP10'
    Cookie = 'PCID=15762415030015024152178; PC_PCID=15762415030015024152178; POC=WP10'
    Cookie = 'PCID=15762417903155346941448; PC_PCID=15762417903155346941448; POC=WP10'
    Cookie = 'PCID=15762438382916685931019; PC_PCID=15762438382916685931019; POC=WP10'
    Cookie = 'PCID=15762438382916685931019; PC_PCID=15762438382916685931019; POC=WP10; mainPop=2019%3A12%3A14%2023%3A59%3A59'
    Cookie = 'PC_PCID=15762554410499260157980; PCID=15762554410499260157980; POC=WP10'
    Cookie = 'PCID=15762592487416071331154; PC_PCID=15762592487416071331154; POC=WP10'
    Cookie = 'PCID=15763115292074873159254; PC_PCID=15763115292074873159254; POC=WP10'
    Cookie = 'PCID=15763115292074873159254; PC_PCID=15763115292074873159254; POC=WP10'
    headers = {
        'Cookie': Cookie,
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                       '(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    }
    try:
        html = urllib.request.Request(URL, headers=headers)

        data = urllib.request.urlopen(html).read()

        try:
            ret = data.decode("utf-8")
        except UnicodeDecodeError as ue:
            print(ue)
            ret = data.decode("utf-8", 'replace')
        return ret
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), URL))
        return None


def tie_string(list):
    ret = ""
    for i in range(1, len(list)):
        if i > 1:
            ret += " "
        ret += str(list[i])
    return ret


def get_page_result(result):
    diction = {'song_song_id': {'song_title': '', 'song_artist': '', 'song_genre': ''}}
    for year in range(start_year, end_year):
        if year < cut_year:
            continue
        for month in range(1, 6 + 1):
            if year == cut_year and month <= cut_month:
                continue
            data_frame = get_pandas(year, month)
            count = 0
            for row in range(0, len(data_frame) - 1):
                song_song_id = data_frame.get('song_id')[row]
                if song_song_id in diction:
                    song_title = diction[song_song_id]['song_title']
                    song_artist = diction[song_song_id]['song_artist']
                    song_genre = diction[song_song_id]['song_genre']
                else:
                    response = get_request_url(song_song_id)
                    soup = bs(response, 'html.parser')
                    section_info = soup.find('div', attrs={'class': 'section_info'})
                    if section_info is not None:
                        song_name_div = section_info.find('div', attrs={'class': 'song_name'})
                        title_div = section_info.find('div', attrs={'class': 'artist'}).findAll('a')
                        meta_div = section_info.find('div', attrs={'class': 'meta'}).findAll('dd')
                        song_title = tie_string(song_name_div.get_text().split())
                        print("===", song_title, "===")
                        if title_div is not None:
                            res = ""
                            for att in title_div:
                                res += att.get('title')
                            song_artist = res
                        else:
                            song_artist = section_info.find('div', attrs={'class': 'artist'}).get_text().strip()
                        song_genre = meta_div[2].get_text()
                        diction[song_song_id] = {'song_title': song_title, 'song_artist': song_artist,
                                                 'song_genre': song_genre}
                song_ranking = data_frame.get('ranking')[row]
                song_year = data_frame.get('year')[row]
                song_month = data_frame.get('month')[row]
                result.append([song_year] + [song_month] + [song_song_id] + [song_ranking]
                              + [song_title] + [song_artist] + [song_genre])
                print(result[count])
                print("====%d row 끝====" % row)
                count += 1
            melon_page_table = pd.DataFrame(result, columns=['song_year', 'song_month', 'song_song_id', 'song_ranking',
                                                             'song_title', 'song_artist', 'song_genre'])
            melon_page_table.to_csv(
                "C:/Users/jay/Desktop/school/2019-2/DataCrawling/DataCrawl/baseData/melon_base_data%d_%d.csv" % (
                    year, month), encoding="utf-8", mode='w', index=True)
            result.clear()


result = []
get_page_result(result)
print("FINISHED")

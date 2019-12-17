import pandas as pd


def get_data_frame(year, month):
    print("current : ", year, month)
    file = 'C:/Users/jay/Jay/기말플젝/baseData/melon_base_data%d_%d.csv'% (
                year, month)
    try:
        data = pd.read_csv(
            file, encoding='cp949',
            names=['song_year', 'song_month', 'song_song_id', 'song_ranking', 'song_title', 'song_artist',
                   'song_genre'], header=None)
    except UnicodeError as e:
        try:
            data = pd.read_csv(
                file, encoding='utf-8',
                names=['song_year', 'song_month', 'song_song_id', 'song_ranking', 'song_title', 'song_artist',
                       'song_genre'], header=None)
        except Exception as e:
            print(e)
    return data


def make_data():
    list = []
    count_catoon = 0
    diction ={}
    for year in range(2000, 2020):
        for month in range(1, 13):
            result = []
            base_data = get_data_frame(year, month)
            dic = {}
            for i in range(0, len(base_data) - 1):
                genre = base_data.get('song_genre')[i]
                gen_list = genre.split(",")
                tempset = set()
                for gen in gen_list:
                    temp = gen.strip()
                    if temp == '국내CCM' or temp == 'CCM' or temp == '워십':
                        temp = '찬송가'
                    elif temp == '만화' or temp == '게임' or temp == '애니메이션/웹툰' or temp == '키즈':
                        temp = '만화/게임OST'
                        count_catoon +=1
                    elif temp == '국외영화' or temp == '국내영화':
                        temp = '영화OST'
                    elif temp == '국내드라마':
                        temp = '드라마OST'
                    elif temp == '국내뮤지컬':
                        temp = '뮤지컬'
                    elif temp == '보컬재즈':
                        temp = '재즈'
                    if temp != '찬송가' and temp != '뮤지컬':
                        tempset.add(temp)
                    else:
                        print(temp)
                if len(tempset) == 0:
                    continue
                for t in tempset:
                    if t in dic:
                        dic[t] = dic[t] + 1
                    else:
                        dic[t] = 1
                tempset.clear()
            for key, value in dic.items():
                # result.append([key] + [value])
                if key in diction:
                    diction[key] += value
                else :
                    diction[key] = value
    for key, value in diction.items():
        print(key, " : ", value, "건")
            # 저장
            # mon = str("0" + str(month)) if month < 10 else str(month)
            # melon_page_table = pd.DataFrame(result, columns=['genre', 'freq'])
            # melon_page_table.to_csv(
            #     "C:/Users/jay/Desktop/school/2019-2/DataCrawling/DataCrawl/arranged_data/arranged_data%d_%s.csv" % (
            #         year, mon), encoding="utf-8", mode='w', index=True)
    print(list)



def main():
    make_data()


# arranged_data


main()

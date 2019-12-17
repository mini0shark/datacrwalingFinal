import pandas as pd
import operator


def get_data_frame(year, month):
    print("current : ", year, month)
    file = 'C:/Users/jay/Jay/기말플젝/baseData/melon_base_data%d_%d.csv'% (
                year, month)
    try:
        data = pd.read_csv(
            file, encoding='cp949',
            names=['song_ranking', 'song_year', 'song_song_id', 'song_month', 'song_title', 'song_artist',
                   'song_genre'], header=None)
    except UnicodeError as e:
        try:
            data = pd.read_csv(
                file, encoding='utf-8',
                names=['song_ranking', 'song_year', 'song_song_id', 'song_month', 'song_title', 'song_artist',
                   'song_genre'], header=None)
        except Exception as e:
            print(e)
    return data


# {'뉴에이지', '애시드/퓨전/팝', '댄스', '재즈', '일렉트로니카', 'EDM', '랩/힙합', 'J-POP', '드라마OST', '-', '인디음악', '록/메탈', '발라드', '영화OST', '성인가요', '클래식', '만화/게임OST', 'POP', '포크/블루스', 'R&B/Soul'}
def show_data(start_y, end_y, key, specially):
    list = []
    artist = {}

    for year in range(start_y, end_y+1):
        for month in range(1, 12 +1):
            count = 0
            base_data = get_data_frame(year, month)

            for i in range(0, len(base_data) - 1):
                genre = base_data.get('song_genre')[i]
                gen_list = genre.split(",")
                for gen in gen_list:
                    temp = gen.strip()
                    if temp == key:
                        print(base_data.get('song_month')[i],"/",base_data.get('song_song_id')[i],"\t","/",
                              base_data.get('song_genre')[i],"\t",base_data.get('song_artist')[i],"/\t\t ", base_data.get('song_title')[i])

                        if base_data.get('song_artist')[i] in artist:
                            artist[base_data.get('song_artist')[i]] +=1
                        else :
                            artist[base_data.get('song_artist')[i]] = 1
                        count += 1
            list.append(count)
    print(list)
    sort_art = sorted(artist.items(), key = operator.itemgetter(1))
    for k, v in sort_art:
        print(v, " :\t  ", k)
    # print(artist.keys())
    print(type(sort_art))



show_data(2013, 2019, "랩/힙합", 9)
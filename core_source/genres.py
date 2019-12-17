import pandas as pd


def get_data_frame(year, month):
    # print("current : ", year, month)
    mon = str("0" + str(month)) if month < 10 else str(month)
    load_file = "C:/Users/jay/Jay/기말플젝/arranged_data/arranged_data%d_%s.csv" % (
        year, mon)
    try:
        data = pd.read_csv(load_file, encoding='cp949',
                           names=['genre', 'count'], header=None)
    except UnicodeError:
        try:
            data = pd.read_csv(load_file, encoding='utf-8',
                               names=['genre', 'count'], header=None)
        except Exception as e:
            print(e)
    return data


def show_genre():
    genre = set()
    for year in range(2000, 2020):
        for month in range(1, 13):
            data = get_data_frame(year, month)
            for i in range(0, len(data)-1):
                genre.add(data.get('genre')[i])
    print(genre)

show_genre()

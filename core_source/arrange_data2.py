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


def get_result():
    genre = ['애시드/퓨전/팝', '드라마OST', '클래식', '인디음악', '영화OST', '발라드', '댄스', '록/메탈',
             'R&B/Soul', '일렉트로니카', '랩/힙합', 'EDM', 'POP', 'J-POP', '성인가요', '재즈', '뉴에이지',
             '포크/블루스', '만화/게임OST', '-']
    step1 = []
    for year in range(2000, 2020):
        for month in range(1, 13):
            data = get_data_frame(year, month)
            temp_list = {}
            count = 0
            for i in range(0, len(data) - 1):
                print(data.get('genre')[i], data.get('count')[i])
                temp_list[data.get('genre')[i]] = data.get('count')[i]
                count += int(data.get('count')[i])
            for key, val in temp_list.items():
                step1.append(["%d-%s" %(year, str("0" + str(month)) if month < 10 else str(month))] +
                             [key] + [int(val)/count*100])

    print(step1)
    result = []
    basic = {}
    for lt in step1:
        for i in range(0, len(genre)):
            if lt[1] == genre[i]:
                if lt[0] not in basic:
                    basic[lt[0]] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                basic.get(lt[0])[i] = lt[2]
        # result.append([lt[0]] + basic)
    print(basic)
    for key, value in basic.items():
        result.append([key] + value)
    melon_page_table = pd.DataFrame(result, columns=['Date', '애시드/퓨전/팝', '드라마OST', '클래식', '인디음악', '영화OST', '발라드', '댄스', '록/메탈',
                                                     'R&B/Soul', '일렉트로니카', '랩/힙합', 'EDM', 'POP', 'J-POP', '성인가요', '재즈',
                                                     '뉴에이지',
                                                     '포크/블루스', '만화/게임OST', '-'])
    melon_page_table.to_csv(
        "C:/Users/jay/Jay/기말플젝/final_data//final.csv", encoding="utf-8", mode='w',
        index=True)
    # 년도 분석


get_result()


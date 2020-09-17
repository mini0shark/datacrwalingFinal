# datacrwalingFinal

2019 2학기 데이터 크롤링

core_source
  ranking.py => melon_ranking.csv 파일을 생성하는 파일
  page_crol.py => melon_base_data.csv 파일을 생성하는 파일
  arrange_data.py =>  melon_base_datayyyy_mm.csv를 arranged_datayyyy_mm.csv로 바꾸는 과정
  arrange_data2.py => arranged_datayyyy_mm.csv를 finla_data로 바꾸는 과정
  genres.py =>  장르 들을 만드는 과정
  find_songs  =>  시간에 따른 장르별 노래를 확인하는 과정
  장르의 월별 특징.ipynb         :     월별 데이터 분석
  20년간의 월간차트를 이용한 음악 트렌드.ipynb    : 전체 추이 분석

some_test_sources
   시계열 분석, 회귀분석등의 테스트 코드들


중간데이터
  melon
    melon_ranking.csv     :   월간 top100을 모두 가져온 파일
    melon_rankingyyyy_mm.csv  :   melon_ranking을 page_cro.py에서 사용하기 편하게 월별로 나눈 파일
  baseData
    melon_base_data.csv   :   melon_rankingyyyy_mm.csv의 song_id를 사용하여 세부 정보를 가져온 파일
    melon_base_datayyyy_mm.csv :   melon_base_data를 page_crol.py에서 사용하기 편하게 나누어 둔 파일
  arranged_data
    arranged_datayyyy_mm  :   melonbase_datayyyy_mm.csv에서 각 장르별 멜론 차트 진입 수를 판별한 것
  final_data
    final_data.csv        :   최종적으로 사용한 데이터
    

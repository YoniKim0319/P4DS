#필요 라이브러리 임포트
from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import load_workbook
import time

# Chrome 웹드라이버 설정
browser = webdriver.Chrome("./chromedriver")

# 엑셀 파일 로드 및 드라마 이름 추출
drama_data = 'C:\\Users\\82104\\PycharmProjects\\pythonProject\\capstone_drama_01.xlsx'
read_xlsx = load_workbook(drama_data)
read_sheet = read_xlsx.active
name_col = read_sheet['D3:D1131']

# 드라마 이름을 리스트에 저장
drama_names = [cell_2.value for cell_1 in name_col for cell_2 in cell_1]

# 네이버 드라마 검색 및 에피소드 크롤링
drama_episode_list = []

crawling_size = 10  # 10개씩 크롤링
for i in range(0, len(drama_names), crawling_size):
    batch_drama_names = drama_names[i: i + crawling_size]

    for drama_search in batch_drama_names:
        browser.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%9C%EA%B5%AD%EB%93%9C%EB%9D%BC%EB%A7%88+{drama_search}")

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 드라마 에피소드 정보 추출
        drama_episode_1 = soup.select_one('div.detail_info > dl > div:nth-child(1) > dd > span > em')

        # 에피소드 정보 전처리 및 리스트에 추가
        try:
            drama_episode_2 = int(drama_episode_1.text.strip('부작'))
            drama_episode_list.append(drama_episode_2)
        except:
            drama_episode_2 = 'fail'
            drama_episode_list.append(drama_episode_2)

        time.sleep(3)  # 각 요청 간의 3초 딜레이

# 업데이트된 에피소드 정보로 엑셀 파일 업데이트
column_to_update = 'F'
start_row = 3

for index, value in enumerate(drama_episode_list):
    read_sheet[f'{column_to_update}{start_row + index}'] = value

# 업데이트된 엑셀 파일 저장
read_xlsx.save(drama_data)

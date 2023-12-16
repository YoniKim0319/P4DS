from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import load_workbook
import time

browser = webdriver.Chrome("./chromedriver")

#-----------------------------------------------------------#
##드라마 제목 엑셀에서 리스트 형태로 불러오기

drama_data = 'C:\\Users\\82104\\PycharmProjects\\pythonProject\\capstone_drama_01.xlsx'
read_xlsx = load_workbook(drama_data)
read_sheet = read_xlsx.active
name_col = read_sheet['D3:D1131'] #D3:D1131

#drama_names 리스트에 엑셀에서 불러온 값을 저장
drama_names = []
for cell_1 in name_col :            #값이 tuple이라 과정이 2번 필요
    for cell_2 in cell_1 :
        drama_names.append(cell_2.value)

#-----------------------------------------------------------#
##네이버에 드라마 검색 -> 회차수를 크롤링 후 drama_episode_list에 저장
drama_episode_list = []

# 50개씩 나누어 크롤링 진행
crawling_size = 10
for i in range(0, len(drama_names), crawling_size):
    batch_drama_names = drama_names[i : i+crawling_size]

    for drama_search in batch_drama_names:

        browser.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%9C%EA%B5%AD%EB%93%9C%EB%9D%BC%EB%A7%88+{drama_search}")

        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')

        drama_episode_1 = soup.select_one('div.detail_info > dl > div:nth-child(1) > dd > span > em')

        # 수집한 회차수를 전처리(int로 만들고 '부작'글자를 삭제) -> 리스트에 append
        try:
            drama_episode_2 = drama_episode_1.text
            drama_episode_2 = int(drama_episode_2.strip('부작'))

            drama_episode_list.append(drama_episode_2)

        except:
            drama_episode_2 = 'fail'  # 검색에 실패할 경우 fail값을 입력
            drama_episode_list.append(drama_episode_2)

    time.sleep(3)  # 간격10초 설정

#-----------------------------------------------------------#
##drama_episode_list에 있는 회차수를 엑셀에 저장

#기존 엑셀의 F열에 3행부터 기입
column_to_update = 'F'
start_row = 3

for index, value in enumerate(drama_episode_list) :
    read_sheet[f'{column_to_update}{start_row + index}'] = value

#기존의 엑셀 파일에 저장
read_xlsx.save(drama_data)
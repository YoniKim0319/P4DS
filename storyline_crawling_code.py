#필요 라이브러리 임포트

import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 웹 드라이버 초기화 - 본인 버전에선 Chrome뒤에 ()를 공란으로 두어야 실행이 되는 것을 확인함
browser = webdriver.Chrome()

# -----------------------------------------------------------#
# 드라마 제목 리스트

# 엑셀 파일 불러오기
read_xlsx = load_workbook('drama_01.xlsx')
read_sheet = read_xlsx.active

# 엑셀에서 드라마 제목 데이터 추출
name_col = read_sheet['D3:D1131']
drama_names = []
for cell_1 in name_col:
    for cell_2 in cell_1:
        drama_names.append(cell_2.value)

# 검증 코드: 처음 50개 항목만 가져오기
# drama_names = [cell_2.value for cell_1 in name_col for cell_2 in cell_1][:50]

# -----------------------------------------------------------#
# 네이버에 드라마 검색 -> 리스트에 저장
drama_storyline_list = []

for drama_name in drama_names:
    drama_search = drama_name

    # 네이버 '한국드라마+드라마제목' 검색한 결과창으로 이동
    browser.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%9C%EA%B5%AD%EB%93%9C%EB%9D%BC%EB%A7%88+{drama_search}")

    # "펼쳐보기" 버튼이 클릭 가능할 때까지 대기
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "story_more"))
        )
        # "펼쳐보기" 버튼 클릭
        element.click()

        # 확장된 내용이 보이도록 대기
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "desc._text"))
        )
    except:
        print("Error clicking the '펼쳐보기' button")

    # 현재 페이지 HTML을 가져와 BeautifulSoup으로 파싱, 즉, 펼쳐보기까지 모두 된 html문서 불러옴
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 확장된 줄거리 내용 선택
    drama_episode_1 = soup.select_one('div.text_expand._img_ellipsis span.desc._text')

    try:
        drama_episode_2 = drama_episode_1.text
        drama_storyline_list.append(drama_episode_2)
    except:
        drama_episode_2 = 'fail'
        drama_storyline_list.append(drama_episode_2)

    # 페이지 로딩 대기를 위한 sleep
    time.sleep(1)

# -----------------------------------------------------------#
# drama_episode_list에 있는 줄거리를 기존 엑셀에 저장

# 기존 엑셀의 F열에 3행부터 기입
column_to_update = 'G'
start_row = 3

# 엑셀에 줄거리 추가
for index, value in enumerate(drama_storyline_list):
    read_sheet[f'{column_to_update}{start_row + index}'] = value

# 변경된 내용을 엑셀 파일에 저장
read_xlsx.save('drama_02.xlsx')

import openpyxl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()

# -----------------------------------------------------------#
# 드라마 제목 리스트
from openpyxl import load_workbook

read_xlsx = load_workbook('capstone_drama_01.xlsx')
read_sheet = read_xlsx.active
name_col = read_sheet['D3:D1131']

drama_names = []
for cell_1 in name_col :
    for cell_2 in cell_1 :
        drama_names.append(cell_2.value)

# -----------------------------------------------------------#
# 네이버에 드라마 검색 -> 리스트에 저장
drama_storyline_list = []

for y in drama_names:
    drama_search = y

    browser.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%9C%EA%B5%AD%EB%93%9C%EB%9D%BC%EB%A7%88+{drama_search}")

    # Wait for the "펼쳐보기" button to be clickable
    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "story_more"))
        )
        # Click the "펼쳐보기" button
        element.click()

        # Wait for the expanded content to be visible
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "desc._text"))
        )
    except:
        print("Error clicking the '펼쳐보기' button")

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Select the expanded storyline content
    drama_episode_1 = soup.select_one('div.text_expand._img_ellipsis span.desc._text')

    try:
        drama_episode_2 = drama_episode_1.text
        drama_storyline_list.append(drama_episode_2)
    except:
        drama_episode_2 = 'fail'
        drama_storyline_list.append(drama_episode_2)

    time.sleep(1)

# -----------------------------------------------------------#
##drama_episode_list에 있는 줄거리를 기존엑셀에 저장

#기존 엑셀의 F열에 3행부터 기입
column_to_update = 'F'
start_row = 3

for index, value in enumerate(drama_storyline_list) :
    read_sheet[f'{column_to_update}{start_row + index}'] = value

#기존의 엑셀 파일에 저장
read_xlsx.save('capstone_drama_01.xlsx')
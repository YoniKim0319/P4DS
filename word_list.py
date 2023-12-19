import openpyxl
from konlpy.tag import Komoran

# 엑셀 파일 경로 지정
excel_file_path = 'storyline_update2.xlsx'  # 실제 파일 경로로 변경해야 합니다.

# 엑셀 파일 열기
workbook = openpyxl.load_workbook(excel_file_path)

# 원하는 시트 선택 (예: 첫 번째 시트 선택)
sheet = workbook.active

# KoNLPy의 Komoran 객체 생성
komoran = Komoran()

# 명사와 형용사 추출
nouns_and_adjectives_per_row_dict = {}
for row in range(1, sheet.max_row + 1):
    text = sheet.cell(row=row, column=1).value
    if text:
        pos_tags = komoran.pos(text)
        extracted_words = [word for word, pos in pos_tags if pos in ['NN', 'NNG', 'NNP', 'VA', 'VAX', 'XR']]
        nouns_and_adjectives_per_row_dict[row] = extracted_words

# 결과 확인 (딕셔너리)
# for row, words in nouns_and_adjectives_per_row_dict.items():
#     print(f"Row {row}: {words}")

print(nouns_and_adjectives_per_row_dict)




# 저장할 엑셀 파일 경로 지정
output_excel_file_path = 'drama_complete.xlsx'

# 기존 엑셀 파일 열기
output_workbook = openpyxl.load_workbook(output_excel_file_path)

# 원하는 시트 선택 (예: 첫 번째 시트 선택)
output_sheet = output_workbook.active

# 결과를 엑셀 파일에 저장 (G열에 저장)
for row, words in nouns_and_adjectives_per_row_dict.items():
    for col, word in enumerate(words, start=1):
        output_sheet.cell(row=row, column=6 + col, value=word)

# 저장한 내용을 엑셀 파일에 반영
output_workbook.save(output_excel_file_path)

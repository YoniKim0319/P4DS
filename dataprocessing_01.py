import pandas as pd

file_path = "C:\\Users\\82104\\PycharmProjects\\pythonProject\\2023\\PDS\\W14\\capstone_drama_test.xlsx"
drama_data_df = pd.read_excel(file_path, header=1)
print(drama_data_df)

# 두 개의 열에 대해 'fail' 값을 가진 행 삭제
drama_data_df = drama_data_df[~((drama_data_df['drama_episode'] == 'fail')
                                & (drama_data_df['drama_summary'] == 'fail'))]
# 'Column1', 'Column2'는 실제 열의 이름으로 바꿔야 합니다.

# 수정된 DataFrame을 새로운 엑셀 파일로 저장
drama_data_df.to_excel('C:\\Users\\82104\\PycharmProjects\\pythonProject\\capstone_drama_no_fail.xlsx', index=False)

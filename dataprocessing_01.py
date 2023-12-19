import pandas as pd

# 파일 불러오기
file_path = "./drama_02.xlsx"
drama_data_df = pd.read_excel(file_path, header=1)
print(drama_data_df)

# 두 개의 열에 대해 'fail' 값을 가진 행 삭제
drama_data_df = drama_data_df[~((drama_data_df['drama_episode'] == 'fail')
                                & (drama_data_df['drama_summary'] == 'fail'))]

# 수정된 DataFrame을 새로운 엑셀 파일로 저장
drama_data_df.to_excel('drama_processing.xlsx', index=False)

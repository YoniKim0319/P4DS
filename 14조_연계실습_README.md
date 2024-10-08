# W15 연계실습 (14조) - 파이썬을 이용한 데이터사이언스

<br>


<br>

## ⭐주제
### *드라마 트렌드 찾기*
### *: 키워드(태그)의 빈도수와 키워드 등장 기간 분석*

<br>


<br>

## 📖목차
<br>

[1. 멤버 소개](#멤버-소개)

[2. 프로젝트 개요](#프로젝트-개요)

[3. 프로젝트 주요 과정](#프로젝트-주요-과정)

[4. 추가 개발 정도](#추가-개발-정도)

[5. 향후 연구 과제](#향후-연구-과제)

<br>


<br>

## 👩‍👧‍👦멤버 소개
<br>

<center>

### <mark>***연계실습 14조 멤버***</mark>

</center>

<center>

|**김주연**|**나예린**|**안교영**|
|:-----------:|:-----------:|:-----------:|
|2021120118|2022111734|2022111744|
|YoniKim0319|N4YE|akyoun|
|수집 - 크롤링|팀장 - 총괄|시각화 - 워드클라우드|

</center>


<br>


<br>

## 📜프로젝트 개요
<br>

1. __프로젝트 배경 및 필요성__
    * 패션업계에서 유행과 트렌드에 민감하듯, 소재의 유행과 트렌드는 드라마에서도 마찬가지인 상황.
    * 하지만 근래에 이르러서는 비슷한 소재가 나오면 시청자들로부터 진부하다는 평가가 나오는 한편, 방송사에서도 해당 내용을 가지고 드라마를 만드는 일이 드물어짐.
    * 따라서 드라마의 트렌드를 빈도수를 이용해 분석하여 경향성을 분석하고 이후 유행할 트렌드를 예측해보고자 함.  
<br>

2. __프로젝트 목표__
    * 첫번째, 요즘 유행하는 드라마의 트렌드를 분석하고 이후 유행할 트렌드를 예측. 
    * 두번째, 과거 유행한 드라마를 키워드의 빈도수 등으로 파악하여 한 소재가 유행하였을 때 그 트렌드의 지속시간에 대해서 분석.
    * 주도된 유행의 경우 지속기간이 얼마나 되는지, 드라마의 평균 시청률을 바탕으로 트렌드가 되었던 ‘드라마’를 선정 후 정리하여 비교해볼 예정.

<br>


<br>

## 🖥️프로젝트 주요 과정
<br>

1. __초기__

    * 데이터 수집
      drama_01.xlsx(원본파일-캡스톤1 산출물): company, year, title 열만 존재
    * 데이터 시각화
      수집된 부분까지 워드클라우드로 시각화함

2. __디벨롭 계획__

    * 데이터 수집
      - webcrawler_01: 회차수 크롤링 => drama_02.xlsx 저장 (episode)
      - webcrawler_02: 줄거리를 크롤링 => drama_02.xlsx 저장 (summary)
         
    * 데이터 전처리
      - episode, summmary 부분 fail값 원인 분석 -> 드라마 이름 오타 => 오타 수정
      - summary의 fail 값 우선 수동 기입 -> 검색해도 안 나올 경우 fail 값 유지
      
      - data_processing: episode와 summary 둘 다 fail인 경우 행 삭제 => drama_processing.xlsx 저장
      - episode의 fail 값 수동 기입 => drama_complete.xlsx 저장
         
    * 데이터 시각화
      - wordcloud: 줄거리 기반 형태소 분석 -> 워드클라우드 진행 => drama_complete.xlsx 저장
      
    * 데이터 분석
      - 초기 분석: 워드클라우드로 시각화하여 빈도수를 파악하고자 함

    * github 관련
      - webcrawler_02의 경우, main브랜치와 연결이 되지 않는 문제 발생 => 강제 병합 후 머지

3. __결과물__
    * 데이터 수집 : 크롤링을 통해 수집한 새로운 데이터 + 기존 데이터 => drama_02.xlsx
    * 데이터 전처리: 오타 수정, fail값 삭제 후 데이터 양 맞춘 데이터 => drama_processing_02.xlsx
    * 데이터 시각화: 줄거리 컬럼 wordcloud => drama_complete.xlsx

<br>


<br>

## 🔩추가 개발 정도


1. __기존 상황__
    * 데이터 수집: 방송사, 방송연도, 드라마 제목만 수집
    * 데이터 전처리: 눈에 보이는 오타들만 정리함
    * 데이터 시각화: 수집된 부분들만 시각화하여 제대로 빈도수를 보지 못함


2. __추가 개발 상황__
    * 데이터 수집: 회차수, 키워드가 포함된 줄거리 데이터 추가 수집하여 분석 데이터의 양을 늘림
    * 데이터 전처리: 오타와 fail값을 더블체크하여 깔끔하게 클렌징했고 흩어진 데이터들을 하나로 모아 분석에 용이하게 함
    * 데이터 시각화: 트렌드를 파악할 수 있는 키워드가 포함된 줄거리 데이터를 시각화했기 때문에 기존보다 트렌드를 잘 파악 할 수 있었음.

    
    ❗산출물인 엑셀파일은 각 브랜치에 정리❗
   <br>(엑셀파일이 같은 공간에 있어야 코드가 오류 없이 실행되기 때문)
   
    * 전반적으로, 수작업으로 진행한 과정을 코드를 사용해 효율성을 높였다.
      <br> 뿐만 아니라, 판다스의 데이터프레임 형식으로 한눈에 데이터를 볼 수 있게끔 발전시켰다. 강의시간에 배웠던 것 처럼 깃 브랜치들을 수집, 전처리, 시각화로 나누어 한눈에 과정을 볼 수 있게 정리했다.
   
    * __실행방식__: drama_01 파일, 크롬드라이버 다운 후, webcrawler_01, webcrawler_02 실행 -> data_processing_01, data_processing_02 파일 실행 -> wordcloud 파일 실행
    * 단발적으로 진행되는 작업들이 많아, 함수화 대신 반복문으로 간단하게 표현해주었다.

3. __최종결과물__
   * 최종 데이터셋
     ![KakaoTalk_20231219_173042535](https://github.com/YoniKim0319/P4DS/assets/129754535/85ede64f-8860-444e-8ebd-eb5473ad648b)

   * 워드클라우드
     ![KakaoTalk_20231219_174344523](https://github.com/YoniKim0319/P4DS/assets/129754535/eec4b58a-e9fe-4c64-aa70-f66fd2582a3e)

<br>


<br>

## 👣향후 연구 과제
<br>

1. __전처리 과정__
   
   합성명사가 과도하게 분리되어 깔끔하게 시각화 되지 못한 wordcloud를 지정어 처리하여 깔끔하게 시각화될 수 있도록
   전처리를 디벨롭하고자 함
   
2.  __유사도 분석__
   
     word-to-vec의 유사도 분석으로 분석 방법을 디벨롭하여 트렌드를 보다 더 정확하게 파악하고자 함

<br>


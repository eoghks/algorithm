#필요
-python v3.8이상

#install
-python [https://www.python.org/downloads/]
*설치시 Add Python version to PATH 체크 필수

#Run
-Add PATH가 된경우
*연결프로그램-python ->더블클릭 실행 ->cmd로 실행

-PATH가 추가되지않은경우
*검색:IDLE -> IDLE -> 좌측 상단 File +Open -> 저장된 파일 OPEN -> RUN(F5)

#실행 파일
main함수만 실행파일 입니다. 나머지는 모듈화 한것입니다.

#input.txt
입력 graph를 가진 입력 파일로 각 edge의 weight를 가지고 있으며 inf의 경우 99999로 변환됩니다. 
99999를 이상의 weight 사용시 load파일의 inf를 99999로 치환해주는 if문의 숫자를 변경해야합니다.

#vertex는 1~n개 까지 존재하나 계산 결과를 제외한 연산에서는 0~n-1의 인덱스를 사용합니다.
(코드내에 결과 값은 1~n으로 바꿔주는 코드 존재)


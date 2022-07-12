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
W:가방이 넣을수있는 최대 무게
item: id: 오름차순 price: 가격 weight: 무게
위의 형식을 따라 입력을 주셔야합니다.

#모듈화한파일
backtracking.py, brand_and_bound.py, dynamic.py 이 세가지 파일은 각자의 방법으로 문제를 푸는 함수를 가지고있습니다.
loadfile:inputfile을 읽는 역할을 합니다.
tree.py: brand_and_bound, backtracking의 입력으로 주는 트리를 생성하는 역할을 합니다.


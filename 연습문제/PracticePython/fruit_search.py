fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
search_fruit = input("찾을 과일을 입력하세요: ")
if search_fruit in fruits:
    print(f"'{search_fruit}'가 목록에 있습니다!")
else:
    print(f"'{search_fruit}'는 목록에 없습니다.")
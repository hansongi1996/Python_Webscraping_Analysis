def greeting(name, message="안녕하세요"):
    print(f"{message}, {name}님!")

def greeting_en(name, message="Hello"):
    print(f"{message}, {name}!")

greeting("김철수")
greeting_en("John")
greeting("이영희", "안녕하세요! 좋은 하루 되세요")

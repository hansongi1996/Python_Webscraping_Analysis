# 좌표 언패킹
coord = (10, 20)
x, y = coord
print(f"좌표: x={x}, y={y}")

# 리스트 언패킹
lst = [1, 2, 3]
a, b, c = lst
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

# *args를 이용한 합계 함수
def total_sum(*args):
    return sum(args)
print(f"가변 인수의 합: {total_sum(10, 20, 30)}")

# **kwargs를 이용한 키워드 인수 출력 함수
def print_kwargs(**kwargs):
    pairs = [f"{k}={v}" for k, v in kwargs.items()]
    print(f"키워드 인수들: {', '.join(pairs)}")
print_kwargs(name="김철수", age=25, city="서울")

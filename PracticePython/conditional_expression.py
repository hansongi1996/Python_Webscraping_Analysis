score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")

numbers = [5, 12, 8, 42, 23]
max_num = max(numbers) if numbers else None
print(f"숫자들의 최대값: {max_num}")

positives = [n for n in numbers if n > 0]
print(f"양수들: {positives}")

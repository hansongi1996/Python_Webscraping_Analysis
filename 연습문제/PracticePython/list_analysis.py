numbers = [15, 3, 27, 8, 19, 12, 31]
sorted_numbers = sorted(numbers, reverse=True)
second_largest = sorted_numbers[1] if len(sorted_numbers) > 1 else None
print(f"숫자 목록: {numbers}")
print(f"최댓값: {sorted_numbers[0]}")
print(f"최솟값: {sorted_numbers[-1]}")
print(f"두 번째로 큰 값: {second_largest}")
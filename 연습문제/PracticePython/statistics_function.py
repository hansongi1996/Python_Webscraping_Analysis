def statistics(nums):
    avg = sum(nums) / len(nums)
    maximum = max(nums)
    minimum = min(nums)
    variance = sum((x - avg) ** 2 for x in nums) / len(nums)
    stddev = variance ** 0.5
    return avg, maximum, minimum, stddev

numbers = [10, 20, 30, 40, 50]
avg, maximum, minimum, stddev = statistics(numbers)

print(f"숫자들: {numbers}")
print(f"평균: {avg:.1f}")
print(f"최댓값: {maximum}")
print(f"최솟값: {minimum}")
print(f"표준편차: {stddev:.2f}")

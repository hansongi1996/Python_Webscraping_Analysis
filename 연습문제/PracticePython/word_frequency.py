from collections import Counter

with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
freq = Counter(words)

print("단어 빈도 분석 결과:")
for word, count in freq.most_common():
    print(f"{word}: {count}번")

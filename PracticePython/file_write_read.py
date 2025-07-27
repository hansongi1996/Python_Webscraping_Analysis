lines = [
    "안녕하세요",
    "파이썬 파일 처리를 연습하고 있습니다",
    "오늘은 좋은 날씨입니다"
]

print("파일에 저장할 내용:")
for line in lines:
    print(line)

with open("sample.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

print("\n파일에서 읽어온 내용:")
with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

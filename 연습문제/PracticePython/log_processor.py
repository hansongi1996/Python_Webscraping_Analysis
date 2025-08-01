logs = [
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족"
]

with open("log.txt", "w", encoding="utf-8") as f:
    for log in logs:
        f.write(log + "\n")

print("로그 파일이 생성되었습니다.\n")

print("ERROR 레벨 로그들:")
with open("log.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())

print("\nWARNING 레벨 로그들:")
with open("log.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "WARNING" in line:
            print(line.strip())

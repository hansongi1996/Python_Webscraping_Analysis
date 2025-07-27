import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version.splitlines()[0]}")
print(f"운영체제: {os.name}")
print(f"환경 변수 PATH 일부: {os.environ.get('PATH', '').split(os.pathsep)[0:3]}")

filepath = "/Users/username/documents/report.txt"
directory = os.path.dirname(filepath)
filename = os.path.basename(filepath)
ext = os.path.splitext(filepath)[1]

print("파일 경로 정보:")
print(f"- 디렉토리: {directory}")
print(f"- 파일명: {filename}")
print(f"- 확장자: {ext}")
print(f"파일 존재 여부: {os.path.exists(filepath)}")

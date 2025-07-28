# 03-1_search_books.py

import requests
import json
import os
import pandas as pd

# 1) 네이버 API 인증키 (수업 때 발급받은 본인 키로 교체)
headers = {
    "X-Naver-Client-Id":     "4dwVypaTc5EgDuwVPV8o",
    "X-Naver-Client-Secret": "3bEt_lKBP8"
}

# 2) API 호출 + 데이터 추출 함수
def search_books(query):
    payload = {
        'query':   query,   # 동적으로 들어오는 검색어
        'display': 50,
        'sort':    'sim'
    }
    url = 'https://openapi.naver.com/v1/search/book.json'
    res = requests.get(url, params=payload, headers=headers)
    res.raise_for_status()               # 혹시 에러나면 중단
    return res.json().get('items', [])   # 'items' 목록만 반환

# 3) JSON 파일로 저장하는 함수
def save_json(data, filepath):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# 4) 직접 실행할 때 동작
if __name__ == "__main__":
    # 원하는 검색어를 여기 바꿔서 실행해 보세요
    books = search_books("파이썬")  
    save_json(books, "data/books.json")
    print("✅ data/books.json 파일 생성 완료!")
df_books = pd.DataFrame(books)      # books 리스트를 DataFrame으로
print(df_books.head())              # 앞 5개 행 확인용 출력

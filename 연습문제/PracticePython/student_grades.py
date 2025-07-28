grades = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최수진': 95
}
print("학생 성적:")
for student, score in grades.items():
    print(f"{student}: {score}점")
average_score = sum(grades.values()) / len(grades)
print(f"평균 점수: {average_score:.1f}점")
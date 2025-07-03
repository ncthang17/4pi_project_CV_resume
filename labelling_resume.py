import pandas as pd

# Load trainee data
trainee_df = pd.read_csv("data_resume.csv")
trainee_df.columns = trainee_df.columns.str.strip()  # Clean header spaces

# ---------------------------
# 1️⃣ Exact Criteria Mapping
# ---------------------------
criteria_mapping = {
    ("성장과정", "가치관"): [
        ("명확하고 긍정적인 가치관 + 구체적 사례", "A"), ("가치관 명확 + 간단한 사례", "B"), ("가치관은 있으나 애매하거나 사례 부족", "C"), ("가치관 불분명 + 사례 없음", "D"), ("내용 부실, 진정성 없음", "E")
    ],
    ("성장과정", "가족/환경의 영향"): [
        ("영향 관계 명확 + 구체적 설명", "A"),
        ("영향 관계 보통 + 적당한 설명", "B"),
        ("영향은 있으나 논리 부족 단편적 언급 + 설명 없음 영향 설명 없음", "C"),
        ("단편적 언급 + 설명 없음", "D"),
        ("영향 설명 없음", "E")
    ],
    ("성장과정", "전환점/특별한 경험"): [
        ("특별한 경험 + 뚜렷한 성찰", "A"),
        ("경험은 있음 + 부분적 성찰", "B"),
        ("경험만 나열, 의미 부족", "C"),
        ("경험 모호, 연결 안 됨", "D"),
        ("전환점 부재", "E")
    ],
    ("성격의 장단점", "장점 기술"): [
        ("직무 연계 + 구체 사례로 강점 증명", "A"),
        ("장점 명확 + 사례 적당", "B"),
        ("장점 기술은 있으나 일반적", "C"),
        ("장점 애매하거나 연관 없음", "D"),
        ("장점 없음 또는 부정적 표현", "E")
    ],
    ("성격의 장단점", "단점 기술 및 극복 노력"): [
        ("솔직 + 뚜렷한 개선 과정", "A"),
        ("극복 의지 있음 + 일부 노력", "B"),
        ("단점 나열 중심, 노력 미흡", "C"),
        ("단점만 있고 개선 없음", "D"),
        ("단점 숨기거나 책임 전가", "E")
    ],
    ("성격의 장단점", "대인관계 성향"): [
        ("대인관계 우수 사례 + 긍정적 결과", "A"),
        ("적절한 사례 + 대체로 원만", "B"),
        ("사례 부족, 원론적 설명 대인관계 소극적 묘사 부정적 내용 포함", "C"),
        ("대인관계 소극적 묘사", "D"),
        ("부정적 내용 포함", "E")
    ],
    ("학창시절", "학업 태도"): [
        ("전공과 연계된 주도적 학습 경험", "A"),
        ("성실하고 자기주도 학습 있음", "B"),
        ("일반적인 학습 서술", "C"),
        ("노력 부족, 피동적 학습", "D"),
        ("학업 태도 언급 없음", "E")
    ],
    ("학창시절", "활동 참여"): [
        ("활동 적극적 참여 + 구체 성과", "A"),
        ("활동 참여 + 간단한 결과", "B"),
        ("활동 경험 있음 + 서술 미흡", "C"),
        ("활동 언급만 있고 내용 부족 활동 없음", "D"),
        ("활동 없음", "E")
    ],
    ("학창시절", "성취 및 도전 경험"): [
        ("뚜렷한 도전 + 성과/교훈 존재", "A"),
        ("도전 있음 + 성과 미흡", "B"),
        ("경험 기술은 있으나 성과 미흡", "C"),
        ("노력 부족, 결과 없음", "D"),
        ("도전 경험 없음", "E")
    ],
    ("지원동기", "회사/직무 이해도"): [
        ("회사 특성과 직무 정확히 이해 + 본인 연결", "A"),
        ("직무 이해 있음 + 부분 연결", "B"),
        ("직무 또는 회사 이해 부족", "C"),
        ("피상적 이해 + 단순 지원", "D"),
        ("이해도 없음, 복붙 의심", "E")
    ],
    ("지원동기", "지원 이유의 명확성"): [
        ("본인 경험/가치와 연결된 명확한 동기", "A"),
        ("개인 목표 중심의 설명", "B"),
        ("단순 관심 표현", "C"),
        ("억지스러운 설명", "D"),
        ("동기 없음 또는 불성실", "E")
    ],
    ("지원동기", "직무 적합성 강조"): [
        ("최근 3년 이내 취득 및 갱신 완료", "A"),
        ("3~5년 이내 취득", "B"),
        ("5년 이상 경과, 갱신 예정", "C"),
        ("오래되었고 활용 미미", "D"),
        ("무효/만료", "E")
    ],
    ("입사 후 포부", "장기 비전"): [
        ("회사 발전과 연계된 비전 + 실현 가능성", "A"),
        ("현실적 비전 제시", "B"),
        ("개인적 희망 수준", "C"),
        ("막연하거나 비현실적", "D"),
        ("비전 없음", "E")
    ],
    ("입사 후 포부", "단기 목표"): [
        ("구체적 + 회사 내 역할 연결", "A"),
        ("구체적이나 직무 연계 약함", "B"),
        ("목표 있으나 막연함", "C"),
        ("형식적 목표 제시", "D"),
        ("목표 없음", "E")
    ],
    ("입사 후 포부", "기여 방안"): [
        ("회사에 대한 이해 + 구체 기여방안", "A"),
        ("기여방안 있으나 설명 부족", "B"),
        ("의지는 있으나 구체성 부족", "C"),
        ("기여 언급만 존재", "D"),
        ("기여 의식 없음", "E")
    ],
    ("직무 경험", "실무 경험"): [
        ("실무 경험 + 성과 및 배움 있음", "A"),
        ("실무 경험 있음 + 적절 설명", "B"),
        ("경험 나열 중심", "C"),
        ("실무 연결 부족", "D"),
        ("경험 없음", "E")
    ],
    ("직무 경험", "직무 관련 능력"): [
        ("직무 필수 역량 다수 보유 + 활용 경험", "A"),
        ("관련 역량 보유 + 일부 활용", "B"),
        ("역량 언급 있으나 약함", "C"),
        ("자격 보유만 있고 활용 미흡", "D"),
        ("관련 역량 없음", "E")
    ],
    ("직무 경험", "문제 해결력"): [
        ("문제 해결 과정 명확 + 결과 도출", "A"),
        ("문제 인식 및 일부 해결 경험", "B"),
        ("해결 노력은 있으나 미흡", "C"),
        ("문제만 제시, 해결 없음", "D"),
        ("문제 인식 또는 해결 없음", "E")
    ]
}

# ---------------------------
# 2️⃣ Matching Function
# ---------------------------
def map_grade(value, mapping_list):
    value = str(value).strip()
    for keyword, grade in mapping_list:
        if keyword == value:
            return grade
    return "E"

# ---------------------------
# 3️⃣ Build Normalized Output
# ---------------------------
records = []

for idx, row in trainee_df.iterrows():
    trainee = row['trainee']
    id_ = row['id']

    # 성장과정
    records.append([
        trainee, id_, "성장과정", "가치관",
        map_grade(row['가치관'], criteria_mapping[("성장과정", "가치관")])
    ])
    records.append([
        trainee, id_, "성장과정", "가족/환경의 영향",
        map_grade(row['가족/환경의 영향'], criteria_mapping[("성장과정", "가족/환경의 영향")])
    ])
    records.append([
        trainee, id_, "성장과정", "전환점/특별한 경험",
        map_grade(row['전환점/특별한 경험'], criteria_mapping[("성장과정", "전환점/특별한 경험")])
    ])

    # 성격의 장단점
    records.append([
        trainee, id_, "성격의 장단점", "장점 기술",
        map_grade(row['장점 기술'], criteria_mapping[("성격의 장단점", "장점 기술")])
    ])
    records.append([
        trainee, id_, "성격의 장단점", "단점 기술 및 극복 노력",
        map_grade(row['단점 기술 및 극복 노력'], criteria_mapping[("성격의 장단점", "단점 기술 및 극복 노력")])
    ])
    records.append([
        trainee, id_, "성격의 장단점", "대인관계 성향",
        map_grade(row['대인관계 성향'], criteria_mapping[("성격의 장단점", "대인관계 성향")])
    ])

    # 학창시절
    records.append([
        trainee, id_, "학창시절", "학업 태도",
        map_grade(row['학업 태도'], criteria_mapping[("학창시절", "학업 태도")])
    ])
    records.append([
        trainee, id_, "학창시절", "활동 참여",
        map_grade(row['활동 참여'], criteria_mapping[("학창시절", "활동 참여")])
    ])
    records.append([
        trainee, id_, "학창시절", "성취 및 도전 경험",
        map_grade(row['성취 및 도전 경험'], criteria_mapping[("학창시절", "성취 및 도전 경험")])
    ])

    # 지원동기
    records.append([
        trainee, id_, "지원동기", "회사/직무 이해도",
        map_grade(row['회사/직무 이해도'], criteria_mapping[("지원동기", "회사/직무 이해도")])
    ])
    records.append([
        trainee, id_, "지원동기", "지원 이유의 명확성",
        map_grade(row['지원 이유의 명확성'], criteria_mapping[("지원동기", "지원 이유의 명확성")])
    ])
    records.append([
        trainee, id_, "지원동기", "직무 적합성 강조",
        map_grade(row['직무 적합성 강조'], criteria_mapping[("지원동기", "직무 적합성 강조")])
    ])

    # 입사 후 포부
    records.append([
        trainee, id_, "입사 후 포부", "단기 목표",
        map_grade(row['단기 목표'], criteria_mapping[("입사 후 포부", "단기 목표")])
    ])
    records.append([
        trainee, id_, "입사 후 포부", "장기 비전",
        map_grade(row['장기 비전'], criteria_mapping[("입사 후 포부", "장기 비전")])
    ])
    records.append([
        trainee, id_, "입사 후 포부", "기여 방안",
        map_grade(row['기여 방안'], criteria_mapping[("입사 후 포부", "기여 방안")])
    ])

    # 직무 경험
    records.append([
        trainee, id_, "직무 경험", "실무 경험",
        map_grade(row['실무 경험'], criteria_mapping[("직무 경험", "실무 경험")])
    ])
    records.append([
        trainee, id_, "직무 경험", "직무 관련 능력",
        map_grade(row['직무 관련 능력'], criteria_mapping[("직무 경험", "직무 관련 능력")])
    ])
    records.append([
        trainee, id_, "직무 경험", "문제 해결력",
        map_grade(row['문제 해결력'], criteria_mapping[("직무 경험", "문제 해결력")])
    ])
# ---------------------------
# 4️⃣ Save to CSV
# ---------------------------
graded_df = pd.DataFrame(records, columns=["trainee", "id", "cat", "subcat", "grade"])
graded_df.to_csv("graded_output_resume.csv", index=False, encoding="utf-8-sig")

print("✅ Grading complete! Output saved as 'graded_output_resume.csv'.")

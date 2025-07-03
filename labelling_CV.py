import pandas as pd

# Load trainee data
trainee_df = pd.read_csv("data.csv")
trainee_df.columns = trainee_df.columns.str.strip()  # Clean header spaces

# ---------------------------
# 1️⃣ Exact Criteria Mapping
# ---------------------------
criteria_mapping = {
    ("학력", "최종 학위 수준"): [
        ("박사 이상", "A"), ("석사", "B"), ("학사", "C"), ("전문대졸", "D"), ("고졸 이하", "E")
    ],
    ("학력", "출신 학교 수준"): [
        ("국내외 최상위권 대학", "A"),
        ("상위권 대학", "B"),
        ("중상위권 대학", "C"),
        ("하위권 대학", "D"),
        ("무인증 교육기관", "E")
    ],
    ("학점", "출신 학교 수준"): [
        ("4.0 이상 / A 이상", "A"),
        ("3.5~3.99 / B+", "B"),
        ("3.0~3.49 / B", "C"),
        ("2.5~2.99 / C", "D"),
        ("2.49 이하", "E")
    ],
    ("경력", "총 경력 연수"): [
        ("10년 이상", "A"),
        ("6-9년", "B"),
        ("3-5년", "C"),
        ("1-2년", "D"),
        ("1년 미만", "E")
    ],
    ("경력", "직무 연관성"): [
        ("완전 일치", "A"),
        ("유사 직무 다수 경험", "B"),
        ("일부 유사", "C"),
        ("직무 전환 경험 있음", "D"),
        ("무관한 분야", "E")
    ],
    ("경력", "성과 및 기여도"): [
        ("수치화된 성과 및 수상 다수", "A"),
        ("팀 프로젝트 리드, 우수 성과 1건 이상", "B"),
        ("성실 근무, 무평가", "C"),
        ("성과 기재 부족", "D"),
        ("관련 정보 없음", "E")
    ],
    ("교육이력", "전문교육 수료 여부"): [
        ("최신 트렌드 반영된 전문 교육 다수", "A"),
        ("최근 3년 내 2개 이상 수료", "B"),
        ("최근 3년 내 1개 수료", "C"),
        ("오래된 교육만 있음", "D"),
        ("없음", "E")
    ],
    ("교육이력", "기업 내 교육 참여"): [
        ("핵심 교육 참여 및 발표 경험", "A"),
        ("정기 교육 다수 이수", "B"),
        ("기본 교육 이수", "C"),
        ("단기 교육만 있음", "D"),
        ("없음", "E")
    ],
    ("교육이력", "자기개발 노력"): [
        ("지속적 학습, 자격 취득 노력 있음", "A"),
        ("관련 분야 학습 기록 있음", "B"),
        ("학습 시도 1회 이상", "C"),
        ("계획은 있으나 이행 부족", "D"),
        ("관련 없음", "E")
    ],
    ("자격증", "직무 관련 자격증 (적합도)"): [
        ("매우 높음", "A"),
        ("높음", "B"),
        ("보통", "C"),
        ("낮음", "D"),
        ("매우 낮음", "E")
    ],
    ("자격증", "자격증 수준"): [
        ("난이도 상, 실무 강력 지원", "A"),
        ("난이도 중, 실무 일부 지원", "B"),
        ("기초 수준 자격", "C"),
        ("실무 관련성 낮음", "D"),
        ("무의미/불명확 자격", "E")
    ],
    ("자격증", "자격증 최신성"): [
        ("최근 3년 이내 취득 및 갱신 완료", "A"),
        ("3~5년 이내 취득", "B"),
        ("5년 이상 경과, 갱신 예정", "C"),
        ("오래되었고 활용 미미", "D"),
        ("무효/만료", "E")
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

    # 학력
    records.append([
        trainee, id_, "학력", "최종 학위 수준",
        map_grade(row['최종 학위 수준'], criteria_mapping[("학력", "최종 학위 수준")])
    ])
    records.append([
        trainee, id_, "학력", "출신 학교 수준",
        map_grade(row['출신 학교 수준'], criteria_mapping[("학력", "출신 학교 수준")])
    ])
    records.append([
        trainee, id_, "학점", "출신 학교 수준",
        map_grade(row['학점'], criteria_mapping[("학점", "출신 학교 수준")])
    ])

    # 경력
    records.append([
        trainee, id_, "경력", "총 경력 연수",
        map_grade(row['총 경력 연수'], criteria_mapping[("경력", "총 경력 연수")])
    ])
    records.append([
        trainee, id_, "경력", "직무 연관성",
        map_grade(row['직무 연관성'], criteria_mapping[("경력", "직무 연관성")])
    ])
    records.append([
        trainee, id_, "경력", "성과 및 기여도",
        map_grade(row['성과 및 기여도'], criteria_mapping[("경력", "성과 및 기여도")])
    ])

    # 교육이력
    records.append([
        trainee, id_, "교육이력", "전문교육 수료 여부",
        map_grade(row['전문교육 수료 여부'], criteria_mapping[("교육이력", "전문교육 수료 여부")])
    ])
    records.append([
        trainee, id_, "교육이력", "기업 내 교육 참여",
        map_grade(row['기업 내 교육 참여'], criteria_mapping[("교육이력", "기업 내 교육 참여")])
    ])
    records.append([
        trainee, id_, "교육이력", "자기개발 노력",
        map_grade(row['자기개발 노력'], criteria_mapping[("교육이력", "자기개발 노력")])
    ])

    # 자격증
    records.append([
        trainee, id_, "자격증", "직무 관련 자격증 (적합도)",
        map_grade(row['직무 관련 자격증 (적합도)'], criteria_mapping[("자격증", "직무 관련 자격증 (적합도)")])
    ])
    records.append([
        trainee, id_, "자격증", "자격증 수준",
        map_grade(row['자격증 수준'], criteria_mapping[("자격증", "자격증 수준")])
    ])
    records.append([
        trainee, id_, "자격증", "자격증 최신성",
        map_grade(row['자격증 최신성'], criteria_mapping[("자격증", "자격증 최신성")])
    ])

# ---------------------------
# 4️⃣ Save to CSV
# ---------------------------
graded_df = pd.DataFrame(records, columns=["trainee", "id", "cat", "subcat", "grade"])
graded_df.to_csv("graded_output.csv", index=False, encoding="utf-8-sig")

print("✅ Grading complete! Output saved as 'graded_output.csv'.")

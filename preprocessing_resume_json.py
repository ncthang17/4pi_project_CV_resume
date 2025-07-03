import pandas as pd
import json

# -----------------------
# Step 1: Load CSV
# -----------------------
df = pd.read_csv("data_resume.csv")
df.columns = df.columns.str.strip()  # clean column names

# -----------------------
# Step 2: Combine columns
# -----------------------
df['성장과정'] = df.get('가치관', '') + ' , ' + df.get('가족/환경의 영향', '') + ' , ' + df.get('전환점/특별한 경험', '')
df['성격의 장단점'] = df.get('장점 기술', '') + ' , ' + df.get('단점 기술 및 극복 노력', '') + ' , ' + df.get('대인관계 성향', '')
df['학창시절'] = df.get('학업 태도', '') + ' , ' + df.get('활동 참여', '') + ' , ' + df.get('성취 및 도전 경험', '')
df['지원동기'] = df.get('회사/직무 이해도', '') + ' , ' + df.get('지원 이유의 명확성', '') + ' , ' + df.get('직무 적합성 강조', '')
df['입사 후 포부'] = df.get('단기 목표', '') + ' , ' + df.get('장기 비전', '') + ' , ' + df.get('기여 방안', '')
df['직무 경험'] = df.get('실무 경험', '') + ' , ' + df.get('직무 관련 능력', '') + ' , ' + df.get('문제 해결력', '')

# -----------------------
# Step 3: Save to preprocessing_resume.csv
# -----------------------
extracted_df = df[['trainee', 'id', '성장과정', '성격의 장단점', '학창시절', '지원동기', '입사 후 포부', '직무 경험']].copy()
# Sort by trainee and id (both ascending)
extracted_df.sort_values(by=['trainee', 'id'], ascending=[True, True], inplace=True)

extracted_df.to_csv("preprocessing_resume.csv", index=False, encoding='utf-8-sig')

# -----------------------
# Step 4: Generate JSON
# -----------------------

# Add '기타' column
extracted_df['기타'] = ''

# Convert to JSON
json_list = extracted_df.to_dict(orient='records')

# Save to preprocessing_resume.json
with open("preprocessing_resume.json", "w", encoding='utf-8') as f:
    json.dump(json_list, f, ensure_ascii=False, indent=2)

# -----------------------
# Confirmation
# -----------------------
print("✅ preprocessing_resume.csv and preprocessing_resume.json have been created successfully.")
print(json.dumps(json_list[0], ensure_ascii=False, indent=2))  # preview first JSON

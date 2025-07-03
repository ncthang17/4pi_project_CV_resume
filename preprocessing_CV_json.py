import pandas as pd
import json

# -----------------------------
# Step 1: Load CSV
# -----------------------------
file_path = "data.csv"  # Ensure this CSV is in your working directory
df = pd.read_csv(file_path)

# Clean column names to remove potential invisible characters or spaces
df.columns = df.columns.str.strip()

# Debug: print column names to avoid KeyError if names changed
print("✅ Columns found:", df.columns.tolist())

# -----------------------------
# Step 2: Combine columns safely with fallback
# -----------------------------
df['학력'] = df.get('최종 학위 수준', '') + ' , ' + df.get('출신 학교 수준', '') + ' , ' + df.get('학점', '')
df['경력'] = df.get('총 경력 연수', '') + ' , ' + df.get('직무 연관성', '') + ' , ' + df.get('성과 및 기여도', '')
df['교육이력'] = df.get('전문교육 수료 여부', '') + ' , ' + df.get('기업 내 교육 참여', '') + ' , ' + df.get('자기개발 노력', '')
df['자격증'] = df.get('직무 관련 자격증 (적합도)', '') + ' , ' + df.get('자격증 수준', '') + ' , ' + df.get('자격증 최신성', '')

# -----------------------------
# Step 3: Extract relevant columns
# -----------------------------
extracted_df = df[['trainee', 'id', '학력', '경력', '교육이력', '자격증']].copy()

# Sort by trainee and id (both ascending)
extracted_df.sort_values(by=['trainee', 'id'], ascending=[True, True], inplace=True)

# -----------------------------
# Step 4: Save to CSV
# -----------------------------
output_csv = "preprocessing_CV.csv"
extracted_df.to_csv(output_csv, index=False, encoding='utf-8-sig')
print(f"✅ Saved cleaned CSV as {output_csv}")

# -----------------------------
# Step 5: Save to JSON
# -----------------------------
# Add '기타' column for consistent structure
extracted_df['기타'] = ''

# Convert to JSON
json_list = extracted_df.to_dict(orient='records')

# Save to file
output_json = "preprocessing_CV.json"
with open(output_json, "w", encoding='utf-8') as f:
    json.dump(json_list, f, ensure_ascii=False, indent=2)

print(f"✅ Saved structured JSON as {output_json}")

# -----------------------------
# Step 6: Preview first JSON record
# -----------------------------
if json_list:
    print("✅ Sample JSON record:\n", json.dumps(json_list[0], ensure_ascii=False, indent=2))
else:
    print("⚠️ No records found in the data.")

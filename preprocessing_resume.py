import pandas as pd

# Load CSV file
df = pd.read_csv("data_resume.csv")

# Clean column names to remove potential invisible characters or spaces
df.columns = df.columns.str.strip()

# Print columns to debug if KeyError occurs
print(df.columns.tolist())

# Combine columns safely with fallback if column names have changed
df['성장과정'] = df.get('가치관', '') + ' , ' + df.get('가족/환경의 영향', '') + ' , ' + df.get('전환점/특별한 경험', '')
df['성격의 장단점'] = df.get('장점 기술', '') + ' , ' + df.get('단점 기술 및 극복 노력', '') + ' , ' + df.get('대인관계 성향', '')
df['학창시절'] = df.get('학업 태도', '') + ' , ' + df.get('활동 참여', '') + ' , ' + df.get('성취 및 도전 경험', '')
df['지원동기'] = df.get('회사/직무 이해도', '') + ' , ' + df.get('지원 이유의 명확성', '') + ' , ' + df.get('직무 적합성 강조', '')
df['입사 후 포부'] = df.get('단기 목표', '') + ' , ' + df.get('장기 비전', '') + ' , ' + df.get('기여 방안', '')
df['직무 경험'] = df.get('실무 경험', '') + ' , ' + df.get('직무 관련 능력', '') + ' , ' + df.get('문제 해결력', '')

# Select final columns
extracted_df = df[['trainee', 'id', '성장과정', '성격의 장단점', '학창시절', '지원동기', '입사 후 포부', '직무 경험']]

# Save to CSV
extracted_df.to_csv("[preprocessing_resume].csv", index=False, encoding='utf-8-sig')

# Preview extracted dataframe
print(extracted_df.head())
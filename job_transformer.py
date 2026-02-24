import pandas as pd
import re

def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def extract_skills(text, target_skills):
    found_skills = []
    words = text.split()
    for skill in target_skills:
        if skill.lower() in words or skill.lower() in text:
            found_skills.append(skill)
    return ", ".join(found_skills) if found_skills else "None"

def transform_data():
    print("Starting data transformation...")
    try:
        df = pd.read_csv("raw_jobs_data.csv")
    except FileNotFoundError:
        print("Error: 'raw_jobs_data.csv' not found.")
        return None
    
    skills_to_hunt = [
        "Python", "SQL", "Java", "NLP", 
        "Analytics", "Deep Learning", "Spark", "AWS"
    ]
    
    df['Cleaned_Text'] = df['Job Title'].apply(clean_text)
    df['Extracted_Skills'] = df['Cleaned_Text'].apply(lambda x: extract_skills(x, skills_to_hunt))
    df = df.drop(columns=['Cleaned_Text'])
    
    return df

if __name__ == "__main__":
    transformed_df = transform_data()
    if transformed_df is not None:
        transformed_df.to_csv("clean_jobs_data.csv", index=False)
        print("Transformation Complete! Saved to clean_jobs_data.csv")

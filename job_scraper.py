import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_jobs():
    print("Starting extraction process...")
    URL = "https://realpython.github.io/fake-jobs/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")
    
    scraped_data = []

    for card in job_cards:
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        
        # Filter for relevant roles
        if "data" in title.lower() or "engineer" in title.lower() or "python" in title.lower():
            scraped_data.append({
                "Job Title": title,
                "Company": company,
                "Location": location
            })

    df = pd.DataFrame(scraped_data)
    return df

if __name__ == "__main__":
    raw_jobs_df = extract_jobs()
    if not raw_jobs_df.empty:
        raw_jobs_df.to_csv("raw_jobs_data.csv", index=False)
        print(f"Successfully extracted {len(raw_jobs_df)} jobs. Saved to raw_jobs_data.csv")
    else:
        print("No relevant jobs found.")

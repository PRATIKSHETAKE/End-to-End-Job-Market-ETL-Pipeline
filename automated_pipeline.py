import time
from job_scraper_poc import extract_jobs
from job_transformer_poc import transform_data
from job_loader_poc import load_data_to_db

def run_pipeline():
    print("🚀 Starting Data Engineering Pipeline...\n")
    start_time = time.time()
    
    # Phase 1: Extract
    print("--- PHASE 1: EXTRACT ---")
    raw_df = extract_jobs()
    if not raw_df.empty:
        raw_df.to_csv("raw_jobs_data.csv", index=False)
        print("✅ Extraction Complete.\n")
    else:
        print("❌ Extraction failed. Stopping pipeline.")
        return

    # Phase 2: Transform
    print("--- PHASE 2: TRANSFORM ---")
    clean_df = transform_data()
    if clean_df is not None:
        clean_df.to_csv("clean_jobs_data.csv", index=False)
        print("✅ Transformation Complete.\n")
    else:
        print("❌ Transformation failed. Stopping pipeline.")
        return

    # Phase 3: Load
    print("--- PHASE 3: LOAD ---")
    load_data_to_db()
    print("✅ Load Complete.\n")

    end_time = time.time()
    print(f"🎉 Pipeline finished successfully in {round(end_time - start_time, 2)} seconds!")

if __name__ == "__main__":
    run_pipeline()

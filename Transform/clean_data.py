import pandas as pd
import numpy as np
import ast
import os

def clean_and_combine_data(adzun_file='../Extract/jobs_listing_adzun.csv', 
                         glassdoor_file='../Extract/jobs_listing.csv',  # Updated filename
                         output_file='cleaned_jobs.csv'):
    """
    Combines and cleans job listing data from Adzuna and Glassdoor CSV files.
    Handles different file encodings.
    """
    
    print(f"Reading files from:")
    print(f"Adzuna: {os.path.abspath(adzun_file)}")
    print(f"Glassdoor: {os.path.abspath(glassdoor_file)}")
    
    try:
        # Try different encodings for reading the files
        encodings = ['utf-8', 'latin1', 'cp1252']
        
        # Read Adzuna file
        df_adzun = None
        for encoding in encodings:
            try:
                df_adzun = pd.read_csv(adzun_file, encoding=encoding)
                print(f"Successfully read Adzuna file with {encoding} encoding")
                break
            except UnicodeDecodeError:
                continue
                
        # Read Glassdoor file
        df_glassdoor = None
        for encoding in encodings:
            try:
                df_glassdoor = pd.read_csv(glassdoor_file, encoding=encoding)
                print(f"Successfully read Glassdoor file with {encoding} encoding")
                break
            except UnicodeDecodeError:
                continue
        
        if df_adzun is None or df_glassdoor is None:
            raise Exception("Could not read one or both files with any of the attempted encodings")
        
        print(f"\nInitial data counts:")
        print(f"Adzuna records: {len(df_adzun)}")
        print(f"Glassdoor records: {len(df_glassdoor)}")
        
        # Combine the dataframes
        df_combined = pd.concat([df_adzun, df_glassdoor], ignore_index=True)
        
        # Clean the data
        
        # 1. Convert skill string to actual list and clean
        def clean_skills(skill_str):
            try:
                if pd.isna(skill_str):
                    return []
                # Convert string representation of list to actual list
                skills = ast.literal_eval(skill_str)
                # Remove empty strings and strip whitespace
                return [s.strip() for s in skills if s.strip()]
            except:
                return []
        
        df_combined['skill'] = df_combined['skill'].apply(clean_skills)
        
        # 2. Clean location data
        df_combined['location'] = df_combined['location'].fillna('Unknown')
        df_combined['location'] = df_combined['location'].str.strip()
        
        # 3. Standardize job type
        df_combined['type'] = df_combined['type'].fillna('Not specified')
        df_combined['type'] = df_combined['type'].str.lower().str.strip()
        
        # 4. Clean seniority level
        df_combined['seniority_level'] = df_combined['seniority_level'].fillna(0)
        df_combined['seniority_level'] = pd.to_numeric(df_combined['seniority_level'], errors='coerce').fillna(0)
        
        # 5. Clean salary data
        df_combined['est_salary'] = pd.to_numeric(df_combined['est_salary'], errors='coerce')
        
        # Calculate median salary for filling missing values
        median_salary = df_combined['est_salary'].median()
        df_combined['est_salary'] = df_combined['est_salary'].fillna(median_salary)
        
        # 6. Clean remote status
        df_combined['remote'] = df_combined['remote'].fillna(False)
        
        # 7. Clean title
        df_combined['title'] = df_combined['title'].fillna('Unknown')
        df_combined['title'] = df_combined['title'].str.strip()
        
        # 8. Clean description
        df_combined['description'] = df_combined['description'].fillna('No description available')
        df_combined['description'] = df_combined['description'].str.strip()
        
        # 9. Remove duplicates
        df_combined = df_combined.drop_duplicates(subset=['title', 'location', 'description'], keep='first')
        
        # Save the cleaned and combined data
        output_path = os.path.join(os.path.dirname(__file__), output_file)
        df_combined.to_csv(output_path, index=False, encoding='utf-8')
        
        print(f"\nCleaning complete!")
        print(f"Output saved to: {os.path.abspath(output_path)}")
        print(f"\nSummary statistics:")
        print(f"Total number of job listings: {len(df_combined)}")
        print(f"Number of unique job titles: {df_combined['title'].nunique()}")
        print(f"Average salary: £{df_combined['est_salary'].mean():.2f}")
        print(f"Number of remote positions: {df_combined['remote'].sum()}")
        
        return df_combined
        
    except Exception as e:
        print(f"Error processing files: {str(e)}")
        return None
from firestore_load import load_csv_to_firestore

if __name__ == "__main__":
    adzun_file_path = '../Extract/jobs_listing_adzun.csv'
    glassdoor_file_path = '../Extract/jobs_listing.csv'
    cleaned_file_path = '../Transform/cleaned_jobs.csv'

    primary_key_fields = ['title', 'location', 'date']

    load_csv_to_firestore(adzun_file_path, 'adzun_jobs', primary_key_fields)
    load_csv_to_firestore(glassdoor_file_path, 'glassdoor_jobs', primary_key_fields)
    load_csv_to_firestore(cleaned_file_path, 'cleaned_jobs', primary_key_fields)
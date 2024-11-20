import requests
from utils import checkTitleLevel, contains_remote, check_job_type, CheckForSkillString, save_jobs_to_csv
from job_posting_glassdoor import Job_Posting_Glassdoor


def main():
    job_object_list = []
    region_codes = ['gb', 'sg', 'us'] # Region codes from UK, Singapore, & US
    for region in region_codes:
        for i in range(1, 3):
            url = f'https://api.adzuna.com/v1/api/jobs/{region}/search/{i}?app_id=8750b7e1&app_key=346fd9f9deae1db97c8e4169999f9056&results_per_page=20&what=developer'
            response = requests.get(url)

            if response.status_code == 200:

                json_data = response.json()

                json_jobs = json_data["results"]
                for job in json_jobs:
                    title = job["title"]
                    location = job["location"]["display_name"]
                    job_desc = job["description"]
                    if region == 'gb' or region ==  'us':
                        job_est_salary = job["salary_min"]
                    else:
                        job_est_salary = job["salary_is_predicted"]
                    job_remote = contains_remote(job_desc)
                    job_level = checkTitleLevel(title)
                    job_type = check_job_type(job_desc)
                    job_skill_list = CheckForSkillString(job_desc)

                    print(f"Title: {title}")
                    print(f"Location: {location}")
                    print(f"Description: {job_desc}")
                    print(f"Remote: {job_remote}")
                    print(f"Level: {job_level}")
                    print(f"Job Type: {job_type}")
                    print(f"Skills: {job_skill_list} \n")

                    job_object = Job_Posting_Glassdoor(
                        title=title,
                        location=location,
                        skills=job_skill_list,
                        type=job_type,
                        seniority_level=job_level,
                        remote=job_remote,
                        est_salary=job_est_salary,
                        description=job_desc
                    )

                    job_object_list.append(job_object)

            else:
                print(f"Failed to fetch error code: {response.status_code}")

    save_jobs_to_csv(job_object_list, filename = 'jobs_listing_adzun.csv')



if __name__ == "__main__":
    main()
import requests
from utils import checkTitleLevel, contains_remote, check_job_type, CheckForSkillString
from job_posting_glassdoor import Job_Posting_Glassdoor
import csv


def main():
    job_object_list = []
    for i in range(1, 3):
        url = f'https://api.adzuna.com/v1/api/jobs/gb/search/{i}?app_id=8750b7e1&app_key=346fd9f9deae1db97c8e4169999f9056&results_per_page=20&what=developer'

        response = requests.get(url)

        if response.status_code == 200:

            json_data = response.json()

            json_jobs = json_data["results"]
            for job in json_jobs:
                title = job["title"]
                location = job["location"]["display_name"]
                job_desc = job["description"]
                job_est_salary = job["salary_min"]

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

    for i in range(1, 3):
        url = f'https://api.adzuna.com/v1/api/jobs/sg/search/{i}?app_id=8750b7e1&app_key=346fd9f9deae1db97c8e4169999f9056&results_per_page=20&what=developer'

        response = requests.get(url)

        if response.status_code == 200:

            json_data = response.json()

            json_jobs = json_data["results"]
            for job in json_jobs:
                title = job["title"]
                location = job["location"]["display_name"]
                job_desc = job["description"]
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

    for i in range(1, 3):
        url = f'https://api.adzuna.com/v1/api/jobs/us/search/{i}?app_id=8750b7e1&app_key=346fd9f9deae1db97c8e4169999f9056&results_per_page=20&what=developer'

        response = requests.get(url)

        if response.status_code == 200:

            json_data = response.json()

            json_jobs = json_data["results"]
            for job in json_jobs:
                title = job["title"]
                location = job["location"]["display_name"]
                job_desc = job["description"]
                job_est_salary = job["salary_min"]

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

    save_jobs_to_csv(job_object_list)


def save_jobs_to_csv(job_listing, filename='jobs_listing_adzun.csv'):
    """Save the job listings to a CSV file."""
    if not job_listing:
        print("No job listings to save.")
        return

    jobs_dict = [job.__dict__ for job in job_listing]
    fieldnames = jobs_dict[0].keys()

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header (column names)
        writer.writerows(jobs_dict)  # Write each job as a row in the CSV file

    print(f"Data saved to {filename}")


if __name__ == "__main__":
    main()
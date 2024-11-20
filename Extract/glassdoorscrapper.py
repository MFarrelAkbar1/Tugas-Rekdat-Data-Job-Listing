import os
from dotenv import load_dotenv
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from job_posting_glassdoor import Job_Posting_Glassdoor
from utils import checkTitleLevel, contains_remote, check_job_type, CheckForSkill, save_jobs_to_csv

# Load environment variables
load_dotenv()

# Constants
GLASSDOOR_URL = 'https://www.glassdoor.com/Job/indonesia-developer-jobs-SRCH_IL.0,9_IN113_KO10,19.htm'
JOB_LEVEL_MAPPING = {
    1: "Junior",
    2: "Mid",
    3: "Senior",
    4: "Executive"
}


# Initialize WebDriver
def initialize_driver():
    """Initialize and return the WebDriver."""
    driver = webdriver.Chrome()
    driver.get(GLASSDOOR_URL)
    return driver


# Fetch job elements
def fetch_job_elements(driver):
    """Fetch job elements from the job list."""
    try:
        job_list = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[aria-label="Jobs List"]'))
        )
        return job_list.find_elements(By.CSS_SELECTOR, '[data-test="jobListing"]')
    except Exception as e:
        print(f"Error fetching job elements: {e}")
        return []


# Parse job details
def parse_job_details(driver, job, index):
    """Parse details for a single job."""
    try:
        if index == 2:
            try:
                close_button = driver.find_element(By.CLASS_NAME, 'CloseButton')
                close_button.click()
            except:
                pass

        job.click()
        job_description = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'JobDetails_jobDetailsSectionContainer__o_x6Z'))
        )

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Extract details
        try:
            job_company_name = soup.find('h4', class_='heading_Heading__BqX5J heading_Subhead__Ip1aW').get_text(strip=True)
        except Exception as e:
            print("Job Company")
        try:
            title = soup.find('h1', class_='heading_Heading__BqX5J heading_Level1__soLZs').get_text(strip=True)
        except Exception as e:
            print("Job Title")
        try:
            job_location = soup.find('div', class_='JobDetails_location__mSg5h').get_text(strip=True)
        except Exception as e:
            print("Job Location")
        job_content = (
                soup.find('div', class_='JobDetails_jobDescription__uW_fK JobDetails_blurDescription__vN7nh') or
                soup.find('div',
                          class_='JobDetails_jobDescriptionWrapper___tqxc JobDetails_jobDetailsSectionContainer__o_x6Z')
        )


        job_desc = [element.get_text() for element in job_content.find_all(True)]
        skill_result = CheckForSkill(job_desc)

        # Optional fields
        job_est_salary = None
        try:
            salary_element = job.find_element(By.CSS_SELECTOR, '[data-test=detailSalary]')
            job_est_salary = salary_element.text if salary_element.text else None
        except:
            pass

        # Analyze job details
        job_remote = contains_remote(job_desc)
        job_level = checkTitleLevel(title)
        job_type = check_job_type(job_desc)

        # Create job object
        job_object = Job_Posting_Glassdoor(
            title=title,
            location=job_location,
            skills=skill_result,
            type=job_type,
            seniority_level=job_level,
            remote=job_remote,
            est_salary=job_est_salary,
            description=job_desc
        )
        return job_object

    except Exception as e:
        print(f"Error parsing job {index + 1}: {e}")
        return None





# Main function
def main():
    driver = initialize_driver()
    try:
        job_elements = fetch_job_elements(driver)
        print(f"Found {len(job_elements)} jobs.")

        job_listing = []
        for index, job in enumerate(job_elements):
            job_object = parse_job_details(driver, job, index)
            if job_object:
                job_listing.append(job_object)

        save_jobs_to_csv(job_listing, filename='jobs_listing_glassdoor.csv')

    finally:
        driver.quit()


if __name__ == "__main__":
    main()

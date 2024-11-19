import os
from dotenv import load_dotenv
import time
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random as rand

from utils import CheckForSkillString

load_dotenv()

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/login')

random_email_num = rand.randint(1,4)

random_email = os.getenv(f'EMAIL_ADDRESS_{random_email_num}')


# Log in
email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(random_email)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(os.getenv('PASSWORD'))
password_field.submit()

# Go to the LinkedIn job search page
driver.get(
    "https://www.linkedin.com/jobs/search/?currentJobId=&geoId=102478259&keywords=developer&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

# Wait until the list container is visible
job_list = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'scaffold-layout__list-container')))
# Get all job items in the ordered list
job_items = job_list.find_elements(By.CSS_SELECTOR, '[data-occludable-job-id]')

while len(job_items) != 25:
    time.sleep(3)
    job_items = job_list.find_elements(By.CSS_SELECTOR, '[data-occludable-job-id]')

if random_email_num == 1:
    for index, item in enumerate(job_items):
        try:
            # Click each job 3 times, since sometimes clicking once doesn't work
            item.click()
            item.click()
            item.click()

            # Wait for the job title to appear
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.t-24.t-bold.inline'))
            )

            WebDriverWait(driver, 3)
            wrapper_location_element = driver.find_element(By.CLASS_NAME, "job-details-jobs-unified-top-card__primary-description-container")

            location_element = wrapper_location_element.find_element(By.CSS_SELECTOR, ".t-black--light.mt2")
            location = location_element.find_elements(By.CSS_SELECTOR, ".tvm__text.tvm__text--low-emphasis")

            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'job-details-preferences-and-skills')))

            time.sleep(5)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find('h1', class_='t-24 t-bold inline').get_text().strip()
            company_name = soup.find('div', class_='job-details-jobs-unified-top-card__company-name').get_text().strip()



            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'job-details')))
                job_description_span =  driver.find_element(By.ID, "job-details")
                job_description = job_description_span.get_attribute("innerHTML")

            except Exception as e:
                print(f"{e}")

            print(f"{company_name}")
            print(f"Job {index + 1}: {title}")
            if job_description != None:
                print(f"{job_description}")



            skill_button = driver.find_element(By.CLASS_NAME, 'job-details-preferences-and-skills')
            skill_button.click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'job-details-skill-match-status-list')))

            skill_list_obj = []

            try:
                skill_lists = driver.find_elements(By.CLASS_NAME, 'job-details-preferences-and-skills__modal-section')
                for skill_list in skill_lists:
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'job-details-preferences-and-skills__modal-section-insights-list-item')))
                    skill_list_item = skill_list.find_elements(By.CSS_SELECTOR,'job-details-preferences-and-skills__modal-section-insights-list-item')
                    for index, skill in enumerate(skill_list_item):
                        if skill.text != "Add":
                            print(skill.text)
                            skill_list_obj.append(skill.text)

            except Exception as e:
                print(e)




            time.sleep(4)
            exit_button = driver.find_element(By.CSS_SELECTOR, '[data-test-modal-close-btn]') or driver.find_element(By.CSS_SELECTOR, '[aria-label="dismiss"]')
            exit_button.click()
            # Optionally, add a short delay to handle dynamic loading
            time.sleep(4)

        except Exception as e:
            print(f"Error on job {index + 1}: {e}")
            continue

else:
    for index, item in enumerate(job_items):

        try:
            # Click each job 3 times, since sometimes clicking once doesn't work
            item.click()
            item.click()
            item.click()

            # Wait for the job title to appear
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.t-24.t-bold.inline'))
            )

            WebDriverWait(driver, 3)
            wrapper_location_element = driver.find_element(By.CLASS_NAME,
                                                           "job-details-jobs-unified-top-card__primary-description-container")

            location_element = wrapper_location_element.find_element(By.CLASS_NAME, "t-black--light")
            location = location_element.find_elements(By.CSS_SELECTOR, ".tvm__text.tvm__text--low-emphasis")

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'job-details-preferences-and-skills')))

            time.sleep(5)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.find('h1', class_='t-24 t-bold inline').get_text().strip()
            company_name = soup.find('div', class_='job-details-jobs-unified-top-card__company-name').get_text().strip()
            li_element = soup.find('li', class_='job-details-jobs-unified-top-card__job-insight')

            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'job-details')))
                job_description_span = driver.find_element(By.ID, "job-details")
                job_description = job_description_span.get_attribute("innerHTML")

            except Exception as e:
                print(f"{e}")

            print(f"{company_name}")
            print(f"Job {index + 1}: {title}")
            if job_description is not None:
                soup2 = BeautifulSoup(job_description, 'html.parser')

                # Remove all comments
                for comment in soup2.findAll(string=lambda text: isinstance(text, Comment)):
                    comment.extract()

                # Extract text content
                job_description_text = soup2.get_text(separator=' ', strip=True)
                print(f"{job_description_text}")
            if li_element:
                spans = li_element.find_all('span', class_='tvm__text tvm__text--low-emphasis')
                for span in spans:
                    print(span.get_text())  # Print the text content of each <span>
            #
            # skill_button = driver.find_element(By.CSS_SELECTOR, '.mv5.t-16.pt1.pb1.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--2.artdeco-button--secondary.ember-view')
            # skill_button.click()
            # driver.execute_script("arguments[0].click();", skill_button)
            # WebDriverWait(driver, 10).until(
            #     EC.visibility_of_element_located((By.CLASS_NAME, 'job-details-skill-match-status-list')))

            skill_list_obj = CheckForSkillString(job_description_text)


            # try:
            #     skill_lists = driver.find_elements(By.CLASS_NAME, 'job-details-preferences-and-skills__modal-section')
            #     for skill_list in skill_lists:
            #         WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            #             (By.CLASS_NAME, 'job-details-preferences-and-skills__modal-section-insights-list-item')))
            #         skill_list_item = skill_list.find_elements(By.CLASS_NAME,
            #                                                    'job-details-preferences-and-skills__modal-section-insights-list-item')
            #         for index, skill in enumerate(skill_list_item):
            #             if skill.text != "Add":
            #                 print(skill.text)
            #                 skill_list_obj.append(skill.text)


            # except Exception as e:
            #     print(e)


            # time.sleep(4)
            # exit_button = driver.find_element(By.CSS_SELECTOR, '[data-test-modal-close-btn]') or driver.find_element(
            #     By.CSS_SELECTOR, '[aria-label="dismiss"]')
            # exit_button.click()
            # # Optionally, add a short delay to handle dynamic loading
            # time.sleep(4)

        except Exception as e:
            print(f"Error on job {index + 1}: {e}")


# Optional: close the driver after completion
driver.quit()



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3988839272&distance=25&f_AL=true&geoId=100212432"
           "&keywords=python%20developer&origin=JOB_COLLECTION_PAGE_KEYWORD_HISTORY&refresh=true&sortBy=R")

time.sleep(3)

sign_in_button = driver.find_element(By.LINK_TEXT, 'Sign in')
sign_in_button.click()

email_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

email_field.send_keys("halidmohamed807@gmail.com")
password_field.send_keys("Haha123@&$", Keys.RETURN)
time.sleep(60)

job_listings = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')

for job in job_listings:
    try:
        job.click()
        time.sleep(2)

        easy_apply = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button--top-card')
        easy_apply.click()
        time.sleep(2)

        mobile_phone_field = driver.find_element(By.CSS_SELECTOR, "[id*='phoneNumber-nationalNumber']")
        mobile_phone_field.send_keys("0927868821", Keys.RETURN)

        next_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Continue to next step']")
        next_button.click()
        time.sleep(2)

        is_next = False
        buttons = driver.find_elements(By.CSS_SELECTOR, 'button')
        for button in buttons:
            if button.text.strip().lower() == 'review':
                button.click()
                is_next = False
                break
            elif button.text.strip().lower() == 'next':
                try:
                    x_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Dismiss"]')
                    x_button.click()
                    discard = driver.find_element(By.CSS_SELECTOR, '[aria-label="Discard"]')
                    discard.click()
                except (NoSuchElementException, ElementClickInterceptedException):
                    pass
                is_next = True
                break

        if is_next:
            # If we found a "Next" button and clicked the discard button, move to the next job
            continue

        submit_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='Submit application']")
        submit_button.click()
        time.sleep(2)

    except (NoSuchElementException, ElementClickInterceptedException):
        # Skip the job if there's an issue clicking it or an element is not found
        continue

time.sleep(5)
driver.quit()

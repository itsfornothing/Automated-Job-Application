LinkedIn Job Auto-Apply Script
Overview
This script automates the job application process on LinkedIn for job listings that support the "Easy Apply" feature. It will sign in to your LinkedIn account, iterate through job listings, and attempt to apply for jobs that are simple, one-step applications. If the application process requires more steps or a note, it will skip those jobs and move to the next one.

Prerequisites
Python 3.x
Selenium WebDriver
Chrome browser
ChromeDriver (make sure the version matches your installed Chrome browser)
Installation
Install Python: Download Python
Install Selenium:
bash
Copy code
pip install selenium
Download the appropriate version of ChromeDriver: ChromeDriver

Add ChromeDriver to your system PATH or specify the executable path in the script.

Usage
Save the script to a .py file.
Replace the placeholder email and password with your LinkedIn credentials.

Script Explanation
Setup WebDriver and Open LinkedIn Jobs Page:

Initializes the Selenium WebDriver for Chrome.
Opens the LinkedIn job search page with specific search parameters.
Sign In:

Finds the "Sign in" button and clicks it.
Enters the email and password, then logs in.
Iterate Through Job Listings:

Retrieves all job listings on the page.
For each job, it attempts to:
Click on the job listing.
Click the "Easy Apply" button.
Fill in the mobile phone number field.
Click the "Next" button.
If a "Review" button is encountered, it clicks it and proceeds with the application.
If a "Next" button is encountered (indicating a multi-step application), it closes the application and moves to the next job.
Exception Handling:

Handles NoSuchElementException and ElementClickInterceptedException to skip jobs that cannot be applied to or interacted with.
Close Browser:

After iterating through all job listings, the browser is closed.

from selenium import webdriver
from selenium.webdriver.common.by import By

# user inputs:
email = "your_email_address"
password = "your_password"
profile_page = "your_profile_page_url" # the url when you click your profile badge on the top right

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
browser = webdriver.Chrome(options=chrome_options)

try:
    browser.get("https://stackoverflow.com")

    print("Got Stackoverflow homepage")
    try:
        login_link = browser.find_element(By.LINK_TEXT, "Log in")
        login_link.click()

        email_input = browser.find_element("xpath", '//*[@id="email"]')
        email_input.send_keys(email)

        password_input = browser.find_element("xpath", '//*[@id="password"]')
        password_input.send_keys(password)

        submit = browser.find_element("xpath", '//*[@id="submit-button"]')
        browser.execute_script("arguments[0].click();", submit)

        print("Submitted email and password")
    finally:
        browser.get(profile_page)
        print("Got Stackoverflow profile page")
        try:
            login_link2 = browser.find_element(By.LINK_TEXT, "Log in")
            print("Failed to login")
        except:
            print("Successfully logged in")
            browser.get(profile_page+"?tab=topactivity")
            print("Got profile activity page")

finally:
    browser.quit()

print("Completed")


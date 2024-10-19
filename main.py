from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fetch_estate_data():
    driver_path = 'C:/Workspace/chromedriver-win64/chromedriver.exe'  # ChromeDriver 절대경로
    service = Service(driver_path)

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    url = 'https://new.land.naver.com/complexes?ms=37.5308521,126.9661009,16&a=APT:PRE&b=A1&e=RETAIL&h=66&i=132&l=300&ad=true'
    driver.get(url)

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'map_wrap'))
        )
        print("Page has fully loaded.")

        map_wrap = driver.find_element(By.CLASS_NAME, 'map_wrap')
        all_links = map_wrap.find_elements(By.TAG_NAME, 'a')
        print(f"Found {len(all_links)} links on the page.")

        for index, link in enumerate(all_links):
            try:
                link_url = link.get_attribute('href')
                print(f"Link {index + 1}: {link_url}")
                time.sleep(3)

            except Exception as e:
                print(f"Error interacting with link {index + 1}: {e}")

    except Exception as e:
        print(f"Error loading the page: {e}")

    input("Enter 'q' to quit: ")
    driver.quit()

if __name__ == "__main__":
    fetch_estate_data()

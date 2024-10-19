from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 절대 경로로 ChromeDriver 경로 지정
driver_path = '/Users/gimgyeong-o/workspace/lib/chromedriver/chromedriver'
service = Service(driver_path)

# 크롬 드라이버 설정 및 브라우저 열기
driver = webdriver.Chrome(service=service)

# 네이버 부동산 매물 URL, filter 매매, 20~30평, 300세대 이상, 아파트
url = 'https://new.land.naver.com/complexes?ms=37.5308521,126.9661009,16&a=APT:PRE&b=A1&e=RETAIL&h=66&i=132&l=300'

# 네이버 부동산 페이지 열기
driver.get(url)

# 페이지가 완전히 로드될 때까지 대기 (최대 10초 대기)
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'a'))  # 'a' 태그가 로드될 때까지 대기
    )
    print("Page has fully loaded.")

    # 모든 'a' 태그 찾기
    all_links = driver.find_elements(By.TAG_NAME, 'a')
    print(f"Found {len(all_links)} links on the page.")

    # 각 링크를 하나씩 클릭하기 (링크 텍스트 출력 후 클릭)
    for index, link in enumerate(all_links):
        try:
            link_text = link.get_attribute('href')
            print(f"Clicking link {index + 1}: {link_text}")
            link.click()  # 링크 클릭

            # 페이지가 로드될 시간을 주기 위해 잠시 대기
            time.sleep(3)

            # 다시 원래 페이지로 돌아오기
            driver.back()

            # 페이지가 다시 로드될 때까지 대기
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'a'))
            )

            # 모든 'a' 태그 다시 찾기 (이전 요소들이 재사용되지 않기 때문에 다시 찾아야 함)
            all_links = driver.find_elements(By.TAG_NAME, 'a')

        except Exception as e:
            print(f"Error clicking link {index + 1}: {e}")

except Exception as e:
    print(f"Error loading the page: {e}")

# Wait for user input to close
while True:
    user_input = input("Enter q to quit: ")
    if user_input.lower() == 'q':
        break

# Close the browser
driver.quit()
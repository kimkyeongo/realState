from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # 자동 설치 라이브러리
import time

def fetch_estate_data():
    # ChromeDriver 자동 다운로드 및 설정
    service = Service(ChromeDriverManager().install())

    # 브라우저 옵션 설정
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # 브라우저 최대화
    chrome_options.add_argument("--disable-notifications")  # 알림 비활성화

    # Chrome 브라우저 열기
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 네이버 부동산 매물 페이지 열기
    url = 'https://new.land.naver.com/complexes?ms=37.5308521,126.9661009,16&a=APT:PRE&b=A1&e=RETAIL&h=66&i=132&l=300&ad=true'
    driver.get(url)

    try:
        # 페이지가 완전히 로드될 때까지 대기
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'map_wrap'))
        )
        print("Page has fully loaded.")

        # map_wrap 요소 안의 모든 'a' 태그 찾기
        map_wrap = driver.find_element(By.CLASS_NAME, 'map_wrap')
        all_links = map_wrap.find_elements(By.TAG_NAME, 'a')
        print(f"Found {len(all_links)} links on the page.")

        # 각 링크의 href 속성 출력
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

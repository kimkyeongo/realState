from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time



def fetch_marker_complex_links():
    # ChromeDriver 자동 설치 및 설정
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # 브라우저 최대화
    chrome_options.add_argument("--disable-notifications")  # 알림 비활성화

    # Chrome 브라우저 실행
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # 네이버 부동산 매물 페이지 열기
    url = 'https://new.land.naver.com/complexes?ms=37.5308521,126.9661009,16&a=APT:PRE&b=A1&e=RETAIL&h=66&i=132&l=300&ad=true'
    driver.get(url)

    try:
        # map_wrap 요소가 로드될 때까지 대기 (최대 15초)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'map_wrap'))
        )
        print("Page has fully loaded.")

        # map_wrap 클래스 안의 모든 <a> 태그 찾기
        map_wrap = driver.find_element(By.CLASS_NAME, 'map_wrap')
        all_a_tags = map_wrap.find_elements(By.TAG_NAME, 'a')

        # marker_complex 클래스가 포함된 <a> 태그에서 id 값 추출
        marker_ids = []
        for a_tag in all_a_tags:
            class_attr = a_tag.get_attribute('class')
            if class_attr and 'marker_complex' in class_attr:
                tag_id = a_tag.get_attribute('id')
                marker_ids.append(tag_id)
                print(f"Found ID: {tag_id}")

        # 순차적으로 ID를 사용해 <a> 태그 클릭
        for tag_id in marker_ids:
            try:
                # ID로 <a> 태그 찾기 및 클릭
                a_tag = driver.find_element(By.ID, tag_id)
                a_tag.click()
                print(f"Clicked on element with ID: {tag_id}")

                # 클릭 후 10초 대기
                time.sleep(10)

                # 원래 페이지로 돌아가기
                # driver.back()

                # 뒤로 가기 후 페이지가 로드될 때까지 대기
                # WebDriverWait(driver, 10).until(
                #     EC.presence_of_element_located((By.CLASS_NAME, 'map_wrap'))
                # )
                print("Returned to the main page.")

            except Exception as e:
                print(f"Error interacting with element with ID {tag_id}: {e}")

    except Exception as e:
        print(f"Error loading the page or finding elements: {e}")

    # 종료 대기
    input("Enter 'q' to quit: ")
    driver.quit()

if __name__ == "__main__":
    fetch_marker_complex_links()

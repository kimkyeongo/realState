from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 'map_area' 클래스 아래에서 'a' 태그를 찾아 하나씩 클릭하는 코드
try:
    # 'map_area' 클래스를 가진 부모 요소 찾기
    map_area_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'map_area'))
    )

    # 'map_area' 아래에 있는 모든 'a' 태그 찾기
    a_tags_in_map_area = map_area_element.find_elements(By.TAG_NAME, 'a')
    print(f"Found {len(a_tags_in_map_area)} links under 'map_area'.")

    # 각 링크를 하나씩 클릭
    for index, link in enumerate(a_tags_in_map_area):
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
                EC.presence_of_element_located((By.CLASS_NAME, 'map_area'))
            )

            # 'map_area' 아래의 'a' 태그들을 다시 검색
            map_area_element = driver.find_element(By.CLASS_NAME, 'map_area')
            a_tags_in_map_area = map_area_element.find_elements(By.TAG_NAME, 'a')

        except Exception as e:
            print(f"Error clicking link {index + 1}: {e}")

except Exception as e:
    print(f"Error locating 'map_area' or links: {e}")

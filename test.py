import requests

def fetch_complex_data(marker_id):
    # API URL 설정 (markerId를 포함하여 동적으로 생성)
    url = (
        "https://new.land.naver.com/api/complexes/single-markers/2.0?"
        "cortarNo=1117012700&zoom=13&priceType=RETAIL&"
        f"markerId={marker_id}&markerType=COMPLEX&selectedComplexNo&"
        "selectedComplexBuildingNo&fakeComplexMarker&realEstateType=APT%3APRE&"
        "tradeType=A1&tag=%3A%3A%3A%3A%3A%3A%3A%3A&rentPriceMin=0&"
        "rentPriceMax=900000000&priceMin=0&priceMax=900000000&areaMin=66&"
        "areaMax=132&oldBuildYears&recentlyBuildYears&minHouseHoldCount=300&"
        "maxHouseHoldCount&showArticle=false&sameAddressGroup=true&"
        "minMaintenanceCost&maxMaintenanceCost&directions=&leftLon=126.957863&"
        "rightLon=126.9857365&topLat=37.5279939&bottomLat=37.5215016&"
        "isPresale=true"
    )

    # 요청 헤더 설정 (필요 시 수정 가능)
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
        ),
        "Referer": "https://new.land.naver.com/complexes",
    }

    # API 호출
    response = requests.get(url, headers=headers)

    # 응답 처리
    if response.status_code == 200:
        data = response.json()
        print("Success:", data)
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # 예제 호출 (marker_id 값을 변경 가능)
    fetch_complex_data(marker_id=117804)
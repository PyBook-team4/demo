import os
import requests
from dotenv import load_dotenv

# book_pj/.env 파일 경로 설정 (현재 위치에 따라 경로 조정)
load_dotenv(dotenv_path=".env")

# 환경 변수에서 API 키 불러오기
api_key = os.getenv("API_KEY")

if not api_key:
    print("❌ API 키를 불러오지 못했습니다. .env 파일 경로와 변수명을 확인해주세요.")
else:
    print(f"🔑 API 키 로드 성공: {api_key[:4]}********")

def test_api_connection():
    # 📌 첨부하신 가이드 문서(국립중앙도서관 등)의 오픈 API 엔드포인트 URL로 변경하세요.
    #url = "https://www.nl.go.kr/NL/search/openApi/search.do"
    url="https://www.nl.go.kr/NL/search/openApi/search.do"
    #url="https://www.nl.go.kr/NL/search/openApi/search.do?key=1cfb17fdc5494dc73fee5d757b7d6399183918aa496d18c88f0cbe481dfcf32e&kwd=%ED%86%A0%EC%A7%80"
    # API 요청 시 필요한 파라미터 구성 (예시)
    params = {
        "key": api_key,         # .env에서 불러온 실제 API 키 변수 삽입
        "kwd": "파이썬",          # 테스트 검색어
        "apiType": "json",      # 다루기 쉬운 JSON 형식으로 요청
        "srchTarget": "total",
        "pageSize": 1,
        "pageNum": 1
    }
    
    try:
        print("🚀 API 호출 테스트 중...")
        # requests가 url과 params를 안전하게 조합해서 요청을 보냅니다.
        response = requests.get(url, params=params, timeout=100)
        
        print(f"📡 응답 상태 코드 (Status Code): {response.status_code}")
        
        if response.status_code == 200:
            print("✅ API 호출 성공! 데이터 응답 정상 수신")
            
            # JSON 형태로 데이터가 잘 오는지 확인
            try:
                data = response.json()
                print("📦 응답 데이터 일부 확인:", str(data)[:300])
            except Exception:
                print(response.text[:300])
                
        else:
            print(f"❌ API 호출 실패. 상태 코드: {response.status_code}")
            print(response.text)
            
    except Exception as e:
        print(f"⚠️ 요청 중 에러가 발생했습니다: {e}")

if __name__ == "__main__":
    test_api_connection()










import os
import requests
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv(dotenv_path=".env")

class BookClient:
    def __init__(self):
        # 환경 변수에서 API 키 불러오기
        self.api_key = os.getenv("API_KEY")
        
        if not self.api_key:
            raise ValueError("API 키를 불러오지 못했습니다. .env 파일 경로와 변수명(API_KEY)을 확인해주세요.")
        
        # 국립중앙도서관 통합검색 API 엔드포인트
        self.url = "https://www.nl.go.kr/NL/search/openApi/search.do"

    def search_book(self, keyword, page_size=5):
        """
        키워드로 도서를 검색하고 결과 딕셔너리를 반환합니다.
        page_size: 한 번에 가져올 검색 결과 개수 (기본값 5)
        """
        params = {
            "key": self.api_key,
            "kwd": keyword,
            "apiType": "json",      # JSON 형식 요청
            "srchTarget": "total",
            "pageSize": page_size,
            "pageNum": 1
        }
        
        try:
            # timeout을 10초로 줄여 무한 대기 방지 (100초는 콘솔 앱에서 너무 깁니다)
            response = requests.get(self.url, params=params, timeout=10)
            
            # HTTP 400~500번대 에러 발생 시 예외(Exception) 발생
            response.raise_for_status() 
            
            # JSON 파싱
            return response.json()
                
        except requests.exceptions.RequestException as e:
            return f"❌ API 통신 오류: {e}"
        except ValueError:
            # apiType=json이 무시되고 XML이 왔거나, 응답이 비어있을 때의 방어 로직
            return f"❌ JSON 파싱 실패. 원본 응답:\n{response.text[:300]}"


# ==========================================
# 🧪 단독 실행 테스트 블록
# 터미널 실행: python utils/book_client.py
# ==========================================
if __name__ == "__main__":
    print("--- 국립중앙도서관 API 연동 테스트 시작 ---")
    try:
        # 1. 클라이언트 객체 생성
        client = BookClient()
        print(f"✅ API 키 로드 성공: {client.api_key[:4]}********")
        
        # 2. 도서 검색 테스트
        test_keyword = "파이썬"
        print(f"🚀 '{test_keyword}' 도서 검색 중...")
        
        result = client.search_book(test_keyword, page_size=1)
        
        # 3. 결과 출력
        print("\n[📦 응답 데이터 확인]")
        print("-" * 50)
        if isinstance(result, dict):
            import json
            # JSON 형태를 보기 좋게 들여쓰기(indent)하여 출력
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            # 에러 메시지(문자열) 출력
            print(result)
        print("-" * 50)
        
    except Exception as e:
        print(f"⚠️ 실행 중 에러가 발생했습니다: {e}")
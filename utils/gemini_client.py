import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env 파일에서 환경변수 로드
load_dotenv()

class GeminiClient:
    def __init__(self):
        # 환경변수에서 GEMINI_API_KEY 가져오기
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY가 설정되지 않았습니다. .env 파일을 확인해주세요.")
        
        # Gemini API 초기화
        genai.configure(api_key=api_key)
        
        # Flash 모델 설정 (속도,효율)
        # (추후 환경에 따라 'gemini-1.5-flash'등 사용 가능한 모델로 변경)
        self.model = genai.GenerativeModel('gemini-3.5-flash')

    def generate_book_quiz(self, book_title):
        """주어진 책 제목에 대한 독서 퀴즈를 생성합니다."""
        prompt = f"""
        너는 PyBook 시스템의 독서 퀴즈 출제 위원이야. 
        사용자가 제공하는 책의 핵심 내용이나 줄거리를 바탕으로 객관식 4지선다 문제를 하나 내주고, 마지막에 정답을 알려줘.
        
        대상 도서: '{book_title}'
        """
        
        try:
            # Gemini 모델을 통한 텍스트 생성
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"퀴즈 생성 중 Gemini API 호출 오류가 발생했습니다: {e}"

#임시 테스트 용 
# 단독 실행 테스트 블록
# 실행 방법: 터미널에서 python utils/gemini_client.py 입력
# ==========================================
if __name__ == "__main__":
    print("--- Gemini API 연동 테스트 시작 ---")
    try:
        # 1. 클라이언트 생성 테스트
        gemini_client = GeminiClient()
        print("Gemini 클라이언트 초기화 성공!")
        
        # 2. API 호출 테스트
        test_book = "이기적 유전자"
        print(f"\n요청 중: '{test_book}' 퀴즈 생성 (약 2~5초 소요)")
        
        quiz_result = gemini_client.generate_book_quiz(test_book)
        
        print("\n[ 테스트 결과 출력]")
        print("-" * 40)
        print(quiz_result)
        print("-" * 40)
        
    except ValueError as ve:
        print(f"\n[설정 오류] {ve}")
    except Exception as e:
        print(f"\n[테스트 실패] {e}")
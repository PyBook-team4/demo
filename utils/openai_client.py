import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
#현재 개발 가이드를 위한 임시 코드 나중에 전체 수정 필요
class OpenAIClient:

    def __init__(self):
        # .env 파일에 저장된 OPENAI_API_KEY를 호출
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY가 올바르지 않습니다. env 파일을 확인해주세요.")
        
        # 클라이언트 초기화
        self.client = OpenAI(api_key=api_key)

    #ai 기반 독서 퀴즈 
    def generate_book_quiz(self, book_title):
        # GPT에게 역할을 부여하고 퀴즈 생성을 요청하는 코드
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini", # 추후 성능보고 다른 모델로 변경예정
                #프롬프트 엔지니어링 헤어야함
                messages=[
                    {"role": "system", "content": "너는 독서 퀴즈 출제 위원이야. 객관식 4지선다 문제를 하나 내줘."},
                    {"role": "user", "content": f"책 '{book_title}'에 대한 퀴즈를 만들어줘."}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"퀴즈 생성 중 API 호출 오류가 발생했습니다: {e}"

#임시 테스트 코드, 추후 테스 폴더에서 진행
if __name__ == "__main__":
    print("--- OpenAI API 연동 테스트 시작 ---")
    try:
        #  클라이언트 생성 테스트
        ai_client = OpenAIClient()
        print("openAI 클라이언트 초기화 성공")
        
        # API 호출 테스트
        test_book = "데미안"
        print(f"\n요청 중: '{test_book}' 퀴즈 생성")
        
        quiz_result = ai_client.generate_book_quiz(test_book)
        
        print("\n[테스트 결과 출력]")
        print("-" * 40)
        print(quiz_result)
        print("-" * 40)
        
    except ValueError as ve:
        print(f"\n[설정 오류] {ve}")
    except Exception as e:
        print(f"\n[테스트 실패] {e}")
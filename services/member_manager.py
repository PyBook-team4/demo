import os
from models.member import Member
from utils.file_handler import FileHandler

class MemberManager:
    def __init__(self, filename="data/members.json"):
        self.filename = filename
        self.members = {}  # {user_id: Member 객체}
        self.current_user = None  # 현재 로그인한 회원 객체
        self.load_members()

    def load_members(self):
        """프로그램 실행 시 JSON 파일에서 회원 정보를 불러옴"""
        data_list = FileHandler.load_json(self.filename)
        for item in data_list:
            member = Member.from_dict(item)
            self.members[member.user_id] = member

    def save_members(self):
        """회원 정보 변경 시 JSON 파일에 즉시 저장"""
        # data 폴더가 없으면 생성
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        data_list = [member.to_dict() for member in self.members.values()]
        FileHandler.save_json(self.filename, data_list)

    def check_duplicate(self, user_id):
        """동일한 회원 아이디 등록 방지 (중복 검사)"""
        return user_id in self.members

    def register(self):
        """회원가입 기능"""
        print("\n--- [회원가입] ---")
        user_id = input("아이디 입력: ").strip()
        
        if self.check_duplicate(user_id):
            print("이미 존재하는 아이디입니다.")
            return False
        
        password = input("비밀번호 입력: ").strip()
        name = input("이름 입력: ").strip()
        phone = input("연락처 입력: ").strip()
        email = input("이메일 입력: ").strip()

        new_member = Member(user_id, password, name, phone, email)
        self.members[user_id] = new_member
        self.save_members()
        print("회원가입이 완료되었습니다!")
        return True

    def login(self):
        """로그인 기능"""
        print("\n--- [로그인] ---")
        user_id = input("아이디 입력: ").strip()
        password = input("비밀번호 입력: ").strip()

        member = self.members.get(user_id)
        if member and member.password == password:
            self.current_user = member
            print(f"로그인 성공! [{member.name}]님 환영합니다.")
            return True
        else:
            print("아이디 또는 비밀번호가 일치하지 않습니다.")
            return False

    def logout(self):
        """로그아웃 기능"""
        if self.current_user:
            print(f"[{self.current_user.name}]님이 로그아웃하셨습니다.")
            self.current_user = None
        else:
            print("로그인된 사용자가 없습니다.")
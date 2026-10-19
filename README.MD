book_project/
│
├── main.py                  #  프로그램 실행 진입점 (메인 메뉴 제어)
├── README.md                #  프로젝트 소개 및 실행 가이드
│
├── models/                  #  데이터 구조(클래스) 정의 패키지
│   ├── __init__.py
│   ├── member.py            # 회원 데이터 클래스
│   ├── book.py              # 도서 데이터 클래스
│   └── record.py            # 독서 기록(상태, 별점, 감상평) 클래스
│
├── services/                # 핵심 비즈니스 로직 및 CRUD 처리 패키지
│   ├── __init__.py
│   ├── member_manager.py    # 회원가입, 로그인, 정보 수정/삭제
│   ├── book_manager.py      # 도서 등록, 상세 조회, 수정/삭제
│   └── record_manager.py    # 독서 상태 관리, 검색, 정렬, 통계
│
├── utils/                   # 공통 유틸리티 및 외부 연동 패키지
│   ├── __init__.py
│   ├── file_handler.py      # JSON/CSV 파일 입출력 공통 함수
│   └── api_client.py        # Open Library API 책 정보 자동 조회 연동
│
├── data/                    # 데이터 영속성 저장소 (JSON/CSV 파일)
│   ├── members.json
│   ├── books.json
│   └── records.json
│
└── tests/                   # 단위 테스트 및 통합 테스트 코드[cite: 1]
    ├── __init__.py
    ├── test_member.py
    └── test_book.py



    # Book Record Management System (독서 기록 관리 시스템)

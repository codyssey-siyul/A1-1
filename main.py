prompts = [
    {
        "title": "메일 초안 작성 도우미",
        "content": "당신은 정중하고 명확한 비즈니스 메일 작성 도우미입니다. "
                   "아래 정보를 바탕으로 제목과 메일 본문을 작성하세요. "
                   "수신자, 목적, 핵심 내용, 원하는 말투를 반영하고 "
                   "불필요하게 길지 않게 작성하세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "광고 영상 키 비주얼 생성",
        "content": "광고 영상용 키 비주얼을 제작합니다. 제품 또는 주인공: [입력]. "
                   "분위기: [입력]. 고정 레퍼런스 스타일: 세련된 상업 광고, "
                   "명확한 제품 강조, 영화 같은 조명, 고품질 이미지. "
                   "텍스트나 로고는 넣지 마세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "뉴스 핵심 요약",
        "content": "아래 뉴스 내용을 핵심 사실 중심으로 요약하세요. "
                   "1) 핵심 요약 3줄, 2) 중요한 수치·인물·날짜, "
                   "3) 예상되는 영향 순서로 작성하세요. "
                   "추측은 사실처럼 쓰지 마세요.",
        "category": "자동화",
        "favorite": False
    }
]
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    
    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = "★" if prompt["favorite"] else ""
        print(f"{index}. [{prompt['category']}] {prompt['title']} {favorite_mark}")

    print(f"\n총 {len(prompts)}개의 프롬프트")
show_menu()
show_list()
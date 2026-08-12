import os
import json

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

try:
    with open("prompts.json", "r", encoding="utf-8") as file:
        prompts = json.load(file)
except FileNotFoundError:
    pass

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. Markdown 내보내기")
    print("0. 종료")

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        input("\n계속하려면 Enter를 누르세요...")
        return
    
    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = "★" if prompt["favorite"] else ""
        print(f"{index}. [{prompt['category']}] {prompt['title']} {favorite_mark}")

    print(f"\n총 {len(prompts)}개의 프롬프트")
    input("\n계속하려면 Enter를 누르세요...")

def show_category():
    print("\n=== 카테고리별 조회 ===")

    categories = []

    for prompt in prompts:
        if prompt["category"] not in categories:
            categories.append(prompt["category"])

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    choice = int(input("조회할 카테고리를 선택하세요: "))

    selected_category = categories[choice - 1]

    print(f"\n=== {selected_category} 카테고리 ===")

    category_prompts = [
        prompt for prompt in prompts
        if prompt["category"] == selected_category
    ]

    if not category_prompts:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    for index, prompt in enumerate(category_prompts, start=1):
        favorite_mark = "★" if prompt["favorite"] else ""
        print(f"{index}. {prompt['title']} {favorite_mark}")

    input("\n계속하려면 Enter를 누르세요...")

def show_search():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색할 키워드를 입력하세요: ")

    search_results = [
        prompt for prompt in prompts
        if keyword in prompt["title"] or keyword in prompt["content"]
    ]

    if not search_results:
        print("검색 결과가 없습니다.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    print(f"\n=== '{keyword}' 검색 결과 ===")

    for index, prompt in enumerate(search_results, start=1):
        favorite_mark = "★" if prompt["favorite"] else ""
        print(f"{index}. [{prompt['category']}] {prompt['title']} {favorite_mark}")

    input("\n계속하려면 Enter를 누르세요...")

def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    choice = input("프롬프트 번호를 입력하세요: ")

    if not choice.isdigit():
        print("올바른 프롬프트 번호를 입력하세요.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    prompt = prompts[index]

    favorite_mark = "★" if prompt["favorite"] else "☆"

    print("\n" + "-" * 40)
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {favorite_mark}")
    print("-" * 40)
    print("내용:")
    print(prompt["content"])
    print("-" * 40)

    input("\n계속하려면 Enter를 누르세요...")

def show_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    choice = input("프롬프트 번호를 입력하세요: ")

    if not choice.isdigit():
        print("올바른 프롬프트 번호를 입력하세요.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    prompt = prompts[index]

    prompt["favorite"] = not prompt["favorite"]

    if prompt["favorite"]:
        print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다.")
    else:
        print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")

    input("\n계속하려면 Enter를 누르세요...")

def show_favorite_list():
    print("\n=== 즐겨찾기 목록 ===")

    favorite_prompts = [
        prompt for prompt in prompts
        if prompt["favorite"]
    ]

    if not favorite_prompts:
        print("즐겨찾기된 프롬프트가 없습니다.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    for index, prompt in enumerate(favorite_prompts, start=1):
        print(f"{index}. [{prompt['category']}] {prompt['title']} ★")

    print(f"\n총 {len(favorite_prompts)}개의 즐겨찾기")

    input("\n계속하려면 Enter를 누르세요...")

def export_markdown():
    print("\n=== Markdown 내보내기 ===")

    os.makedirs("markdown", exist_ok=True)

    categories = []

    for prompt in prompts:
        if prompt["category"] not in categories:
            categories.append(prompt["category"])

    for category in categories:
        filename = f"markdown/{category}.md"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"# {category}\n\n")

            for index, prompt in enumerate(
                [p for p in prompts if p["category"] == category],
                start=1
            ):
                favorite_mark = "⭐" if prompt["favorite"] else ""

                file.write(f"## {index}. {prompt['title']} {favorite_mark}\n\n")
                file.write(f"**카테고리:** {prompt['category']}\n\n")
                file.write("### 내용\n\n")
                file.write(f"{prompt['content']}\n\n")
                file.write("---\n\n")

    print("Markdown 파일로 내보냈습니다.")
    print("markdown 폴더를 확인하세요.")

    input("\n계속하려면 Enter를 누르세요...")

def show_add():
    print("\n=== 프롬프트 추가 ===")

    print("(뒤로가기: 0)")
    title = input("제목: ")

    if title == "0":
        print("\n프롬프트 추가를 취소했습니다.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    while not title.strip():
        print("제목은 비워둘 수 없습니다.")
        title = input("제목: ")

        if title == "0":
            print("\n프롬프트 추가를 취소했습니다.")
            input("\n계속하려면 Enter를 누르세요...")
            return

    print("(뒤로가기: 0)")
    content = input("내용: ")

    if content == "0":
        print("\n프롬프트 추가를 취소했습니다.")
        input("\n계속하려면 Enter를 누르세요...")
        return

    while not content.strip():
        print("내용은 비워둘 수 없습니다.")
        content = input("내용: ")

        if content == "0":
            print("\n프롬프트 추가를 취소했습니다.")
            input("\n계속하려면 Enter를 누르세요...")
            return
        
    categories = [
        "텍스트 생성",
        "이미지 생성",
        "영상 생성",
        "페르소나",
        "자동화",
        "기타"
    ]

    print("\n카테고리를 선택하세요.")
    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")
    print("7. 직접 입력")
    print("0. 뒤로가기")

    category_choice = input("선택: ")

    while True:
        if category_choice == "0":
            print("\n프롬프트 추가를 취소했습니다.")
            input("\n계속하려면 Enter를 누르세요...")
            return

        if category_choice.isdigit():
            category_index = int(category_choice)

            if 1 <= category_index <= len(categories):
                category = categories[category_index - 1]
                break

            if category_index == 7:
                category = input("카테고리를 입력하세요: ")

                if category == "0":
                    print("\n프롬프트 추가를 취소했습니다.")
                    input("\n계속하려면 Enter를 누르세요...")
                    return

                if category.strip():
                    category = category.strip()
                    break

                print("카테고리는 비워둘 수 없습니다.")

            else:
                print("올바른 카테고리 번호를 입력하세요.")

        else:
            print("올바른 카테고리 번호를 입력하세요.")

        category_choice = input("선택: ")

    prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(prompt)

    print("\n프롬프트가 추가되었습니다!")

    input("\n계속하려면 Enter를 누르세요...")

while True:
    show_menu()

    choice = input("메뉴를 선택하세요: ")

    if choice == "1":
     show_add()

    elif choice == "2":
        show_list()

    elif choice == "3":
        show_category()

    elif choice == "4":
        show_search()

    elif choice == "5":
        show_detail()

    elif choice == "6":
        show_favorite()

    elif choice == "7":
        show_favorite_list()

    elif choice == "8":
        export_markdown()

    elif choice == "0":
        with open("prompts.json", "w", encoding="utf-8") as file:
            json.dump(prompts, file, ensure_ascii=False, indent=4)

        print("프로그램을 종료합니다.")
        break

    else:
        print("올바른 메뉴 번호를 입력하세요.")
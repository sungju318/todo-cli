import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEDULE_FILE = os.path.join(SCRIPT_DIR, "schedule.txt")

def list_todos():
    """schedule.txt 파일을 읽어 할 일 목록을 출력합니다."""
    print("--- 할 일 목록 ---")
    try:
        with open(SCHEDULE_FILE, "r", encoding="utf-8") as f:
            todos = f.readlines()
            if not todos:
                print("할 일이 없습니다.")
            else:
                for i, todo in enumerate(todos, 1):
                    print(f"{i}. {todo.strip()}")
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다. 'add' 명령으로 새 할 일을 추가하세요.")

def add_todo(todo_text):
    """새로운 할 일을 파일에 추가합니다."""
    with open(SCHEDULE_FILE, "a", encoding="utf-8") as f:
        f.write(f"[ ] {todo_text}\n")
    print(f"추가되었습니다: {todo_text}")

def done_todo(item_number):
    """지정된 번호의 할 일을 완료 처리합니다."""
    try:
        with open(SCHEDULE_FILE, "r", encoding="utf-8") as f:
            todos = f.readlines()

        if 0 < item_number <= len(todos):
            index = item_number - 1
            if todos[index].startswith("[ ]"):
                todos[index] = "[x]" + todos[index][3:]
                with open(SCHEDULE_FILE, "w", encoding="utf-8") as f:
                    f.writelines(todos)
                print(f"완료 처리: {todos[index].strip()}")
            else:
                print("이미 완료된 항목입니다.")
        else:
            print(f"오류: 잘못된 항목 번호입니다. (1-{len(todos)})")

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")

def main():
    """명령어에 따라 기능을 실행합니다."""
    command = sys.argv[1] if len(sys.argv) > 1 else "list"

    if command == "list":
        list_todos()
    elif command == "add":
        if len(sys.argv) > 2:
            todo_text = " ".join(sys.argv[2:])
            add_todo(todo_text)
        else:
            print("오류: 추가할 할 일의 내용이 없습니다.")
            print("사용법: python main.py add [할 일 내용]")
    elif command == "done":
        if len(sys.argv) > 2:
            try:
                item_number = int(sys.argv[2])
                done_todo(item_number)
            except ValueError:
                print("오류: 항목 번호는 숫자여야 합니다.")
        else:
            print("오류: 완료할 할 일의 번호가 없습니다.")
            print("사용법: python main.py done [번호]")
    else:
        print(f"알 수 없는 명령어: {command}")
        print("사용 가능한 명령어: list, add, done")

if __name__ == "__main__":
    main()

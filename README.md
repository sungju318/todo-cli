# CLI 할 일 관리 프로그램 (CLI To-Do List Manager)

## 프로젝트 개요 (Overview)

이 프로젝트는 터미널(명령줄) 환경에서 사용할 수 있는 간단한 할 일 관리 프로그램입니다. 사용자는 이 프로그램을 통해 할 일을 추가하고, 목록을 확인하고, 완료 처리할 수 있습니다. 모든 할 일은 `schedule.txt` 파일에 저장됩니다.

## 사용법 (Usage)

### 할 일 목록 보기 (List To-Dos)
현재 저장된 모든 할 일 목록을 봅니다.
```bash
python main.py
# 또는
python main.py list
```

### 할 일 추가하기 (Add a To-Do)
새로운 할 일을 목록에 추가합니다.
```bash
python main.py add [할 일 내용]
```
**예시:**
```bash
python main.py add 파이썬 과제 제출하기
```

### 할 일 완료하기 (Complete a To-Do)
지정한 번호의 할 일을 완료 상태로 변경합니다.
```bash
python main.py done [번호]
```
**예시:**
```bash
python main.py done 2
```
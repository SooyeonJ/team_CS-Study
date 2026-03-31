import os
import requests
import datetime
import re

def get_today_kst():
    # GitHub Actions 서버는 UTC 기준이므로 한국 시간(KST)으로 변환합니다.
    now_utc = datetime.datetime.utcnow()
    now_kst = now_utc + datetime.timedelta(hours=9)
    return now_kst.strftime("%m-%d")

def parse_today_problem(date_str):
    filename = "2026-04.md"
    if not os.path.exists(filename):
        return None

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if date_str in line and "|" in line:
            # 파이프(|) 기호로 열을 분리합니다.
            columns = [col.strip() for col in line.split("|")]
            if len(columns) < 6:
                continue
            
            day_type = columns[3] # 유형
            prob1 = columns[4]    # 문제 1
            prob2 = columns[5]    # 문제 2
            return {"type": day_type, "p1": prob1, "p2": prob2}
    return None

def send_slack_message(data, date_str):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("Error: SLACK_WEBHOOK_URL is not set.")
        return

    message = {
        "text": f"오늘({date_str})의 코딩테스트 학습 안내",
        "attachments": [
            {
                "color": "#36a64f",
                "fields": [
                    {"title": "학습 유형", "value": data["type"], "short": False},
                    {"title": "문제 1", "value": data["p1"], "short": True},
                    {"title": "문제 2", "value": data["p2"], "short": True}
                ],
                "footer": "GitHub Actions 스터디 봇"
            }
        ]
    }

    response = requests.post(webhook_url, json=message)
    if response.status_code == 200:
        print("Success: Message sent to Slack.")
    else:
        print(f"Error: Slack API returned {response.status_code}")

if __name__ == "__main__":
    today_date = get_today_kst()
    problem_data = parse_today_problem(today_date)

    if problem_data:
        send_slack_message(problem_data, today_date)
    else:
        print(f"No problem scheduled for {today_date}.")

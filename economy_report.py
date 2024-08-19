import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import datetime
import os

def fetch_economic_data():
    url = 'https://example.com/economy'  # 실제 경제 데이터 제공 사이트로 변경
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headline = soup.find('h1').text
    summary = soup.find('p').text
    
    return headline, summary

def generate_article(headline, summary):
    today = datetime.datetime.now().strftime("%Y년 %m월 %d일")
    article = f"""
    경제 현황 보고서 - {today}

    제목: {headline}

    요약: {summary}

    자세한 내용은 아래 링크를 참조하세요.
    """
    return article

def send_email(article, recipient_email):
    sender_email = os.environ['EMAIL_ADDRESS']
    sender_password = os.environ['EMAIL_PASSWORD']
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "오늘의 경제 현황 보고서"

    msg.attach(MIMEText(article, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, recipient_email, text)
    server.quit()

if __name__ == "__main__":
    headline, summary = fetch_economic_data()
    article = generate_article(headline, summary)
    recipient_email = "recipient@example.com"
    send_email(article, recipient_email)
    print("이메일이 성공적으로 전송되었습니다.")

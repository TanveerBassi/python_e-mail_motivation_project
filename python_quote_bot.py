import requests
import yagmail

def fetch_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()
    author = data['author']
    text = data['content']
    return f"{text} - {author}"

def send_email(quote, recipients):
    yag = yagmail.SMTP("your_email", "your_password")
    subject = "Daily Motivational Quote"
    yag.send(to=recipients, subject=subject, contents=quote)

quote = fetch_quote()
recipients = ["email1@example.com", "email2@example.com"]
send_email(quote, recipients)

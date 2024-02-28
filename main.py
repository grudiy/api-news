import requests

from send_email import send_email

API_KEY = '667c5435450b4aec80d0283XXX'
query = "Ukraine"
url = "https://newsapi.org/v2/everything?q=" + query + "&from=2024-01-27&sortBy=publishedAt&apiKey=" + API_KEY

response = requests.get(url)
content = response.json()

body = ""
for article in content["articles"]:
    if article is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)

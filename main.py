import requests

API_KEY = '667c5435450b4aec80d0283f0765a3b1'
query = "Ukraine"
url = "https://newsapi.org/v2/everything?q=" + query + "&from=2024-01-27&sortBy=publishedAt&apiKey=" + API_KEY

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
import requests

GOOGLE_URL = "https://www.google.com/search"

def goolesearch(keywords):
    print("Google検索:", GOOGLE_URL, "キーワード:", *keywords)
    q = "+".join(keywords)
    response = requests.get(GOOGLE_URL, params={"q": q})
    return response
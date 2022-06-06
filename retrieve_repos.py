import requests, json

username = "talisainen"
def retrieve_repos(username):
    
  url = requests.get(f"https://api.github.com/users/{username}")

  return url

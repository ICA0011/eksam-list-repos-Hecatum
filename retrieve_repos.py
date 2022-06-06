import requests, json

username = "talisainen"
def retrieve_repos(username):
    
  req = requests.get(f"https://api.github.com/users/{username}/repos")

  json_list = req.json()

  return json_list


print(retrieve_repos(username))
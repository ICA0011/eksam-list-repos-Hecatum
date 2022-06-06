import requests, json

username = "talisainen"
def retrieve_repos(username):
    
  req = requests.get(f"https://api.github.com/users/{username}/repos")

  json_list = req.json()

  for i in range(0,len(json_list)):
    print("Project Number: ",i+1)


retrieve_repos(username)
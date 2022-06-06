import requests, json

username = "talisainen"
def retrieve_repos(username):
    
  req = requests.get(f"https://api.github.com/users/{username}/repos")

  json_list = req.json()

  amount_of_repos = 0

  for i in range(0,len(json_list)):
    amount_of_repos += 1
  
  return amount_of_repos



print(retrieve_repos(username))
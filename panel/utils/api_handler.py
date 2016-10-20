import requests
import json

def get_project_stats(id):
    try:
        url = 'http://localhost:8000/api/v1/projects/%s/stats' %(id)
        headers = {'Authorization': 'Bearer eyJ1c2VyX2F1dGhlbnRpY2F0aW9uX2lkIjo0fQ:1bt1F1:zUFg6olVQIltyTYG7aiD-zXOvnI'}
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        return data

    except:
        print("Error")

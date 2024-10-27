import requests

BASE = "http://127.0.0.1:5000/"

# data = [{"likes": 10, "name": "Kevin", "views": 10000},
#         {"likes": 100, "name": "How to make REST API", "views": 100000},
#         {"likes": 1000, "name": "Tim", "views": 1000000}]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())
# input()                     

response = requests.patch(BASE + "video/2", {"views": 99, "likes": 101})
print(response.json())

import requests
import os
import time

SECRET_KEY = os.environ['SECRET_KEY']

def uploadActivities(activities, endpoint, athleteId):
  header = {
    'SECRETKEY': SECRET_KEY,
    'ATHLETE': str(athleteId),
    'Content-Type': 'application/x-www-form-urlencoded',
  }
  numActivities = len(activities)
  batchSize = 50
  startIndex = 0
  while startIndex < numActivities:
    batch = activities[startIndex : startIndex + batchSize]
    jsonData = convertToJson(batch)
    try:
      res = requests.post(
        endpoint,
        headers=header,
        json=jsonData
      )
      if not res.status_code in [201, 200]:
        print('Activity Upload Invalid Status:', res.status_code, res.text)
      time.sleep(2)
      startIndex += batchSize
    except Exception as e:
      print(e)

def convertToJson(batch):
  jsonData = dict.fromkeys(batch[0].keys())
  for key in jsonData:
    jsonData[key] = [activity[key] for activity in batch]
  return jsonData

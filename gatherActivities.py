import datetime
import requests

def gatherActivities(token):
  baseUrl = 'https://www.strava.com/api/v3/athlete/activities'
  header = {
    'Authorization': f'Bearer {token}'
  }
  activities = []
  now = int(datetime.datetime.today().timestamp())
  # Max: 5000
  for i in range(1, 25):
    page = requests.get(
      baseUrl,
      headers=header,
      params={
        'before': now,
        'after': 0,
        'page': i,
        'per_page': 200,
      }
    )
    if page.status_code != 200:
      raise Exception(f'Status {page.status_code}: {page.text}')
    if not page.json():
      break
    activities.extend(page.json())
  return activities
  
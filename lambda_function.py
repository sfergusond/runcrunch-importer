from gatherActivities import gatherActivities
from formatActivities import formatActivities
from uploadActivities import uploadActivities
from buildPolyline import buildPolyline
from uploadPolyline import uploadPolyline

def lambda_handler(event, context):
  try:
    rawActivities = gatherActivities(event['token'])
    print('Raw:', len(rawActivities))
  except Exception as e:
    print(e)
    return
  
  try:
    formattedActivities = formatActivities(rawActivities)
    print('Formatted:', len(formattedActivities))
    uploadActivities(
      formattedActivities,
      event['uploadEndpoint'],
      event['athleteId']
    )
  except Exception as e:
    print(e)
    return
  
  # Polyline
  try:
    polyline = buildPolyline(rawActivities)
    uploadPolyline(polyline, event['athleteId'])
  except Exception as e:
    print(e)
  
if __name__ == '__main__':
  event = {
    'token': 'TOKEN',
    'athleteId': 4,
    'uploadEndpoint': 'http://localhost:8000/api/activity/bulk/create/',
  }
  lambda_handler(event, None)

def formatActivities(activities):
  formattedActivities = []
  for a in activities:
    if 'Run' in a['type'] or a['type'] in ['Walk', 'Hike']:
      try:
        formattedActivity = formatActivity(a)
        formattedActivities.append(formattedActivity)
      except Exception as e:
        print('Format Error:', e)
  return formattedActivities

def formatActivity(activity):
  formattedActivity = {}
  formattedActivity['distance'] = int(round(
    activity['distance'])) if activity.get('distance') else None
  formattedActivity['elevation'] = int(round(
    activity['total_elevation_gain'])) if activity.get('total_elevation_gain') else None
  formattedActivity['averageHr'] = round(
    int(activity['average_heartrate'])) if activity.get('average_heartrate') else None
  formattedActivity['timestamp'] = activity['start_date_local'].replace('T', ' ')
  formattedActivity['time'] = activity.get('moving_time', 0)
  formattedActivity['title'] = activity['name'][:500].replace('\'', ' ').replace('\"', ' ')
  formattedActivity['stravaId'] = activity['id']
  return formattedActivity

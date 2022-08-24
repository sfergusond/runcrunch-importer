import boto3
import os

client = boto3.client('s3')

def uploadPolyline(polyline, athleteId):
  key = f'polyline-{athleteId}.txt'
  bytes = polyline.encode('utf-8')
  try:
    client.put_object(
      Body=bytes,
      Key=key,
      Bucket='runcrunch-polyline'
    )
  except Exception as e:
    print(e)

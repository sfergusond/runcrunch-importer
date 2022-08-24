RAW_MAP = {
  8:r'\b',
  7:r'\a',
  12:r'\f',
  10:r'\n',
  13:r'\r',
  9:r'\t',
  11:r'\v'
}

def buildPolyline(activities):
  summaryPolyline = r''
  for a in activities:
    polyline = a['map']['summary_polyline']
    if polyline:
      raw = r''.join(
        i if ord(i) > 32 else RAW_MAP.get(ord(i), i) for i in polyline
        )
      summaryPolyline += raw + r','
  return summaryPolyline

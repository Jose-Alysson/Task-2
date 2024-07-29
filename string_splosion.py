'''
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''

def string_splosion(str):
  part1 = str[:1]
  part2 = str[:2]
  part3 = str[:3]
  part4 = str[:4]
  part5 = str[:5]
  if len(str) == 3:
    return part1 + part2 + part3
  if len(str) == 1:
    return part1
  if len(str) < 3:
    return part1 + part2
  else:
    return part1 + part2 + part3 + part4
  if len(str) == 5:
    return part1 + part2 + part3 + part4 + part5

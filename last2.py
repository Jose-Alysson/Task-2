'''
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
'''
def last2(str):
  count = 0
  for x in range(len(str)- 2):
    print(x)
    if x < len(str[:]):
      return count + 1
  else:
    return count





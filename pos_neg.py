def pos_neg(a, b, negative):
  if negative == False and a >= 0 and b <=0 or a <= 0 & b >= 0:
    return True
  if negative == True and a <= 0 and b <= 0:
    return True
  if negative == True and >= 0 and b >= 0:
    return False
  if negative == False and a < 0 and b < 0:
   return False

def power(number, pow):
  ans = 1
  while pow!=1:
    ans = ans*number
    pow -=1
  return ans

number = input()
pow = 1
flag = 0
while flag == 0 :
  if number == (power(2, pow)*(power(2, pow+1)-1)):
    print ("perfect number")
    flag = 1
  if number < (power(2, pow)*(power(2, pow+1)-1)):
    print("not a perfect number")
    flag = 1
  if number > (power(2, pow)*(power(2, pow+1)-1)):
    pow+=1
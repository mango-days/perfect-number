number = input()
p = 1
flag = 0
while flag == 0 :
  if number == (pow(2, p)*(pow(2, p+1)-1)):
    print ("perfect number")
    flag = 1
  if number < (pow(2, p)*(pow(2, p+1)-1)):
    print("not a perfect number")
    flag = 1
  if number > (pow(2, p)*(pow(2, p+1)-1)):
    p+=1

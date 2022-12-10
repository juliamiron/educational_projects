#Given an integer x, return true if x is a palindrome, and false otherwise.

n = int(input())
temp = n
reverse = 0
while (n > 0):
  last_number = n % 10
  reverse = reverse * 10 + last_number
  n = n // 10
if(temp == reverse):
  print('это палиндром')
else:
  print('это не палиндром')
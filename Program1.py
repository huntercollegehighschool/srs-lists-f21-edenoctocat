'''
*********
PROGRAM 1
*********
Define a function number_of_odds that takes a list of integers as an argument. The function returns how an integer, how many odd numbers are in the list.
'''
def number_of_odds(lst):
  odds = 0
  for number in lst:
    if number % 2 == 1:
      odds += 1
  return odds
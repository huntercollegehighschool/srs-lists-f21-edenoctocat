'''
*********
PROGRAM 3
*********
Define a function second_smallest that takes a list of integers or floats as an argument. The function returns the 2nd smallest number in the list.
'''
def second_smallest(lst):
  smallest = lst[0]
  secsmallest = lst[0]
  for number in lst:
    if number < smallest:
      secsmallest = smallest
      smallest = number
    elif number < secsmallest:
      secsmallest = number
  return secsmallest

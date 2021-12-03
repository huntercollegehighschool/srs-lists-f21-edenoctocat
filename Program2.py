'''
*********
PROGRAM 2
*********
Define a function odd_reverse that takes a list as an argument. The function creates a new list containing only the elements in the odd indices (indices 1, 3, 5, ...) and then reverses it. The function returns that list.
'''
def odd_reverse(lst):
  oddlst = []
  for number in lst:
    if number % 2 == 1:
      oddlst.append(number)
  return oddlst

def linear_serach(list,target):
  """""
  returns index of the target value if exists else returns None
  """""

  for i in range(0,len(list)): 
    if list[i] == target :
      return i

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_serach(list,4)
print(result)

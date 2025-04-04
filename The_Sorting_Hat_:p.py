import time

print('Today will be an important day for you will be sent to one of the great 4 houses in the world of magic')
time.sleep(5)
print('You will be asked 3 questions and based on your answers the sorting hat will decide which house you will be sent to')
time.sleep(4)
print('Let the magic begin!')
time.sleep(3)
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
q1 = int(input('Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk '))
if q1 == 1 :
  gryffindor += 1
  ravenclaw += 1
elif q1 == 2 :
  hufflepuff += 1
  slytherin += 1
else :
  print('Wrong input')

q2 = int(input('When I’m dead, I want people to remember me as : \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold '))
if q2 == 1 :
  gryffindor +=2
elif q2 == 2 :
  ravenclaw +=2
elif q2 == 3 :
  hufflepuff +=2
elif q2 == 4 :
  slytherin +=2
else :
  print('Wrong input')

q3 = int(input('Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum '))
if q3 == 1 :
  gryffindor +=4
elif q3 == 2 :
  ravenclaw +=4
elif q3 == 3 :
  hufflepuff +=4
elif q3 == 4 :
  slytherin +=4
else :
  print('Wrong input')

max_points = max(gryffindor,ravenclaw,hufflepuff,slytherin)
print('The house with max points is :')
if max_points == gryffindor:
    print('🦁 Gryffindor!')
if max_points == ravenclaw:
    print('🦅 Ravenclaw!')
if max_points == hufflepuff:
    print('🦡 Hufflepuff!')
if max_points == slytherin:
    print('🐍 Slytherin!')
print('Congratulations')

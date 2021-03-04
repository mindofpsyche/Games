import random
opt = ["s", "w", "g"]
c1 = random.choice(opt)           #random choice by cpu
print('WELCOME TO THE GAME\n'
      'This is computer based Snake,water and gun game.\n')
r1 = int(input('How many rounds will you like to play?\n'))
p1 = 0
p2 = 0
#defining rules for winning

def rules():
      global p1 #defined p1 & p2 as a global variable so that it's value remains same and change accordingly both
             # outside and inside the function
      global p2

      if c1 == c2:
            print('Round DRAW\n')
            p1 += 0
            p2 += 0
      elif c1 == 's' and c2 == 'w':
            print('YOU LOOSE. \nCPU took snake so it won.')
            p1 += 1
            p2 += 0
      elif  c1 == 's'   and c2 == 'g' :
            print('\nYOU WON.\n CPU took snake so it lost.')
            p2 += 1
            p1 += 0
      elif  c1 == 'w' and c2 == 's'  :
            print('\nYOU WON.\n CPU took water so it lost.')
            p2 += 1
            p1 += 0
      elif c1 == 'w' and c2 == 'g':
            print('YOU LOOSE.\nCPU took water so it won.')
            p1 += 1
            p2 += 0
      elif c1 == 'g' and c2 =='s':
            print('YOU LOOSE.\nCPU took gun so it won.')
            p1 += 1
            p2 += 0
      elif c1 == 'g' and c2 == 'w':
            print('YOU WON.\nCPU took gun so it lost.')
            p2 += 1
            p1 += 0
      else :
            print('YOU ENTERED A WRONG CHOICE')



#taking input from the player
i=1
while i < (r1+1):

       print('Round',i)

       c2 = input(
      '\nEnter your choice among Snake,water and gun.\n'
      '\nFor  snake,s.\n'
      'For water,w.\n'
      'For gun,g.\n')
       i += 1
       rules()
       print('\nSCOREBOARD >>>>>>> CPU',p1,"-",'YOU',p2,'<<<<<<<<')
if p1 > p2 :
       print('\nCPU WON THE WHOLE  MATCH')
elif p1 < p2 :
       print('\nYOU WON THE WHOLE  MATCH')
else:
      print('MATCH DRAW')

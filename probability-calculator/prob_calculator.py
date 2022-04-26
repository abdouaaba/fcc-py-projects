import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
    contents = list()
    for key in args.keys():
        for color in range(args[key]):
          contents.append(key)
    self.contents = contents

  def draw(self, number):
    contents = self.contents
    if number >= len(contents):
      self.contents = []
      return contents
    listDrawn = list()
    for i in range(number):
      index = random.randrange(len(contents))
      
      toDraw = contents[index]
      listDrawn.append(toDraw)
      contents = contents[0:index] + contents[index + 1:]

    self.contents = contents
    return listDrawn





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  N = num_experiments
  M = 0
      
  for i in range(N):
    copiedHat = copy.copy(hat)
    listDrawn = copiedHat.draw(num_balls_drawn)
    flag = True
    for color in expected_balls.keys():
      if expected_balls[color] > listDrawn.count(color):
        flag = False
        break
    
    if flag == True:
      M += 1
      
  return M/N
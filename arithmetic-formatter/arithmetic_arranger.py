def arithmetic_arranger(problems, flag = False):
  if len(problems) > 5:
    return "Error: Too many problems."
  
  #initialising
  first = list()
  operator = list()
  second = list()
  solution = list()
  arranged_list = ['','','']
  arranged_problems = ''
  s = ''
  
  #seperating the problems, numbers and operators into lists
  for prob in problems:
    problem = prob.split(" ")

    if len(problem[0]) > 4 or len(problem[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    first.append(problem[0])
    operator.append(problem[1])
    second.append(problem[2])
    
    if problem[1] == '+':
      
      try:
        s = int(problem[0]) + int(problem[2])
      except ValueError:
        return "Error: Numbers must only contain digits."
    
    elif problem[1] == '-':
      
      try :  
        s = int(problem[0]) - int(problem[2])
      except ValueError:
        return "Error: Numbers must only contain digits."
    
    else:
      return "Error: Operator must be '+' or '-'."
    
    solution.append(str(s))

  #arranging everything in one list
  for i in range(len(problems)):
    diff1 = len(first[i]) - len(second[i])
    
    #first line
    if diff1 < 0:
      arranged_list[0] += '  ' + abs(diff1)*' ' + first[i] + 4*' '
    else:
      arranged_list[0] += '  ' + first[i] + 4*' '
    
    #second line
    if diff1 < 0:
      arranged_list[1] += operator[i] + ' ' + second[i] + 4*' '
    else:
      arranged_list[1] += operator[i] + ' ' + diff1*' ' + second[i] + 4*' '

    #third line
    l = max(len(first[i]), len(second[i])) + 2
    arranged_list[2] += l*'-' + 4*' '

    if flag == True:
      #solutions line 
      if i == 0:
        arranged_list.append('')
      diff2 = l - len(solution[i])   
      arranged_list[3] += diff2*' ' + solution[i] + 4*' '

  #turning everything into a string
  for j in range(len(arranged_list)):
    if j != (len(arranged_list)-1):
      arranged_problems += arranged_list[j].rstrip() + '\n'
    else:
      arranged_problems += arranged_list[j].rstrip()

  return arranged_problems
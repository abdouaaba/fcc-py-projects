class Category:
  def __init__(self, name):
    self.ledger = []
    self.amount = 0
    self.name = name
  
  def deposit(self, amount, description = ''):
    self.amount += amount
    self.ledger.append({"amount":amount, "description":description})
  
  def check_funds(self, amount):
    if amount <= self.amount:
      return True
    else:
      return False

  def get_balance(self):
    return self.amount

  def withdraw(self, amount, description = ''):
    if self.check_funds(amount):
      self.amount -= amount
      self.ledger.append({"amount":-amount, "description":description})
      return True
    else:
      return False

  def transfer(self, amount, dest):
    descrTo = "Transfer to {}".format(dest.name)
    descrFr = "Transfer from {}".format(self.name)
    if self.check_funds(amount):
      self.amount -= amount
      self.ledger.append({"amount":-amount, "description":descrTo})
      dest.amount += amount
      dest.ledger.append({"amount":amount, "description":descrFr})
      return True
    else:
      return False
  
  def __str__(self):
    l1 = len(self.name)
    n = int((30-l1)/2)
    result = ''
    if n < (30-l1)/2:
      result += (n+1)*'*' + self.name + (n)*'*' + '\n'
    else:
      result += (n)*'*' + self.name + (n)*'*' + '\n'

    for trans in self.ledger:
      l2 = len(trans["description"])
      if l2 >= 23:
        result += trans["description"][:23]
      else:
        result += trans["description"] + (23-l2)*' '
      
      if isinstance(trans["amount"], int):
        newNum = str(trans["amount"]) + '.00'
      else:
        newNum = str(trans["amount"])
      l3 = len(newNum)
      result += (7-l3)*' ' + newNum + '\n'
    
    result += "Total: " + str(self.amount)
    return result



def create_spend_chart(categories):
  res = ''
  res += "Percentage spent by category\n"

  spent = []
  percentage = []
  for i in range(len(categories)):
    spent.append(0)
    for j in categories[i].ledger:
      if j["amount"] < 0:
        spent[i] += j["amount"]
  
  for i in range(len(categories)):
    percentage.append(0)
    percentage[i] = round((abs(spent[i]/sum(spent))*100))

  n = 100
  for i in range(11):
    if i == 0:
      res += str(n) + '|'
      for j in percentage:
        if j >= n:
          res += ' o '
        else:
          res += '   '
    elif i == 10:
      res += '  ' + str(n) + '|'
      for j in percentage:
        if j >= n:
          res += ' o '
        else:
          res += '   '
    else:
      res += ' ' + str(n) + '|'
      for j in percentage:
        if j >= n:
          res += ' o '
        else:
          res += '   '
    res += ' \n'
    n -= 10

  res += 4*' ' + (3*len(categories)+1)*'-' + '\n'

  longest = 0
  for i in categories:
    if len(i.name) > longest:
      longest = len(i.name)

  for i in range(longest):
    res += 4*' '
    for categ in categories:
      try:
        res += ' ' + categ.name[i] + ' '
      except IndexError:
        res += 3*' '
    if i != longest-1:
      res += ' \n'
    else:
      res += ' '
  
  return res
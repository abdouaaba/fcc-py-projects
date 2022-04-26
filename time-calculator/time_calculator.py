def add_time(start, duration, day = None):
  daysLater = 0
  
  days = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
  nbr_list = list(days.keys())
  day_list = list(days.values())
  day_list = [x.upper() for x in day_list]

  sTime = start.split(' ')[0]
  wTime = start.split(' ')[1]
  
  startHours = int(sTime.split(':')[0])
  startMinutes = int(sTime.split(':')[1])

  addHours = int(duration.split(':')[0])
  addMinutes = int(duration.split(':')[1])

  if addHours >= 24:
    daysLater += int(addHours/24)
    addHours -= 24*daysLater

  newMinutes = startMinutes + addMinutes
  newHours = startHours + addHours

  if newMinutes >= 60:
    newMinutes -= 60
    newHours += 1
  
  if newHours >= 12:
    if newHours > 12:
        newHours -= 12
    if wTime == 'AM':
      wTime = 'PM'
    else:
      wTime = 'AM'
      daysLater += 1


  newHours = str(newHours)
  newMinutes = str(newMinutes)
  if len(newMinutes) == 1:
    newMinutes = '0' + newMinutes
  

  new_time = ' '.join((':'.join((newHours,newMinutes)),wTime))


  if day:
    newDay = nbr_list[day_list.index(day.upper())] + daysLater
    if newDay > 7:
      newDay -= (int(daysLater/7)*7 + 7)
    newDay = days.get(newDay)
    new_time = ', '.join((new_time, newDay))
  
  if daysLater == 1:
    new_time = ' '.join((new_time, '(next day)'))
  elif daysLater > 1:
    new_time = ' '.join((new_time, '({} days later)'.format(daysLater)))

  return new_time

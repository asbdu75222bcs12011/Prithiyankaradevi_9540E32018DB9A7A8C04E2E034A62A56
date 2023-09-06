def isleapyear (year):
  if(year%4==0):
    print('{} is a leap year'.format(year))
  else:
    print('{} is not a leap year'.format(year))
year=int(input("enter a year value"))
isleapyear(year)



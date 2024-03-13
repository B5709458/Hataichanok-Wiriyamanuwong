#TEST Hataichanok Wiriyamanuwong
#Variable
A = 1
B = 5
Z = 10
L = 50
C = 100
D = 500
R = 1000

AB = 4
AZ = 9
ZL = 40
ZC = 90
CD = 400
CR = 900

sum = 0
i = 0

#input
Anum = input("Input: s = ")
Anum += " "
#Process
while i < len(Anum) -1 :
  # Trigger for check is subtract
  trigger = False
  # Check Substract conditions
  if Anum[i] + Anum[i+1] == 'AB' :
    sum += AB
    trigger = True # if conditional is true, set trigger to True
  elif Anum[i] + Anum[i+1] == 'AZ' :
    sum += AZ
    trigger = True
  elif Anum[i] + Anum[i+1] == 'ZL' :
    sum += ZL
    trigger = True
  elif Anum[i] + Anum[i+1] == 'ZC' :
    sum += ZC
    trigger = True
  elif Anum[i] + Anum[i+1] == 'CD' :
    sum += CD
    trigger = True
  elif Anum[i] + Anum[i+1] == 'CR' :
    sum += CR
    trigger = True

  # When trigger, move array to +2 of indexs
  if trigger :
    i += 2

  # When not substract conditions
  if not trigger :
  #Check A
    if Anum[i] == 'A' :
      sum+=A
  #Check B
    elif Anum[i] =='B' :
      sum+=B
  #Check Z
    elif Anum[i] =='Z' :
        sum+=Z
  #Check L
    elif Anum[i] =='L' :
      sum+=L
  #Check C
    elif Anum[i] =='C' :
      sum+=C
  #Check D
    elif Anum[i] =='D' :
      sum+=D
  #Check R
    elif Anum[i] =='R' :
      sum+=R
  #Check Other
    else :
      break

    i += 1 # and then move array to +1 of index

#output
print("Output :",sum)
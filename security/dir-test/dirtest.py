import requests
import time
s=True
while(s):
  l=[]
  print("----- Welcome to DirTest! ----- \n")
  time.sleep(0.5)
  target = input("\nEnter target url :")
  file = input("Enter the payload file location :")
  wordlist = open(file,"r")
  for loop in wordlist:
      response = requests.get(url=f"{target}/{loop.strip()}")
      code=str(response.status_code)
      if int(code[0]) == 1 or int(code[0]) == 2 or int(code[0]) == 3:
        print(f"{target}/{loop} does exists! {code}")
        l.append(loop[0:-2])
      else:
          print(f"{target}/{loop} hit a wall {code} ")
  time.sleep(0.9)
  print("Available directory from the list are : ",l)
  time.sleep(3)
  choice = input("Do you wanna exit (Y/N)")
  if choice.lower() == 'y':
    s = False 
print("--------- END ---------")

n = input()
if int(n) % 2 != 0:
    print("Weird")
else:
    if int(n) % 2 == 0 and int(n) in range (2,6):
      print("Not Weird")
    else: 
        if int(n) % 2 == 0 and int(n) in range (6, 21):
           print("Weird")
        else: 
         if int(n) % 2 == 0 and int(n) > 20:
             print("Not Weird")

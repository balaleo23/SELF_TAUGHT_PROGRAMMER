import csv 

with open("C:/Users/jai/Desktop/python/SELF_TAUGHT_PROGRAM/new" ,"w") as f:
    write =csv.writer(f,delimiter=" ")
    write.writerow(["Top Gun", "Risky Business", "Minority Report"])
    write.writerow(["Titanic", "The Revenant", "Inception"])
    write.writerow(["Training Day", "Man on Fire", "Flight"])
    print("completed")

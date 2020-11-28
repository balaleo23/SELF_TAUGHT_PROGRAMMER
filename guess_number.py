listof = [1,3,8,10,15,25,35]
user = input("Enter the number between 0-100?")
while user != "q":
    user = input("Enter the number between 0-100?")
    if int(user) in listof:
        print("guessed correctly")
        break    
    


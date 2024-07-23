"""2) შექმენით პროგრამა რომელსაც ჰქვია guess game, თქვენი დავალებაა, მომხმარებელს იქამდე შემოატანინოთ რიცხვი სანამ არ გამოიცნობს რიცხვ 5_ს,
როცა გამოიცნობს ტერმინალში დაუბეჭდეთ რომ მან მოიგო, სხვა შემთხვევაში დაუბეჭდეთ რომ მან წააგო"""



#Guess game
num = int(input("please enter your number: "))

while num != 5:
    num = int(input("please enter number: "))
    if num == 5:
        print("you won")
    else:
        print("please try again: ")





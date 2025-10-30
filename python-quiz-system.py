Z = { 
    'A': "Add Question",
    'B': "Show Question",
    'C': "Start Question",
    'D': "Exit"
}
print(Z)

M_L = []
question = None
answer = None

while True:

    choice = str(input("select one: ")).lower().upper()

    if choice == "A":
        i = int(input("How many question you want to add: "))
        for i in range(i):
            question = str(input("Add Question: "))
            answer = str(input("Add Answer: "))
            M_L.append({"question" : question , "Answer":answer})
    
     # print(M_L)
    elif choice == "B":
        for itmes in M_L:
            print("Question :",itmes["question"],"\n" ,",","Answer :",itmes["Answer"])

    elif choice == "C":
        if not M_L:
            print("No question available")
        else:
            for Q in M_L:
                user_answer = str(input(Q["question"] + ": "))
                if user_answer == Q["Answer"]:
                    print("Correct")
                else:
                    print("Incorrect! The correct answer is: " + Q["Answer"])
    else:
        print("Exit")
        break

        
            
        
    

        
            
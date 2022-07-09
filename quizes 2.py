
quiz = ["Do you like staying indoors(a) or outdoors(b)?",
        "Do you have good communication skills? yes(a) or no(b)",
        "Are you interested more in people(a) or things(b)?",
        "Are you physically fit(a) or not(b)?",
        "Freinds(a) or BBT(b)?"
        ]

Career = ["Engineer",
          "Diplomat",
          "Doctor",
          "Olympian",
          "Academia",
         ]


def _input(): 
     _input.input1 = input(quiz[0])
     _input.input2 = input(quiz[1])
     _input.input3 = input(quiz[2])
     _input.input4 = input(quiz[3])
     _input.input5 = input(quiz[4])


def main():
    if _input.input1 == 'b':
        print (Career[0])
     
    
    if _input.input2 == "a":
        print (Career[1])
    

    if _input.input3 == "b":
        print (Career[2])   
    

    if _input.input4 == "a":
        print (Career[3])
    
    if _input.input5 == "b":
        print (Career[4])
    else:
        print("Try again")
        
        
        
_input()        
input("press 'ENTER' to view your suitable career")
main()





   



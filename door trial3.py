from datetime import datetime

date = datetime.today()
open_door = "open"
close_door = "close"
_quit = "quit"


pass_word = "12345"


def main():
        _input = input("Type in your command")

        if _input==open_door:
            x = input("Type in your password")
                        
            while x!= pass_word:
              print("wrong password. Try again")
              x = input("Type in your password")
            print("door is now open")
            print("Door last open at:" + str(date))
            
            
            _input2 = input("what do you want to do?")
            while _input2 == open_door:
                print("the door is already open")            
                _input2 = input("what else do you wish to do?")
                
            logic()            
            

        elif _input == close_door:
                print("door is now locked")
                print("Door last open at:" + str(date))
                
                input4 = input("what else do wish to do?")
                while input4 == close_door:
                     print("the door is already closed")            
                     input4 = input("what else do you wish to do?")

                main()
                 
        elif _input == _quit:
                print("End of process")
                                 
                
        else:
            print("Invalid command")
            main()
                     
def logic():
        _input3 = input("Type in your command?")

        if _input3 == close_door:
            print("door is now locked")
            print("Door last open at:" + str(date))
            main()
            
        if _input3 == open_door:
            print("door is now open")
            print("Door last open at:" + str(date))
            main()                
        elif  _input3 == _quit:
            print("End of process")
        elif (_input3 != _quit):
             print("Invalid command")
             main()
        elif(_input3 != open_door):
             print("Invalid command")
             main()      
        elif(_input3 != close_door):
            print("Invalid command")    
            main()             
    
print("welcome to this door")
main()



    



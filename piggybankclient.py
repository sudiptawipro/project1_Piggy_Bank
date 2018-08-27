
# coding: utf-8

# In[8]:

import piggybank as pg

class piggybankclient:
    def main():
        obj=pg.piggybank()
        nm=input("Hi Kid, what's your name ? ")
        obj.setname(nm)
        print("Thank you !! Piggybank has set your name as " + nm )
        
        while(1):
            start_end=input("Start or End? ")
            
            if start_end.lower() == 'start':
                step=input(obj.getname() + ", would you like to Add, Withdraw or Check? ")

                if step.lower() =='add':
                    add_amt = input("Add amount : ")
                    obj.add(int(add_amt))
                    bal=obj.check_balance()
                    print(obj.getname() + ", after adding, your updated balance is: Rs.",bal)

                elif step.lower() =='withdraw':
                    with_amt=input("Withdraw amount : ")
                    obj.takeout(int(with_amt))
                    bal=obj.check_balance()
                    print(obj.getname() + ", after withdraw, your updated balance is: Rs.",bal)

                elif step.lower() =='check':
                    bal=obj.check_balance()
                    print(obj.getname() + ", your current balance is: Rs.",bal)
                
                else:
                    print("Incorrect Entry {}".format(step))
                    print("Try - Add, Withdraw OR Check.")

            elif start_end.lower() == 'end':
                print("Exiting application..Thank you " + obj.getname() + '!')
                break
                
            else:
                print("Incorrect Entry {}: ".format(start_end))
                print("Try - Start OR End.")
                
    if __name__ == '__main__':
        main()
    


# In[ ]:




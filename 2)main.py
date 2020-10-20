#!/usr/bin/env python
# coding: utf-8

# In[1]:



from dehelper import DBHelper

def main():
    
    db = DBHelper()
    
          
   
    while True:
        print("***********WELCOME**********")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to exit program")
        print()
        
        try:
            choice = int(input())
            if(choice==1):
                uid = int(input("Enter User ID: "))
                username = (input("Enter User Name: "))
                userphone = (input("Enter User Phone: "))
                db.insert_user(uid,username,userphone)
                
            elif choice==2:
                db.fetch_all()
                
            elif choice==3:
                uid = int(input("Enter User ID which user you want to delete: "))
                db.delete_user(uid)
                
            elif choice==4:
                uid = int(input("Enter User ID of user which you want to update: "))
                username = (input("Enter New Name: "))
                userphone = (input("Enter New Phone: "))
                db.update_user(uid,username,userphone)
                
            elif choice==5:
                break
            else:
                print("Invalid Input. Please Try Again.")                
                
        except Exception as e:
            print(e)
            print("Invalid Details. Please enter correct details")
            
        


            
if __name__ =="__main__":
    main()
    
                
 
    
        
        
        

#helper = DBHelper()
#helper.insert_user(1452,"Monica","23525")
#helper.insert_user(1453,"Charmy","23543")
#helper.insert_user(1454,"Shraddha","56789")
#helper.insert_user(1455,"Madhavi","12390")
#helper.fetch_all()
#helper.delete_user(56789)
#helper.fetch_all()
#helper.update_user(1452,'Ankit','12380904')
#helper.fetch_all()


# In[ ]:





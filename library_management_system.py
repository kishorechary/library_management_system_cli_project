# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:50:59 2026

@author: KISHORE
"""

#library management system 

Books=[]

def add_book():
    name=input("enter the name of book")
    
    try:
        issued=input("enter the issue : ")
    except:
        print("invalid issue  enter true or false.")
        return
    
    book={"name":name, "issued":issued}
    Books.append(book)
    
    print("added successfully!")


def show_book():
    if len(Books)==0:
        print("no books found!")
        return
    
    print("Book list!")
    for i,b in enumerate(Books,start=1):
        print(i,b)
        
def search_book():
    name=input("enter the name of book: ")
    
    found=False
    for i in Books:
        if i["name"].lower()==name.lower():
            print(f"found! {i['name']} - issued :{i['issued']}")
            found=True
            
    if not found:
        print("book not found!")


def delete_book():
    name=input("enter the name if the book: ")
    
    for i in Books:
        if i["name"].lower()== name.lower():
            Books.remove(i)
            print("book deleted!")
            return
        
    print("book not found!")
    
    
def issued_book():
    name=input("enter the name of book: ")
    
    found=False
    print("book issued!")
    for i in Books:
        if i["name"].lower()==name.lower():
            print(f"found! {i['name']} - issued :{i['issued']}")
            found=True
            
    if not found:
        print("book not issued")
        

def update_book():
    name=input("enter the name of the book : ")
    
    for i in Books:
        if i["name"].lower() == name.lower():
            try:
                new_issued = input("Enter new issue: ")
                i["issued"] = new_issued
                print("✏️ issued updated successfully\n")
            except:
                print("Invalid input!\n")
            return
    
    print("book not found\n")
    


while True:
    print("-- library management system!")
    print("1. Add book")
    print("2. Show book")
    print("3. Search book")
    print("4. Delete book")
    print("5. issued book")
    print("6. Update book")     
    print("7. Exit")
    
    choice=int(input("enter the choice: "))
    
    if choice==1:
        add_book()
    elif choice==2:
        show_book()
    elif choice==3:
        search_book()
    elif choice==4:
        delete_book()
    elif choice==5:
        issued_book()
    elif choice==6:
        update_book()
    elif choice==7:
        print("existing program!")
        break
    else:
        print("invaild number")


 


   
        
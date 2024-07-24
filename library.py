import pandas  as pd
import matplotlib.pyplot as plt
from datetime import date


print("----------------------LIBRARY MANAGEMENT SYSTEM----------------------")

def addNewBook():
 bookid = int(input("Enter a book id : "))
 title = input("Enter book title : ")
 author = input("Enter author of the book : ")
 publisher = input("Enter book  publisher : ")
 edition = input("Enter edition of book : ")
 cost = int(input("Enter cost of the book : "))
 category = input("Enter category of book : ")
 bdf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\book.csv")
 n = bdf["bookid"].count()
 bdf.at[n] = [bookid,title,author,publisher,edition,cost,category]
 bdf.to_csv(r"C:\Users\User\Desktop\Library Management System\book.csv", index = False)
 print("Book added successfully")
 print(bdf)


def searchBook():
    title = input("Enter a book name : ")
    bdf=pd.read_csv(r"C:\Users\User\Desktop\Library Management System\book.csv")
    df=bdf.loc[bdf["title"]==title]
    if df.empty:
        print("No book found with given code")
    else:
        print("Book details are :")
        print(df)


def deleteBook():
    bookid = float(input("Enter a book id : "))
    bdf=pd.read_csv(r"C:\Users\User\Desktop\Library Management System\book.csv")
    bdf=bdf.drop(bdf[bdf["bookid"]==bookid].index)
    bdf.to_csv(r"C:\Users\User\Desktop\Library Management System\book.csv", index= False)
    print("Book Deleted Successfully")
    print(bdf)


def showBooks():
    bdf=pd.read_csv(r"C:\Users\User\Desktop\Library Management System\book.csv")
    print(bdf)


def addNewMember():
    mid = int(input("Enter a member id : "))
    mname = input("Enter member name : ")
    phoneno = int(input("Enter phone number : "))
    numberofbooksissued=0
    mdf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\member.csv")
    n = mdf["mid"].count()
    mdf.at[n] = [mid,mname,phoneno,numberofbooksissued]
    mdf.to_csv(r"C:\Users\User\Desktop\Library Management System\member.csv",index = False)
    print("New Member added successfully")
    print(mdf)


def searchMember():
    mname = input("Enter a member name : ")
    bdf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\member.csv")
    df = bdf.loc[bdf["m_name"]== mname]
    if df.empty:
        print("No memberfound with given name")
    else:
        print("Members details are : ")
        print(df)


def deleteMember():
    mid = float(input("Enter a member id : "))
    bdf=pd.read_csv(r"C:\Users\User\Desktop\Library Management System\member.csv")
    bdf=bdf.drop(bdf[bdf["mid"]== mid].index)
    bdf.to_csv(r"C:\Users\User\Desktop\Library Management System\member.csv", index= False)
    print("Member Deleted Successfully")
    print(bdf)


def showMembers():
    bdf=pd.read_csv(r"C:\Users\User\Desktop\Library Management System\member.csv")
    print(bdf)


def issueBooks():
    book_name = input("Enter book name : ")
    bdf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\book.csv")
    bdf = bdf.loc[bdf["title"] == book_name]
    if bdf.empty:
        print("No Book Found in the Library")
        return


    m_name = input("Enter member name : ")
    mdf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\member.csv")
    mdf = mdf.loc[mdf["m_name"] == m_name]
    if mdf.empty:
        print("No such Member Found")
        return


    dateofissue = int(input("Enter date of issue : "))
    numberofbookissued = int(input("Enter number of book issued : "))
    bdf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv")
    n = bdf["book_name"].count()
    bdf.at[n] = [book_name,m_name,date.today(),numberofbookissued,""]
    bdf.to_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv", index=False)
    print("Book issued successfully")
    print(bdf)


def returnBook():
    m_name = input("Enter a member name : ")
    book_name = input("Enter book name : ")
    idf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv")
    idf = idf.loc[idf["book_name"] == book_name]
    if idf.empty:
        print("The book is not issued in records")
    else:
        idf = idf.loc[idf["m_name"] == m_name]
        if idf.empty:
            print("The book is not issued to the member")
        else:
            print("Book can be returned")
            ans = input("Are you sure you want to return the book : ")
            if ans.lower() == "yes":
                idf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv")
                idf = idf.drop(idf[idf["book_name"] == book_name].index)
                idf.to_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv", index=False)
                print("Book Returned Successfully")
            else:
                print("Return operation cancelled")


def showissuedBooks():
    idf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv")
    print(idf)


def deleteissuedBooks():
    book_name = input("Enter a book name : ")
    bdf = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv")
    bdf = bdf.drop(bdf[bdf["book_name"] == book_name].index)
    bdf.to_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv", index = False)
    print("Deleted Issued Book Successfully")
    print(bdf)


def showCharts():
    print("Press 1 - Books and their Cost")
    print("Press 2 - Number of Books issued by members")
    ch = int(input("Enter your choice : "))
    if ch == 1:
        df = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\book.csv")
        df = df[["title","cost"]]
        df.plot("title","cost",kind="bar")
        plt.xlabel('title------->')
        plt.ylabel('cost------->')
        plt.show()

    if ch == 2:
        df = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\issuebooks.csv")
        df = df[["numberofbookissued","m_name"]]
        df.plot(kind='bar', color="red")
        plt.show()


def login():
    uname = input("Enter Username : ")
    pwd = input("Enter Password : ")
    df = pd.read_csv(r"C:\Users\User\Desktop\Library Management System\users.csv")
    df = df.loc[df["username"] == uname]
    if df.empty:
        print("Invaild username given")
        return False
    else:
        df = df.loc[df["password"] == pwd]
        if df.empty:
            print("Invaild Password")
            return False
        else:
            print("Username and Password matched successfully")
            return True


def showMenu():
    print("-----------------------------------------------------------------------")
    print("                      LIBRARY MANAGEMENT SYSTEM                        ")
    print("-----------------------------------------------------------------------")
    print("Press 1 - Add a New Book")
    print("Press 2 - Search for a Book")
    print("Press 3 - Delete a Book")
    print("Press 4 - Show All Book")
    print("Press 5 - Add a New Member")
    print("Press 6 - Search for a Member")
    print("Press 7 - Delete a Member")
    print("Press 8 - Show All Members")
    print("Press 9 - Issue a Book")
    print("Press 10 - Return a Book")
    print("Press 11 - Show All Issued Books")
    print("Press 12 - Delete a Issue a Book")
    print("Press 13 - To view Charts")
    print("Press 14 - To exit")
    choice = int(input("Enter your choice : "))
    return choice
if login():
    while True:
        ch = showMenu()
        if ch == 1:
            addNewBook()
        elif ch == 2:
            searchBook()
        elif ch == 3:
            deleteBook()
        elif ch == 4:
            showBooks()
        elif ch == 5:
            addNewMember()
        elif ch == 6:
            searchMember()
        elif ch == 7:
            deleteMember()
        elif ch == 8:
            showMembers()
        elif ch == 9:
            issueBooks()
        elif ch == 10:
            returnBook()
        elif ch == 11:
            showissuedBooks()
        elif ch == 12:
            deleteissuedBooks()
        elif ch == 13:
            showCharts()

        elif ch == 14:
            break
        else:
            print("Invaild Option Selected")

print("THANK YOU FOR VISITING THE LIBRARY")            

            
    
            
                 
          
    
          
        
        
            
        
    
    



                
   
    
    
                      
    
    
            

    
    


    
    
    

 
    

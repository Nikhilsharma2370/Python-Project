class Library:
    def __init__(self,listofbook):
        self.book = listofbook

    def display(self):
        print("Books are persent in library are: ")
        for i in self.book:

            print(f"\t *{i}")

    def barrow(self,bookname):
        if bookname in self.book:
            print(f"You have been issued {bookname}.Please keep it safe")
            self.book.remove(bookname)
            return True
        else:
            print("This book not available")
            return False
    
    def returnbook(self,bookname):
        self.book.append(bookname)
        print("Thanks for returning this book! Hope you enjoy reading it")


class Student:
    def requestBook(self):
        self.book = input("Enter your book name:  ")
        return self.book
    
    def returnbooks(self):
        self.book = input("Enter your book name:  ")
        return self.book


if __name__ == "__main__":
    ns = Library(["python","java","Php","css"])
    student = Student()
    # ns.display()

    while(True):
        print(f''' ===Welcome to Central Library===
             1. Show Books Names
             2. Request a book
             3. Add/ Return a book
             4. Exit the Library   
             ''')
        a = int(input("Enter your Choise: "))
        if a == 1:
            ns.display()
        elif a == 2:
            ns.barrow(student.requestBook())
        elif a == 3:
            ns.returnbook(student.returnbooks())
        elif a== 4:
            print("Thanks for choosing Central library. Have a great day a head")
            exit()
        else:
            print("Invalid choice")
            
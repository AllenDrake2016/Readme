#author: Zihang Huang
#decription: a generic Publication class -- meant to be inherited

from Html_Form import*

class Book(Publication):

    def __init__(self,title,pages,author):
        Publication.__init__(self,title,pages)
        self.author=author

    def get(self):
        return self.author

    def set(self,author):
        self.author=author
        return self.author


    def __str__(self):
        return "Book:"+"\n\t title:"+ str(self.get_title())+\
            "\n\t pages:"+str(self.get_pages())+\
            "\n\t author:"+str(self.set(465))
            # "\n\t author:"+self.get()
            #"\n\t author:"+self.__author

    def class_print(self,author):
        print(Book.set(author))
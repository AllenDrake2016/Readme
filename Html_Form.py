class Publication:

    def __init__(self,title,pages):
        self.__title=title
        self.__pages=pages

    def get_title(self):
        return self.__title

    def set_title(self,title):
        self.__title=title

    def get_pages(self):
        return self.__pages

    def set_pages(self,pages):
        self.__pages=pages

    def __str__(self):
        return "Publication:"+"\n\t title:"+self.__title+\
            "\n\t pages:"+str(self.get_pages())
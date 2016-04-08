class Movie:


    def __init__(self,title,year,director):
        self.__title=title
        self.__year=year
        self.__director=director

    def get_title(self):
        return self.__title

    def set_title(self,title):
        self.__title=title

    def get_year (self):
        return self.__year

    def set_year(self,year):
        self.__year=year

    def get_director(self):
        return self.__director

    def set_director(self,director):
        self.__director=director


    def __str__(self):
        return "Movie"+"\n\t Title:" + self.get_title() +"\n\t Year:" + str(self.get_year()) +"\n\t Director:" +self.get_director()

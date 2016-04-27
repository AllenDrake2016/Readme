# author: (Zihang Huang)
# date: 4/3/2016
# description: List and Loop assignment
# proposed points (out of 20): 20, I think I deserve 20 points since
#                              I have done all the additional requirements.



def main():
    ratings_matrix = []
    books = []
    myratings=[]
    name=[]

# read in data for name
    infile = open("names.txt", "r")
    for line in infile:
        data = line.rstrip("\n")
        list = data.split()
        name.append(list)
    infile.close()


# read in data for my rating
    infile = open("MyRating.txt", "w")
    infile.close()
    infile = open("MyRating.txt", "r")
    for line in infile:
        data = line.rstrip("\n")
        list = data.split()
        myratings.append(list)
    infile.close()


# read in data for ratings matrix
    infile = open("bookRatings.txt", "r")
    for line in infile:
        data = line.rstrip("\n")
        list = data.split()
        ratings_matrix.append(list)
    infile.close()

# read in book titles
    infile = open("books.txt", "r")
    for line in infile:
        data = line.rstrip("\n")
        books.append(data)
    infile.close()

# initialize variables
    max_book_sum = 0
    max_book_index = 0


    # go through all of the books
    for book in range(55):
        sum_of_ratings = 0


        # consider all of the person ratings
        for person in range(86):
            sum_of_ratings += int(ratings_matrix[person][book])

        # insert code here to determine maximum book
        if sum_of_ratings>max_book_sum:
            max_book_sum=sum_of_ratings
            max_book_index=book
    print("The most popular book")
    print("Value:",max_book_sum, "Index Number:",max_book_index+1)
    print(books[max_book_index])
    print()

# initialize variables
    min_book_sum = 0
    min_book_index = 0


    # go through all of the books
    for book in range(55):
        sum_of_ratings = 0


        # consider all of the person ratings
        for person in range(86):
            sum_of_ratings += int(ratings_matrix[person][book])

        # insert code here to determine minimum book
        if sum_of_ratings<min_book_sum:
            min_book_sum=sum_of_ratings
            min_book_index=book
    print("The least favorite book")
    print("Value:",min_book_sum, "Index number:",min_book_index+1)
    print(books[min_book_index])
    print()


# find compatibility with person

    max_score=0
    max_person_index=0

    for person_index in range(86):
        score=0

        for book in range(55):
            score+=int(ratings_matrix[person_index][book])

        # insert code here to determine maximum book
        if score>max_score:
            max_score=score
            max_person_index=person_index

    print("The best person match my rating is",name[max_person_index])
    print("Person Index number:",max_person_index+1)
    print()

# Recommended Books
    print("Books recommended to read:")
    for book in range(55):
        if int(ratings_matrix[max_person_index][book])==5:
            print(books[book])


main()

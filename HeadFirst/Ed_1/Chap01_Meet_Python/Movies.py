def printList1(movie_list):
    for each_item in movie_list:
        print(each_item)


def printList2(movie_list):
    for each_item in movie_list:
        if isinstance(each_item, list):
            for nested_item in each_item:
                print(nested_item)
        else:
            print(each_item)


def printList3(movie_list):
    for each_item in movie_list:
        if isinstance(each_item, list):
            for nested_item in each_item:
                if isinstance(nested_item, list):
                    for deeper_item in nested_item:
                        print(deeper_item)
                else:
                    print(nested_item)
        else:
            print(each_item)


def printList4(movie_list):
    for each_item in movie_list:
        if isinstance(each_item, list):
            printList4(each_item)
        else:
            print(each_item)


if __name__ == '__main__':
    movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]

    # insert the first year
    # Solution 1
    movies.insert(1, 1975)
    movies.insert(3, 1979)
    movies.append(1983)
    print(f"Solution 1: {movies}\n")

    # Solution 2
    movies = ["The Holy Grail", 1975, "The Life of Brian", 1979, "The Meaning of Life", 1983]
    print(f"Solution 2: {movies}\n")

    # For loop
    fav_movies = ["The Holy Grail", "The Life of Brian"]
    # print(fav_movies[0])
    # print(fav_movies[1])
    for each_flick in fav_movies:
        print(each_flick)

    # Print lists
    movies = [
        "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
        ["Graham Chapman",
         ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]
    print("\n=== Print list 1 ===")
    printList1(movies)
    print("\n=== Print list 2 ===")
    printList2(movies)
    print("\n=== Print list 3 ===")
    printList3(movies)
    print("\n=== Print list 4 : Recursive ===")
    printList4(movies)

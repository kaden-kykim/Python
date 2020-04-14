if __name__ == '__main__':
    cast = ["Cleese", 'Palin', 'Jones', "Idle"]
    print(f"Cast: {cast}")
    print(f"Length: {len(cast)}")
    print(f"Cast[1]: {cast[1]}\n")

    cast.append("Gilliam")
    print(f"Cast after append: {cast}")

    popItem = cast.pop()
    print(f"Cast after pop: {cast}")
    print(f"Pop item: {popItem}")

    extendItem = ["Gilliam", "Chapman"]
    cast.extend(extendItem)
    print(f"Cast after extend '{extendItem}': {cast}")

    removeItem = "Chapman"
    cast.remove(removeItem)
    print(f"Cast after remove '{removeItem}': {cast}")

    insertItem = removeItem
    cast.insert(0, insertItem)
    print(f"Cast after insert '{insertItem}' at index 0: {cast}")


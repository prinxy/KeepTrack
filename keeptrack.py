class Item:

    room = []

    def __init__(self, item_name):
        self.item_name = item_name

    def additem(self, item_name):
        item_location = str.lower(input("Location: "))
        Creation.location(item_location)

        userinput = str.lower(input("Add more? y/n "))

        if userinput == "y":
            Creation.object()

        elif userinput == "n":
            main()

        else:
            print("Wrong Selection")
            main()

    def removeitem():
        pass

        # print(Item.room)  # check
        # item_name = str.lower(input("Input name of item: "))
        # item_location = str.lower(input("Location: "))
        # userdata = open("locations.txt", "r")
        # userdata.read()
        # # with open(filename) as myFile:

        # else:
        #     print("Item does not exist")
        #     Item.removeitem()

    def removelocation():
        userinput = str.lower(input("Location: "))
        if userinput in Item.room:
            Item.room.pop(userinput)
            print(Item.room)
            main()

        elif userinput not in Item.room:
            print("Location does not exist")
            main()

    @staticmethod
    def viewitems():
        # print(Item.room)
        # print(Item.room) # check
        main()

    @staticmethod
    def viewlocations():
        with open("locations.txt", "r") as userdata:
            locations = userdata.readlines()
            locations = [x.strip() for x in locations]
            for location in locations:
                print(location[:-2])

        main()


class Creation():

    def object():  # Object should have 2 values, name and location
        item_name = str.lower(input("Item name: "))
        item = Item(item_name)
        item.additem(item_name)

    def location(item_location):
        # item_location = str.lower(input("New Location: "))
        if item_location in Item.room:
            print("In room")

        elif item_location not in Item.room:
            pass
            # Item.room.append(item_location)
            # location_index = Item.room.index(item_location)
            # print(location_index)
            # with open("locations.txt", "a") as userlocations:
            #     userdata.write("{}-{} \n".format(location_index, ))
            #     userdata.close()
        else:
            pass


def main():

    # Check file for data and conditionalize as needed
    if Item.room == []:
        with open("locations.txt", "r") as userdata:
            locations = userdata.readlines()
            locations = [x.strip() for x in locations]
            print(locations)

    print("""
    (A)dd (I)tem, (A)dd (L)ocation, (R)emove (I)tem, (R)emove (L)ocation
    (V)iew (I)tems or (V)iew (L)ocations
    """)

    userinput = str.lower(input("Enter Selection: "))

    if userinput == "ai":
        Creation.object()

    elif userinput == "ri":
        Item.removeitem()

    elif userinput == "rl":
        Item.removelocation()

    elif userinput == "vi":
        Item.viewitems()

    elif userinput == "vl":
        Item.viewlocations()

    elif userinput == "al":
        item_location = str.lower(input("Location: "))
        Creation.location(item_location)

    else:
        print("Wrong selection")
        main()


if __name__ == '__main__':
    main()

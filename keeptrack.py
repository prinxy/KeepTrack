# Import Modules
import sys


class Thing:

    room = []  # create empty list named room

    # initilize object creation values
    def __init__(self, thing_name):
        self.thing_name = thing_name

    def add_thing(self, thing_name):
        thing_place = str.lower(input("Place: "))
        Creation.item_with_location(thing_name, thing_place)

        user_input = str.lower(input("Add more? y/n "))

        if user_input == "y":
            Creation.thing()

        elif user_input == "n":
            main()

        else:
            print("Wrong Selection")
            main()

    def remove_thing():
        pass
        # print(Item.room)  # check
        # item_name = str.lower(input("Input name of item: "))
        # item_place = str.lower(input("place: "))
        # userdata = open("places.txt", "r")
        # userdata.read()
        # # with open(filename) as myFile:

        # else:
        #     print("Item does not exist")
        #     Item.remove_item()

    def remove_place():
        pass
        # user_input = str.lower(input("Place: "))
        # if user_input in Thing.room:
        #     # place_index = Thing.room.index(user_input)
        #     Thing.room.remove(user_input)
        #     # remove_thing()
        #     with open("things.txt", "r") as load_things:
        #         things = load_things.readlines()
        #         thing = [thing.strip() for thing in things]
        #         # if place_index in thing:
        #     print(Thing.room)
        #     main()
        #
        # elif user_input not in Thing.room:
        #     print("place does not exist")
        #     main()

    @staticmethod
    def view_things():
        with open("things.txt", "r") as load_things:
            things = load_things.readlines()
            thing = [thing.strip() for thing in things]
            print(thing)
            for each_thing in thing:
                for i in range(len(Thing.room)):

                    if each_thing[-1] == '{}'.format(i):
                        print("{} belongs"
                              + "to {}".format(each_thing, Thing.room[i]))

        main()

    @staticmethod
    def view_places():
        print(Thing.room)
        main()


class Creation():

    def thing():  # Object should have 2 values, name and place
        thing_name = str.lower(input("Thing name: "))
        thing = Thing(thing_name)
        thing.add_thing(thing_name)

    def place(thing_place):
        # item_place = str.lower(input("New place: "))
        if thing_place in Thing.room:
            print("In room")

        elif thing_place not in Thing.room:
            Thing.room.append(thing_place)
            place_index = Thing.room.index(thing_place)
            print(place_index)
            with open("places.txt", "a") as user_places:
                user_places.write("{}-{}\n".format(thing_place, place_index))
            return

        else:
            pass

    def item_with_location(thing_name, thing_place):
        if thing_place in Thing.room:
            place_index = Thing.room.index(thing_place)
            print(place_index)
            with open("things.txt", "a") as user_things:
                user_things.write("{}-{}\n".format(thing_name, place_index))

        elif thing_place not in Thing.room:
            Creation.place(thing_place)
            place_index = Thing.room.index(thing_place)
            with open("things.txt", 'a') as user_things:
                user_things.write("{}-{}\n".format(thing_name, place_index))

        else:
            pass


def main():

    # Check file for data and conditionalize as needed
    if Thing.room == []:
        with open("places.txt", "r") as load_places:
            places = load_places.readlines()
            for place in places:
                Thing.room.append(place[:-3])
            print(Thing.room)

            # we now have a list named room having places as values
        #
        # with open("things.txt", "r") as load_things:
        #     things = load_things.readlines()
        #     thing = [thing.strip() for thing in things]
        #     # the_things = things.split('\n')
        # print(thing)
        # # print(thing[1])
        # # total_places = len(Thing.room)
        # for each_thing in thing:
        #     for i in range(len(Thing.room)):
        #
        #         if each_thing[-1] == '{}'.format(i):
        #             print("{} belongs"
        #                   + "to {}".format(each_thing, Thing.room[i]))

    print("""
1. Add Things
2. Remove Things
3. View Things
4. Add Places
5. Remove Places
6. View Places
7. Exit
    """)

    user_input = str(input("Enter Selection: "))

    if user_input == '1':
        Creation.thing()

    elif user_input == '2':
        Thing.remove_thing()

    elif user_input == '3':
        Thing.view_things()

    elif user_input == '4':
        thing_place = str.lower(input("Place: "))
        Creation.place(thing_place)
        main()

    elif user_input == '5':
        Thing.remove_place()

    elif user_input == '6':
        Thing.view_places()

    elif user_input == '7':
        # pass
        # Add save file method and the end bro
        sys.exit()

    else:
        print("Wrong selection")
        main()


if __name__ == '__main__':
    main()

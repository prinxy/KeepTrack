# Import Modules
import sys


class Thing:

    room = []  # create empty list named room
    user_items = []
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
        to_remove = str.lower(input("To remove: "))
        if to_remove in Thing.user_items:
            the_index = Thing.user_items.index(to_remove)
            Thing.user_items.pop(the_index)
            main()
        else:
            pass

    def remove_place():
        user_input = str.lower(input("Place: "))
        if user_input in Thing.room:
            place_index = Thing.room.index(user_input)
            Thing.room.pop(place_index)
            with open("places.txt", "r") as load_things:
                things = load_things.readlines()
                thing = [thing.strip() for thing in things]
                print(thing)

    @staticmethod
    def view_things():
        print(Thing.user_items)
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
            Thing.user_items[place_index].append(thing_name)
            print(Thing.room)
            print(Thing.user_items)
            # place_index = Thing.room.index(thing_place)
            # print(place_index)
            # with open("things.txt", "a") as user_things:
            #     user_things.write("{}-{}\n".format(thing_name, place_index))

        elif thing_place not in Thing.room:
            # Append the place to list room
            Thing.room.append(thing_place)
            place_index = Thing.room.index(thing_place)
            try:
                Thing.user_items[place_index].append(thing_name)
            except IndexError:
                Thing.user_items.insert(place_index, [])
                Thing.user_items[place_index].append(thing_name)
            print(Thing.room)
            print(Thing.user_items)

            # Creation.place(thing_place)
            # place_index = Thing.room.index(thing_place)

        else:
            pass


def main():

    # Check file for data and conditionalize as needed
    if Thing.room == [] and Thing.user_items == []:
        with open("places.txt", "r") as load_places:
            places = load_places.readlines()
            for place in places:
                Thing.room.append(place[:-3])
            print(Thing.room)

            # we now have a list named room having places as values

        with open("things.txt", "r") as load_things:
            the_things = load_things.readlines()
            thing = [thing.strip() for thing in the_things]
            for i in range(len(Thing.room)):
                Thing.user_items.insert(i, [])
                for each_thing in thing:
                    print('{}'.format(each_thing[-1]))
                    if each_thing[-1] == '{}'.format(i):
                        Thing.user_items[i].append(each_thing[:-2])
            print(Thing.user_items)

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
        with open("places.txt", 'w') as place_in_file:
            for each_place in Thing.room:
                place_index = Thing.room.index(each_place)
                place_in_file.write("{}-{}\n".format(each_place,
                                                     place_index))

        with open("things.txt", 'w') as thing_to_file:
            for each_thing in Thing.user_items:
                length = len(each_place)
                if length > 0:
                    for one_thing in each_thing:
                        print(one_thing)
                        thing_index = each_thing.index(one_thing)
                        thing_to_file.write("{}-{}\n".format(one_thing,
                                                             thing_index))

                elif length == 0:
                    pass
                else:
                    pass

                sys.exit()

    else:
        print("Wrong selection")
        main()


main()

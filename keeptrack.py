"""DOCSTRING."""
# Import Modules
import pickle
import sys
import os


class Thing:
    """DOCSTRING."""

    room = []  # create empty list named room
    things = []
    # initilize object creation values

    def __init__(self, thing_name):
        self.thing_name = thing_name

    def add_thing(self, thing_name):
        """DOCSTRING."""
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

    @staticmethod
    def remove_thing():
        """DOCSTRING."""
        to_remove = str.lower(input("To remove: "))
        # create a loop that will go through each item
        # or if place is known, get place_index and use it to
        # get the nested list and remove item
        for group_things in Thing.things:
            if to_remove in group_things:
                group_index = Thing.things.index(group_things)
                print(group_index)
                item_index = Thing.things[group_index].index(to_remove)
                print(item_index)
                Thing.things[group_index].pop(item_index)
                break
        else:
            print("Item Does not exist")

        main()

    @staticmethod
    def remove_place():
        """DOCSTRING"""
        user_input = str.lower(input("Place: "))
        if user_input in Thing.room:
            place_index = Thing.room.index(user_input)
            Thing.room.pop(place_index)
            Thing.things.pop(place_index)
            main()

    @staticmethod
    def view_things():
        """DOCSTRING.."""
        # View all
        print(Thing.things)
        main()
        # View all in a place

    @staticmethod
    def view_places():
        """DOCSTRING."""
        for every_place in Thing.room:
            print(every_place)
        # print(Thing.room)
        main()


class Creation():
    """DOCSTRING."""

    @staticmethod
    def thing():
        """DOCSTRING."""
        thing_name = str.lower(input("Thing name: "))
        thing = Thing(thing_name)
        thing.add_thing(thing_name)

    @staticmethod
    def place(thing_place):
        """DOCSTRING."""
        # item_place = str.lower(input("New place: "))
        if thing_place in Thing.room:
            print("In room")

        elif thing_place not in Thing.room:
            Thing.room.append(thing_place)
            place_index = Thing.room.index(thing_place)
            print(place_index)

        else:
            pass

    @staticmethod
    def item_with_location(thing_name, thing_place):
        """
        DOCSTRING.
        """
        if thing_place in Thing.room:
            place_index = Thing.room.index(thing_place)
            try:
                Thing.things[place_index].append(thing_name)
            except IndexError:
                Thing.things.insert(place_index, [])
                Thing.things[place_index].append(thing_name)
            print(Thing.room)
            print(Thing.things)

        elif thing_place not in Thing.room:
            # Append the place to list room
            Thing.room.append(thing_place)
            place_index = Thing.room.index(thing_place)
            try:
                Thing.things[place_index].append(thing_name)
            except IndexError:
                Thing.things.insert(place_index, [])
                Thing.things[place_index].append(thing_name)
            print(Thing.room)
            print(Thing.things)

            # Creation.place(thing_place)
            # place_index = Thing.room.index(thing_place)

        else:
            pass


class FileOperations:
    """DOCSTRING.."""

    places_path = "places.txt"
    things_path = "things.txt"

    @staticmethod
    def fetch_places():
        """DOCSTRING."""

        with open("places.txt", "rb") as load_places:
            try:
                Thing.room = pickle.load(load_places)
                print(Thing.room)
            except EOFError:
                pass

    @staticmethod
    def fetch_things():
        """DOCSTRING."""
        with open("things.txt", "rb") as load_things:
            Thing.things = pickle.load(load_things)
            print(Thing.things)

    @staticmethod
    def save_places():
        """DOCSTRING."""
        with open("places.txt", 'wb') as place_in_file:
            pickle.dump(Thing.room, place_in_file)

    @staticmethod
    def save_things():
        """DOCSTRING."""
        with open("things.txt", 'wb') as thing_to_file:
            pickle.dump(Thing.things, thing_to_file)

    @staticmethod
    def reset_files():
        """DOCSTRING."""
        pass
        # with open("places.txt", 'w'):
        #     pass
        # with open("things.txt", 'w'):
        #     pass
        # main()


def main():
    """DOCSTRING."""

    print("""
1. Add Things
2. Remove Things
3. View Things
4. Add Places
5. Remove Places
6. View Places
7. Reset
8. Exit
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
        Thing.room = []
        Thing.things = []
        FileOperations.reset_files()
        main()

    elif user_input == '8':
        FileOperations.save_places()
        FileOperations.save_things()
        sys.exit()

    else:
        print("Wrong selection")
        main()


if os.path.getsize(FileOperations.places_path
                   and FileOperations.things_path) > 0:
    if Thing.room == [] and Thing.things == []:
        FileOperations.fetch_places()
        FileOperations.fetch_things()

main()

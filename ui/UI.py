from controller.controller import Controller
from entities.exception import ScrambleException


class UI:
    def __init__(self):
        self.__controller = Controller("repository/input.txt")

    def run(self):
        while self.__controller.dead() == True:
            try:
                print(self.__controller.list_scramble())
                cmd = input("Please insert command: ").split()
                if not cmd:
                    print("Error!!! Please insert command!!!\n")
                elif cmd[0] == "undo":
                    self.__controller.undo()
                elif cmd[0] == "swap":
                    if len(cmd) != 6:
                        print("Error!!! Please insert a valid command!!! swap word_1 letter_1 - word_2 letter_2\n")
                    else:
                        self.__controller.swap(int(cmd[1]), int(cmd[2]), int(cmd[4]), int(cmd[5]))
                else:
                    print("Error!!! Invalid command!!! It must be either undo or swap!!!\n")
            except ValueError:
                print("Error!!! Invalid types for swap!!!\n")
            except ScrambleException as ex:
                print(ex)
        print(self.__controller.dead())

from random import randint

from entities.exception import ScrambleException
from entities.sentence import Sentence


class Repository:
    def __init__(self, filename):
        """
        Initialize the repository with the filename where the program is supposed to read the sentences
        :param filename:
        """
        self.__filename = filename
        self.__elements = []
        self.__load()

    def __load(self):
        """
        Load all the sentances from the file into the list of elements
        :return:
        """
        try:
            file = open(self.__filename, "r")  # open the file in read mode
            for line in file:  # take line by line
                self.__elements.append(Sentence(line.strip("\n")))  # edit the sentence and append as a Sentence object
            file.close()
        except IOError:  # if we have a file opening error we pass it to the upper layers
            raise ScrambleException("Error opening the data file!!!\n")

    def get_scramble(self):
        """
        Returns a randomly picked sentence object from the list of sentences
        :return:
        """
        return self.__elements[randint(0, len(self.__elements) - 1)]

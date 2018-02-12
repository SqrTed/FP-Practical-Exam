from entities.exception import ScrambleException
from repository.repository import Repository
from validation.validator import Validator


class ControllerException(ScrambleException):
    pass


class Controller:
    def __init__(self, filename):
        """
        Initializing the controller
        :param filename:
        """
        self.__repo = Repository(filename)  # initialize the repository with the filename
        self.__validator = Validator()  # initialize the validator for checking if the input is ok
        self.__scramble = self.__repo.get_scramble()  # getting the randomly picked sentence from repo
        self.__undo = None

    def dead(self):
        """
        Check if it is either a win, lose or we can't decide yet
        :return:
        """
        if self.__scramble.score == 0:  # if the score is 0 it's a lose
            return "You Lose!"
        elif self.__scramble.sentance == self.__scramble.scramble:  # if the scramble sentence is solved it's a win
            return "You Win!"
        else:
            return True  # otherwise we cant decide yet

    def swap(self, word_1, letter_1, word_2, letter_2):
        """
        Swapping the letters
        :param word_1:
        :param letter_1:
        :param word_2:
        :param letter_2:
        :return:
        """
        self.__validator.validate_swap(word_1, letter_1, word_2, letter_2,
                                       self.__scramble.id)  # check if the input is correct
        self.__scramble.swap(word_1, letter_1, word_2,
                             letter_2)  # swap the elements using the swap function from the Sentence class
        self.__scramble.dec_score(1)  # decrease the score by one
        self.__undo = [word_1, letter_1, word_2, letter_2]  # add the move to undo

    def undo(self):
        """
        Undo the last operation
        :return:
        """
        if self.__undo is None:  # if we can not undo anymore we raise an error
            raise ControllerException("Error!!! Can't undo anymore!!!\n")
        else:  # otherwise we simply do the swap from the undo list once more
            self.__scramble.swap(self.__undo[0], self.__undo[1], self.__undo[2], self.__undo[3])
            # self.__scramble.inc()
            self.__undo = None  # undo becomes None because we don't want the user to do multiple undo operations

    def list_scramble(self):
        """
        Returns the str of the self.__scramble object for printing
        :return:
        """
        return str(self.__scramble)

    def _get_scramble(self):
        """
        This functions only purpose is testing for the controller
        :return:
        """
        return self.__scramble

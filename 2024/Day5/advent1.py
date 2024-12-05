
import sys

class Page:
    """
    Class representing a Page with a page number and lists of pages before and after.
    """
    def __init__(self, pageNumber, pagesBefore=None, pagesAfter=None):
        """
        Constructor for the Page class.
        :param pageNumber: The page number.
        :param pagesBefore: List of page numbers that this page shall come before.
        :param pagesAfter: List of page numbers that this page shall come after.
        """
        self.pageNumber = pageNumber
        self.pagesBefore = pagesBefore if pagesBefore else []
        self.pagesAfter = pagesAfter if pagesAfter else []

    def add_pageBefore(self, page):
        """
        Method to add a page number to the list of pages before.
        :param page: The page number to add.
        """
        self.pagesBefore.append(page)

    def add_pageAfter(self, page):
        """
        Method to add a page number to the list of pages after.
        :param page: The page number to add.
        """
        self.pagesAfter.append(page)

    def pretty_print(self):
        """
        Method to print the page number and the list of pages before and after.
        """
        print(f"Page Number: {self.pageNumber}")
        print(f"Pages Before: {', '.join(str(num) for num in self.pagesBefore)}")
        print(f"Pages After: {', '.join(str(num) for num in self.pagesAfter)}")
        print("-"*20)

class Update:
    """
    Class representing an Update with a list of page numbers.
    """
    def __init__(self, pageNumbers=None):
        """
        Constructor for the Update class.
        :param pageNumbers: List of page numbers in the update.
        """
        self.pageNumbers = pageNumbers if pageNumbers else []

    def check_update_order(self, pages):
        """
        Method to check if the order of page numbers in the update is correct.
        :param pages: Dictionary of pages.
        :return: True if the order is correct, False otherwise.
        """
        for pageNumber in self.pageNumbers:
            if pageNumber in pages:
                for pageAfter in pages[pageNumber].pagesAfter:
                    if pageAfter in self.pageNumbers[self.pageNumbers.index(pageNumber):]:
                        return False
        return True

    def extract_middle(self):
        """
        Method to extract the middle page number from the update.
        :return: The middle page number.
        """
        return self.pageNumbers[int(len(self.pageNumbers)/2)]

def parse_file_1(filename):
    """
    Function to parse a file and create a dictionary of pages.
    :param filename: The name of the file to parse.
    :return: Dictionary of pages.
    """
    pages = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == '':
                break
            pageNumber, pageBefore = map(int, line.split('|'))
            if pageNumber not in pages:
                pages[pageNumber] = Page(pageNumber)
            pages[pageNumber].add_pageBefore(pageBefore)

            if pageBefore not in pages:
                pages[pageBefore] = Page(pageBefore)
            pages[pageBefore].add_pageAfter(pageNumber)

    return pages


def parse_file_2(filename):
    """
    Function to parse a file and create a list of updates.
    :param filename: The name of the file to parse.
    :return: List of updates.
    """
    updates = []
    with open(filename, 'r') as file:
        start_reading = False
        for line in file:
            if line.strip() == '':
                start_reading = True
                continue
            if start_reading:
                pageNumbers = list(map(int, line.split(',')))
                updates.append(Update(pageNumbers))
    return updates


if __name__ == "__main__":
    """
    Main function to parse the file, create pages and updates, and print the total count of pages.
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    pages = parse_file_1(filename)
    updates = parse_file_2(filename)

    for update in updates:
        for page in update.pageNumbers:
            if page not in pages:
                pages[page] = Page(page)

    total = 0
    for update in updates:
        if update.check_update_order(pages):
            total += update.extract_middle()

    print(f"Pages count: {total}")


import sys

class Page:
    """
    Class representing a page with its number and the pages before and after it.
    """
    def __init__(self, pageNumber, pagesBefore=None, pagesAfter=None):
        """
        Initialize a Page object.

        Parameters:
        pageNumber (int): The number of the page.
        pagesBefore (list): List of page numbers that come before this page.
        pagesAfter (list): List of page numbers that come after this page.
        """
        self.pageNumber = pageNumber
        self.pagesBefore = pagesBefore if pagesBefore else []
        self.pagesAfter = pagesAfter if pagesAfter else []

    def add_pageBefore(self, page):
        """
        Add a page number to the list of pages before this page.

        Parameters:
        page (int): The page number to add.
        """
        self.pagesBefore.append(page)

    def add_pageAfter(self, page):
        """
        Add a page number to the list of pages after this page.

        Parameters:
        page (int): The page number to add.
        """
        self.pagesAfter.append(page)

    def pretty_print(self):
        """
        Print the page number and the lists of pages before and after this page.
        """
        print(f"Page Number: {self.pageNumber}")
        print(f"Pages Before: {', '.join(str(num) for num in self.pagesBefore)}")
        print(f"Pages After: {', '.join(str(num) for num in self.pagesAfter)}")
        print("-"*20)

class Update:
    """
    Class representing an update with a list of page numbers.
    """
    def __init__(self, pageNumbers=None):
        """
        Initialize an Update object.

        Parameters:
        pageNumbers (list): List of page numbers in the update.
        """
        self.pageNumbers = pageNumbers if pageNumbers else []

    def check_update_order(self, pages):
        """
        Check the order of the update.

        Parameters:
        pages (dict): Dictionary of Page objects.

        Returns:
        tuple: Indices of pages in the wrong order, or (0, 0) if the order is correct.
        """
        for pageNumber in self.pageNumbers:
            if pageNumber in pages:
                for pageAfter in pages[pageNumber].pagesAfter:
                    if pageAfter in self.pageNumbers[self.pageNumbers.index(pageNumber):]:
                        return (self.pageNumbers.index(pageNumber), self.pageNumbers.index(pageAfter))
        return (0, 0)

    def swap_elements(self, index1, index2):
        """
        Swap two elements in the page numbers list.

        Parameters:
        index1 (int): Index of the first element.
        index2 (int): Index of the second element.
        """
        self.pageNumbers[index1], self.pageNumbers[index2] = self.pageNumbers[index2], self.pageNumbers[index1]

    def reorder(self, pages):
        """
        Reorder the page numbers in the update.

        Parameters:
        pages (dict): Dictionary of Page objects.
        """
        res = self.check_update_order(pages)
        while res != (0,0):
            self.swap_elements(res[0], res[1])
            res = self.check_update_order(pages)

    def extract_middle(self):
        """
        Extract the middle element from the page numbers list.

        Returns:
        int: The middle element of the list.
        """
        return self.pageNumbers[int(len(self.pageNumbers)/2)]

def parse_file_1(filename):
    """
    Parse a file and return a dictionary of Page objects.

    Parameters:
    filename (str): The name of the file to parse.

    Returns:
    dict: Dictionary of Page objects.
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
    Parse a file and return a list of Update objects.

    Parameters:
    filename (str): The name of the file to parse.

    Returns:
    list: List of Update objects.
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
    Main function to parse a file and print the count of pages.
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
        if update.check_update_order(pages) != (0,0):
            update.reorder(pages)
            total += update.extract_middle()

    print(f"Pages count: {total}")

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:40:59 2015

@author: Arjun
"""


import re


class Book:
    def __init__(self, index, string):

        self.book_id = index
        self.whole_string = string
        # split the data as | is the delimiter in the file
        seperate_entries = string.split('|')
        self.call_number = re.sub('[^a-z0-9 ]+', '', seperate_entries[0].lower())
        self.title = re.sub('[^a-z0-9 ]+', '', seperate_entries[1].lower())
        self.subjects = re.sub('[^a-z0-9 ]+', '', seperate_entries[2].lower())
        self.description = re.sub('[^a-z0-9 ]+', '', seperate_entries[4].lower())
        self.year = re.sub('[^0-9 ]+', '', seperate_entries[7].lower())
        self.notes = re.sub('[^a-z0-9 ]+', '', seperate_entries[9].lower())

    def __str__(self):
        # Called when using print on the Book object
        return self.whole_string

    def get_string(self):
        # function to return the entire row so that we can display this as final result of search !
        string = '\n##-- Book --##\n'
        st = self.whole_string.split('|')
        string += '  Call Number: '+st[0] + '\n  Title: '+st[1] +'\n  Subject: '+st[2] +'\n  Description: '+st[4]+'\n  Year: '+st[7]+'\n  Notes: '+st[9].strip()
        return string

# BookList class is the class which contains the list of Books. Book is one row. BookList is the whole file book.txt
class BookList:
    def __init__(self, list_of_books):
        self.list_of_books = [Book(index,string) for (index,string) in enumerate(list_of_books)]

    def get_dictionary(self, filter_condition):
        dictionary = dict()
        # Have created seperate entries for call_number, title, subject and others. Different dictionaries are created
        if filter_condition == 'call_number':
            for books in self.list_of_books:
                call_number_list = books.call_number.split()
                for individual_entry in call_number_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(books.book_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {books.book_id}

        elif filter_condition == 'title':
            for books in self.list_of_books:
                title_list = books.title.split()
                for individual_entry in title_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(books.book_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {books.book_id}

        elif filter_condition == 'subject':
            for books in self.list_of_books:
                subject_list = books.subjects.split()
                for individual_entry in subject_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(books.book_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {books.book_id}

        elif filter_condition == 'other':
            for books in self.list_of_books:
                other_list = books.description.split() + books.notes.split() + books.year.split()
                for individual_entry in other_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(books.book_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {books.book_id}

        return dictionary

    def get_searchList(self, dictionary, search_string):
        listSearch = list()
        selected_set = set()
        if search_string in dictionary:
            selected_set = dictionary[search_string]
        for i in selected_set:
            listSearch.append(self.list_of_books[i].get_string())
        return listSearch

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:33:10 2015

@author: Arjun
"""

# List of imports required. Check the .py files to see whats in them.
from books import BookList
from periodic import PeriodicList
from films import FilmList
from videos import VideoList
from search_util import print_list
import sys

# Main class - Responsible for kicking things off
class SearchLibrary:

    def __init__(self):
        self.call_number = 'call_number'
        self.title = 'title'
        self.subject = 'subject'
        self.other = 'other'
        #It opens the respective file, converts it to list and passes it to BookList class in books.py. It automatically calls its constructor. 
        self.bookList = BookList(list(open('book.txt')))
        self.periodicList = PeriodicList(list(open('periodic.txt')))
        self.filmList = FilmList(list(open('film.txt')))
        self.videoList = VideoList(list(open('video.txt')))

    def searchAndPrint(self, category, search_string):
        # They have mentioned to return everything in a unified list. That is the final_list here.
        final_list = list()
        # Dictionary is created with words as key and position as values. Read books.py for more info
        dictionary_book = self.bookList.get_dictionary(category)
        dictionary_film = self.filmList.get_dictionary(category)
        dictionary_periodic = self.periodicList.get_dictionary(category)
        dictionary_video = self.videoList.get_dictionary(category)
        # Returns a list of strings which pass search criteria
        book_list = self.bookList.get_searchList(dictionary_book,search_string)
        film_list = self.filmList.get_searchList(dictionary_film,search_string)
        periodic_list = self.periodicList.get_searchList(dictionary_periodic,search_string)
        video_list = self.videoList.get_searchList(dictionary_video,search_string)
        final_list = book_list + film_list + periodic_list + video_list
        #final_list is the final combination of everything.
        print_list(final_list)
        return final_list

search = SearchLibrary()
#sys.argv provides the arguments passed to this script
if len(sys.argv)==3:
    if sys.argv[1] == 'call_number' or sys.argv[1] == 'title' or sys.argv[1] == 'subject' or sys.argv[1] == 'other':
        final_list = search.searchAndPrint(sys.argv[1],sys.argv[2])
            else:
        print('Error !! \nArguments should be as follows \n1. Category [call_number; title; subject; other] \n2. Search String \nExample - search_library.py other future')
else:
    print('Error !! \n2 Arguments are required\n1. Category [call_number; title; subject; other] \n2. Search String \nExample - search_library.py other future')

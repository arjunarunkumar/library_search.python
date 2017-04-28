# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 18:40:40 2015

@author: Arjun
"""

import re

class Film:
    def __init__(self, index, string):
        self.film_id = index
        self.whole_string = string
        seperate_entries = string.split('|')
        self.call_number = re.sub('[^a-z0-9 ]+', '', seperate_entries[0].lower())
        self.title = re.sub('[^a-z0-9 ]+', '', seperate_entries[1].lower())
        self.subjects = re.sub('[^a-z0-9 ]+', '', seperate_entries[2].lower())
        self.director = re.sub('[^a-z0-9 ]+', '', seperate_entries[3].lower())
        self.notes = re.sub('[^a-z0-9 ]+', '', seperate_entries[4].lower())
        self.year = re.sub('[^0-9 ]+', '', seperate_entries[5].lower())

    def __str__(self):
        return self.whole_string

    def get_string(self):
        string = '\n##-- Film --##\n'
        st = self.whole_string.split('|')
        string += '  Call Number: '+st[0] + '\n  Title: '+st[1] +'\n  Subject: '+st[2] +'\n  Director: '+st[3]+'\n  Notes: '+st[4]+'\n  Year: '+st[5].strip()
        return string

class FilmList:
    def __init__(self, film_list):
        self.films_list = [Film(index,string) for (index,string) in enumerate(film_list)]

    def get_dictionary(self, filter_condition):
        dictionary = dict()
        if filter_condition == 'call_number':
            for film in self.films_list:
                call_number_list = film.call_number.split()
                for individual_entry in call_number_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(film.film_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {film.film_id}

        elif filter_condition == 'title':
            for film in self.films_list:
                title_list = film.title.split()
                for individual_entry in title_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(film.film_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {film.film_id}

        elif filter_condition == 'subject':
            for film in self.films_list:
                subject_list = film.subjects.split()
                for individual_entry in subject_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(film.film_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {film.film_id}

        elif filter_condition == 'other':
            for film in self.films_list:
                other_list = film.notes.split() + film.director.split() + film.year.split()
                for individual_entry in other_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(film.film_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {film.film_id}

        return dictionary

    def get_searchList(self, dictionary, search_string):
        listSearch = list()
        selected_set = set()
        if search_string in dictionary:
            selected_set = dictionary[search_string]
        for i in selected_set:
            listSearch.append(self.films_list[i].get_string())
        return listSearch

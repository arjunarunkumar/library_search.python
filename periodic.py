# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:44:20 2015

@author: Arjun
"""

import re

class Periodic:
    def __init__(self, index, string):
        self.periodic_id = index
        self.whole_string = string
        seperate_entries = string.split('|')
        self.call_number = re.sub('[^a-z0-9 ]+', '', seperate_entries[0].lower())
        self.title = re.sub('[^a-z0-9 ]+', '', seperate_entries[1].lower())
        self.subjects = re.sub('[^a-z0-9 ]+', '', seperate_entries[2].lower())
        self.description = re.sub('[^a-z0-9 ]+', '', seperate_entries[4].lower())
        self.notes = re.sub('[^a-z0-9 ]+', '', seperate_entries[8].lower())
        self.series = re.sub('[^a-z0-9 ]+', '', seperate_entries[7].lower())
        self.related_titles = re.sub('[^a-z0-9 ]+', '', seperate_entries[9].lower())

    def __str__(self):
        return self.whole_string

    def get_string(self):
        string = '\n##-- Periodic --##\n'
        st = self.whole_string.split('|')
        string += '  Call Number: '+st[0] + '\n  Title: '+st[1] +'\n  Subject: '+st[2] +'\n  Description: '+st[4]+'\n  Series: '+st[7]+'\n  Notes: '+st[8] + '\n  Related titles: '+st[9].strip()
        return string

class PeriodicList:
    def __init__(self, periodic_list):
        self.periodic_list = [Periodic(index,string) for (index,string) in enumerate(periodic_list)]

    def get_dictionary(self, filter_condition):
        dictionary = dict()
        if filter_condition == 'call_number':
            for periodic in self.periodic_list:
                call_number_list = periodic.call_number.split()
                for individual_entry in call_number_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(periodic.periodic_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {periodic.periodic_id}

        elif filter_condition == 'title':
            for periodic in self.periodic_list:
                title_list = periodic.title.split()
                for individual_entry in title_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(periodic.periodic_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {periodic.periodic_id}

        elif filter_condition == 'subject':
            for periodic in self.periodic_list:
                subject_list = periodic.subjects.split()
                for individual_entry in subject_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(periodic.periodic_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {periodic.periodic_id}

        elif filter_condition == 'other':
            for periodic in self.periodic_list:
                other_list = periodic.description.split() + periodic.notes.split() + periodic.series.split() + periodic.related_titles.split()
                for individual_entry in other_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(periodic.periodic_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {periodic.periodic_id}

        return dictionary

    def get_searchList(self, dictionary, search_string):
        listSearch = list()
        selected_set = set()
        if search_string in dictionary:
            selected_set = dictionary[search_string]
        for i in selected_set:
            listSearch.append(self.periodic_list[i].get_string())
        return listSearch

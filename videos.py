# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 19:26:50 2015

@author: Arjun
"""


import re

class Video:
    def __init__(self, index, string):
        self.video_id = index
        self.whole_string = string
        seperate_entries = string.split('|')
        self.call_number = re.sub('[^a-z0-9 ]+', '', seperate_entries[0].lower())
        self.title = re.sub('[^a-z0-9 ]+', '', seperate_entries[1].lower())
        self.subjects = re.sub('[^a-z0-9 ]+', '', seperate_entries[2].lower())
        self.description = re.sub('[^a-z0-9 ]+', '', seperate_entries[3].lower())
        self.distributor = re.sub('[^a-z0-9 ]+', '', seperate_entries[4].lower())
        self.notes = re.sub('[^a-z0-9 ]+', '', seperate_entries[5].lower())

    def __str__(self):
        return self.whole_string

    def get_string(self):
        string = '\n##-- Video --##\n'
        st = self.whole_string.split('|')
        string += '  Call Number: '+st[0] + '\n  Title: '+st[1] +'\n  Subject: '+st[2] +'\n  Description: '+st[3]+'\n  Distributor: '+st[4]+'\n  Notes: '+st[5].strip()
        return string

class VideoList:
    def __init__(self, video_list):
        self.videos_list = [Video(index,string) for (index,string) in enumerate(video_list)]

    def get_dictionary(self, filter_condition):
        dictionary = dict()
        if filter_condition == 'call_number':
            for video in self.videos_list:
                call_number_list = video.call_number.split()
                for individual_entry in call_number_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(video.video_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {video.video_id}

        elif filter_condition == 'title':
            for video in self.videos_list:
                title_list = video.title.split()
                for individual_entry in title_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(video.video_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {video.video_id}

        elif filter_condition == 'subject':
            for video in self.videos_list:
                subject_list = video.subjects.split()
                for individual_entry in subject_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(video.video_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {video.video_id}

        elif filter_condition == 'other':
            for video in self.videos_list:
                other_list = video.description.split() + video.notes.split() + video.distributor.split()
                for individual_entry in other_list:
                    if individual_entry in dictionary:
                        temp = dictionary[individual_entry]
                        temp.add(video.video_id)
                        dictionary[individual_entry] = temp
                    else:
                        dictionary[individual_entry] = {video.video_id}

        return dictionary

    def get_searchList(self, dictionary, search_string):
        # Returns the search list. Very simple. It output's book rows which are successfully selected from the search query
        listSearch = list()
        selected_set = set()
        if search_string in dictionary:
            selected_set = dictionary[search_string]
        for i in selected_set:
            listSearch.append(self.videos_list[i].get_string())
        return listSearch

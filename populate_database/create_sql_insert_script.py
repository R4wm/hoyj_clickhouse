#!/usr/bin/env python3
from datetime import datetime


dump_file="dump.txt"

def get_file_type(a_filename :str) -> str:
    if '.mp3' in a_filename:
        return 'mp3'
    if '.mp4' in a_filename:
        return 'mp4'
    return "na"

def get_timestamp(a_filename: str) -> str:
    ts = a_filename.split('-')[0]
    #print(f"ts: {ts}")
    if ts.startswith("20"):
        try:
            date = datetime.strptime(ts, '%Y%m%d').strftime('%Y-%m-%d')
            return date
        except Exception:
            return "1984-07-10"
            
    else:
        #print("no ts found for {a_filename}")
        return "1984-07-10"

def get_title(a_filename: str) -> str:
    return a_filename.split('.')[0]

def get_topic(a_full_path: str) -> str:
    topic_name = a_full_path.split('/')[-2]
    return topic_name.lower().replace('-', ' ')

with open(dump_file) as df:
    lines = [line.rstrip() for line in df]
    
for i in lines:
    basename = i.split('/')[-1]
    #print("basename: ", basename)
    file_type = get_file_type(basename)
    #print(f"file type is {file_type}")
    ts = get_timestamp(basename)
    title = get_title(basename)
    #print(f'title: {title}')
    topic = get_topic(i)
    #print(f'topic: {topic}')
    
    print(f'INSERT INTO hoyj.media (dt, title, topic, file_type, file_location) VALUES ({ts},\'{title}\', \'{topic}\', \'{file_type}\', \'{i}\')')

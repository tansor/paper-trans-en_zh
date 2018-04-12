# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from xvfbwrapper import Xvfb

###### pre-process text

f_list = list()
result = ""

f_in  = open("raw.txt", "r")
file_lines = f_in.readlines()
for i in range(0, len(file_lines)):
    line = file_lines[i].strip()
    if len(line):
        if line[-1] == "-":
            line = line[:-1]
        else:
            line += " "
        result += line
        if i == len(file_lines)-1:
            f_list.append(result[:-1])
    else:
        if len(result):
            f_list.append(result[:-1]) # one more space
            result = ""
        else:
            result = ""
            continue
f_in.close()

f_out = open("mid.txt", "w")
for element in f_list:
    f_out.write(element+"\n\n")
f_out.close()

###### google translate

will_show_chrome = input("Will show Chrome? y/[n] : ")
display = Xvfb()
if will_show_chrome != 'y':
    display.start()

path = "/home/tyq/Software/Chrome/chromedriver"
paper_path = "mid.txt"

browser = webdriver.Chrome(executable_path=path)

# browser.get("https://translate.google.com/?source=gtx#en/zh-CN/")
browser.get("https://translate.google.com/?tr=f&#en/zh-CN/")
print(browser.title)
browser.find_element_by_id("file").send_keys(paper_path)
browser.find_element_by_id("gt-submit").click()
while browser.title != "":
    pass
print("Translation Done.")

text = browser.find_element_by_tag_name("pre").text
# print(text)

browser.close()
if will_show_chrome != 'y':
    display.stop()

###### post-process text

trans = text.split('\n')
trans = [x for x in trans if x != '']

f_replace = open("word-replacer.txt", "r")
replace_lst = []
for line in f_replace.readlines():
    old = line.split(" ")[0]
    new = line.split(" ")[1]
    if new[-1] == '\n':
        new = new[:-1]
    replace_lst.append((old,new))

f_out = open("paper.txt", "w")
for i in range(0, len(f_list)):
    for j in range(0, len(replace_lst)):
        trans[i] = trans[i].replace(replace_lst[j][0], replace_lst[j][1])
    f_out.write(f_list[i]+"\n"+trans[i]+"\n\n")
    print(f_list[i]+"\n"+trans[i]+"\n") # Because print create a '\n'
f_out.close()

will_remove_files = input("Will remove raw.txt and mid.txt. [y]/n : ")
if will_remove_files != 'n':
    os.remove("raw.txt")
    os.remove("mid.txt")

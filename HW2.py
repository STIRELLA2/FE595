from flask import Flask,render_template
from bs4 import BeautifulSoup
import requests
import re
for i in range(0,50):

    source = requests.get('http://3.85.131.173:8000/random_company').text
    soup = BeautifulSoup(source, 'html.parser')
    y = (soup.get_text())

    Purpose = re.search('(?<=Purpose: )(.*)(?=\n)', y)
    Purpose.group(0)

    Name = re.search('(?<=Name: )(.*)(?=\n)', y)
    Name.group(0)

    NamePurpose = Name.group(0) +" | "+ Purpose.group(0)+'\n'
    print(NamePurpose)

    f = open(r"C:\Users\spenc\Desktop\HW2.txt","a")
    f.write(NamePurpose)



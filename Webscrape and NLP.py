#Spencer Tirella FE 595 HW2
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re
for i in range(0,50):

    source = requests.get('http://3.85.131.173:8000/random_company').text
    soup = BeautifulSoup(source, 'html.parser')
    y = (soup.get_text())

    Purpose = re.search('(?<=Purpose: )(.*)(?=\n)', y)
    Purpose2 = re.search('(?<=Purpose: )(.*)',y)
    Name = re.search('(?<=Name: )(.*)(?=\n)', y)

    NamePurpose = Name.group(0) +" | "+ Purpose.group(0)+'\n'
    f = open(r"C:\Users\spenc\Desktop\HW2.txt","a")
    f.write(NamePurpose)

df1 = pd.read_csv(r"C:\Users\spenc\Desktop\HW2.txt", sep='|',header=None)
df2 = pd.read_csv(r"C:\Users\spenc\Desktop\HW2 Z.txt", sep='|',header=None)
df = pd.concat([df1, df2])

sentences = df[1]
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
#df2= df[1].apply(analyzer.polarity_scores)
df['compound'] = [analyzer.polarity_scores(df[1])['compound'] for x in df[1]]
df['neg'] = [analyzer.polarity_scores(x)['neg'] for x in df[1]]
df['neu'] = [analyzer.polarity_scores(x)['neu'] for x in df[1]]
df['pos'] = [analyzer.polarity_scores(x)['pos'] for x in df[1]]
df3 = pd.DataFrame(df)
df3.sort_values('neg')

df3.to_csv(r"C:\Users\spenc\Desktop\Spencer Tirella FE 595 HW2.txt", mode='a')

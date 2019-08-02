import pandas as pd
import numpy as np
import nltk
from sklearn.feature_extraction.text import CountVectorizer
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from zemberek_python import main_libs as ml
import os.path
import glob

zemberek_api = ml.zemberek_api(libjvmpath="C:/Program Files/Java/jdk-12.0.1/bin/server/jvm.dll",
                               zemberekJarpath="./zemberek_python/zemberek-tum-2.0.jar").zemberek()

path='C:/Users/bugia/Desktop/nltk/test/ekonomi/*.txt' #EKONOMİDEKİ TÜM TXTLERİ OKUYOR FAKAT KARISIK OKUYOR
path2='C:/Users/bugia/Desktop/nltk/test/magazin/*.txt'
path3='C:/Users/bugia/Desktop/nltk/test/saglik/*.txt'
path4='C:/Users/bugia/Desktop/nltk/test/spor/*.txt'
def CleanData(doc):
    stop_words = set(stopwords.words("turkish"))  #bu stop words işlemi
    words = word_tokenize(data)    #tokenize işlemi
    filtered_sentence = []
    for w in words:
        if w not in stop_words:
            filtered_sentence.append(w)
    words1 = ml.ZemberekTool(zemberek_api).metinde_gecen_kokleri_bul(filtered_sentence)  #zemberek işlemi

   # print(words1)  #okudugum işlelerini yaptıgım verimin son hali
    wordfreq = [words1.count(w) for w in words1]
    result=zip(words1, wordfreq)
    resultSet = set(result)
    print(resultSet)#burada kaçar tane geçtiği Direk yazıdırdımda Bi listeye ekleyip vektör matrisinde kullanmaya yardım olabilir.
    print (" ")
print("Train Verisi : Sınıf-Kaç Adet Geçtiği")
for text in glob.glob(path):  # burada global path ile txt açıyor bunun amacı tüm dosyaları okuyabilmek
        f = open(text)
        data = f.read().lower()  # burada da küçük harfe çevirdi
        data = re.sub(r'[^\w\s]', '', data)  # burda noktalama işaretlerini atıyor
        print("Ekonomi Sınıfı: ")
        words = CleanData(data)

for text in glob.glob(path2):  # burada global path ile txt açıyor bunun amacı tüm dosyaları okuyabilmek
        f = open(text)
        data = f.read().lower()  # burada da küçük harfe çevirdi
        data = re.sub(r'[^\w\s]', '', data)  # burda noktalama işaretlerini atıyor
        print("Magazin Sınıfı: ")
        words = CleanData(data)

for text in glob.glob(path3):  # burada global path ile txt açıyor bunun amacı tüm dosyaları okuyabilmek
        f = open(text)
        data = f.read().lower()  # burada da küçük harfe çevirdi
        data = re.sub(r'[^\w\s]', '', data)  # burda noktalama işaretlerini atıyor
        print("Sağlık Sınıfı: ")
        words = CleanData(data)

for text in glob.glob(path4):  # burada global path ile txt açıyor bunun amacı tüm dosyaları okuyabilmek
        f = open(text)
        data = f.read().lower()  # burada da küçük harfe çevirdi
        data = re.sub(r'[^\w\s]', '', data)  # burda noktalama işaretlerini atıyor
        print("Spor Sınıfı: ")
        words = CleanData(data)
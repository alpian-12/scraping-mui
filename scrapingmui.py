from asyncore import write
from cgi import test
from distutils.filelist import findall
import string
from traceback import print_tb
from bs4 import  BeautifulSoup
import requests
import csv

data = []
# data_restaurant = [43,46,47,51]

for x in range(7):
    x+=1
    url = "https://halalmui.org/mui14/searchproduk/search/caribycategory/?groupcode=31&kategori=nama_produk&katakunci=jakarta+utara&page="+str(x)
    print(url,end="\n")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('td')
    if  len(lists)== 0:
        print(x) 
    for j in lists:
        for i in j.find_all("span") :
            if "Nama Produk :" in i.text :
                product_name = i.text.replace("Nama Produk :","")
            if "Nomor Sertifikat :" in i.text:
                Certificate_number = i.text.replace( "Nomor Sertifikat :","")
                data.append([product_name,Certificate_number])


header =["Nama Produk","Nomor Sertifikat"] 
with open('Jakarta_Utara_Mui_halal_restaurant.csv','w', encoding='UTF8', newline='') as f:
    write =csv.writer(f)

    write.writerow(header)

    write.writerows(data)



data = []
for x in range(5):
    x+=1
    url = "https://halalmui.org/mui14/searchproduk/search/caribycategory/?groupcode=31&kategori=nama_produk&katakunci=jakarta+pusat&page="+str(x)
    print(url,end="\n")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('td')
    if  len(lists)== 0:
        print(x) 
    for j in lists:
        for i in j.find_all("span") :
            if "Nama Produk :" in i.text :
                product_name = i.text.replace("Nama Produk :","")
                # print(i.text.replace("Nama Produk :",""))
            if "Nomor Sertifikat :" in i.text:
                Certificate_number = i.text.replace( "Nomor Sertifikat :","")
                # print(i.text.replace( "Nomor Sertifikat :",""),end="\n\n")
                # print(data_restaurant,end="\n\n")

                data.append([product_name,Certificate_number])


header =["Nama Produk","Nomor Sertifikat"] 
with open('Jakarta_Pusat_Mui_halal_restaurant.csv','w', encoding='UTF8', newline='') as f:
    write =csv.writer(f)

    write.writerow(header)

    write.writerows(data)


data = []
for x in range(11):
    x+=1
    url = "https://halalmui.org/mui14/searchproduk/search/caribycategory/?groupcode=31&kategori=nama_produk&katakunci=jakarta+barat&page="+str(x)
    print(url,end="\n")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('td')
    if  len(lists)== 0:
        print(x) 
    for j in lists:
        for i in j.find_all("span") :
            if "Nama Produk :" in i.text :
                product_name = i.text.replace("Nama Produk :","")
                # print(i.text.replace("Nama Produk :",""))
            if "Nomor Sertifikat :" in i.text:
                Certificate_number = i.text.replace( "Nomor Sertifikat :","")
                # print(i.text.replace( "Nomor Sertifikat :",""),end="\n\n")
                # print(data_restaurant,end="\n\n")

                data.append([product_name,Certificate_number])


header =["Nama Produk","Nomor Sertifikat"] 
with open('Jakarta_Barat_Mui_halal_restaurant.csv','w', encoding='UTF8', newline='') as f:
    write =csv.writer(f)

    write.writerow(header)

    write.writerows(data)



data = []
for x in range(11):
    x+=1
    url = "https://halalmui.org/mui14/searchproduk/search/caribycategory/?groupcode=31&kategori=nama_produk&katakunci=jakarta+timur&page="+str(x)
    print(url,end="\n")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('td')
    if  len(lists)== 0:
        print(x) 
    for j in lists:
        for i in j.find_all("span") :
            if "Nama Produk :" in i.text :
                product_name = i.text.replace("Nama Produk :","")
                # print(i.text.replace("Nama Produk :",""))
            if "Nomor Sertifikat :" in i.text:
                Certificate_number = i.text.replace( "Nomor Sertifikat :","")
                # print(i.text.replace( "Nomor Sertifikat :",""),end="\n\n")
                # print(data_restaurant,end="\n\n")

                data.append([product_name,Certificate_number])


header =["Nama Produk","Nomor Sertifikat"] 
with open('Jakarta_Timur_Mui_halal_restaurant.csv','w', encoding='UTF8', newline='') as f:
    write =csv.writer(f)

    write.writerow(header)

    write.writerows(data)


data = []
for x in range(11):
    x+=1
    url = "https://halalmui.org/mui14/searchproduk/search/caribycategory/?groupcode=31&kategori=nama_produk&katakunci=jakarta+selatan&page="+str(x)
    print(url,end="\n")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    lists = soup.find_all('td')
    if  len(lists)== 0:
        print(x) 
    for j in lists:
        for i in j.find_all("span") :
            if "Nama Produk :" in i.text :
                product_name = i.text.replace("Nama Produk :","")
                # print(i.text.replace("Nama Produk :",""))
            if "Nomor Sertifikat :" in i.text:
                Certificate_number = i.text.replace( "Nomor Sertifikat :","")
                # print(i.text.replace( "Nomor Sertifikat :",""),end="\n\n")
                # print(data_restaurant,end="\n\n")

                data.append([product_name,Certificate_number])


header =["Nama Produk","Nomor Sertifikat"] 
with open('Jakarta_Selatan_Mui_halal_restaurant.csv','w', encoding='UTF8', newline='') as f:
    write =csv.writer(f)

    write.writerow(header)

    write.writerows(data)


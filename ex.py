# # import os
# # from selenium import webdriver
# # from selenium.webdriver.common.keys import Keys
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time

# # def extract_link():
# #     root = os.path.abspath(os.curdir + r"\progetto\link")
# #     # filepaths = [os.path.join(root + r'\link',i) for i in os.listdir(root + r'\testi')]
# #     PATH = os.path.abspath(os.curdir + r'\chromedriver.exe')
# #     #il web browser che vogliamo usare è chrome e il path del driver è PATH
# #     driver = webdriver.Chrome(PATH)
# #     driver.maximize_window()

# #     driver.get('https://www.allmovie.com/genres')
# #     WebDriverWait(driver, 100000000000000)

# #     # if not os.path.exists(root):
# #     #     os.mkdir(r"progetto\link")
# #     # filepaths = os.path.join(root, 'filename')
# #     # i = 1
# #     # txt_link = open(path+str(i), 'w')
#     # try:
#         # main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))
            
# #         articles = main.find_elements_by_class_name("image")
# #         for article in articles: 
# #             link = article.find_element_by_tag_name('a')
# #             link = link.get_attribute('href')
# #                 # txt_link.write(link)
# #                 # txt_link.write('\n')
# #                 # i = i+1
# #     except:
# #         driver.quit()


# # lists = ['title','year','time','storyline','genre']
# # title = ["mortal kombat","pera","banana"]
# # year = ["2000","1000","2002","2000"]
# # time = [1,2,3]
# # storyline = ["ciao","mio","tuo"]
# # genre = [["action","drama"],"comedy","drive"]

# # # dictionary = {}

# # # i = 1
# # for t, y, ti, s, g, i in zip(title, year, time, storyline, genre, list(range(len(title)))):
# #     print(t)
# # # for i in :
# #     print(i+1)
# #     nasted_dictionary = {}
# #     # nasted_dictionary["title"].append(t)
# #     nasted_dictionary.update({"year":y})
# #     nasted_dictionary.update({"time":ti})
# #     nasted_dictionary.update({"storyline":s})
# #     nasted_dictionary.update({"genre":g})
# #     # dictionary["film"].append(nasted_dictionary)
# #     dictionary.update({f"{t}":nasted_dictionary})
# #     i = i+1
# # # print(dictionary)
# # for k, v in dictionary.items():
# #     # print (k, v)
# #     for vv, m in v.items():
# #         print(k, vv, m)
# # for pair in dictionary.items():
# #     # print(pair)
# #     # print("\n", pair[0])
# #     for valu in pair[1].items():
# #         print(valu)
# # print("\n",dictionary["film 2"]["year"])
# # print("\n",dictionary["film"][2])
# # import re
# import json
# import os
# # str1 = 'Retf\u00e6rdighedens ryttere\u00a0'
# # str1 = "16 October 2020"
# # str1 = str1.strip()
# # print(type(str1))
# # y = []
# # matched = re.match(r"[0-9]{1,2}[\s][A-z]{1,9}[\s][0-9]{4}",str1)
# # is_match = bool(matched)
# # print(is_match)
# # if not is_match:
# #     str1 = ""
# # y.append(str1)
# # print(y[0])
# # dictionary = {"title":[]}
# # dictionary["title"].append(y)
# # # with open("idbm.txt", "w", encoding="utf8") as f:
# # #         f.write(y[0])
# # with open(r"idbm.json", "w", encoding="utf8") as f:
# #         json.dump(dictionary,f,indent=4,ensure_ascii=False)
# # import datetime
# # from dateutil.parser import parse
# # open the json file
# root = os.path.abspath(os.curdir)
# # print(root)
# lista_director = []
# filepaths = [os.path.join(root + r'\json_file',i) for i in os.listdir(root + r'\json_file')]
# for filename in filepaths:
#     # print(filename)
#     with open(filename, encoding="utf8") as f:
#         data = json.loads(f.read())
#         # print("1")
#         for v in data.values():
#             # title = v["title"]
#             # year = v["year"]
#             # y = parse(year)
#             # y= y.strftime('%Y/%m/%d')
#             # print(y)
#             # try:
#             #     article_date = datetime.datetime.strptime(y, "%Y/%m/%d")     # convert the string in a date obj
#             # except (ValueError):
#             #     article_date = datetime.datetime.strptime("1970-01-02", "%Y-%m-%d")
#             # storyline = v["storyline"]
#             # genre = v["genre"]
#             lista_director.append(v["director"])
            
#             # print(title,year,genre,director)
#             # print(article_date)
# lista_director = list(set(lista_director))
# f = open("registi.txt", "w+", encoding="utf8")
# for i in lista_director:
#     f.write(i)
#     f.write("\n")

# # print (lista_director)
#                 # print(k,m)
# # for pair in dictionary.items():
# #     # print(pair)
# #     # print("\n", pair[0])
# #     for valu in pair[1].items():
# #         print(valu)
# # print("\n",dictionary["film 2"]["year"])
# # print("\n",dictionary["film"][2])
    
# # print(str1)




# # dictionary = {"title": [], "year":[], "time":[], "storyline":[], "genre":[]}
# # for t, y, ti, s, g in zip(title, year, time, storyline, genre):
# #     if t == None or not y or ti == None or s == None or g == None:
# #         pass
# #     else:
# #         dictionary["title"].append(t)
# #         dictionary["year"].append(y)
# #         dictionary["time"].append(ti)
# #         dictionary["storyline"].append(s)
# #         dictionary["genre"].append(g)

# # for d in year:
# #     if not d:
# #         pass
# #     else:
# #         print(d)
# # print(is_match)
# # print(dictionary)
# # def ciao(t):
# #     di = {'ti': []}
# #     di['ti'].append(t[0])
# #     return di

# # a = ciao(year)
# # print(a) 
# # if year.count("1000") == 0 and title.count("mela") == 0:
# #     print("no")
# # else:
# #     print("esiste")
# # def fr(r):
# #     del r[:]
# # e = [1,4,7,6]
# # fr(e)
# # e.append(3)
# # print(e)

# # from dateutil.parser import parse
# # e = parse(e)
# # print(e)
# # # datetime.datetime(2010, 2, 15, 0, 0)
# # print(e.strftime('%d/%m/%Y'))
# # # 15/02/2010

# # from collections import OrderedDict

# # year = OrderedDict.fromkeys(year)
# # year = list(year)
# # print(year)

# # t = "mortal kombat"
# # sto = "d"

# # if title.count(t) == 0 or storyline.count(sto) == 0:
# #     title.append(t)
# #     storyline.append(sto)

# # print(title, storyline)


# # import requests
# # import re
# # import os
# # import json
# # from bs4 import BeautifulSoup
# # from string import punctuation
# # from dateutil.parser import parse

# # # Richiede la pagina Web
# # r = requests.get('https://www.themoviedb.org/movie/2300-space-jam')
# # # Parser della pagina
# # soup = BeautifulSoup(r.content, 'html.parser')
     
# # # Recupero tutti i link delle categorie
# # i = soup.find('div', {'class':'full-table'})
# # for link in i.find_all('div', {'class':'table-row'}):
# #     link = link.find('a').get('href')
# #     link = 'https://www.imdb.com' + link

# #     page_genre = requests.get(link)
# #     soup2 = BeautifulSoup(page_genre.content, 'html.parser')

# #     # Per ogni categoria navigo per N pagine
# #     for page in range(1,3):

# #         # Recupero il link alla prossima pagina
# #         next_page = soup2.find('div', {'class':'desc'})
# #         for href in next_page.find_all('a'):
# #             link_next = href.get('href')
# #             button_next = href.text.split()
# #             if button_next[0] == "Next":
# #                 next_page = 'https://www.imdb.com' + link_next

# #         # Recupero il link dei film nella categoria
# #         for j in soup2.find_all('div', {'class':'lister-item-content'}):
# #             link = j.find('a').get('href')
# #             document_link = 'https://www.imdb.com' + link
        
# #             page_link = requests.get(document_link)
# #             soup3 = BeautifulSoup(page_link.content, 'html.parser')

# #             # Recupero il titolo
# #             for i in soup3.find_all('div', {'class':'title_wrapper'}):
# #                 tit = i.find('h1')
# #                 if tit is not None:
# #                     tit = tit.text.strip()
# #                     # elimina eventuali date scritte tra parentesi
# #                     tit = re.sub(r"\([^()]*\)", "", tit)
# #                     tit = tit.strip()
# #                     print(tit)

#             #     ti = i.find('time')
#             #     if ti is not None:
#             #         ti = ti.text.strip()

#             # # Raccolgo il regista
#             # i = soup3.find('div', {'class':'plot_summary'})
#             # i = i.find('div', {'class':'credit_summary_item'})
#             # di = i.find('a')
#             # di = di.text.strip()

#             # # Raccolgo l'anno
#             # i = soup3.find('div', {'id':'titleDetails'})
#             # if i.find('h4').text != 'Official Sites:':
#             #     div = i.find('div', {'class': 'txt-block'}).find_next_sibling().find_next_sibling()
#             # else:
#             #     div = i.find('div', {'class': 'txt-block'}).find_next_sibling().find_next_sibling().find_next_sibling()
                            
#             # y = div.find('h4').next_element.next_element
#             # y = re.sub(r"\([^()]*\)", "", y)
#             # y = y.strip()

#             # #controllo che la data sia scritta come gg/mm/aa
#             # matched = re.match(r"[0-9]{1,2}[\s][A-z]{1,9}[\s][0-9]{4}",y)
#             # is_match = bool(matched)
#             # if not is_match:
#             #     y = ""
#             # else:
#             #     # modifico il formato della data
#             #     y = parse(y)
#             #     y= y.strftime('%d/%m/%Y')
#             # y = y.strip()
            
#             # # Raccolgo le trame
#             # i = soup3.find('div', {'id':'titleStoryLine'})
#             # i = i.find('div', {'class':'inline canwrap'})
#             # story = i.find('span')
#             # if story is not None:
#             #     story = story.text.strip()
                        
#             # # Raccolgo i generi
#             # i = soup3.find('div', {'class':'see-more inline canwrap'}).find_next_sibling('div', {'class':'see-more inline canwrap'})
#             # if i is not None:
#             #     ge = []
#             #     for gen in i.find_all('a'):
#             #         if gen is not None:
#             #             ge.append(gen.text.strip())
        
#             # # Controllo se ci sono duplicati
#             # check_duplicate(tit,y,ti,story,ge,di)
        
#         # Vado alla prossima pagina
#         # next_page_genre = requests.get(next_page)
#         # soup2 = BeautifulSoup(next_page_genre.content, 'html.parser')

# # # Creo un dizionario
# # dictionary = create_dictionary(title,year,time,storyline,genre,director)

# # # Creo un file json contente i film
# # with open(root + r"\idbm.json", "w", encoding="utf8") as f:
# #     json.dump(dictionary,f,indent=4,ensure_ascii=False)

# # d = "Director, Writer"
# # d = d.split()
# # f = re.sub(r",$","",d[0])
# # if f == "Director":
# #     print(f)



# # import time as fun_time

# # def inizialize_list():
# #     del title[:]
# #     del year[:]
# #     del time[:]
# #     del storyline[:]
# #     del genre[:]
# #     del director[:]

# # # Funzione che crea un dizionario
# # def create_dictionary(title,year,time,storyline,genre,director):
# #     dictionary = {"title": [], "year":[], "time":[], "storyline":[], "genre":[], 'director':[]}
    
# #     for t, y, ti, s, g, d in zip(title, year, time, storyline, genre, director):
# #         if t == None or y == None or not y or ti == None or s == None or s == "The plot is unknown." or g == None or g == [] or d == None:
# #             pass
# #         else:
# #             dictionary["title"].append(t)
# #             dictionary["year"].append(y)
# #             dictionary["time"].append(ti)
# #             dictionary["storyline"].append(s)
# #             dictionary["genre"].append(g)
# #             dictionary["director"].append(d)
# #     return dictionary

# # # Funzione che mi controlla se ci sono duplicati
# # def check_duplicate(tit,y,ti,story,ge,di):
# #     if title.count(tit) == 0 or storyline.count(story) == 0:
# #         title.append(tit)
# #         year.append(y)
# #         genre.append(ge)
# #         time.append(ti)
# #         storyline.append(story)
# #         director.append(di)

# # root = os.path.abspath(os.curdir + r"\json_file")
# # if not os.path.exists(root):
# #     os.mkdir(r"\json_file")

# # title = []
# # year = []
# # time = []
# # storyline = []
# # genre = []
# # director = []

# # # # Richiede la pagina Web
# # r = requests.get('https://www.filmsomniac.com/browse/genres')
# # # # Parser della pagina
# # soup = BeautifulSoup(r.content, 'html.parser')

# # inizialize_list()

# # Recupera tutti i link delle categorie
# # i = soup.find_all('div', {'class':'event-list'})
# # for page_genre in i[3].find_all('a'):
# #     page_genre = page_genre.get('href')
# #     page_genre = 'https://www.filmsomniac.com' + page_genre

# #     page_genre = requests.get(page_genre)
# #     soup2 = BeautifulSoup(page_genre.content, 'html.parser')

# #     # Per ogni categoria navigo per N pagine
# #     for _ in range(0,1):

# #         # Recupero la pagina successiva
# #         i = soup2.find('ul', {'class':'pagination'})
# #         if i is None:
# #             next_page = None
# #         else:
# #             next_page = i.find('a').get('href')

# #         # Recupero tutti i film per categoria
# #         i = soup2.find('div', {'class':'flex-wrap-movielist'})
# #         for film in i.find_all('div', {'class':'movie-item-style-2 item-row hide-for-small'}):
# #             film = film.find('a').get('href')
# #             film = 'https://www.filmsomniac.com' + film

# #             film = requests.get(film)
# #             soup3 = BeautifulSoup(film.content, 'html.parser')

# #             # Recupero il titolo
# #             tit = soup3.find('h1', {'id':'film-title'}).text
# #             tit = re.sub(r"\b\d{4}\b$", "", tit)
# #             tit = tit.strip()

# #             # Recupero la trama
# #             summary = soup3.find('p', {'class':'film-summary'})
# #             if summary is not None:
# #                 matched = re.match(r".*plot unknown.*",summary.text.lower())
# #                 is_match = bool(matched)
# #                 if is_match or summary == "The plot is unknown at this time.":
# #                     summary = None
# #                 else:
# #                     summary = summary.text.strip()

# #             # Recupero il contenitore con le info
# #             i = soup3.find('div', {'class':'col-md-3 col-xs-12 col-sm-12 hide-for-small'})
# #             ge = []
# #             directed = None
# #             release = None
# #             ti = "None"

# #             for info in i.find_all('div', {'class':'sb-it'}):
# #                 tipo = info.find('h6').text
# #                 if tipo == "Directed by: ":
# #                     if info.find('p').text.strip() != "":
# #                         directed = info.find('p').text
# #                         directed = re.sub(r"\s+"," ",directed).strip()

# #                 if tipo == "Genres:":
# #                     ge = []
# #                     for all_gen in info.find_all('span'):
# #                         if all_gen is not None:
# #                             ge.append(all_gen.text.strip())

# #                 if tipo == "Released:":
# #                     release = info.find('p').text.strip()
# #                     release = parse(release)
# #                     release = release.strftime('%d/%m/%Y')

# #                 if tipo == "Runtime:":
# #                     time_format = info.find('p').text.strip()
# #                     time_format = time_format.split()
# #                     time_format = int(time_format[0]) * 60
# #                     ti = fun_time.strftime("%Hh %Mm", fun_time.gmtime(time_format))
# #                     ti = re.sub(r"^0+(?!$)", "",ti)
                    
# #                     matched = re.match(r"^h",ti)
# #                     is_match = bool(matched)
# #                     if is_match:
# #                         ti = re.sub(r"^h","",ti).strip()

# #             check_duplicate(tit,release,ti,summary,ge,directed)

# #         # Se non ci sono altre pagine passo alla caregoria successiva
# #         if next_page is None:
# #             break

# #         # Richiedo la pagina successiva
# #         next_page = requests.get(next_page)
# #         soup2 = BeautifulSoup(next_page.content, 'html.parser')
    
# # # Creo un dizionario
# # dictionary = create_dictionary(title,year,time,storyline,genre,director)

# # # Creo un file json contente i film
# # with open(root + r"\filmsomniac.json", "w", encoding="utf8") as f:
# #     json.dump(dictionary,f,indent=4,ensure_ascii=False)









# # def retrive_link_ibdm():
#     # # Richiede la pagina Web
#     # r = requests.get('https://www.imdb.com/feature/genre/?ref_=nv_ch_gr')
#     # # Parser della pagina
#     # soup = BeautifulSoup(r.content, 'html.parser')

#     # # inizialize_list()
        
#     # # Recupero tutti i link delle categorie
#     # i = soup.find('div', {'class':'full-table'})
#     # for link in i.find_all('div', {'class':'table-row'}):
#     #     link = link.find('a').get('href')
#     #     link = 'https://www.imdb.com' + link

#     #     page_genre = requests.get(link)
#     #     soup2 = BeautifulSoup(page_genre.content, 'html.parser')

#     #     # Per ogni categoria navigo per N pagine
#     #     for _ in range(0,1):

#     #         # Recupero il link alla prossima pagina
#     #         next_page = soup2.find('div', {'class':'desc'})
#     #         for href in next_page.find_all('a'):
#     #             link_next = href.get('href')
#     #             button_next = href.text.split()
#     #             if button_next[0] == "Next":
#     #                 next_page = 'https://www.imdb.com' + link_next
#     #             else:
#     #                 next_page = None

#     #         # Recupero il link dei film nella categoria
#     #         for j in soup2.find_all('div', {'class':'lister-item-content'}):
#     #             link = j.find('a').get('href')
#     #             document_link = 'https://www.imdb.com' + link
            
#     #             page_link = requests.get(document_link)
#     #             soup3 = BeautifulSoup(page_link.content, 'html.parser')

#     #             # Recupero il titolo
#     #             tit = None
#     #             for i in soup3.find_all('div', {'class':'title_wrapper'}):
#     #                 if i is not None:
#     #                     tit = i.find('h1')
#     #                     if tit is not None:
#     #                         tit = tit.text.strip()
#     #                         # elimina eventuali date scritte tra parentesi
#     #                         tit = re.sub(r"\([^()]*\)", "", tit)
#     #                         tit = tit.strip()

#     #                     # ti = i.find('time')
#     #                     # if ti is not None:
#     #                     #     ti = ti.text.strip()
#     #                 # else:
#     #                 #     tit = None
#     #                     # ti = None

#     #             # Raccolgo il regista
#     #             i = soup3.find('div', {'class':'plot_summary'})
#     #             di = None
#     #             if i is not None:
#     #                 for j in i.find_all('div', {'class':'credit_summary_item'}):
#     #                     dire = j.find('h4', {'class':'inline'})
#     #                     if dire is not None and dire.text == "Director:":
#     #                         di = j.find('a')
#     #                         di = di.text.strip() 

#     #             # Raccolgo l'anno
#     #             y = None
#     #             i = soup3.find('div', {'id':'titleDetails'})
#     #             if i is not None:
#     #                 if i.find('h4').text != 'Official Sites:':
#     #                     div = i.find('div', {'class': 'txt-block'}).find_next_sibling().find_next_sibling()
#     #                 else:
#     #                     div = i.find('div', {'class': 'txt-block'}).find_next_sibling().find_next_sibling().find_next_sibling()
               
#     #                 if div is not None:
#     #                     y = div.find('h4')
#     #                     if y is not None:
#     #                         y = y.next_element.next_element
#     #                         y = re.sub(r"\([^()]*\)", "", y)
#     #                         y = y.strip()

#     #                         #controllo che la data sia scritta come gg/mm/aa
#     #                         matched = re.match(r"[0-9]{1,2}[\s][A-z]{1,9}[\s][0-9]{4}",y)
#     #                         is_match = bool(matched)
#     #                         if not is_match:
#     #                             y = ""
#     #                         else:
#     #                             # modifico il formato della data
#     #                             y = parse(y)
#     #                             y= y.strftime('%d/%m/%Y')
#     #                         y = y.strip()
                
#     #             # Raccolgo le trame
#     #             i = soup3.find('div', {'id':'titleStoryLine'})
#     #             story = None
#     #             if i is not None:
#     #                 i = i.find('div', {'class':'inline canwrap'})
#     #                 if i is not None:
#     #                     story = i.find('span')
#     #                     if story is not None:
#     #                         if story.text.strip() == "The plot is unknown.":
#     #                             story = None
#     #                         else:
#     #                             story = story.text.strip()
                            
#     #             # Raccolgo i generi
#     #             i = soup3.find('div', {'class':'see-more inline canwrap'})
#     #             if i is not None:
#     #                 i = i.find_next_sibling('div', {'class':'see-more inline canwrap'})
#     #             if i is not None:
#     #                 ge = []
#     #                 for gen in i.find_all('a'):
#     #                     if gen is not None:
#     #                         ge.append(gen.text.strip())
#     #             else:
#     #                 ge = None

#     #             print(tit,y,story,ge,di)

# # retrive_link_ibdm()

# from win32api import GetSystemMetrics

# print("Width =", GetSystemMetrics(0))
# print("Height =", GetSystemMetrics(1))

# import ctypes
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# print(screensize)

# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
# print(screensize)

# w.winfo_height()
# w.winfo_width()

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Learn")
# root.iconbitmap('c:/gui')
root.geometry("500x400")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window=second_frame, anchor="nw")

for thing in range(100):
    Button(second_frame, text=f'Button {thing} Yo').grid(row=thing, column=0, pady=10, padx=10)

root.mainloop()



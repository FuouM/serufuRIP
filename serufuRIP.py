from bs4 import BeautifulSoup
import timeit
import requests

template ='https://desuarchive.org/a/thread/'

def get_thread_info(thread_id: int):
    resp = requests.get(f'{template}{thread_id}')
    html = resp.text
    soup = BeautifulSoup(html, "html.parser")
    ttitle, ttext = "", ""
    for tags in soup.find_all('h2'):
        if tags.text:
            ttitle = tags.text
            break
    for tags in soup.find_all('div', {'class': 'text'}):
        if tags.text:
            ttext = str(tags.text).strip()
            break
    if not ttitle:
        return ttext
    if not ttext:
        return ttitle
    return f"{ttitle} - {ttext}"
        
n = 233911588
# print(get_thread_title(n))
checkpoint = 0
with open('cute4.txt', 'r', encoding='utf-16', errors='ignore') as file: 
    count = 0
    
    for i in file:
        count += 1
        
        if count < checkpoint:
            print(count)
            pass
        else:
            timeStart = timeit.default_timer()
            info = get_thread_info(int(i.strip()))
            timeStop = timeit.default_timer()
            try:
                print(f"{info} [{timeStop - timeStart}s] [{count}]")
                with open('output4.txt', 'a') as file2:
                    file2.write(f"4chan org - Anime & Manga - {i.strip()} - {info}\n")
            except:
                print(f"{i} [{count}]")
       
        

    


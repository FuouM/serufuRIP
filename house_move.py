import shutil

prefix = '4chan org - Anime & Manga - '
source = f'D:\\1 My home\\Images\\biz\\Anime\\New folder\\New folder (4)\\New folder (2)\\{prefix}'

tid = [
]

# print(common)

current = 'Unsortable'.strip()
destination = f'D:\\1 My home\Images\\biz\Anime\\redemption\\1temp\\{current}\\'
for i in list(set(tid)):
    try:
        dest = shutil.move(f'{source}{i}', f'{destination}{prefix}{i}')
        print(dest)
    except:
        pass

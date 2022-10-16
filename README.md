# serufuRIP
*Sorting thousands of downloaded 4chan threads semi-automatically*


## Reason
If you are like me, you enjoy downloading images from 4chan (safe boards) and hoarding all those images. 

![datahoarding](/Assets/www1.png)

Some of them are properly named, most aren't (with random timecode filenames).

You can easiliy sort **named** images using many solutions out there, but **un-named** files proved to be very difficult to sort.

#### **What about using an image search api?**
Most searches will fail, saucenao limits 100 free requests per 24 hours. When you have hundred of thousands of images, it is virtually impractical.

#### **What about using a proper database like Hydrus?**

It is no good, because all it does well is removing duplicates, which can be done using tools like [dupeguru](https://github.com/arsenetar/dupeguru), file names are destroyed on import (can't use [Everything](https://www.voidtools.com/) to search). 

There is almost no info attatched to said images, so you can't tag them automatically and obviously, tagging 400.000 images is just crazy. It is just not convenient enough for shitposting.

### Is there any hope?

Yes! Through the power of Python, Excel/Google Sheets, and most importantly, desuarchive.

## Ze plan

1. Obtain the list of thread ids.
2. Obtain the title and OP text of said threads.
3. Sort and search for certain topics (Anime, character names,...)
4. Move folders of said threads to their corresponding new properly named folders.
5. Do manual searches using said new folders for images of topics you want.

It won't change the fact that most of those images are un-named. But the folders that they are in are **named** and sorted folders. That is infinitely more useful for shitposts.

### Additional notes

I'm retarded so this is definitely not the best way to do it. I could've had a system in place that attatch title-text info onto these threads. I'm just not gonna bother. The software I used to download these threads is JDownloader 2. I do several batch downloads of these threads once or twice a day. Most of it is inefficiently manual but it gives me the satisfaction.

## Actually doing it

### 1 - Obtain thread ids and put them into a txt file

This can easily be done using cmd or powershell.

`dir | Out-File [filename]` (I used `cute.txt`)

We can then remove all the unnecesary details using code or Notepad++. I used [Notepad2](https://github.com/zufuliu/notepad2).

We are left with 

![cute.txt](/Assets/www2.png)

### 2 - Obtain the title and OP text of said threads

I used the [requests](https://github.com/psf/requests) (to obtain the thread's html source) and [BeautifulSoup](https://code.launchpad.net/beautifulsoup) (to parse the html and extract title - text).

The code can be found in `serufu.py`

Turns out the the title is stored in the first `h2` element and the OP text is stored in the first `div text`.

I have no idea how html works.

After `requests` got the html, `BeautifulSoup (BS)` got  the title - text, we save that to a new text file

`output.txt` <-- this will be important.

This is what we get after running through every thread id stored in `cute.txt`

![output.txt](/Assets/www3.png)

### 3 - Sort and search for certain topics

For this we will use Excel/Sheets. I used Sheets

In the first pass, we will obtain all threads where the OP included the Anime/Topic in the title as the first thing. We do an alphabetical sort and separate them into a different sheet.

![sheets 1](/Assets/www4.png)

In the second pass we will search for said Anime/Topic in the title and/or OP text that wasn't picked up by our first pass. You can do this pass only but it is better to get what we are 100% on topic into the right folders.

```
=FIND(E2,LOWER(B2),1)
```


![sheets 2](/Assets/www5.png)

### 4 - Move folders to new named folders

Code can be found in `house_move.py` 

We copy the thread ids sorted from step 3 and move those threads to their new home. `shutil` module was used. I am amzed by how fast it took to move thousands of folders.

### 5 - Manual searches

This is pretty self explanatory.

## Final words

I own everything and I am happy. This was a good python exercise and I learned new things everyday. Thanks for visiting and reading this far. Watch Hidamari Sketch.

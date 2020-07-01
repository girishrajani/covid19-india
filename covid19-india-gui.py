from tkinter import *
import requests
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
URL = "https://www.mygov.in/covid-19"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
counter = soup.findAll(class_="iblock_text")
counter1 = soup.findAll(class_="info_title")
counts = soup.find(id="state-covid-data").get_text().strip()
as_of = counter1[0].get_text().strip()
active = counter[0].get_text().strip()
cured = counter[1].get_text().strip()
deaths = counter[2].get_text().strip()
root = Tk()

def openstates():
    top = Toplevel()
    states = []
    alldata = {}
    for count in soup.find_all(class_="st_name"): 
        states.append(count.get_text().strip())
    b=0
    for a in soup.find_all(class_="st_all_counts"):
        numbers = a.get_text()
        numbers = numbers.replace("\n","   ")
        alldata[states[b]] = numbers
        b=b+1
    
    top.geometry("1150x1000")
    top.title("States and UT Data")
    top.iconbitmap("covid.ico")
    Label(top, text ='States and UT Data',font = "150").pack() 
    Button(top,text="Exit", command=top.quit, font="100").pack()
    scroll_bar = Scrollbar(top) 
    scroll_bar.pack(side = RIGHT,fill = Y)
    mylist = Listbox(top,width="1000",height="1000",font="50", yscrollcommand = scroll_bar.set)  
    for x,y in alldata.items():
        mylist.insert(END,x)
        mylist.insert(END,y)  
        mylist.insert(END," ")
    mylist.pack( side = LEFT, fill = BOTH ) 
    scroll_bar.config( command = mylist.yview ) 

root.geometry("1150x1000") 
root.title("COVID-19 India")
root.iconbitmap("covid.ico")
Label(root, text=as_of,font="100").pack()
Label(root, text="",font="100").pack()
Label(root, text=active,font="50").pack()
Label(root, text="",font="100").pack()
Label(root, text=cured,font="50").pack()
Label(root, text="",font="100").pack()
Label(root, text=deaths,font="50").pack()
Label(root, text="",font="100").pack()
Button(root,text="Show States and UT Data", command=openstates, font="100").pack()
Label(root, text="",font="100").pack()
Button(root,text="Exit", command=root.quit, font="100").pack()
img = ImageTk.PhotoImage(Image.open("covid.jpg"))
panel = Label(root, image = img).pack()
root.mainloop()


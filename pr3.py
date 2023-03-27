from tkinter import *
import requests
from urllib.request import urlopen
from PIL import ImageTk,Image
import io
import webbrowser

class NewsApp:
    def __init__(self):
            # fetch data
            self.data=requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=07ce6431517e45c5b04b589c36e5bed6').json()
            #  GUI work
            self.loadGui()
           
            self.load_items(0) 

    def loadGui(self):
          self.root=Tk()
          self.root.geometry('350x600')
          self.root.resizable(0,0)
          self.root.title('InShort News App')
          self.root.config(background='#a2a8d3')    


    def clear(self):
           for i in self.root.pack_slaves():
                  i.destroy()

    def load_items(self,index):
        #   clear screen before item present
        self.clear()
        try:
        # if self.data['articles'][index]['urlToImage'] is not None:
            img_url=self.data['articles'][index]['urlToImage']
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo=ImageTk.PhotoImage(im)

        except:
            img_url='https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930'
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo=ImageTk.PhotoImage(im)


        Label(self.root,image=photo).pack()



        heading=Label(self.root,text=self.data['articles'][index]['title'],background='#a2a8d3',foreground='black', wraplength=350,justify='center') 
        heading.config(font=('verdana',15))
        heading.pack(pady=(10,20))
        
        details=Label(self.root,text=self.data['articles'][index]['description'],background='#a2a8d3',foreground='black', wraplength=350,justify='center') 
        details.config(font=('verdana',12))
        details.pack(pady=(10,20))


        frame=Frame(self.root,background='#a2a8d3').pack(expand=True,fill=BOTH)

        if index != 0:
            prev=Button(frame,text="Previous",width=12,height=3,command=lambda : self.load_items(index-1)).pack(side=LEFT)

        read=Button(frame,text="Read More",width=12,height=3,command=lambda : self.open_link(self.data['articles'][index]['url'])).pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            next=Button(frame,text="Next",width=12,height=3,command=lambda : self.load_items(index+1)).pack(side=LEFT)

  


        self.root.mainloop()   
             

    def open_link(self,url):
          webbrowser.open(url)

obj=NewsApp()
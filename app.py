from tkinter import *
import tkinter as tk
import requests

wd = tk.Tk()
wd.title("Pythontpoint")
wd.geometry('500x400')



def search():
        user_name = user.get()
        url = f"https://www.instagram.com/{user_name}/?__a=1"
        
        dataofinsta = requests.get(url).json()
        print(dataofinsta)



        def pic():
                import webbrowser
                d1 = dataofinsta['graphql']['user']['profile_pic_url']
                webbrowser.open(d1)


        if details.get(1.0,END) != "":
                details.delete(1.0,END)
                details.insert(1.0,f"\t username : {dataofinsta['graphql']['user']['username']} \n     followers : {dataofinsta['graphql']['user']['edge_followed_by']['count']}      following : {dataofinsta['graphql']['user']['edge_follow']['count']} \n   full name : {dataofinsta['graphql']['user']['full_name']} \n Total post : {dataofinsta['graphql']['user']['edge_owner_to_timeline_media']['count']}  category : {dataofinsta['graphql']['user']['category_enum']} \nbio-link:{dataofinsta['graphql']['user']['external_url']}private account:{dataofinsta['graphql']['user']['is_private']} || verified account:{dataofinsta['graphql']['user']['is_verified']}  bussiness account:{dataofinsta['graphql']['user']['is_business_account']}  \n \n   see profile picture" )



                Button(innerframe1,text="ClickMe to see",relief=RAISED,borderwidth=3,font=('Times New Roman',10,'bold'),bg='white',fg="black",command=pic).place(x=180,y=145)
        



frame1 = Frame(wd,width=600,height=400,relief=RIDGE,borderwidth=5,bg='#248aa2')
frame1.place(x=0,y=0)

innerframe = LabelFrame(frame1,width=480,height=80,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe.place(x=5,y=5)


user = Entry(frame1,width=30,relief=RIDGE,borderwidth=3)
user.place(x=70,y=15)

search = Button(frame1,text="Search",relief=RAISED,borderwidth=2,font=('verdana',8,'bold'),bg='#248aa2',fg="black",command=search)
search.place(x=270,y=15)


innerframe = LabelFrame(frame1,width=380,height=240,relief=RIDGE,borderwidth=3,bg='#248aa2',highlightbackground="white", highlightcolor="white", highlightthickness=2)
innerframe.place(x=5,y=45)


innerframe1 = LabelFrame(innerframe,text="Username Information",width=370,height=230,highlightbackground="white", highlightcolor="white", highlightthickness=5,font=('verdana',10,'bold'))
innerframe1.place(x=0,y=0)


details = Text(innerframe1,height=12,width=47,relief=RIDGE,borderwidth=5,highlightbackground="white", highlightcolor="white",font=('courier',9,''))
details.place(x=5,y=5)

wd.mainloop()
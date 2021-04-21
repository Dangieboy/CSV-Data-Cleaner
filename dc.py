import tkinter as tk
import pandas as pd
import tkinter,tkinter.messagebox
import numpy as np
from tkinter import *




main = tk.Tk()
w, h= main.winfo_screenwidth(), main.winfo_screenheight()
main.geometry("%dx%d+0+0" % (w, h))
main.configure(background='green')


def read(*args):
    #try:
        k=ee2.get()
        dfi=ee1.get()

        if len(dfi)<1:
             tkinter.messagebox.showwarning \
                 ("Warning", "Please enter a link !  ")
        elif len(k) < 1:
             tkinter.messagebox.showwarning \
                ("Warning", "Please enter the name of the new file ! ")

        else:
       #   try:
             dfi=str(dfi)
             df=pd.read_csv(dfi)


             def clean1():


                ##get rows columns and elements
                rowc=len(df)
                rowc=str(rowc)
                colc=len(df.columns)
                colc=str(colc)
                elem=df.size
                elem=str(elem)
                ##general info box###

                gi=tk.Label(main,text=' General information:',width=20,font=('Times ',21,'bold' ),fg='white',bg='green')
                gi.place(rely=0.04,relx=0.0023)
                cl1=tk.Label(main,text='columns: '+colc,width=20,height=2,font=('Times ',18,'bold'),fg='white',bg='green')
                cl1.place(rely=0.1,relx=0.00655)
                cl2=tk.Label(main,text='rows: '+rowc,width=20,height=2,font=('Times ',18,'bold'),fg='white',bg='green' )

                cl2.place(rely=0.17,relx=0.000015)
                cl3=tk.Label(main,text='total elements: '+elem,width=20,height=2,font=('Times ',18,'bold'),fg='white',bg='green' )
                #cl3.configure(background='wheat')
                cl3.place(rely=0.24,relx=0.03)


                ### Main df###########################




            #############datatypes
                def dfr():
                    class viw1:
                        def __init__(self):
                            # def dft():self.
                            self.main5 = tk.Tk()
                            w, h = self.main5.winfo_screenwidth(), self.main5.winfo_screenheight()
                            self.main5.geometry("%dx%d+0+0" % (w, h))
                            self.main5.configure(background='green')

                            self.vsb = tk.Scrollbar(self.main5, orient="vertical", command=self.OnVsb)
                            self.vsb.pack(side="right", fill="y")

                            self.tkl = tk.Text(self.main5, width=200, height=100, font=('Times ', 15, 'bold'), bg='green',
                                               yscrollcommand=self.vsb.set)

                            with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
                                self.tkl.insert(END, df)

                            self.tkl.pack()

                        def OnVsb(self, *args):
                            self.tkl.yview(*args)

                    viw1()

                   #change astype

                def f():
                    class viw1:
                        def __init__(self):
                            # def dft():
                            self.main2 = tk.Tk()
                            ###scrollbar##########

                            # this prevents default bindings from firing, which
                            # would end up scrolling the widget twice

                            self.vsb = tk.Scrollbar(self.main2, orient="vertical", command=self.OnVsb)
                            self.vsb.pack(side="right", fill="y")
                            l = []
                            dft = df.dtypes
                            l.append(dft)
                            for dft in l:
                                dft = str(dft)

                            self.tkl2 = tk.Text(self.main2, width=40, height=20, font=('Times ', 15, 'bold'), yscrollcommand=self.vsb.set)

                            for l in dft:
                                self.tkl2.insert(END, l)

                            self.tkl2.pack(side=LEFT, fill=Y)

                        def OnVsb(self, *args):
                            self.tkl2.yview(*args)

                    viw1()
                def change():
                        main3=tk.Tk()
                        w, h= main3.winfo_screenwidth(), main3.winfo_screenheight()
                        main3.geometry("%dx%d+0+0" % (w, h))
                        main3.configure(background='green')
                        def ende():
                             main3.destroy()

                        def cch():

                            b1.destroy()
                            b2.destroy()
                            ##change column names##

                            ec1=tk.Entry (main3,width=20,font=('Times ',15,'bold'))
                            lc1=tk.Label(main3,text='current column name:',width=18,height=2,font=('Times ',15,'bold'),bg='green')
                            lc2=tk.Label(main3,text='new column name:    ',width=18,height=2,font=('Times ',15,'bold'),bg='green')
                            ec2=tk.Entry (main3,width=20,font=('Times ',15,'bold'))
                            te=tk.Text(main3,width=50,height=30,font=('Times ',15,'bold'))

                            dft=df.columns.values
                            te.insert(END,dft)
                            te.pack()

                            #func to rename columns######
                            def ccn():

                                g1=ec1.get()
                                g2=ec2.get()
                                if g1 in df.columns:
                                        df.rename(columns={g1:g2},inplace=True)
                                        df.to_csv(k)
                                        con= tk.Label(main3,text='column has been renamed',width=25,font=('Times ',17,'bold'),height=2,bg='green')
                                        con.place(relx=0.13,rely=0.25)






                                elif g1 not in df.columns:
                                    warn= tk.Label(main3,text='column could not be found',width=25,font=('Times ',17,'bold'),height=2,bg='red')
                                    warn.place(relx=0.13,rely=0.25)


                            conf1= tk.Button(main3,text='confirm changes',width=15,font=('Times ',17,'bold'),height=2,bg='grey',command=ccn)
                            conf1.place(relx=0.17,rely=0.17)

                            lc1.place(relx=0.05,rely=0.05)
                            ec1.place(relx=0.17,rely=0.06)
                            lc2.place(relx=0.0475,rely=0.1)
                            ec2.place(relx=0.17,rely=0.11)

                            ##change astype####
                        def cat():

                              b1.destroy()
                              b2.destroy()


                             ##entry##labels###

                              ek1=tk.Entry (main3,width=20,font=('Times ',15,'bold'))
                              le1=tk.Label(main3,text='convert data type in column:',width=25,height=2,font=('Times ',15,'bold'),bg='green')

                              le2=tk.Label(main3,text='new datatype must be: int, float or object',width=35,height=2,font=('Times ',15,'bold'),bg='green')
                              rb1=tk.Entry(main3,width=10,font=('Times ',15,'bold'))

                              def rel():

                                      def OnVsb(*args):
                                        tkl3.yview(*args)
                                      vsb = tk.Scrollbar(main3,orient="vertical", command=OnVsb)
                                      vsb.pack(side="right",fill="y")
                                      l=[]
                                      dft=df.dtypes
                                      l.append(dft)
                                      for dft in l:
                                            dft=str(dft)
                                      #  self.tkl1=tk.Text(self.main2,width=20,height=20,font=('Times ',15,'bold'), yscrollcommand = self.vsb.set)
                                      tkl3=tk.Text(main3,width=30,height=20,font=('Times ',15,'bold'), yscrollcommand = vsb.set)

                                      for l in dft:
                                            tkl3.insert(END,l)
                                      tkl3.pack(side=RIGHT,fill=Y)


                              rel()



                              class convert:
                                def __init__(self):
                                 def cas():
                                  try:
                                      col=ek1.get()
                                      ast=rb1.get()

                                      df[col]=df[col].astype(ast)
                                      df.to_csv(k)
                                      self.con= tk.Label(main3,text='column type has been changed ',width=45,font=('Times ',13,'bold'),height=2,bg='green')
                                      self.con.place(relx=0.13,rely=0.25)

                                  except:
                                      self.warn2= tk.Label(main3,text='could not convert this data type please try another type',width=45,font=('Times ',13,'bold'),height=2,bg='red')
                                      self.warn2.place(relx=0.13,rely=0.25)

                                 cas()
                              conf2= tk.Button(main3,text='confirm changes',width=15,font=('Times ',17,'bold'),height=2,bg='grey',command=convert)
                              conf2.place(relx=0.17,rely=0.17)

                              le1.place(relx=0.05,rely=0.05)
                              ek1.place(relx=0.22,rely=0.06)
                              le2.place(relx=0.0475,rely=0.1)
                              rb1.place(relx=0.275,rely=0.11)

                        b1=tk.Button(main3,text='change column names',width=20,height=2,font=('Times ',20,'bold'),borderwidth=5,relief='solid',command=cch)
                        b1.pack(pady=50)
                        b2=tk.Button(main3,text='change data types',width=20,height=2,font=('Times ',20,'bold'),borderwidth=5,relief='solid',command=cat)
                        b2.pack(pady=50)

                ###change column order index########
                def ind():
                        main4 = tk.Tk()
                        w, h = main4.winfo_screenwidth(), main4.winfo_screenheight()
                        main4.geometry("%dx%d+0+0" % (w, h))
                        main4.configure(background='green')
                   

                        def conf():

                            try:
                                e1 = ek1.get()
                                l = []
                                e1 = e1.split(',')
                                l.append(e1)
                                df.columns = l
                                df.to_csv(k)
                                warn = tk.Label(main4, text='the column order has been successfully changed ', width=45,font=('Times ', 13, 'bold'), height=2, bg='green')
                                warn.place(relx=0.13, rely=0.25)
                            except:
                                warn = tk.Label(main4, text='could not change the columns please check your entry',
                                                width=45, font=('Times ', 13, 'bold'), height=2, bg='red')
                                warn.pack(pady=5)

                        le2 = tk.Label(main4,
                                       text='remember that false inputs like wrong column names get saved, so make sure to copy the columns from the textbox below without the brackets !',
                                       width=130, height=2, font=('Times ', 13, 'bold'),bg='yellow')
                        le1 = tk.Label(main4,
                                       text='type in all columns in the correct order; make sure that they are all separated with a comma; example:column1,column2',
                                       width=130, height=1, font=('Times ', 15, 'bold'),bg='green')
                        ek1 = tk.Entry(main4, width=100, font=('Times ', 15, 'bold'))
                        cf = tk.Button(main4, text='confirm changes', width=15, font=('Times ', 17, 'bold'), height=2,
                                       bg='grey', command=conf)
                        te = tk.Text(main4, width=70, height=20, font=('Times ', 15, 'bold'))

                        dft = df.columns
                        dft = str(dft)
                        dft2 = dft.replace("‘", '').replace("’", '').replace("'", '')
                        te.insert(END, dft2)


                        le1.pack(pady=10)
                        le2.pack(pady=10)
                        ek1.pack(pady=10)
                        te.pack(pady=10)
                        cf.pack(pady=10)

                    #b1 = tk.Button(main4, text='change column order', width=20, height=2, font=('Times ', 17, 'bold'),relief="solid",borderwidth=5,command=colo)
                    #b1.pack(pady=20)

                def qc():
                    main4 = tk.Tk()
                    w, h = main4.winfo_screenwidth(), main4.winfo_screenheight()
                    main4.geometry("%dx%d+0+0" % (w, h))
                    main4.configure(background='green')
                    def qcd():
                        try:
                            df.replace("?", np.nan, inplace=True)
                            df.dropna(inplace=True)
                            df.to_csv(k)
                            con = tk.Label(main4, text='successfully executed quick cleaning!', width=45, font=('Times ', 25, 'bold'), height=2,
                                                bg='green')
                            con.pack( pady=10)

                            rowc = len(df)
                            rowc = str(rowc)
                            cl2 = tk.Label(main, text='rows: ' + rowc, width=20, height=2, font=('Times ', 18, 'bold'), fg='white', bg='green')

                            cl2.place(rely=0.17, relx=0.000015)

                        except:
                                con = tk.Label(main4, text='could not quick clean your data', width=45, font=('Times ', 13, 'bold'), height=2,
                                              bg='red')
                                con.pack( pady=10)

                    qc1=tk.Label(main4,bg='green',text='"qucik cleaning" simply deletes all rows with missing values in it ',width=50,
                                 height=2, font=('Times ', 20, 'bold'))
                    qc1.pack(pady=20)
                    qc2 = tk.Label(main4, width=50, height=2,text='you cannot withdraw your deleted data!',font=('Times ', 20, 'bold'),bg='yellow')
                    qc2.pack(pady=20)
                    con=tk.Button(main4,text='quick clean',width=50, height=2,font=('Times ', 20, 'bold'),bg='red',command=qcd)
                    con.pack(pady=20)

                def drop():
                        main4 = tk.Tk()
                        w, h = main4.winfo_screenwidth(), main4.winfo_screenheight()
                        main4.geometry("%dx%d+0+0" % (w, h))
                        main4.configure(bg="green")

                        def mis():
                            class viw1:
                                def __init__(self):
                                    self.main4 = tk.Tk()
                                    self.main4.configure(background='green')

                                    self.vsb = tk.Scrollbar(self.main4, orient="vertical", command=self.OnVsb)
                                    self.vsb.pack(side="right", fill="y")

                                    self.l1 = tk.Label(self.main4, text="missing values in the columns below", width=35, height=2,
                                                       font=('Times ', 17, 'bold'), bg="green")
                                    self.tkl1 = tk.Text(self.main4, width=30, height=15, font=('Times ', 20, 'bold'))
                                    df.replace("?", np.nan, inplace=True)

                                    missing = df.columns[df.isnull().any()].values  #
                                    self.tkl1.insert(END, missing)
                                    self.l1.pack(pady=10)
                                    self.tkl1.pack(pady=20)

                                def OnVsb(self, *args):
                                    self.tkl1.yview(*args)

                            viw1()

                        #replace drop values####

                        def repl ():

                            b1.destroy()
                            b2.destroy()
                            b3.destroy()


                            lc0 = tk.Label(main4, text='The replacement only works for numeric values!', width=50, height=2,
                                           font=('Times ', 15, 'bold'), bg='green')

                            lc1 = tk.Label(main4, text=' column name:', width=23, height=2, font=('Times ', 15, 'bold'), bg='green')
                            lc2 = tk.Label(main4, text='data type of column: int/float', width=23, height=2, font=('Times ', 15, 'bold'), bg='green')
                            ec1 = tk.Entry(main4, width=20, font=('Times ', 15, 'bold'))
                            ec2 = tk.Entry(main4, width=20, font=('Times ', 15, 'bold'))
                            ##replace mean##
                            def cO():
                              try:
                                cn=ec1.get()
                                at=ec2.get()
                                df.replace("?", np.nan, inplace=True)
                                mean = df[cn].astype(at).mean()
                                df[cn].replace(np.nan, mean, inplace=True)
                                df.to_csv(k)
                                con = tk.Label(main4 ,text='data has been replaced', width=25, font=('Times ', 17, 'bold'), height=2, bg='green')
                                con.place(relx=0.13, rely=0.17)

                              except:

                                  con2 = tk.Label(main4, text='could not replace data', width=25, font=('Times ', 17, 'bold'), height=2, bg='red')
                                  con2.place(relx=0.13, rely=0.17)
                                #drop########
                            def dru():
                              try:
                                cn = ec1.get()
                                df.dropna(subset=[cn],axis=0,inplace=True)
                                df.to_csv(k)
                                con = tk.Label(main4, text='data has been dropped', width=25, font=('Times ', 17, 'bold'), height=2, bg='green')
                                con.place(relx=0.13, rely=0.17)

                                rowc = len(df)
                                rowc = str(rowc)
                                cl1 = tk.Label(main, text='columns: ' + colc, width=20, height=2, font=('Times ', 18, 'bold'), fg='white', bg='green')
                                cl1.place(rely=0.1, relx=0.00655)
                                cl2 = tk.Label(main, text='rows: ' + rowc, width=20, height=2, font=('Times ', 18, 'bold'), fg='white', bg='green')

                                cl2.place(rely=0.17, relx=0.000015)
                              except:

                                con2 = tk.Label(main4, text='data could not be dropped', width=25, font=('Times ', 17, 'bold'), height=2, bg='red')
                                con2.place(relx=0.13, rely=0.17)

                            C = tk.Button(main4, text="replace with the mean value of the column",bg='grey', width=45, height=2, font=('Times ', 17, 'bold')
                                          , command=cO)

                            C2=tk.Button(main4,text="drop rows with missing values in the column",
                                         bg='grey', width=45, height=2, font=('Times ', 17, 'bold'),command=dru)

                            C.place(relx=0.17,rely=0.25)
                            C2.place(relx=0.17,rely=0.35)
                            lc0.pack()
                            lc1.place(relx=0.05, rely=0.05)
                            ec1.place(relx=0.21, rely=0.06)
                            lc2.place(relx=0.05, rely=0.1)
                            ec2.place(relx=0.21, rely=0.11)

                        def drc():
                            b1.destroy()
                            b2.destroy()
                            b3.destroy()

                            ec1 = tk.Entry(main4, width=20, font=('Times ', 15, 'bold'))
                            def dro():
                              try:
                                cn=ec1.get()
                                df.drop(columns=cn,inplace=True)
                                df.to_csv(k)
                                colc = len(df.columns)
                                colc = str(colc)
                                con = tk.Label(main4, text='column has been dropped', width=25, font=('Times ', 17, 'bold'), height=2, bg='green')
                                con.place(relx=0.5,rely=0.5)
                              except:
                                  con2 = tk.Label(main4, text='column could not be dropped', width=25, font=('Times ', 17, 'bold'), height=2, bg='red')
                                  con2.place(relx=0.4,rely=0.4)

                            C5 = tk.Button(main4, text="drop the entered column",
                                           bg='grey', width=45, height=2, font=('Times ', 17, 'bold'), command=dro)
                            ec1.pack(pady=30)
                            C5.pack(pady=30)

                        b1 = tk.Button(main4, text="see missing values", width=35, height=2, font=('Times ', 17, 'bold'),borderwidth=5,relief='solid', command=mis)
                        b1.pack(pady=20)
                        b2 = tk.Button(main4, text="replace/drop missing values in rows", width=35,borderwidth=5,relief='solid', height=2, font=('Times ', 17, 'bold'),command=repl)
                        b2.pack(pady=20)
                        b3 = tk.Button(main4, text="drop columns", width=35,borderwidth=5,relief='solid',height=2, font=('Times ', 17, 'bold'),command=drc)
                        b3.pack(pady=20)


                ####main menu buttons######

                mb1=tk.Button(main,text='see the whole dataframe',width=27,height=2,font=('Times ',20,'bold'),relief='solid',borderwidth=5,command=dfr)
                mb1.pack(pady=25)

                mb2=tk.Button(main,text='identify data types/columns',width=27,height=2,font=('Times ',20,'bold'),relief='solid',borderwidth=5,command=f)
                mb2.pack(pady=25)
                main.unbind('<Return>')

                mb3=tk.Button(main,text='change data types/column names',width=27,height=2,font=('Times ',20,'bold'),relief='solid',borderwidth=5,command=change)
                mb3.pack(pady=25)

                mb4 = tk.Button(main, text='manage column order', width=27, height=2, font=('Times ', 20, 'bold'),relief='solid',borderwidth=5, command=ind)
                mb4.pack(pady=25)

                mb5 = tk.Button(main, text='drop/replace missing values', width=27, height=2, font=('Times ', 20, 'bold'), relief='solid',
                                borderwidth=5,command=drop)
                mb5.pack(pady=25)

                mb5 = tk.Button(main, text='quick clean', width=27, height=2, font=('Times ', 20, 'bold'), relief='solid',
                                borderwidth=5, command=qc)
                mb5.pack(pady=25)
      #  df=pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/module_5_auto.csv')
             l1.destroy()
             ee1.destroy()
             bb1.destroy()
             ee2.destroy()
             bb2.destroy()
             bb3.destroy()
             clean1()
    #except:
     #   tkinter.messagebox.showwarning \
      #      ("Warning","Invalid data path/link ")
# main window first#######
l1=tk.Label(main,text='enter your path or link:',width=35,font=('Times ',23,'bold' ),bg='green')




#df=pd.read_csv( "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv")
ee1=tk.Entry(main,width=70,bg="white",font=( 'Times ',15,'bold' ))


ee2=tk.Entry(main,width=70,bg="white",font=( 'Times ',15,'bold' ))

bb1=tk.Button(main,text='get started',command=read,height=1,width=20,bg="white",font=( 'Times ',20,'bold' ),relief='solid',borderwidth=1)

bb2=tk.Label(main,text='name of the new file:',height=1,width=20,font=( 'Times ',23,'bold' ),bg='green')
bb3=tk.Label(main,text='you can also choose a dot ending like: .csv',height=1,width=40,font=( 'Times ',12,'bold' ),bg='green')
l1.pack(pady=30)
ee1.pack(pady=20)
bb2.pack(pady=20)
bb3.pack(pady=20)
ee2.pack(pady=20)
bb1.pack(pady=20)
main.bind('<Return>', read)


main.mainloop()

        






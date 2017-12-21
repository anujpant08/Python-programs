import pymysql
import datetime
from tkinter import *

class prog:

    def __init__(self):
        root=Tk( )
        frame = Frame(root)
        frame.pack()

        labeltitle = Label(root, text = "Welcome to Python Car Mechanics")
        labeltitle.place( x=150,y=100)

        def callbackupdt():
            db = pymysql.connect("localhost","root","chelsea22","automobilebooking" )
            root=Tk( )
            frame = Frame(root)
            frame.pack()

            labelid= Label(root, text = "Original 4-Digit ID")
            labelid.place( x=0,y=20)
            textid = Entry(root, bd = 5)
            textid.place(x=110,y=20)
            labelid= Label(root, text = "New 4-Digit ID")
            labelid.place( x=0,y=80)
            textnewid = Entry(root, bd = 5)
            textnewid.place(x=110,y=80)

            def callbackupdtdisp():


                id=textid.get()
                newid=textnewid.get()
                cursor=db.cursor()
                sqlupdate="UPDATE carwash SET id='%s' WHERE id='%s'" % (newid,id)

                try:
                   top = Tk()
                   # Execute the SQL command
                   #print(id)
                   cursor.execute(sqlupdate)
                   db.commit()

                   labeltitle= Label(top, text = "Data updated successfully.")
                   labeltitle.place( x=25,y=50)
                   top.geometry('{}x{}'.format(200, 100))
                   top.mainloop()

                except:
                   #db.rollback()
                   top = Tk()

                   labeltitle= Label(top, text = "Error! Check the details you entered.")
                   labeltitle.place( x=25,y=50)

                   top.geometry('{}x{}'.format(300, 200))
                   top.mainloop()
                   print ("Error: Inavalid ID.")


            B = Button(root, text = "Submit", command=callbackupdtdisp)
            B.place(x = 100, y = 130)

            root.geometry('{}x{}'.format(250, 200))
            root.mainloop()
            db.close()



        def callbackrec():

            db = pymysql.connect("localhost","root","chelsea22","automobilebooking" )

            root=Tk( )
            frame = Frame(root)
            frame.pack()

            labelid= Label(root, text = "4-Digit ID")
            labelid.place( x=10,y=20)
            textid = Entry(root, bd = 5)
            textid.place(x=50,y=50)

            def callbackdisp():

                id=textid.get()
                cursor=db.cursor()
                sqlselect = "SELECT * FROM carwash WHERE id='%s'" % (id)
                sqldel="DELETE FROM carwash WHERE id='%s'" % (id)

                try:
                   cursor.execute(sqlselect)
                   results = cursor.fetchall()

                   for row in results:
                       idno = row[0]
                       name = row[1]
                       date = row[2]
                       prob = row[3]
                       price = row[4]
                       #print(idno, name, date, prob,price)
                       # Now display fetched result

                   top = Tk()
                   labelid= Label(top, text = "4-Digit ID")
                   labelid.place( x=50,y=50)
                   labeli= Label(top, text = idno)
                   labeli.place( x=150,y=50)


                   labeluser = Label(top, text = "Name")
                   labeluser.place( x=50,y=100)
                   labelu= Label(top, text = name)
                   labelu.place( x=150,y=100)

                   labeldate = Label(top, text = "Date")
                   labeldate.place(x=50,y=150)
                   labeld= Label(top, text = date)
                   labeld.place( x=150,y=150)

                   labelprob = Label(top, text = "Problem")
                   labelprob.place(x=50,y=200)
                   labelp= Label(top, text = prob)
                   labelp.place( x=150,y=200)

                   labelprice = Label(top, text = "Price")
                   labelprice.place(x=50,y=250)
                   labelpr= Label(top, text = price)
                   labelpr.place( x=150,y=250)

                   #DELETE RECORD FROM TABLE AFTER RECIEVING THE CAR
                   cursor.execute(sqldel)
                   db.commit()

                   top.geometry('{}x{}'.format(300, 300))
                   top.mainloop()

                except:
                   db.rollback()
                   top = Tk()

                   labeltitle= Label(top, text = "Error! Check the details you entered.")
                   labeltitle.place( x=25,y=50)

                   top.geometry('{}x{}'.format(250, 100))
                   top.mainloop()
                   print ("Error: Inavalid ID.")


            B = Button(root, text = "Submit", command=callbackdisp)
            B.place(x = 100, y = 100)


            root.geometry('{}x{}'.format(250, 200))
            root.mainloop()
            db.close()


        def callbackfix():
            root=Tk( )
            frame = Frame(root)
            frame.pack()

            labelid= Label(root, text = "4-Digit ID")
            labelid.place( x=50,y=50)
            textid = Entry(root, bd = 5)
            textid.place(x=180,y=50)

            labeluser = Label(root, text = "Name")
            labeluser.place( x=50,y=100)
            textuser = Entry(root, bd = 5)
            textuser.place(x=180,y=100)

            labeldate = Label(root, text = "Date (YYYY-MM-DD)")
            labeldate.place(x=50,y=150)
            textdate = Entry(root, bd = 5)
            textdate.place(x=180,y=150)

            def callbackengine():
                self.engine(int(textid.get()),textuser.get(),textdate.get(),"ENGINE",2000)

            def callbackbreak():
                self.breaking(int(textid.get()),textuser.get(),textdate.get(),"BREAKING",3000)

            def callbacktrans():
                self.transmission(int(textid.get()),textuser.get(),textdate.get(),"TRANSMISSION",2500)

            def callbackfull():
                self.analysis(int(textid.get()),textuser.get(),textdate.get(),"FULL ANALYSIS",7000)


            B = Button(root, text = "ENGINE", command=callbackengine)
            B.place(x = 50, y = 200)

            B = Button(root, text = "BREAKING",command=callbackbreak)
            B.place(x = 120, y = 200)

            B = Button(root, text = "TRANSMISSION",command=callbacktrans)
            B.place(x = 200, y = 200)

            B = Button(root, text = "FULL ANALYSIS",command=callbackfull)
            B.place(x = 320, y = 200)

            root.geometry('{}x{}'.format(500, 500))
            root.mainloop()

        Bfix = Button(root, text = "Fix a problem", command=callbackfix)
        Bfix.place(x = 80, y = 200)

        Brecieve = Button(root, text = "Recieve fixed car", command=callbackrec)
        Brecieve.place(x = 180, y = 200)

        Bupdt = Button(root, text = "Update details", command=callbackupdt)
        Bupdt.place(x = 300, y = 200)

        #setting dimensions for the window
        root.geometry('{}x{}'.format(500, 400))
        root.mainloop()

    def engine(self,id,name,date,problem,price):

        db = pymysql.connect("localhost","root","chelsea22","automobilebooking" )

        cursor=db.cursor()

        sqlselect = "SELECT * FROM carwash"

        sqlinsert="INSERT INTO carwash VALUES ('%d', '%s', '%s', '%s', '%d' )" % \
          (id, name, date, problem,price)

        try:
           top = Tk()
           # Execute the SQL command
           print("Connected")
           cursor.execute(sqlinsert)
           db.commit()


           labeltitle= Label(top, text = "Problem submitted successfully!")
           labeltitle.place( x=25,y=50)

           top.geometry('{}x{}'.format(250, 100))
           top.mainloop()

           # Fetch all the rows in a list of lists.

        except:
           db.rollback()
           top = Tk()

           labeltitle= Label(top, text = "Error! Check the details you entered.")
           labeltitle.place( x=25,y=50)

           top.geometry('{}x{}'.format(250, 100))
           top.mainloop()
           print ("Error: Check the details entered.")
        db.close()

    def breaking(self,id,name,date,problem,price):

        db = pymysql.connect("localhost","root","chelsea22","automobilebooking" )

        cursor=db.cursor()

        sqlselect = "SELECT * FROM carwash"

        sqlinsert="INSERT INTO carwash VALUES ('%d', '%s', '%s', '%s', '%d' )" % \
          (id, name, date, problem,price)

        try:
           top = Tk()
           # Execute the SQL command
           print("Connected")

           cursor.execute(sqlinsert)
           db.commit()
           labeltitle= Label(top, text = "Problem submitted successfully!")
           labeltitle.place( x=25,y=50)
           top.geometry('{}x{}'.format(250, 100))
           top.mainloop()
           # Fetch all the rows in a list of lists.

        except:
           top=Tk()
           db.rollback()
           print ("Error: Check the details entered.")
           top.geometry('{}x{}'.format(250, 100))
           top.mainloop()
        db.close()


    def transmission(self,id,name,date,problem,price):

        db = pymysql.connect("localhost","root","chelsea22","automobilebooking" )

        cursor=db.cursor()

        sqlselect = "SELECT * FROM carwash"

        sqlinsert="INSERT INTO carwash VALUES ('%d', '%s', '%s', '%s', '%d' )" % \
          (id, name, date, problem,price)

        try:
           top = Tk()
           # Execute the SQL command
           print("Connected")

           cursor.execute(sqlinsert)
           db.commit()
           labeltitle= Label(top, text = "Problem submitted successfully!")
           labeltitle.place( x=25,y=50)
           top.geometry('{}x{}'.format(250, 100))
           top.mainloop()
           # Fetch all the rows in a list of lists.

        except:
           top=Tk()
           db.rollback()
           print ("Error: Check the details entered.")
           top.geometry('{}x{}'.format(250, 100))
           top.mainloop()
        db.close()



    def analysis(self,id,name,date,problem,price):

        db = pymysql.connect("localhost","root","chelsea22","automobilebooking" )

        cursor=db.cursor()

        sqlselect = "SELECT * FROM carwash"

        sqlinsert="INSERT INTO carwash VALUES ('%d', '%s', '%s', '%s', '%d' )" % \
          (id, name, date, problem,price)

        try:
           top = Tk()
           # Execution of the SQL command
           print("Connected")
           cursor.execute(sqlinsert)
           db.commit()
           labeltitle= Label(top, text = "Problem submitted successfully!")
           labeltitle.place( x=25,y=50)
           top.geometry('{}x{}'.format(250, 100))
           top.mainloop()

        except:
           top=Tk()
           print ("Error: Check the details entered.")
           top.geometry('{}x{}'.format(250, 100))
           top.mainloop()
           db.rollback()
        db.close()

ob=prog()

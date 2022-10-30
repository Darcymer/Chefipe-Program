# darcy merilan database... please note this is a work in progress and does not illustrate my full understanding of python and sql
import sqlite3

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute('''CREATE Table style (
              ID INT PRIMARY KEY     NOT NULL,
              style_name text NOT NULL
              )''')

cur.execute('''CREATE TABLE recipie (
             ID INT PRIMARY KEY     NOT NULL,
             r_name   text NOT NULL,
             calories real
             )''')

cur.execute("""CREATE TABLE Ingrediants (
              ID INT PRIMARY KEY     NOT NULL,	
 	          Name     text NOT NULL,
 	          Price    real,
 	          Amount   real,
 	         Measurement   text 
 	        )""")

con.commit

class recipebook:
    def __init__(self):
        self.menu_option = int(input("what is your selection?"))

    def menu():
        print(" ")
        print("Welcome to Your Cheif Recipie Table, Please Select the following:")
        print(" ")
        print ("0. Exit Program")
        print("1. Show all Recipes")
        print("2. Show all Base")
        print("3. Insert Base")
        print("4. Delete Base")
        print("5. Insert Recipe")
        print("6. Delete Recipe")
        print("7. Insert Ingrediant")
        print("8. Delete Ingrediant")
        print("9. Modify Ingrediant")

    def option_0():
        print(" ")
        print("Thank you for trying out my program")
        print(" ")
        con.close

    def option_1():
        try:
            cur.execute("SELECT * FROM recipie")
            con.commit
        except:
            print (" Oh, we cannot seem to find your recipie please insert a recipie into the list!")
  

    def option_2():
        try:
            cur.execute("SELECT * FROM style")
            con.commit()
            print(cur.fetchall())
        except:
            print (" Oh, we cannot seem to find your Base please insert the name of the Base for your recipie into the list!")

    def option_3():
        try:
            id_num = int(input("Whats the ID #:"))
            s_name = input("What is the Style name: ")
            cur.execute("INSERT INTO style (ID, style_name) values ('{}');").format(id_num,s_name)
            con.commit
            print(cur.fetchall())
        except:
            print (" Oh, we cannot seem to find your recipie please insert the name of the recipie below to list it!")
        
    def option_4():
        # This is the delete option, i am trying to solve how to delete trough a user input
        #cur.execute("Delete From style where ('{}');")
        pass

    def option_5():
        try:
            id_num = int(input("Whats the ID #:"))
            re_name = input("What is the recipe's name: ")
            calo = int(input("What is the recipe's calories: "))
            cur.execute("INSERT INTO recipie (ID , r_name, calories) values ('{}','{}');").format(id_num,re_name, calo)
            con.commit
            print(cur.fetchall())
        except:
            print (" Oh, we cannot seem to find your recipie please insert the name of the recipie below to list it!")

        
    def option_6():
        # This is the delete option, i am trying to solve how to delete trough a user input
        #cur.execute("Delete From recipie where ('{}');")
        pass

    def option_7():
        try:
            id_num = int(input("Whats the ID #:"))
            in_name = input("What is the ingrediants's name: ")
            pri = float(input("What is the ingrediants's prince: "))
            amo = float(input("How much do you need: "))
            meas = input("What is the measurment: ")
            cur.execute("INSERT INTO Ingrediants (ID ,Name, Price,Amount,Measurement)values ('{}','{}','{}','{}','{}');").format(id_num,in_name, pri, amo, meas)
            con.commit
            print(cur.fetchall())
        except:
            print (" Oh, we cannot seem to find your ingrediants, please try again!")
        
    def option_8():
        # This is the delete option, i am trying to solve how to delete trough a user input
        #try:
        #    del_ing = input("Please delete an ingrediant from the recipebook: ")
        #    cur.execute("Delete From Ingrediants where ('{}');")
        #except:
        #    print ("Can Not Compute, Please try again")
        pass

    def option_9():
        # This is the modify option, to be updated later
        pass


recipebook.menu()
menu_option = int(input(""))

while recipebook.menu() != 0:
    if menu_option == 1:
        recipebook.option_1()
    elif menu_option == 2:
        recipebook.option_2()
    elif menu_option == 3:
        recipebook.option_3()
    elif menu_option == 4:
        recipebook.option_4()
    elif menu_option == 5:
        recipebook.option_5()
    elif menu_option == 6:
        recipebook.option_6()
    elif menu_option == 7:
        recipebook.option_7()
    elif menu_option == 8:
        recipebook.option_8()
    elif menu_option == 9:
        recipebook.option_9()
    else:
        recipebook.option_0()
        break

    recipebook.menu()
    menu_option = int(input(""))
    
#  print (recipebook)
# print(cur.fetchall())

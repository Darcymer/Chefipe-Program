import sqlite3
from typing import final

con = sqlite3.connect("recipies.db")
cur = con.cursor()

class recipebook:
    def __init__(self):
        pass

    def menu():
        print("Welcome to Your Cheif Recipie Table, Please Select the following:")
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
        pass

    def option_1():
        try:
            #cur.execute("SELECT * FROM recipie")
            pass
        except:
            print (" Oh, we cannot seem to find your recipie please insert the name of the recipie below to list it!")
            # cur.execute('''CREATE Table recipie (
        #      style_name text
        #      )''')
            pass
        pass

    def option_2():
        try:
            #cur.execute("SELECT * FROM style")
            pass
        except:
            print (" Oh, we cannot seem to find your recipie please insert the name of the recipie below to list it!")
            # cur.execute('''CREATE TABLE style (
        #      style_name text
        #      )''')
            pass
        pass

    def option_3():
        #if table not found 
        # cur.execute('''CREATE TABLE style (
        #      style_name text
        #      )''')
        #else look below

        #stle_name = input("What is the style you want to put in:")
        # Replace meat with user style prefrence
        #cur.execute("INSERT INTO style values ('Meat')")
        pass
    def option_4():
        pass
    def option_5():
        #if table not found
        # Connect One table to another with primary key
        # cur.execute('''CREATE TABLE recipie (
#             Rec_Id 
#             r_name   text
#             Calories real
#             styleId
#             )''')
        #else look below

        #stle_name = input("What is the Recipie you want to put in:")
        # Replace meat with user style prefrence
        #cur.execute("INSERT INTO recipie values ('Meat')")

        # con.commit()
        pass
    def option_6():
        pass
    def option_7():
         #if table not found 
        # cur.execute("""CREATE TABLE Ingrediants (
# 	          Ing_ID		
# 	          Name     text
# 	          Price    real
# 	          Amount   real
# 	     Measurement   text
# 	        Recipe ID  
# 	)""")
        #else look below

        #stle_name = input("What is the style you want to put in:")
        # Replace meat with user style prefrence
        #cur.execute("INSERT INTO style values ('Meat')")
        pass
    def option_8():
        pass
    def option_9():
        pass


recipebook.menu()
menu_option = int(input(""))

while menu_option != 0:
    print()
    recipebook.menu()









# cur.execute('''CREATE TABLE style (
#             styleId 
#             base_name text
#             )''')


# cur.execute('''CREATE TABLE recipie (
#             Rec_Id 
#             r_name   text
#             Calories real
#             styleId
#             )''')

# cur.execute("""CREATE TABLE Ingrediants (
# 	          Ing_ID		
# 	          Name     text
# 	          Price    real
# 	          Amount   real
# 	     Measurement   text
# 	        Recipe ID  
# 	)""")

# cur.execute("INSERT INTO style values ('Meat')")
# cur.execute("INSERT INTO style values ('Fish')")
# cur.execute("INSERT INTO style values ('Sweets')")
# cur.execute("INSERT INTO style values ('Veggies')")
# cur.execute("INSERT INTO style values ('Juice')")
# cur.execute("INSERT INTO style values ('Hot Drinks')")

# cur.execute("SELECT * FROM style")

#  print (recipebook)
# print(cur.fetchall())

# con.commit()

# con.close()
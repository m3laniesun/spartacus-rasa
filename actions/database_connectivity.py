import mysql.connector

def DataUpdate(FirstName,LastName): 
    mydb = mysql.connector.connect( 
        host="localhost", 
        user="root",
        passwd="root",
        database="rasa_users") 
    mycursor = mydb.cursor() 
    sql='INSERT INTO users (firstName, lastName, feedback) VALUES ("{0}","{1}");'.format(FirstName,LastName) 
    mycursor.execute(sql) 
    
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
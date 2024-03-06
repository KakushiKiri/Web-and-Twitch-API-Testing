def print_songtbl(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM songs")
    tables = mycursor.fetchall()
    for table in tables:
        print(table)
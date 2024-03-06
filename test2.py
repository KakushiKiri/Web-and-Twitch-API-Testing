import mysql.connector
import test
from test import print_songtbl
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TTV~KakuKiri1",
    database="karaoke"
)

print_songtbl(mydb)
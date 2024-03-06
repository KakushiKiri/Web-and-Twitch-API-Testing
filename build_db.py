import mysql.connector
import json

#Load song info into list of dictionaries
local_fname = "Song_List.json"
data = json.load(open(local_fname))

#Connect to mySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TTV~KakuKiri1",
    database="karaoke"
)

#Set up cursor for database
mycursor = mydb.cursor()

#Delete any existing tables
mycursor.execute("DROP TABLE IF EXISTS Songs")
mycursor.execute("DROP TABLE IF EXISTS Artists")
#Create songs and artists tables
mycursor.execute("CREATE TABLE Artists (ArtistID int AUTO_INCREMENT PRIMARY KEY, Artist_Name varchar(255))")
mycursor.execute("CREATE TABLE Songs (SongID int AUTO_INCREMENT PRIMARY KEY, Song_Name varchar(255), Genre varchar(255), Language varchar(255), ArtistID int, FOREIGN KEY (ArtistID) REFERENCES Artists(ArtistID))")

#Loop through data variable, and insert into respective table
for song in data:
    #Grab ArtistID from current artist name
    check_artist_sql = "SELECT ArtistID FROM Artists WHERE Artist_Name = %s"
    check_artist_vals = (song['artist'],)
    mycursor.execute(check_artist_sql, check_artist_vals)
    existing_artist = mycursor.fetchone()

    #Check if ID's match, if not then insert artist to Artist's table and use the current ID
    if existing_artist:
        artist_id = existing_artist[0]
    else:
        artist_sql = "INSERT INTO Artists (Artist_Name) VALUES (%s)"
        artist_vals = (song['artist'],)
        mycursor.execute(artist_sql, artist_vals)

        artist_id = mycursor.lastrowid

    song_sql = "INSERT INTO Songs (Song_Name, Genre, Language, ArtistID) VALUES (%s,%s,%s,%s)"
    song_vals = (song['song_name'],song['genre'],song['language'], artist_id)
    mycursor.execute(song_sql,song_vals)

mydb.commit()

mycursor.execute("SELECT * FROM songs")
tables = mycursor.fetchall()
for table in tables:
    print(table)
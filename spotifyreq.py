#Nam Pham, 9/5/2024
from module import *
#user interactivity

x = 10;
token = get_token()
artist_chosenflag = False
while(x > 0):
    
    if not artist_chosenflag:
       artist = input("Please choose an artist:")
       result = search_for_artist(token, artist)
       artist_chosenflag = True
       artist_id = result["id"]
       
    print("\nWhat would you like to see about this artist?")
    print("1. Top songs!")
    print("2. Top album!")
    print("3. Ascii!")
    print("4. Search for new artist")
    print("-1 Quit")
    value = input();
    if int(value) == 1:
        songs = get_songs_by_artist(token, artist_id)
        print("\n Their top songs are: ")
        for idx, song in enumerate(songs):
         print(f"{idx + 1}.{song['name']}")
    if int(value) == 2:
        print("\nTheir top album is: " + get_top_album(token,artist_id)["name"])
    if int(value) == 3:
        imagetoascii(get_top_album(token, artist_id)["images"][1]["url"])
        print("\nASCII image of their top album cover has been generated!\n")
    if int(value) == 4:
        artist_chosenflag = False
    if int(value) == -1:
        x = -1

print("Thank you!")


#handling spotify api requests
from dotenv import load_dotenv
import os
import base64
import requests
from requests import post, get
import json

#dotenv a pip module that allows interactivity with apis
#load loads in the environemtn variables from the .env file also within the folder
from PIL import Image
load_dotenv() 

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")



def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers = headers, data = data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer "+ token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0 :
        print("No artist with this name exists")
        return None
    
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_top_album(token, artist_id):
    songs = get_songs_by_artist(token, artist_id)
    albumid = songs[0]["album"]["id"]
    url = f"https://api.spotify.com/v1/albums/{albumid}"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result


#All spotify related defs above, below are image to ascii

def imagetoascii(url): 
    #getting image url from get otp album and then downloading it
    filename = "albumcover.webp"
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Image saved as {filename}")
    image = Image.open(filename)
    width = 120;
    image = image.resize((120, 45))
    image = image.convert('L')
    chars = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
    px = image.getdata()
    new_pixels = [chars[pixel//25] for pixel in px]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + width] for index in range(0, new_pixels_count, width)]
    ascii_image = "\n".join(ascii_image)
 
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

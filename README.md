##What is this program:

####Python program that provides the user the ability to:
    1. Lookup the top songs in an artist's catalogue
    2. Lookup the album in which the artist's top song belongs to
    3. Create an ascii image of the cover of the artist's top album as well as downloads the cover (saved as webp and txt files in folder)

##Setup:
    ####Spotify for developers:
        Go to the [Spotify for developers dashboard](https://developer.spotify.com/dashboard) and create a project
            We will be needing two bits of information from this: Your client ID and Client Secret in order to make requests to Spotify's api
        After logging into your Spotify account into the dashboard, create an app and put any name, description, and URI within the required fields and select "Web API for which API you will
            You can use http://localhost:3000 for for the sake of simplicity within the URI section
        After agreeing to the terms, click on your settings for the project and copy down your client ID as well as your client secret (Click on "View client secret")
    
    ####Setting up the app:
        After retrieving your Client ID and client secret, create a new folder and put the spotifyreq.py program into it
        Additionally, you will need to create a ".env" file within this folder to store your environment variables (Client ID and Client Secret)
            Within this .env file, make two string variables called "CLIENT_SECRET" and "CLIENT_ID"
        After setting up your environment variables and saving, the program should be ready to run!
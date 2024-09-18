#This file is only for creating the verification credentials for the document!
import gspread
#if i have a proble with the credentials, needs to look for the appdata folder and delete credentials
# C:\Users\rick_\AppData\Roaming\gspread
#If have another credentials problem refer to https://medium.com/@soderholm.conny/authentication-problems-with-gspreads-oauth-c97c4d4b79fd
#access creds

access = gspread.oauth(
    credentials_filename="D:\Descargas\credentials.json",
    #i do not need to write authorized_user_filename="C:\Users\rick_\AppData\Roaming\gspread\authorized_user.json"
)
#also python will create a new authorized_user.json in my pc the path is C:\Users\rick_\AppData\Roaming\gspread

#i can also deleate credentials file and just let access = gspread.oauth() after the authorization

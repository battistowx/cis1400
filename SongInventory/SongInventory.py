# Author: Chris Battisto
# Date: 12/03/2014
# Program: SongInventory.py
# Descr:
# This program takes a user input of a song's data
# and saves that information to a song_inventory.dat file

# Song class located on whichever directory specified:
from Song import Song

def main():
    song1=[]
    song2=[]
    songInfo=[]
    totalTime=float()
    print('Please enter the information for song 1:')
    getSongInfo(songInfo)
    song1=songInfo
    writeFile(song1)
    print('Please enter the information for song 2:')
    getSongInfo(songInfo)
    song2=songInfo
    writeFile(song2)
    totalTime=((song1[2])+(song2[2]))/60
    print('The total time of songs (minutes): ', totalTime)

def getSongInfo(songInfo):
    song=Song()
    artist=input('Artist Name: ')
    song.setArtist(artist)
    title=input('Song Title: ')
    song.setTitle(title)
    time=int(input('Song Time in seconds: '))
    song.setTime(time)
    year=input('Year: ')
    song.setYear(year)
    # retrieve data from Song class to store in songInfo list
    songInfo.append(song.getArtist())
    songInfo.append(song.getTitle())
    songInfo.append(song.getTime())
    songInfo.append(song.getYear())
    return songInfo
    
def writeFile(song):
    song1=str()
    song2=str()
    song1=str(song[0:3])
    song2=str(song[4:7])
    # open file for writing in whichever directory specified:
    myFile=open('c:\\Users\\Chris\\Desktop\\song_inventory.dat','w')
    myFile.write(song1)
    myFile.write('\n'+song2)
    myFile.close()

main()

##MAIN OUTPUT:
##Please enter the information for song 1:
##Artist Name: Talking Heads
##Song Title: Animals
##Song Time in seconds: 210
##Year: 1979
##Please enter the information for song 2:
##Artist Name: Interpol
##Song Title: Not Even Jail
##Song Time in seconds: 347
##Year: 2005
##The total time of songs (minutes):  7.0

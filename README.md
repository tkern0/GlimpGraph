# GlimpGraph
A PC interpreter of BGLs from the app Glimp.

## Setup
This assumes you already have Glimp setup to read from your sensor.

#### Method A
1. Connect your phone to your PC as a media device  

2. Browse to the phone, and from the base directory copy the file 'GlicemiaMisurazioni.csv' elsewhere on your PC
   Make sure not to use the same file, the program makes it unreadable by Glimp

3. Download the latest release of this program from [here](https://github.com/tkern0/GlimpGraph/releases).  
   This is a single .exe which you can store anywhere.

4. Drag and drop 'GlicemiaMisurazioni.csv' onto this exe.  
   ![PC Usage](https://github.com/tkern0/GlimpGraph/blob/master/Images/05%20PC%20Usage.PNG)  
   The program will start and guide you through the rest.

#### Method B
1. Connect Glimp to Dropbox  
   Tap the drop down menu and go to 'Options' then 'Remote glucose monitoring'.
   ![Remote glucose monitoring](https://github.com/tkern0/GlimpGraph/blob/master/Images/01%20Remote%20glucose%20monitoring.png)  
   Tap Dropbox. This will bring up a window in your browser.  
   ![Dropbox login](https://github.com/tkern0/GlimpGraph/blob/master/Images/02%20Dropbox%20login.png)  
   Either create a Dropbox account, log into one, or log into a Google Account.  
   Allow Glimp access.  
   ![Permission](https://github.com/tkern0/GlimpGraph/blob/master/Images/03%20Permission.png)  
   You will be returned to Glimp. If everything's gone correctly you should see "Connected" under the Dropbox heading. 
   ![Connected](https://github.com/tkern0/GlimpGraph/blob/master/Images/04%20Connected.png)  

2. Get access to the file on your PC.  
   The specific file you want is 'GlicemiaMisurazioni.csv'.  
   Make sureto copy the file elsewhere, the program makes it unreadable by Glimp 
   You have two options here.
   1. Log into Dropbox [here](https://www.dropbox.com), and every time you want to use this download the file.
   2. Download and install the Dropbox desktop app from [here](https://www.dropbox.com/download). This will automatically sync the files whenever they are updated.

3. Download the latest release of this program from [here](https://github.com/tkern0/GlimpGraph/releases).  
   This is a single .exe which you can store anywhere.

4. Drag and drop 'GlicemiaMisurazioni.csv' onto this exe.  
   ![PC Usage](https://github.com/tkern0/GlimpGraph/blob/master/Images/05%20PC%20Usage.PNG)  
   The program will start and guide you through the rest.



# WearMerge
Merges data from an Android smartwatch with data from your phone

### Use:
1. Obtain 'GlicemiaMisurazioni.csv' following the instructions above
2. Download and install [ADB](http://lifehacker.com/the-easiest-way-to-install-androids-adb-and-fastboot-to-1586992378)
3. Connect your smartwatch straight to your PC
4. Open command prompt and run 'adb pull /storage/sdcard0/GlicemiaWearMisurazioni.csv'. This will copy this file to 'C:\Users\[your username]'
6. Copy 'GlicemiaMisurazioni.csv' and 'GlicemiaWearMisurazioni.csv' to the same folder as 'WearMerge.exe'
7. Run WearMerge.exe
This will create a new file called 'Merged.csv'. You can rename this to 'GlicemiaMisurazioni.csv' and upload it to dropbox/replace the file on your phone to get any data that did not sync.

===============================================
               Encryptor v1.16
-----------------------------------------------
          Class 12 Computer Project
===============================================

Please Note:
 - The program is attached as a .exe setup application.

 - You will need to download the exe file and run it.

 - The Setup will extract our project folder 
   to any destination (by default it is on the Desktop).

 - Once the setup is over you will find a folder
   in your destination, named "Encryptor vx.xx".

 - This Folder contains various files in it.

 - You will need to run the Application named
   Encryptor.exe to try the program out for yourself

 - The source code is contained with to 2 .py files
   (main.py , functions.py)

 - You may Open it in your Text Editor / IDE and read the source code :)

 - Please Do not move the .py files out of the folder 

 - It will cause the program to stop working from the exe application


-----------------------------------------------
Project Description:
   
   This Project Aims to show light on the hashing and encryption modules
   and its real life applications. The Program Opens up a Main Window from
   where the user can login or register a new "account" which uses the 
   hashing methods to store the password of the user safely in a file using
   File Handling and the hashlib module

   Once the User Logs in they are presented with a text box which is unique for
   Every User. The user can store any string in the text box and then click on
   the Proceed Button. This Encrypts the Data on the text box and stores it
   in a file.These files are unique for each user.The Encryption is done using
   a module called Fernet under the cryptography module.

   When the same user logs back in his/her data will be displayed in the same
   text box for them to use or read


-----------------------------------------------

Modules Used:

+-----------------+------------------+------------------+
|                 |                  |                  |
|   Module Name   |   Description    |  Use in Program  |
|                 |                  |                  |
+-----------------+------------------+------------------+
|                 | Used for making  | For making       |
|    tkinter      | Interactable GUIs|       Windows    |
+-----------------+------------------+------------------+
|                 | Used for         | For hashing      |
|    hashlib      |      Hashing     |       passwords  |
+-----------------+------------------+------------------+
|                 | Used for making  | For Generating   |
|     uuid        | random UUIDs     | Salt for Hashing |
+-----------------+------------------+------------------+
|                 | Used for         | For Deleting  &  |
|      os         |  various things  |  Adding Files    |
+-----------------+------------------+------------------+
|                 | Part of          | Used for         |
|    Fernet       |    cryptography  |    Encryption    |
+-----------------+------------------+------------------+
|                 | Converts py to   | Used to make the |
|  pyinstaller    |             exe  | program an app   |
+-----------------+------------------+------------------+
|                 |  Sotring Binary  | Used for storing |
|    pickle       |       Data       | Encryption key   |
+-----------------+------------------+------------------+

Misc:

+-----------------+------------------+------------------+
|                 | Converts files to| Used to make the |
| NSIS (Software) | Compressed Setups| app to a setup   |
+-----------------+------------------+------------------+


-----------------------------------------------

Credits:

 - Sakthi Swaroopan
 - Raghav Srivatsan
 - Rohith Krishna

-----------------------------------------------

Contacts:
 - sakthiswaroopan@gmail.com
 - rohith142003@gmail.com
 - arcreacraghav@gmail.com

----------------------------------------------
===============================================
                  Thank You!
===============================================

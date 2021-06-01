# Quickcrypt
Script for quick encription of files

Generaring a key file will save a randomly-generated key to encrypt the data with, after the file is encrypted it will require the SAME key to be decrypted, using a different key to decrypt the data will corrupt the data and the original key won't work to decrypt it anymore. 

Start by running the Quickcrypt.exe 

![00](https://user-images.githubusercontent.com/23648113/120394900-f85d5700-c2e8-11eb-9ea5-6d6cfe6b9b0d.PNG)

*GENERATE NEW KEY*
Click the Generate Key button in the bottom-center side of the window and a pop-up will show 

![02](https://user-images.githubusercontent.com/23648113/120395204-77528f80-c2e9-11eb-8573-3d657b97d765.PNG)

By default the key will be saved in the current working directory, if you want to change that, uncheck the box

![02](https://user-images.githubusercontent.com/23648113/120394902-f8f5ed80-c2e8-11eb-995a-4dd82828e28e.jpg)

Fill it up and click cancel to abort or generate to create the key file, if the directory doesn't exist, it'll create one and save the key file there

![03](https://user-images.githubusercontent.com/23648113/120394903-f8f5ed80-c2e8-11eb-895f-1287f17a5efa.PNG)
 
 At this point a file will be created in the specified location
 
![04](https://user-images.githubusercontent.com/23648113/120394889-f6939380-c2e8-11eb-8e3e-99eda9ca1937.PNG)


*ENCRYPT FILE*

To encrypt we first need a key, if we don't have one yet we'll have to create one following the steps above, to select a key file clicl on Open key

![01](https://user-images.githubusercontent.com/23648113/120394901-f85d5700-c2e8-11eb-845f-0ecbc080fdf1.jpg)

A window dialog will pop up, navigate to the keys location and open it

![05](https://user-images.githubusercontent.com/23648113/120394891-f6939380-c2e8-11eb-9a86-53d066f7dd45.PNG)


Repeate the operation now with the Open file button to select the file to encrypt

![06](https://user-images.githubusercontent.com/23648113/120394892-f72c2a00-c2e8-11eb-8246-e987d96853b2.PNG)

Here is the result of trying to open an encrypted txt file
Original:
![07](https://user-images.githubusercontent.com/23648113/120394893-f72c2a00-c2e8-11eb-90f9-417a3b42f936.PNG)

After encrypting:
![09](https://user-images.githubusercontent.com/23648113/120394896-f7c4c080-c2e8-11eb-861e-770f298f41ab.PNG)

*DECRYPT FILE*

To decrypt a file we'll have to follow the same steps to chose the key and file to be decrypted 
      **MAKE SURE TO USE THE SAME KEY TO DECRYPT AS THE ONE YOU USED TO ENCRYPT THAT FILE**

Once the key and input files are selected just click on Decrypt and the file will return to normal and will behave as usual
![10](https://user-images.githubusercontent.com/23648113/120394897-f7c4c080-c2e8-11eb-9ffe-6a26a0b87fbf.PNG)


**WARNING!** 
Lossing the original key or encrypting/decrypting twice in a row may result in unrecoverable data, use it under own risk, the idea behind it is "I'd rather lose this info than have it stolen"

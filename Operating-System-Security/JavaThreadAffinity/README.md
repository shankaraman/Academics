JavaThreadAffinity
==================

JavaThreadAffinity

a) Running the code without Eclipse :

Step:1

    Clone the repository in your local machine and download the jna.jar file (from internet).
    After cloning, you can find the files in side the path JavaThreadAffinity/src/com/threads/

Step:2

    Run the C program using the following command,
    
          $ gcc -fPIC -o libctest.so -shared ctest.c
          
Step:3

    To compile and run Java file, run the following commnads.
    
          $ javac -classpath jna-4.0.0.jar HelloWorld.java java -classpath jna-4.0.0.jar:. HelloWorld
          
    PS: Replace HelloWorld.java with your Java file.
    

b) Running the code in Eclipse :

Step 1:

    Clone the repository and import the project files inside your workspace.
    
Step 2:

    Download the jna.jar file from the internet.
    
Step 3:

    Add both, the class path and directory path of the jna.jar file in your workspace.

Step 4:

    Run the compile.sh file to create the shared object.
    
                  $ ./compile.sh

Step 5:
      
      Then build and run the program.

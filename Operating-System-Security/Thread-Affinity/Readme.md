Clone all the files into your local machine in a directory.

First try to see run the C program

/* ctest.c */

gcc -fPIC -o libctest.so -shared ctest.c

I have uploaded the "libtest.so" file which I got after executing the command given above. 


Second compile and run the java code:

/* HelloWorld.java */

javac -classpath jna-4.0.0.jar HelloWorld.java
java -classpath jna-4.0.0.jar:. HelloWorld

Third program 

/* JNATestOne.java */

There are few errors in the program. Yet to be fixed.

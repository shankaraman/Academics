gcc -o libctest.so -shared src/com/threads/ctest.c -fPIC -pthread
sudo cp libctest.so /usr/lib

touch myfile
chmod 444 myfile
echo "Read permission granted"
ls -l myfile
chmod 660 myfile
echo "Read and Write permission granted for Owner and Group"
ls -l myfile
chmod 640 myfile
echo "Write permission removed from all user except Owner"
chmod 710 myfile
echo "Execute permission granted for Owner and Group"
ls -l myfile
rm myfile

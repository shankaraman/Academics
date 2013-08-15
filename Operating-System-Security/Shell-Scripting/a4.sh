mkdir myfolder
for i in {1..3}
do
    touch myfolder/file.$i
done

chmod 444 myfolder/*
echo "READ permission is assigned to all"
ls -l myfolder/*

chmod 220 myfolder/*
echo "WRITE permission is assigned to OWNER and GROUP"
ls -l myfolder/*

chmod 022 myfolder/*
echo "WRITE permission is assigned to everyone except OWNER"
ls -l myfolder/*

chmod 310 myfolder
echo "WRITE && EXE -> OWNER and EXE -> GROUP" 

chmod +x myfolder
ls -l 
sudo rm -r myfolder

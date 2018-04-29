import os, binascii

#read and write one file at a time for all in the directory
for idx, filename in enumerate(os.listdir("./resultFinal")):
    data = ""
    
    #read file in binary mode (rb)
    with open(os.path.join("resultFinal", filename), "rb") as binary_file:
        data = binary_file.read()

    #Since you can't append anything to the start of the file, create a new one
    with open(os.path.join("result", filename), "ab") as binary_file:
        binary_file.write(binascii.unhexlify('EFBBBF')) #Write UTF-8 BOM to start of file so word can open them
        binary_file.write(data) #append the rest of the original file
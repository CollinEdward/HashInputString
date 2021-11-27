import hashlib
# make a function that hash input

print("\thashing types:")
print("\t\tmd5\n\t\tsha1\n")


which_hash_type = input("Which hash type do you want to hash your string in?: ")

hashinput = input("plain text: ")

def md5_hash(data):
    hash_object = hashlib.md5()
    hash_object.update(str(data).encode())
    print(hash_object.hexdigest())


def sha1_hash(data):
    hash_object = hashlib.md5()
    hash_object.update(str(data).encode())
    print(hash_object.hexdigest())


def choose():
    if which_hash_type.lower() == "md5":
        md5_hash(data=hashinput)
    elif which_hash_type.lower() == "sha1":
        sha1_hash(data=hashinput)    
        
if __name__ ==  '__main__':
    choose()

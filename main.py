import hashlib

def read_dictionary(file_path):
    with open(file_path,'r') as file:
        return [line.strip() for line in file]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def crack_password(target_hash,dictionary):
    for word in dictionary:
        hashed_word=hash_password(word)
        if hashed_word==target_hash:
            return word
    return None

if __name__=='__main__':
    target_hash="03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    dictionary_file="D:\dictionary.txt"
    dictionary=read_dictionary(dictionary_file)
    cracked_password=crack_password(target_hash,dictionary)
    if cracked_password:
        print(f"password cracked the password is:{cracked_password}")
    else:
        print("password not found")

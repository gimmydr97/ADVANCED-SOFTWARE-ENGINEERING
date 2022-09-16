import utils
import string

def encrypt_caesar(plaintext):
    
    
    
    alphabet = string.ascii_uppercase
    alphabet = alphabet + "ABC"
    print(alphabet)
    cripherseq = ""
    for char in plaintext:
        if (index := alphabet.find(char)) != -1:
            cripherseq += alphabet[index+3]
        else:
            cripherseq += char
    return cripherseq

def decrypt_caesar(ciphertext):

    alphabet = string.ascii_uppercase
    print(alphabet)
    decryptseq = ""

    for char in ciphertext:
        if(index := alphabet.find(char)) != -1:
            decryptseq += alphabet[index-3]
        else:
            decryptseq += char

    return decryptseq

def setKeyword(plaintext, keyword):
    
    newKeyword =""
    lenp = len(plaintext)
    lenkeyw = len(keyword)

    if lenp > lenkeyw:

        pi = lenp // lenkeyw
        r  = lenp % lenkeyw

        for i in range(pi):
            newKeyword += keyword

        for i in range(r):
            newKeyword += keyword[i]

    elif lenp < lenkeyw:
        
        newKeyword = keyword[:lenp]

    else:
        newKeyword = keyword

    return newKeyword

def encrypt_vigenere(plaintext, keyword):

    alphabet = string.ascii_uppercase
    cripherseq = ""
    keyword = setKeyword(plaintext, keyword)

    for i in range(len(plaintext)):

        sum = alphabet.find(plaintext[i]) + alphabet.find(keyword[i])
        cripherseq += alphabet[sum % 26]

    return cripherseq

def decrypt_vigenere(ciphertext, keyword):

    alphabet = string.ascii_uppercase
    cripherseq = ""
    keyword = setKeyword(ciphertext, keyword)

    for i in range(len(ciphertext)):

        sum = alphabet.find(ciphertext[i]) - alphabet.find(keyword[i])
        cripherseq += alphabet[sum]

    return cripherseq

def main():
    """ for i in range(18):
        a=input("").strip()
        d=input("").strip()
        print("a: "+a)
        print("d: "+d)

        ea = encrypt_caesar(a).strip()
        dd = decrypt_caesar(d).strip()

        print("dd: "+dd)
        print("ea: "+ea)

        if a==dd and d == ea:
            print("ok!")
        else:
            print("no")
    """
    """
    for i in range(11):
        p=input("").strip()
        c=input("").strip()
        ept=input("").strip()

        print("p: "+p)
        print("c: "+c)
        print("ept: "+ept)

        ep = encrypt_vigenere(p,c).strip()
        dp = decrypt_vigenere(ept,c).strip()

        print("dp: "+dp)
        print("ep: "+ep)

        if p==dp and ep == ept:
            print("ok!")
        else:
            print("no")
    """
if __name__ == '__main__':
    main()

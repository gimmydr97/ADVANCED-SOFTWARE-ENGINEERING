"""Assignment 1: 

Replace this placeholder text with a description of this module.
"""
import utils
import string

#################
# CAESAR CIPHER #
#################

def encrypt_caesar(plaintext):

    alphabet = string.ascii_uppercase #assign the string containig the alphabet to alphabet
    alphabet = alphabet + "ABC"
    cripherseq = ""

    for char in plaintext:

        if (index := alphabet.find(char)) != -1:
            cripherseq += alphabet[index+3]

        else:
            cripherseq += char

    return cripherseq
    
def decrypt_caesar(ciphertext):
   
    alphabet = string.ascii_uppercase
    decryptseq = ""
    
    for char in ciphertext:

        if (index := alphabet.find(char)) != -1:
            decryptseq += alphabet[index-3]

        else:
            decryptseq += char

    return decryptseq


###################
# VIGENERE CIPHER #
###################
def setKeyword(plaintext, keyword): #for set keyword to the lenght of plaintext
    
    newKeyword =""
    lenp = len(plaintext) #lenght of plaintext
    lenkeyw = len(keyword) #lenght of keyword

    if lenp > lenkeyw:

        pi = lenp // lenkeyw #integer part
        r  = lenp % lenkeyw  #remainder of the division

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

########################################
# MERKLE-HELLMAN KNAPSACK CRYPTOSYSTEM #
########################################

def generate_private_key(n=8):
    """Generate a private key to use with the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key
    components of the MH Cryptosystem. This consists of 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        Note: You can double-check that a sequence is superincreasing by using:
            `utils.is_superincreasing(seq)`
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q`
        Note: You can use `utils.coprime(r, q)` for this.

    You'll also need to use the random module's `randint` function, which you
    will have to import.

    Somehow, you'll have to return all three of these values from this function!
    Can we do that in Python?!

    :param n: Bitsize of message to send (defaults to 8)
    :type n: int

    :returns: 3-tuple private key `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    # Your implementation here.
    raise NotImplementedError('generate_private_key is not yet implemented!')


def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in
    the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r ?? w_i mod q

    Hint: this can be written in one or two lines using list comprehensions.

    :param private_key: The private key created by generate_private_key.
    :type private_key: 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    :returns: n-tuple public key
    """
    # Your implementation here.
    raise NotImplementedError('create_public_key is not yet implemented!')


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    Following the outline of the handout, you will need to:
    1. Separate the message into chunks based on the size of the public key.
        In our case, that's the fixed value n = 8, corresponding to a single
        byte. In principle, we should work for any value of n, but we'll
        assert that it's fine to operate byte-by-byte.
    2. For each byte, determine its 8 bits (the `a_i`s). You can use
        `utils.byte_to_bits(byte)`.
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk of the message.

    Hint: Think about using `zip` and other tools we've discussed in class.

    :param message: The message to be encrypted.
    :type message: bytes
    :param public_key: The public key of the message's recipient.
    :type public_key: n-tuple of ints

    :returns: Encrypted message bytes represented as a list of ints.
    """
    # Your implementation here.
    raise NotImplementedError('encrypt_mh is not yet implemented!')


def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key.

    Following the outline of the handout, you will need to:
    1. Extract w, q, and r from the private key.
    2. Compute s, the modular inverse of r mod q, using the Extended Euclidean
        algorithm (implemented for you at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum problem using c' and w to recover
        the original plaintext byte.
    5. Reconstitute the decrypted bytes to form the original message.

    :param message: Encrypted message chunks.
    :type message: list of ints
    :param private_key: The private key of the recipient (you).
    :type private_key: 3-tuple of w, q, and r

    :returns: bytearray or str of decrypted characters
    """
    # Your implementation here.
    raise NotImplementedError('decrypt_mh is not yet implemented!')

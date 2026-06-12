def encrypt(message,shift):
    encrypted=""
    shift=int(shift)
    for char in message:
        if char.isupper():
            encrypted+=chr((((ord(char)-65)+shift)%26)+65)
        elif char.islower():
            encrypted+=chr((((ord(char)-97)+shift)%26)+97)
        elif char==" ":
            encrypted+=char
        else:
            encrypted+=char
    return encrypted
def decrypt(message,shift):
    decrypted=""
    shift=int(shift)
    for char in message:
        if char.isupper():
            decrypted+=chr((ord(char)-65-shift)%26+65)
        elif char.islower():
            decrypted+=chr((ord(char)-97-shift)%26+97)
        elif char==" ":
            decrypted+=char
        else:
            decrypted+=char
    return decrypted
def zee_encrypt (message):
    shift=int(len(message)+10)%26
    return encrypt(message,shift)
def zee_decrypt(message):
    shift=int(len(message)+10)%26
    return decrypt(message,shift)
print("---------------------------------------------")
print("------------WELCOME TO ZEENCRYPT-------------")
print("---------------------------------------------")
print("---------------------------------------------")
while True:
    print("Enter Your Choice......")
    print("What You Want To Do?")
    choice=int(input("1.Ceaser Cypher \n2.ZeeCypher \n3.Exit\n"))
    if choice==1:
        while True:
            print("---------Ceaser Cypher-----------")
            ceaser_choice=int(input("\n Enter Your Choice :\n1.Encrypt. \n 2.Decrypt\n3.Exit\n"))
            if ceaser_choice==1:
                message=str(input("Enter the message below which you want to encrypt(symbols and numbers will not be    encrypted.....):\n"))
                shift=input("Enter the shift you want to give to your text...(must be an integer)")
                if shift.isdigit():
                    print(f"\n Your Encrypted Text Is: {encrypt(message,shift)}")
                else:
                    print("Kindly enter the shift that should be an interger...:")
            elif ceaser_choice==2:
                dec_message=str(input("Enter the message you want to decrypt :\n"))
                dec_shift=input("Enter the shift you gave while encrypting this text.....:")
                if dec_shift.isdigit():
                    print(f"\n Your Decrypted Text Is: {decrypt(dec_message,dec_shift)}")
            elif ceaser_choice==3:
                break
            else:
                print("Invalid Choice.....Enter A Valid One.......:")
    elif choice==2:
        while True:
            print("---------Zee Cypher-----------")
            print("My Own Made Encryption/Decryption Algorithm...")
            zee_choice=int(input("\n Enter Your Choice :\n1.Encrypt. \n 2.Decrypt\n3.Exit\n"))
            if zee_choice==1:
                zee_message=str(input("Enter the message below which you want to encrypt(symbols and numbers will not be    encrypted.....):\n"))
                print(f"Your encrypted cypher is given below:\n {zee_encrypt(zee_message)}")
            elif zee_choice==2:
                zee_dec_message=str(input("Enter the message you want to decrypt no key needed: \n But important notice is that is should be encrypted by zee_cypher otherwise will give invalid text...."))
                print(f"Your decrypted cypher is given below:\n {zee_decrypt(zee_dec_message)}")
            elif zee_choice==3:
                break
            else:
                print("Invalid Choice! Please Enter A Valid Choice: ")
    elif choice==3:
        break
    else:
        print("Invalid Choice! Please Enter A Valid Choice: ")
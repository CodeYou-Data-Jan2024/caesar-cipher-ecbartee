ref_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z']

#Assignment Version
Phrase = input("Please enter a sentence to encrypt: ").lower ()
encrypted_phrase = ""
print(encrypted_phrase)
for letter in Phrase:
    if letter in ref_alphabet:
        x = ref_alphabet.index(letter)
        print (x)
        y = (x + 5) % 26
        # z = ref_alphabet.index(y)
        # print (z)
        #Phrase += ref_alphabet.index[y]  - I could not get this to work - there was something wrong with how I planned to return the new character with the index including the shift.
        encrypted_phrase += ref_alphabet[y]
    else:
        encrypted_phrase += letter
print("The encrypted sentence is: ", encrypted_phrase )


#Game Version
number = input("What is the shift? Please enter a number less than 26: ")
if number.isdigit():
    number = int(number)
    print("Thank you for entering a number! Let's see if it is less than 26.  ")
    if number < 26:
        print ("Thank you for entering an accepted number.")
        Phrase = input("Please enter a sentence to encrypt: ").lower ()
        encrypted_phrase = ""
        print(encrypted_phrase)
        for letter in Phrase:
            if letter in ref_alphabet:
                x = ref_alphabet.index(letter)
                print (x)
                y = (x + number) % 26
                encrypted_phrase += ref_alphabet[y]
            else:
                encrypted_phrase += letter
        print("The encrypted sentence is: ", encrypted_phrase )
    else:
        print ("Your number doesn't follow the rules, no encryption for you.")
else:
    print("Please enter whole numbers only, no decimals, letters or special characters.")

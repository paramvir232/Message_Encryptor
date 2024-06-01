from art import logo  #importing ASCII art from other file
#Combining list of all the alphabets,symbols and numbers so that we can encrypt everything
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " "
]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
finalList = alphabet + symbols + numbers
lengthOfList = len(finalList)


#the main function which encrypts and decrypts the texts
def ceaser(text, shift, direction):
    both_text = ""
    for letter in text:
        if letter not in finalList:  #if input text letter's are not in our list
            both_text += letter
            continue
        indexInlist = finalList.index(letter)
        if direction == "encode":
            shifted_index = indexInlist + shift
            if (shifted_index > (lengthOfList - 1)):
                shifted_index -= lengthOfList  #loop back to list
        else:
            shifted_index = indexInlist - shift
            if (shifted_index < 0):
                shifted_index += lengthOfList  #loop back to list
        both_text += finalList[shifted_index]
    print(f"The {direction}d text: {both_text}\n")


print(logo)
varRestart = True
# While loop in which our function runs
while varRestart:
    print('-' * 60 + "\n")
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    if shift > lengthOfList:  #adjusting shift according to length of list
        shift = shift % lengthOfList
    ceaser(text, shift, direction)
    print('-' * 60)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if restart == "no":
        varRestart = False
        print(f"{'-'*26} GoodBye {'-'*26}")

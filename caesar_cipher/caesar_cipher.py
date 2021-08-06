import nltk

nltk.download("words", quiet=True)
nltk.download("names", quiet=True)

from nltk.corpus import words, names

lower_case = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

upper_case = []

for letter in lower_case:
    upper_case.append(letter.upper())

# from caesar_cipher.words_names import words
word_list = words.words()
name_list = names.words()

# print(word_list)

# The qucik brown fox jumped over the lazy sleeping dog
# Shift of 15
# IWT FJXRZ QGDLC UDM YJBETS DKTG IWT APOXAN HATTEXCV SDV

#           23, 4 - > 67
def encrypt(plain_text, key):
    encrypted_text = ""
    # print(f"The plain text number is {plain_text}.")

    # lower_case = ord("a")
    # upper_case = ord("A")

    for char in plain_text:
        if char in lower_case:
            temp = lower_case.index(char)
            temp2 = (temp + key) % 26
            encrypted_text += lower_case[temp2]
        elif char in upper_case:
            temp = upper_case.index(char)
            temp2 = (temp + key) % 26
            encrypted_text += upper_case[temp2]
        else:
            encrypted_text += char
    return encrypted_text
    # print(encrypt_text)


def decrypt(encoded, key):
    decrypt_text = ""
    decrypt_text = encrypt(encoded, -key)
    return decrypt_text
    # print(decrypt_text)


def crack(message):
    message_list = [message]
    # new_message_list = message_list[0].split()
    # print(new_message_list)

    decrypted = []
    testing = []

    decrypt_text = ""
    found = False

    while found == False:

        counter_and_array = []
        for i in range(len(lower_case)):
            decrypted.append([decrypt(message, i)])

        for sample in decrypted:
            testing.append(sample[0].split())

        for array in range(len(testing)):
            to_append = ""
            counter = 0
            for words in testing[array]:
                if words in word_list or name_list:
                    counter += 1
                to_append += f"{words} "
            counter_and_string = [to_append, counter]

            counter_and_array.append(counter_and_string)
        # print(counter_and_array)
        value = counter_and_array[0][1]
        counter = 0
        for i in range(len(counter_and_array)):
            if value < counter_and_array[i][1]:
                counter = i
                value = counter_and_array[i][1]
            found = True
            return counter_and_array[counter][0]

    return decrypt_text


enigma = encrypt("It was the best of times, it was the worst of times.", 5)
print(crack(enigma))

# if __name__ == "__main__":
# print(encrypt("23", 6))  # 89
# print(encrypt("23", 4))  # 67
# print(encrypt("2345", 7))  # 9012
# print(encrypt("2345", 108345345345))  # 9012
# print(decrypt("12345", 6))

# 1234567890

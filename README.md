Project Lab 18: Cryptography

Deployed on: [Link](https://github.com/kevinhenry/caesar-sipher)

PR: [Link](https://github.com/kevinhenry/caesar-sipher/pulls)

Collaboration:
  Tony Regalado, Anthony Williams

Overview: Today we’ll be tackling a cryptographic classic - the Caesar Cipher.

Your job will be to devise a method to encrypt a message that can then be decrypted when supplied with the corresponding key.

But don’t stop there! You’ll also need to devise a way to decipher the encrypted message event when you do NOT have the key!

## Feature Tasks and Requirements
- Create an `encrypt` function that takes in a plain text phrase and a numeric shift.
    - the phrase will then be `shifted` that many letters.
        - E.g. encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’
    - shifts that exceed 26 should wrap around
        - E.g. encrypt(‘abc’,27) would return ‘bcd’
    - shifts that push a letter out or range should wrap around
        - E.g. encrypt(‘zzz’,1) would return ‘aaa’
- Create a `decrypt` function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
- create a `crack` function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
- Devise a method for the computer to determine if code was broken with minimal human guidance.


## Implementation Notes
- In order to accomplish a certain task you’ll need access to a `corpus` of English words.
- search on something like [python list of english](https://www.programcreek.com/python/example/97191/nltk.corpus.words.words) words should get you going.


### User Acceptance Tests:
[x] encrypt a string with a given shift
[x] decrypt a previously encrypted string with the same shift
[x] encryption should handle upper and lower case letters
[x] encryption should allow non-alpha characters but ignore them, including white space
[x] decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
* refer to supplied unit tests.

Tools Used
NLTK
Corpus

Python
Pytest
Poetry
PyEnv

Getting Started
Clone this repository to your local machine.

$ git clone [Link](https://github.com/kevinhenry/caesar-cipher.git)
Once downloaded, activate your virtual environment and run by ____________

`poetry init`
`poetry shell`

# Caesar-Cipher-Algorithm
A Caesar Cipher encryption and decryption tool

# Usage
NOTE: You must have python installed on your pc to be able to use this tool.
- <a href="https://realpython.com/installing-python/">Guide</a> to install and setup python

## On PC
- Download the file <a href="https://github.com/HybridCodes/Caesar-Cipher-Algorithm/releases">here</a>
- Extract it into a folder
- Open command prompt and navigate to the folder in which you extracted the file

## On Android
- Download <a href="https://play.google.com/store/apps/details?id=com.termux&hl=en_US&gl=US">Termux</a> from the play store
- Open Termux and execute the following commands:
```bash
# Hit enter after typing each command to execute the command

$ pkg update && upgrade / -y
$ pkg install python
$ pkg install pip 
$ pkg install git
$ pip install --upgrade pip
$ termux-setup-storage # Allow access to storage
$ cd storage
$ dir # Execute this command to check the list of items in the directory in which you're currently in
  # In my case;
  dcim       external-1  music    shared
  downloads  movies      pictures
$ cd downloads # To navigate to the downloads folder
$ git clone https://github.com/codebytesz/Caesar-Cipher-Algorithm.git
$ dir # To show the items in the downloads folder now, you should see the cloned item among the files listed
  Caesar-Cipher-Algorithm
$ cd Caesar-Cipher-Algorithm
$ dir # (Optional) To see the items in the Caesar-Cipher-Algorithm folder
$ python caesar_cipher.py
```
# Report a bug :beetle:
If you experience any bugs or want to make a contribution, create an <a href="https://github.com/codebytesz/Caesar-Cipher-Algorithm/issues">issue</a>.
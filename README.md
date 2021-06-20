# Pnwed-Password-Checker
This code is to check passwords if they have been hacked

The code uses tkinter to collect passwords from a message box. You can type multiple passwords seperated by space. The password is hidden by default but there is an option to show it for you to see what you have typed. 
On clicking submit, the code hashes the password and uses the first five character of the hashed password to search in the database of pnwed passwords and returns a list of all passwords that has same first five letters.
The remaining part of the hashed password is then used to check if the password is in the list of returned passwords from the database and the number of times it appears.
This is the relayed back to you. In relaying the final result, you password is hidden and only the first and last characters shown. This is to ensure that your password is not made visible all the way and your password remains hidded all through the check.
The code also guarantees that your password dose not remain in the command line if run from the terminal. After running it your passwords is not recorded anywhere giving you a guarantee of safety.

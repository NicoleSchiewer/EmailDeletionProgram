# DeleteEmailsUsingIMAPandPython

The following program in this file can be used to delete e-mail messages on Gmail from specific e-mail senders.
The query criteria can be changed to many different options dependent upon what messages are to be deleted.
Overall, this program is very useful when wanting to search through e-mails to see which are to be saved/deleted, but many from each sender exist.

This program works by using IMAP and Python to connect to the IMAP server for Gmail. Once connected and logged in, query criteria is specified to find messages within a specified mailbox. Once messages are found, parts of the messages are found and decoded to a recognizable string (console prints "Deleting (subject of e-mail)." The message is then labeled as "Trash" and deleted (sent to the Trash mailbox) from the specified mailbox.

To run the program, simply enter your Gmail username and password into the corresponding locations within the program. Then, specify the mailbox to be searched (default is the "All Mail" mailbox), and enter in search criteria for specific messages. Once completed, run the program.

NOTE*: If an error is returned after inputting password into program, this could be due to 2-factor verification being enabled. An auth credential may have to be created in Gmail to bypass this. Please ask if you have questions, and I can explain the process further.

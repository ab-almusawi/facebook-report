# facebook-report
Report FaceBook Accounts
--------------------------------------
You need python2 to run This Program
---------------------------------------------
write the command in the cmd or terminal to install the required libraries:

pip install -r requirements.txt
----------------------------

After installation Complete

open the cookies generating file:

python GenerateCookies.py
----------------------------
First: enter the count of accounts for which we will generate cookies for use later in the reporting process.

Second: enter  email - phone number - account id, then the password for the account and repeat the process until the required number is finished.

After completing the cookie generation process, exit the GenerateCookies.py file and open the Report.py file
write the command:

python Report.py
----------------------------

First: enter the id number of the account to be reported
It can be found either in the link of the account or via the website: https://lookup-id.com

Second: choose the type of report by entering the report number

Third: write the number of reports - and it must be equal to the number of cookies that were generated by the file: GenerateCookies.py

Fourth: enter the required waiting period between report and the other - sleep (in seconds).

Fifth: choose whether or not if you want to use proxies by entering the letter y or n

Note / Before choosing to use proxies, you must put them in the

proxies.txt file
----------------------------

Which is located in the same folder as the program
Proxies are placed in the following manner, line by line:

10.10.10.1:2222

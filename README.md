How to Run PHD

1. Install Python version 3.7.3
#	a. Be sure to check the box in the installer 'ADD TO PATH' in order to access pip installations
2. Install MS SQL Native SQL Server 2012
3. Install MS SQL ODBC Driver 13
4. Install Visual Studio Code
5. Unzip 'PHD-master.zip' file & open in VS Code
6. Open a terminal window in VS Code in the 'bash' console
#	a. To verify Python proper install, type 'python' or 'python3'
#		b. If success, type 'exit()' and then 'pip3 install flask'
#		c. Once installed, type 'python' again and this time type 'import flask' before exiting
#	b. Then type 'python3 -m venv venv' to install a virtual environment and 'venv/Scripts/activate' to activate it
#	c. Then type 'pip3 install -r requirements.txt' and 'export FLASK_APP=phd.py'
#	d. To allow set up ticket/user creation and update functionality, type set MAIL_USERNAME='INSERT_EMAIL_HERE' and set MAIL_PASSWORD='INSERT_PASSWORD_HERE'
#	e. After this, type 'flask run' and Ctrl + Click to navigate to the webpage
7. To view the database in real time, install MS SQL Server Management Studio
#	a. Connection type: MS SQL Server
#	b. Server: partahelpdeskserver.database.windows.net
#	c. Port: 1433
#	d. Username: phdadmin
#	e. Password: *****
#	f. Authentication Type: SQL Login

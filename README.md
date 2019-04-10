# PHD
PARTA Help Desk (PHD) is an internal, information technology ticketing system for the Portage Area RTA. PHD will facilitate asset tracking, ticket creation and reporting for PARTA’s IT department. Employees from other departments will now be able to create request technical assistance when they have an issue with the technology they are interacting with while working.  
# Important things
Any user of PHD must first access the login URL while also connected to PARTA’s intranet system. PHD will only be available to those with computer systems that have already been granted permission to join PARTA’s domain. Once logged in, users will land on PHD’s dashboard and choose to either edit/ view data or generate a report. If they request to edit/ view data, a call to PHD’s Microsoft SQL Server Database will be made to pull the relevant information and display it back in PHD. If the user requests a report be generated, based on data within the database, a relevant report will be rendered.
# export FLASK_APP=phd.py
# flask run

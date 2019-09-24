from datetime import datetime

def check_birthdate(year,month,day):
	today = datetime.now()
	birthdate = datetime(year,month, day)
	if birthdate > today:
		return False
	else:
		return True 
def calculate_age(year,month,day):
	today = datetime.now()
	birthday = datetime(year,month, day)

	age = today - birthday

	print("Your current age is %d years old" % (age.days/365))

year = int(input("what is your birth year?"))
month = int(input("what is your birth month?"))
day = int(input("what is your birth day?"))

if check_birthdate(year,month, day) == True:
	calculate_age(year,month,day)
else: 
	print("Invalid birthdate.")

'''
+--------+--------+--------+--------+--------+--------+--------+--------+
| > This script is used to crack the password of a pdf file.				|
| > Iny my case I knew that the password was a 5 digit number,				|
| so I bootstraped the script to generate all the possible 5 digit		|
| numbers and then I tried to open the pdf file with each of the			|
| generated numbers.																		|
| > The script will print the password if it is found and the time		|
| taken to find the password.															|
| > In your case you can channge that in with that suitbale for you.		|
| > I will leave a comment there so that you can change it.					|
+--------+--------+--------+--------+--------+--------+--------+--------+
'''
import pikepdf
import time
# Change the filename.pdf to the name of your pdf file
pdf_file = "<<filename.pdf>>"
# Make you changes here accroding to your needs, or you can use a text file containing all the passwords, you will find text files of passwords on the internet.
passwords = []
for i in range(1, 100000):
	if len(str(i)) < 5:
		passwords.append("0" * (5 - len(str(i))) + str(i))
	else:
		passwords.append(str(i))

i = 0

start_time = time.time()
for password in passwords:

	i += 1
	print("\r {} Password Tested!".format(i), end = "")
	try:
		pikepdf.open(pdf_file, password=password)
		print("\n", "* " * 15)
		end_time = time.time()
		print("Password Found")
		print("Password: {}".format(password))
		print("[{}] Password Tested in: {} seconds".format(i, str(end_time - start_time)[:4]))
		print("* " * 15)
		break
	except:
		print("Something went wrong!")
		pass

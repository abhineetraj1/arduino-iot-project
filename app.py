from time import sleep
from flask import *
from flask import render_template
from pyfirmata import Arduino

# Trying to connect computer with boarding
for i in range(1,6):
	try:
		ard=Arduino("COM"+str(i))
		break
	except:
		print("Error")

# Turning off all the switches in circuit
ard.digital[3].write(1)
ard.digital[4].write(1)
ard.digital[2].write(0)
ard.digital[5].write(1)

# Creating a function to give output through arduino
def funcn(n):
	if "on" in n:
		if "red" in n:
			ard.digital[3].write(1)
			ard.digital[4].write(1)
			ard.digital[5].write(0)
		elif "green" in n:
			ard.digital[4].write(1)
			ard.digital[5].write(1)
			ard.digital[3].write(0)
		elif "blue" in n:
			ard.digital[3].write(1)
			ard.digital[5].write(1)
			ard.digital[4].write(0)
		elif "buzzer" in n:
			ard.digital[2].write(1)
		else:
			return "error"
	elif "off" in n:
		ard.digital[3].write(1)
		ard.digital[4].write(1)
		ard.digital[2].write(0)
		ard.digital[5].write(1)
	elif n == "emergency":
		# Declaring function for emergency, where buzzer will sound beep beep in loop
		ard.digital[5].write(0)
		for i in range(0,21):
			ard.digital[2].write(i%2)
			sleep(0.3)
		ard.digital[5].write(1)
	else:
		return "error"

#Setting up server and declaring routes
app = Flask(__name__, template_folder="temp", static_folder="static")

# Making route for user handling
@app.route("/", methods=["POST","GET"])
def a():
	if request.method == "GET":
		return render_template("index.html")
	else:
		funcn(request.data.decode("utf-8"))
		return render_template("index.html")

# Made by Abhineet Raj (https://github.com/abhineetraj1)
if __name__ == '__main__':
	app.run()
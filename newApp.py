from flask import Flask, render_template, redirect, request, url_for, jsonify
#import RPi.GPIO as GPIO
import time
from database import setName
# servo = True
pass_scan = True ## they haven't passed the scan is false
add_success = False
app = Flask(__name__)

# Set up GPIO pin for the servo motor
""" servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50 Hz frequency """

""" while (pass_scan==False):
        servo.start(2.5)  # Start servo motor at 0 degrees position
        time.sleep(1)
        servo.ChangeDutyCycle(7.5)  # Rotate servo motor to 90 degrees position
        time.sleep(1) """

@app.route("/start_scan", methods=["POST"])
def scan_on_r():
    global pass_scan
    print("Start scan")
    # Code to scan the face and determine if it is successful
    # If the face is successfully scanned, turn off the servo motor
    pass_scan = True
    # servo.stop()  # Stop the servo motor
    if (pass_scan == True):
        #if pass_scan is true, link to another page
        return redirect(url_for("access_granted"))
    return render_template("home_page.html", title="Home")

@app.route("/stop_scan", methods=["POST"])
def scan_off_r():
    print("Stop Scan")
    return "ok"

@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home_page.html", title="Home")

@app.route("/access_granted", methods=["GET"])
def access_granted():
    return render_template("access_granted.html", title="Access Granted")


@app.route("/add_face", methods=["POST"])
def adding_face():
    name = request.json['name']
    setName(name)
    # Process the name and add it to the database
    message = 'Face added: {}'.format(name)
    return jsonify({'message': message})


@app.route("/stop_add", methods=["POST"])
def face_added():
    print("Stop Scan")
    return "ok"


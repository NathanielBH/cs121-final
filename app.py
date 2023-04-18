from flask import Flask, render_template, redirect, url_for
import RPi.GPIO as GPIO
import time

# servo = True
pass_scan = False ## they haven't passed the scna is false
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
       #! /usr/bin/python

    # import the necessary packages
    from imutils.video import VideoStream
    from imutils.video import FPS
    import face_recognition
    import imutils
    import pickle
    import time
    import cv2

    #Initialize 'currentname' to trigger only when a new person is identified.
    currentname = "unknown"
    #Determine faces from encodings.pickle file model created from train_model.py
    encodingsP = "encodings.pickle"

    # load the known faces and embeddings along with OpenCV's Haar
    # cascade for face detection
    print("[INFO] loading encodings + face detector...")
    data = pickle.loads(open(encodingsP, "rb").read())

    # initialize the video stream and allow the camera sensor to warm up
    # Set the ser to the followng
    # src = 0 : for the build in single web cam, could be your laptop webcam
    # src = 2 : I had to set it to 2 inorder to use the USB webcam attached to my laptop
    vs = VideoStream(src=0,framerate=10).start()
    #vs = VideoStream(usePiCamera=True).start()
    time.sleep(2.0)

    # start the FPS counter
    fps = FPS().start()

    # loop over frames from the video file stream
    while True:
    	    # grab the frame from the threaded video stream and resize it
	    # to 500px (to speedup processing)
	    frame = vs.read()
	    frame = imutils.resize(frame, width=500)
	    # Detect the fce boxes
	    boxes = face_recognition.face_locations(frame)
	    # compute the facial embeddings for each face bounding box
	    encodings = face_recognition.face_encodings(frame, boxes)
	    names = []

	    # loop over the facial embeddings
	    for encoding in encodings:
		    # attempt to match each face in the input image to our known
		    # encodings
		    matches = face_recognition.compare_faces(data["encodings"],
			    encoding)
		    name = "Unknown" #if face is not recognized, then print Unknown

		    # check to see if we have found a match
		    if True in matches:
			    # find the indexes of all matched faces then initialize a
			    # dictionary to count the total number of times each face
			    # was matched
			    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			    counts = {}

			    # loop over the matched indexes and maintain a count for
			    # each recognized face face
			    for i in matchedIdxs:
				    name = data["names"][i]
				    counts[name] = counts.get(name, 0) + 1

			    # determine the recognized face with the largest number
			    # of votes (note: in the event of an unlikely tie Python
			    # will select first entry in the dictionary)
			    name = max(counts, key=counts.get)

			    #If someone in your dataset is identified, print their name on the screen
			    if currentname != name:
				    currentname = name
				    print(currentname)
				    pass_scan = True
				   # time.sleep(10)
				   # return redirect(url_for("access_granted"))
                                   # return "ok"
		    # update the list of names
		    names.append(name)

	    # loop over the recognized faces
	    for ((top, right, bottom, left), name) in zip(boxes, names):
		    # draw the predicted face name on the image - color is in BGR
		    cv2.rectangle(frame, (left, top), (right, bottom),
			    (0, 255, 225), 2)
		    y = top - 15 if top - 15 > 15 else top + 15
		    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			    .8, (0, 255, 255), 2)

	    # display the image to our screen

	    cv2.imshow("Facial Recognition is Running", frame)
	    key = cv2.waitKey(1) & 0xFF

	    # quit when 'q' key is pressed
	    if key == ord("q"):
		    break

	    # update the FPS counter
	    fps.update()

    # stop the timer and display FPS information
    fps.stop()
    print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()

    # Code to scan the face and determine if it is successful
    # If the face is successfully scanned, turn off the servo motor
    #pass_scan = True
    # servo.stop()  # Stop the servo motor
    if (pass_scan == True):
        #if pass_scan is true, link to another page
        return redirect(url_for("access_granted"))
    return "ok"

@app.route("/stop_scan", methods=["POST"])
def scan_off_r():
    print("Stop Scan")
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("home_page.html", title="Home")

@app.route("/access_granted", methods=["GET"])
def access_granted():
    return render_template("access_granted.html", title="Access Granted")

@app.route("/add_face", methods=["POST"])
def adding_face():
    global add_success
    print("Adding")
    add_success = True
    if (add_success == True):
        #code for adding face to database
        #return redirect(url_for("face_added"))
        print('nice')
    return "ok"

@app.route("/stop_add", methods=["POST"])
def face_added():
    print("Stop Scan")
    return "ok"

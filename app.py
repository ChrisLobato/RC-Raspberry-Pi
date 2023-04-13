import RPi.GPIO as GPIO
from time import sleep
from flask import Flask, render_template,request
from flask import Flask, request

app = Flask(__name__)


 # Sets up the pin layout/ Naming system we want to use
GPIO.setmode(GPIO.BOARD)

#declare the pins and their names
Motor1input1 = 35
Motor1input2 = 37
motor_pin1Enable = 33

Motor2input1 = 19
Motor2input2 = 21
motor_pin2Enable = 32

#Set all the pins of the first motor to outputs
GPIO.setup(motor_pin1Enable, GPIO.OUT)
GPIO.setup(Motor1input1, GPIO.OUT)
GPIO.setup(Motor1input2, GPIO.OUT)

GPIO.setup(motor_pin2Enable, GPIO.OUT)
GPIO.setup(Motor2input1, GPIO.OUT)
GPIO.setup(Motor2input2, GPIO.OUT)

#Default going forward
GPIO.output(Motor1input1, GPIO.HIGH)
GPIO.output(Motor1input2, GPIO.LOW)
GPIO.output(Motor2input1, GPIO.HIGH)
GPIO.output(Motor2input2, GPIO.LOW)
motorPWM1 = GPIO.PWM(motor_pin1Enable, 800) ##second argument can be changed affects how "Nicely" the motor runs
motorPWM1.start(0)
motorPWM2 = GPIO.PWM(motor_pin2Enable, 800) ##second argument can be changed affects how "Nicely" the motor runs
motorPWM2.start(0)


@app.route("/", methods=['GET','POST'])
def main():


   return render_template('main.html')

@app.route("/FORWARD")
def forward():

   
   return render_template('main.html')
   
@app.route("/STOP")
def stop():
   
   
   return render_template('main.html')


@app.route('/update_speed', methods=['GET','POST'])
def update_slider():
    if request.method == 'POST':

      value = request.form['value']
      
    return value



if __name__ == "__main__":
   try :
      app.run(host= '0.0.0.0', port=80, debug = True)
   finally: GPIO.cleanup()


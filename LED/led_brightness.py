
# Author: LearningEmbedded.com
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this code and associated documentation files , to use, copy, modify, merge,
# publish, distribute when you agree to the following conditions:
# Attribution — You must give appropriate credit, provide a link to the license, 
#               and indicate if changes were made. You may do so in any reasonable
#               manner, but not in any way that suggests the licensor endorses you 
#               or your use.
# No additional restrictions — You may not apply legal terms or technological 
#                              measures that legally restrict others from doing
#                              anything the license permits.

# http://learningembedded.com/

import RPi.GPIO as GPIO				    # imports Raspberry Pi's GPIO module
ledPin = 18             			    #defines a variable with 18 value  
GPIO.setmode(GPIO.BCM) 			    	# sets GPIO pins naming same as BCM SoC
GPIO.setup(led_pin, GPIO.OUT) 		# sets 18 pin as output
pwmLed = GPIO.PWM(ledPin, 500) 		# create PWM with ledPin as channel & frequency 500
pwmLed.start(100) 				      	# to start PWM with duty cycle 100
while True:
	duty_s = raw_input("Enter Brightness (0 to 100):") 	# for inputting data
	duty = int(duty_s) 									                # typecasting to int
	pwmLed.ChangeDutyCycle(duty) 					            	# to change duty cycle
	

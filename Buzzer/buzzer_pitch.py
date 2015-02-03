
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
 
 import RPi.GPIO as GPIO 		# imports Raspberry Pi's GPIO module
 import time 					# imports time module
 buzzerPin = 18  				#defines a variable with 18 value  
 GPIO.setmode(GPIO.BCM) 		# sets GPIO pins naming same as BCM SoC
 GPIO.setup(buzzerPin, GPIO.OUT)# sets 18 pin as output
 def buzz(pitch, duration):		#define a function called buzz
 period = 1.0 / pitch       	#calculate period
 delay = period / 2        		# calculate delay
 cycles = int(duration * pitch) # calculate cycle
 for i in range(cycles): 
	GPIO.output(buzzerPin, True)	# true sets buzzer pin high
	time.sleep(delay)
	GPIO.output(buzzerPin, False) 	#false sets buzzer pin low
	time.sleep(delay)
 while True:
	pitch_s = raw_input("Enter Pitch (200 to 2000): ") 	#  inputting pitch
	pitch = float(pitch_s)								# typecasting inputed data to float type
	duration_s = raw_input("Enter Duration (seconds): ")# inputting duration
	duration = float(duration_s)						# typecasting inputed data to float type
	buzz(pitch, duration)								# execute buzz function
	


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

import RPi.GPIO as GPIO                 # imports Raspberry Pi's GPIO module
import time                             # imports time module
GPIO.setmode(GPIO.BCM)                  # sets GPIO pins naming same as BCM SoC
GPIO.setup(18, GPIO.OUT) 				# sets 18 pin as output
while (True): 
	GPIO.output(18, True) 				# true sets buzzer pin high
	time.sleep(0.5) 					#delay of 0.5 sec
	GPIO.output(18, False)   			#false sets buzzer pin low
	time.sleep(0.5) 					#delay of 0.5 sec
	

	

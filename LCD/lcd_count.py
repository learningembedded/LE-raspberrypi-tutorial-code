 
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

 from lcd import CharLCD 	          # import CharLCD module
 from time import sleep 	          #import sleep module
 lcd = CharLCD()      
 lcd.begin(16,2)    	            	# initialize LCD

 i = 0
 while True:
	lcd.clear()  		      	          # clear LCD
	lcd.message('Counting: ' + str(i)) # LCD message displaying the numbers
	sleep(1) 						               # sleep for 1 sec
	i = i + 1 						             # increment i variable by 1

	
	

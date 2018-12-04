# Import required libraries
import time
import datetime
import RPi.GPIO as GPIO
import numpy

#   LCD SETUP
# Define GPIO to LCD mapping
LCD_RS = 26
LCD_E  = 19
LCD_D4 = 13
LCD_D5 = 6
LCD_D6 = 5
LCD_D7 = 11


# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

SPOTS = numpy.zeros(10)


#def manipulateArray(pin):




def sensorCallback(channel):
  # Called if sensor output changes
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  if GPIO.input(channel):
    # No magnet
    # MANIPULATE ARRAY
    if channel == 17:
      SPOTS[0]= 0
    elif channel == 23:
      SPOTS[1] = 0
    elif channel == 21:
      SPOTS[2] = 0
    elif channel == 18:
      SPOTS[3] = 0
    elif channel == 27:
      SPOTS[4] = 0
    elif channel == 25:
      SPOTS[5]= 0
    elif channel == 22:
      SPOTS[6] = 0
    elif channel == 20:
      SPOTS[7] = 0
    elif channel == 16:
      SPOTS[8] = 0
    elif channel == 12:
      SPOTS[9] = 0

    print("Space " + str(channel) + " EMPTY " + stamp)
  else:
    # Magnet present
    if channel == 17:
      SPOTS[0]= 1
    elif channel == 23:
      SPOTS[1] = 1
    elif channel == 21:
      SPOTS[2] = 1
    elif channel == 18:
      SPOTS[3] = 1
    elif channel == 27:
      SPOTS[4] = 1
    elif channel == 25:
      SPOTS[5]= 1
    elif channel == 22:
      SPOTS[6] = 1
    elif channel == 20:
      SPOTS[7] = 1
    elif channel == 16:
      SPOTS[8] = 1
    elif channel == 12:
      SPOTS[9] = 1


    print("Space " + str(channel) + " OCCUPIED " + stamp)

def buttonPress(channel):
  timestamp = time.time()
  stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  print("Button Pressed")
  i = 0
  spotOpenFlag = False
  for spot in SPOTS:
    if spot == 0:
      spotOpenFlag = True
      break
    i = i + 1

  spotString = ""
  if i == 0:
    spotString = "Park in spot 1"
  elif i == 1:
    spotString = "Park in spot 2"
  elif i == 2:
    spotString = "Park in spot 3"
  elif i == 3:
    spotString = "Park in spot 4"
  elif i == 4:
    spotString = "Park in spot 5"
  elif i == 5:
    spotString = "Park in spot 6"
  elif i == 6:
    spotString = "Park in spot 7"
  elif i == 7:
    spotString = "Park in spot 8"
  elif i == 8:
    spotString = "Park in spot 9"
  elif i == 9:
    spotString = "Park in spot 10"


  # Output reccomendation
  if not spotOpenFlag:
    lcd_string("Lot is FULL", LCD_LINE_1)
    lcd_string("Come again later",LCD_LINE_2)
    time.sleep(3) # 3 second delay
    lcd_string("", LCD_LINE_1)
    lcd_string("",LCD_LINE_2)
  else:
    lcd_string(spotString,LCD_LINE_1)
    lcd_string(stamp,LCD_LINE_2)
    time.sleep(3) # 3 second delay
    lcd_string("", LCD_LINE_1)
    lcd_string("",LCD_LINE_2)



def main():
  # Wrap main content in a try block so we can
  # catch the user pressing CTRL-C and run the
  # GPIO cleanup function. This will also prevent
  # the user seeing lots of unnecessary error
  # messages.

  spot1 = 17
  spot2 = 23
  spot3 = 21
  spot4 = 18
  spot5 = 27
  spot6 = 25
  spot7 = 22
  spot8 = 20
  spot9 = 16
  spot10 = 12

  # Get initial reading
  sensorCallback(spot1)
  sensorCallback(spot2)
  sensorCallback(spot3)
  sensorCallback(spot4)
  sensorCallback(spot5)
  sensorCallback(spot6)
  sensorCallback(spot7)
  sensorCallback(spot8)
  sensorCallback(spot9)
  sensorCallback(spot10)
  #button press
  buttonPress(4)

  # Initialise display
  lcd_init()


  try:
    # Loop until users quits with CTRL-C
    while True :
      time.sleep(0.1)

  except KeyboardInterrupt:
    # Reset GPIO settings
    GPIO.cleanup()

# Tell GPIO library to use GPIO references
GPIO.setmode(GPIO.BCM)

print("Setup GPIO pins")

# Set Switch GPIO as input
# Pull high by default

GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
GPIO.setup(LCD_E, GPIO.OUT)  # E
GPIO.setup(LCD_RS, GPIO.OUT) # RS
GPIO.setup(LCD_D4, GPIO.OUT) # DB4
GPIO.setup(LCD_D5, GPIO.OUT) # DB5
GPIO.setup(LCD_D6, GPIO.OUT) # DB6
GPIO.setup(LCD_D7, GPIO.OUT) # DB7





#GPIO 17 SPOT 1
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO 23 SPOT 2
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(23, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

# GPIO 21 SPOT 3
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(21, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO 18 SPOT 4
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO 27 SPOT 5
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(27, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO 25 SPOT 6
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(25, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO 22 SPOT 7
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(22, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO 20 SPOT 8
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(20, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO 16 SPOT 9
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(16, GPIO.BOTH, callback=sensorCallback, bouncetime=200)

#GPIO 12 SPOT 10
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(12, GPIO.BOTH, callback=sensorCallback, bouncetime=200)



#Buttton Press
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(4, GPIO.RISING, callback=buttonPress, bouncetime=100)



def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD) # 110011 Initialise
  lcd_byte(0x32,LCD_CMD) # 110010 Initialise
  lcd_byte(0x06,LCD_CMD) # 000110 Cursor move direction
  lcd_byte(0x0C,LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
  lcd_byte(0x28,LCD_CMD) # 101000 Data length, number of lines, font size
  lcd_byte(0x01,LCD_CMD) # 000001 Clear display
  time.sleep(E_DELAY)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  lcd_toggle_enable()

def lcd_toggle_enable():
  # Toggle enable
  time.sleep(E_DELAY)
  GPIO.output(LCD_E, True)
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)
  time.sleep(E_DELAY)

def lcd_string(message,line):
  # Send string to display




  message = message.ljust(LCD_WIDTH," ")

  lcd_byte(line, LCD_CMD)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)



if __name__=="__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)
    lcd_string("Goodbye!",LCD_LINE_1)
    GPIO.cleanup()


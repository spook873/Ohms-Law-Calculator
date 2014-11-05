# Ohms Law.py
#   This program calculates voltage, Amperes, and resistance.
#   Created by: Spook

print "This program calculates Voltage, Amperes, and Resistance"
print "What would you like to calculate?"
x = input("Voltage, Amps, or Resistance")

if x == 1: #Voltage
    i = input("How many Amps?") + .0
    r = input("What's the Resistance?") + .0
    answer = i * r
    
if x == 2: #Amps
    v = input("What's the Voltage?") + .0
    r = input("What's the Resistance") + .0
    answer = v / r
    
if x == 3: #Resistance
    v = input("What's the Voltage?") + .0
    i = input("What's the Amps?") + .0
    answer = v / i

print "The answer is:", answer

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "

show_version.strip()
data = show_version.split()

print()
#a continuación se obtiene el valor del campo 1 data, se le pasa a minúsculas y después se evalúa su igualdad 
vendor_cisco = "cisco" in data[1].lower()
print("Checking if model contains Cisco: {}".format(vendor_cisco))

print("Is 881 in the serial Number?" , '881' in data[2])

print (f"Model {data[1]},\nSerial Number {data[2]}")




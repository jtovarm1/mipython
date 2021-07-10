"""
4. Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

Obtain the list entry associated with the FastEthernet4 interface. You can just hard-code the
index at this point since we haven't covered for-loops or regular expressions.
Use the string .split() method to obtain both the IP address and the corresponding interface
associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero.
You might need to 'pip install pycodestyle' on your computer (you should be able to type this
from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.
"""

from pprint import pprint

with open("show_ip_int_brief.txt") as f:
    address = f.readlines()

intf4 = address[5]  # el valor 5 de la lista pasa a ser el string intf4
data = intf4.split()
intf_name = data[0]
ip_address = data[1]

intf4Tuple = (intf_name, ip_address)

print(type(intf4))
pprint(intf4Tuple)

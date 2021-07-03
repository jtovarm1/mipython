"""
3. Read in the 'show_arp.txt' file using the readlines() method. Use a list slice to
remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)

Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single
string using the newline character ('\n') as the separator.

Write this string containing the three ARP entries out to a file named 'arp_entries.txt'.
"""
from pprint import pprint

with open("show_arp.txt") as f:
    arp = f.readlines()
print("Lista original:")
pprint(arp)
arp = arp[1:]
arp.sort()
print()
print("Lista sin cabecera y ordenada por direcciones IP")
pprint(arp)
nuevo_arp = arp[:3]  # se empieza del elemento[0] hasta PERO SIN INCLUIR el [3] >> 0,1,2
print()
print("Las tres primeras entradas de la lista son:")
pprint(nuevo_arp)
# ahora se van unir las listas de nuevo_arp tomando "\n" como caracter de unión
# y después se va va a cambiar el tipo de dato a string y asignar a la constante "DIR"
DIR = str("\n".join(nuevo_arp))
print()
print("La próxima estructura es:", type(DIR))
print(DIR)

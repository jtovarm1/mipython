"""
Se va a romper una direccion ipv4 en sus octetos y estos
se van a mostrat en una columna en decimal, bin y hex
"""

O1 = "Octet1"
O2 = "Octet2"
O3 = "Octet3"
O4 = "Octet4"

ip_addr = input("Please type in an IPv4 address: ")

octets = ip_addr.split(".")
print("-" * 60)
print("{:^15}{:^15}{:^15}{:^15}".format(O1, O2, O3, O4))
print("-" * 60)
print(f'{octets[0]:^15}{octets[1]:^15}{octets[2]:^15}{octets[3]:^15}')

# los resultados del split es str y eso no se puede pasar a binario o a hex
# para ellos es necesario convertir el str a int y eso convertirlo
# a bin o hex se trabaja de adentro hacia afuera


print(
    "{:^15}{:^15}{:^15}{:^15}".format(
        bin(int(octets[0])),
        bin(int(octets[1])),
        bin(int(octets[2])),
        bin(int(octets[3]))
        )
    )

# En la prox linea el backslash rompe la linea pero mantiene la unidad
# Es necesario que no haya un espacio en blanco después

print(f'{hex(int(octets[0])):^15}{hex(int(octets[1])):^15}\
{hex(int(octets[2])):^15}{hex(int(octets[3])):^15}')

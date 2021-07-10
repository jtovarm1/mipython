"""
Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain
the first and last lines of the output.
From the first line use the string .split() method to obtain the local AS number.
From the last line use the string .split() method to obtain the BGP peer IP address.
Print both local AS number and the BGP peer IP address to the screen.
"""
with open("show_ip_bgp_summ.txt") as f:
    lines = f.readlines()

line1 = lines[0]  # line1 es un string
line_final = lines[-1]  # line_final también

data_line1 = line1.split()  # la función split() devuelve una clase lista
data_line_final = line_final.split()
local_AS = data_line1[-1]  # Se usa corchete porque es una lista
peer_IP = data_line_final[0]  # Con paréntesis, devuelve: 'list' object is not callable

print("El tipo de dato de line1 es:", type(line1))
print("El tipo de dato de data_line1 es:", type(data_line1))
print()
print(f"Local AS number= {local_AS}, Peer IP address = {peer_IP}")

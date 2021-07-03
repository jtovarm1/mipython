""""
2. Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list.
Use the .extend() method to add two more IP addresses to the end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list.
Print out the last IP address in the list.

Using the .pop() method to remove the first IP add in the list and the last IP add in the list.

Update the new first IP add in the list to be '2.2.2.2'. Print out the new first IP add in the list.
"""
address = ["192.168.1.1", "1.1.1.1", "10.0.0.1", "172.16.0.4", "8.8.8.8"]

print(address)
address.append("8.8.4.4")
print(address)
address.extend(["4.4.4.4", "2.2.2.2"])
print(address)
address = address + ["192.168.2.1", "192.168.3.1"]
print(address)
print("La primera direccion: ", address[0])
print("La última dirección: ", address[-1])# así se muestra el último item
print("Items en la lista: ", len(address))
address.pop() #de esta manara se elimina el último item
address.pop(0)
print("Se eliminaron el primer y último item de la lista.\nNueva lista: ", address)
address[0] = "2.2.2.2"
print("Se actualizó el item[0] de la lista.\nNuevo item[0] en la lista :", address[0])

mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"
c1 = "IP ADDR"
c2 = "MAC ADDRESS"
sep = "-"*19

addr1 = mac1.split()
addr2 = mac2.split()
addr3 = mac3.split()

print()
print(f"{c1:>20}{c2:>20}")
print(f"{sep:>20} {sep:20}")
print(f"{addr1[1]:>20}{addr1[3]:>20}")
print(f"{addr2[1]:>20}{addr2[3]:>20}")
print(f"{addr3[1]:>20}{addr3[3]:>20}")

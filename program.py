#hello friends, this is not a very good way to implement IP subnetting
#this is because i only used my existing knowledge of Python with no help from Google ¯\_(ツ)_/¯
# as a result, this took me a lot more time than I had anticipated and so I felt like I needed to put it on github
# because of all the time I wasted
# but yea, it works

import numpy as np

#converts an octet to a list of booleans
def octetToBinary(octet):
    n = 7
    octetInt = int(octet)
    list = []

    while (n >= 0):

        curr = 1 * (2**n)
        if octetInt % curr == octetInt:
            list.append(False)

        else:
            list.append(True)
            octetInt = octetInt % curr
        n -= 1

    return list

#converts a list of 8 booleans to an octet
def binaryToOctet(binary):
    oct = 0
    n = 7
    index = 0
    while n >= 0:
        if binary[index]:
            oct += 1 * (2**n)
        index += 1
        n -= 1
    return oct


#returns a list of 4 boolean lists from a string formatted IP address
def ipToBinary(ip):
    ipSplit = ip.split(".")
    list = []
    for i in ipSplit:
        list.append(octetToBinary(i))
    return list

#returns a list of 4 boolean lists to represent a subnet mask based on the cidr block
def subnetMaskBinary(cidr):
    list = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    initialPop = int(cidr/8)
    initialRemainder = cidr % 8

    if initialPop == 4:
        l1 = [True]*8
        l2 = [True]*8
        l3 = [True]*8
        l4 = [True]*8
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    if initialPop == 3:
        l1 = [True]*8
        l2 = [True]*8
        l3 = [True]*8
        diff = 8 - initialRemainder
        l4 = [True]*initialRemainder
        while diff > 0:
            l4.append(False)
            diff -= 1
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    if initialPop == 2:
        l1 = [True]*8
        l2 = [True]*8
        diff = 8 - initialRemainder
        l3 = [True] * initialRemainder
        while diff > 0:
            l3.append(False)
            diff -= 1
        l4 = [False]*8
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    if initialPop == 1:
        l1 = [True]*8
        l3 = [False]*8
        l4 = [False]*8
        diff = 8 - initialRemainder
        l2 = [True] * initialRemainder
        while diff > 0:
            l2.append(False)
            diff -= 1
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    if initialPop == 0:
        diff = 8 - initialRemainder
        l1 = [True] * initialRemainder
        while diff > 0:
            l1.append(False)
            diff -= 1
        l2 = [False]*8
        l3 = [False]*8
        l4 = [False]*8
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    return list

#returns a list of 4 boolean lists to represent the inverse of a subnet mask
def subnetMaskBinaryInverse(cidr):
    list = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    initialPop = int(cidr/8)
    initialRemainder = cidr % 8

    if initialPop == 4:
        l1 = [False]*8
        l2 = [False]*8
        l3 = [False]*8
        l4 = [False]*8
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    if initialPop == 3:
        l1 = [False]*8
        l2 = [False]*8
        l3 = [False]*8
        diff = 8 - initialRemainder
        l4 = [False]*initialRemainder
        while diff > 0:
            l4.append(True)
            diff -= 1
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    if initialPop == 2:
        l1 = [False]*8
        l2 = [False]*8
        diff = 8 - initialRemainder
        l3 = [False] * initialRemainder
        while diff > 0:
            l3.append(True)
            diff -= 1
        l4 = [True]*8
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    if initialPop == 1:
        l1 = [False]*8
        l3 = [True]*8
        l4 = [True]*8
        diff = 8 - initialRemainder
        l2 = [False] * initialRemainder
        while diff > 0:
            l2.append(True)
            diff -= 1
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    if initialPop == 0:
        diff = 8 - initialRemainder
        l1 = [False] * initialRemainder
        while diff > 0:
            l1.append(True)
            diff -= 1
        l2 = [True]*8
        l3 = [True]*8
        l4 = [True]*8
        list.append(l1)
        list.append(l2)
        list.append(l3)
        list.append(l4)

    return list

#given an ip address and subnet mask, return the network address in binary
def networkAddr(x, y):

    s1 = np.array(x)
    s2 = np.array(y)
    return (s1 & s2).tolist()

#given an ip address and subnet mask(inverse), return the broadcast address in binary
def broadcastAddr(x, y):
    s1 = np.array(x)
    s2 = np.array(y)
    return (s1 | s2).tolist()

#returns an IP address in a string format from a binary
def buildIP(binary):
    s = ""
    for i in range(0, 4):
        if i == 3:
            s += str(binaryToOctet(binary[i]))
        else:
            s += str(binaryToOctet(binary[i])) + "."
    return s

#returns true if given IP string is valid, else returns false
def ipValidate(ipString):
    status = True
    split = ipString.split(".")
    if len(split) != 4:
        status = False
    for num in split:
        if int(num) > 255:
            status = False
        if int(num) < 0:
            status = False
    return status

#returns true if given cidr block is valid, else returns false
def cidrValidate(cidr):
    if cidr > 32:
        return False
    if cidr < 0:
        return False
    else:
        return True

#increments a binary by 1
def binaryIncrement(binary):
    list = []
    list.append([False]*8)
    list.append([False]*8)
    list.append([False]*8)
    list.append([False, False, False, False, False, False, False, True])
    s1 = np.array(list)
    s2 = np.array(binary)
    return (s1 | s2).tolist()

#decrements a binary by 1
def binaryDecrement(binary):
    list = []
    list.append([True] * 8)
    list.append([True] * 8)
    list.append([True] * 8)
    list.append([True, True, True, True, True, True, True, False])
    s1 = np.array(list)
    s2 = np.array(binary)
    return (s1 & s2).tolist()

#returns a string formatted host range of ip addresses from the network address and broadast address
def buildHostRange(networkAddress, broadcastAddress):

    return "Range of host addresses: " + buildIP(binaryIncrement(networkAddress)) + " - " + buildIP(binaryDecrement(broadcastAddress))

#start of program
print("Python IP Address Subnetting Tool")
print("**************************")

while True:

    ip = input("Please enter an IP address: ")
    if ipValidate(ip) == False:
        print("Please enter a valid IP address ex: 120.33.31.48\n")
        continue
    else:

        while True:

            cidr = input("Please enter a CIDR block: ")
            if cidrValidate(int(cidr)) == False:
                print("Please enter a valid CIDR block. CIDR can range from 0 - 32\n")
                continue
            else:

                print()

                ipBinary = ipToBinary(ip)

                subnetMaskB = subnetMaskBinary(int(cidr))

                subnetMaskInverse = subnetMaskBinaryInverse(int(cidr))

                networkBinary = networkAddr(subnetMaskB, ipBinary)

                broadcastBinary = broadcastAddr(subnetMaskInverse, ipBinary)

                networkBinaryInc = binaryIncrement(networkBinary)

                print("Subnet Mask: " + buildIP(subnetMaskB))
                print("Network Address: " + buildIP(networkBinary))
                print("Broadcast Address: " + buildIP(broadcastBinary))
                print(buildHostRange(networkBinary, broadcastBinary))
                break

    break

"""
The idea is very simple for Mode A just take consequetive differences and add the absolute value
For ModeB sort the floors in reverse when they are in DOWN and normal in UP. Take the differences
after flattening the list
Usage:
python Elevator.py --filename="Input.txt" --mode="A"
python Elevator.py --filename="Input.txt" --mode="B"

Output

python Elevator.py --filename 'Input.txt' --mode "A"
Input Sequence: 10:8-1
Output Sequence: 10 8 1 ( 9 )
Input Sequence: 9:1-5,1-6,1-5
Output Sequence: 9 1 5 1 6 1 5 ( 30 )
Input Sequence: 2:4-1,4-2,6-8
Output Sequence: 2 4 1 4 2 6 8 ( 16 )
Input Sequence: 3:7-9,3-7,5-8,7-11,11-1
Output Sequence: 3 7 9 3 7 5 8 7 11 1 ( 36 )
Input Sequence: 7:11-6,10-5,6-8,7-4,12-7,8-9
Output Sequence: 7 11 6 10 5 6 8 7 4 12 7 8 9 ( 40 )
Input Sequence: 6:1-8,6-8
Output Sequence: 6 1 8 6 8 ( 16 )


python Elevator.py --filename 'Input.txt' --mode "B"
Input Sequence: 10:8-1
Output Sequence: 10 8 1 ( 9 )
Input Sequence: 9:1-5,1-6,1-5
Output Sequence: 9 1 5 6 ( 13 )
Input Sequence: 2:4-1,4-2,6-8
Output Sequence: 2 4 2 1 6 8 ( 12 )
Input Sequence: 3:7-9,3-7,5-8,7-11,11-1
Output Sequence: 3 3 5 7 8 9 11 1 ( 18 ) **
Input Sequence: 7:11-6,10-5,6-8,7-4,12-7,8-9
Output Sequence: 7 11 10 6 5 6 8 12 7 4 8 9 ( 30 )
Input Sequence: 6:1-8,6-8
Output Sequence: 6 1 6 8 ( 12 )

** I have really concerns about the output denoted by line **, since the first entry is starting floor
3 and series of floors visited is 3 5 7 and so on. Hence repition of 3 . However total number of floors
is unaffected.

"""

from compiler.ast import flatten
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--filename", action="store", help="Read From FILE", metavar="FILE")
parser.add_option("-m", "--mode", action="store", help="Print the mode of Operation")

(options, args) = parser.parse_args()


def returnTravelModeA(x):

    print "Input Sequence: %s" % x
    Xsplit = x.split(':')
    init_floor = int(Xsplit[0])
    y = Xsplit[1].split(',')
    z = [[p.split('-')[0], p.split('-')[1]] for p in y]
    # remove duplicate
    Zf = _remove_Duplicate(flatten(z))
    Zfint = map(int, Zf)
    Zfdiff = [Zfint[i] - Zfint[i - 1] for i in range(len(Zfint))][1:]
    k = map(abs, Zfdiff)
    d = abs(init_floor - Zfint[0])
    total = sum(k) + d
    output_str = Xsplit[0] + " " + ' '.join(Zf) + " ( " + str(total) + " )"
    print  "Output Sequence: " + output_str
    return 0


def returnTravelModeB(x):

    zfinal = []
    upbucket = []
    downbucket = []
    index = 0
    print "Input Sequence: %s" % x
    xsplit = x.split(':')
    init_floor = int(xsplit[0])
    y = xsplit[1].split(',')
    ## Generate a new list involving traveling the same direction
    z = [[p.split('-')[0], p.split('-')[1]] for p in y]
    zint = [map(int, p) for p in z]
    p = len(zint)
    while index < p:
        if zint[index][0] > zint[index][1]:
            downbucket = []
            upbucket.extend([zint[index][1], zint[index][0]])
            upbucket.sort(reverse=True)
            zfinal.append(upbucket)

        elif zint[index][1] > zint[index][0]:
            upbucket = []
            downbucket.extend([zint[index][1],  zint[index][0]])
            downbucket.sort()
            zfinal.append(downbucket)
        else:
            continue
        index += 1
    Zint = _remove_Duplicate(zfinal)
    ZInt = flatten(Zint)
    Zunique = _remove_Duplicate(ZInt)
    zfdiff = [Zunique[i] - Zunique[i - 1] for i in range(len(Zunique))][1:]
    k = map(abs, zfdiff)
    d = abs(init_floor - Zunique[0])
    total = sum(k) + d
    output_str = xsplit[0] + " " + ' '.join(map(str, Zunique)) + " ( " + str(total) + " )"
    print  "Output Sequence: " + output_str

    return 0


def _remove_Duplicate(z):
    znew = [z[0]]
    for i in z:
        if znew[-1] != i:
            znew.append(i)
    return znew


if __name__ == "__main__":

    (options, args) = parser.parse_args()
    with open(options.filename, 'r') as fd:
        lines = fd.readlines()
        for line in lines:
            if line != ' ':
                inputline = line.split('\n')[0]
                if options.mode == "A":
                    returnTravelModeA(inputline)
                if options.mode == "B":
                    returnTravelModeB(inputline)

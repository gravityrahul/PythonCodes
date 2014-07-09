#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Problem: Given a number print all its factors without duplication. See Example for Details

The Logic behind the algorithm is recursively break the factors until prime factors are reached.
Also, take care of all the duplicates. I have run all the cases in the example and recored the time.

I was also thinking of another approach where, I would calculate all the prime factors and then start 
building all the numbers equal to given number. But didn't approach in that direction. 

The Worked out Example in this Code

rahul@Milkyway:~$ python ReturnFactors.py -n 96 
Generating factors for 96
###############################################
96 x 1
48 x 2
32 x 3
24 x 4
16 x 6
12 x 8
24 x 2 x 2
16 x 3 x 2
12 x 4 x 2
8 x 6 x 2
8 x 4 x 3
6 x 4 x 4
12 x 2 x 2 x 2
8 x 3 x 2 x 2
6 x 4 x 2 x 2
4 x 4 x 3 x 2
6 x 2 x 2 x 2 x 2
4 x 3 x 2 x 2 x 2
3 x 2 x 2 x 2 x 2 x 2
###############################################

Execution time = 0.000440 secs
rahul@Milkyway:~$
rahul@Milkyway:~$ python ReturnFactors.py -n 102
Generating factors for 102
###############################################
102 x 1
51 x 2
34 x 3
17 x 6
17 x 3 x 2
###############################################

Execution time = 0.000163 secs


'''
import math
import time
import sys

from optparse import OptionParser



parser = OptionParser()
parser.add_option("-n", type="int", action="store", help="Please print the integer")
(options, args) = parser.parse_args()


GrandList = []

class GenerateFactors(object):

    def __init__(self, n):
        self.n = n
        List_of_Factor_pairs=self.DetermineFactorPairs(n)
        for pair in List_of_Factor_pairs:
            print str(pair[0])+' x '+ str(pair[1])
        InitPairs = self.DetermineFactorPairs(n)[1:]
        self.GenerateReduction(InitPairs)

    def DetermineFactorPairs(self, m):
        pfactors=[i for i in range(1, int(math.sqrt(m))+1) if not m%i]
        List_of_Pairs=[]
        for p in pfactors:
            List_of_Pairs.append([m//p, p])
        return List_of_Pairs

    def Reduce(self, pair):
        a = pair[0]
        b = pair[1:]
        subList=self.DetermineFactorPairs(a)
        z = subList[1:]
        znew=[]
        for p in z:
            p.extend(b)
            p.sort()
            znew.append(p)
        return znew

    def PrintNums(self, GL):
        for p in GL:
            p.reverse()
            k = map(str, p)
            print ' x '.join(k)

    def IterativeReduction(self, ListInit):

        ListFinal=[]
        for pair in ListInit:
            for p in self.Reduce(pair):
                if p not in ListFinal:
                    ListFinal.append(p)
        return ListFinal


    def GenerateReduction(self, Init_Pairs):
        ListFinal = self.IterativeReduction(Init_Pairs)
        while(ListFinal):
            ListFinal = self.IterativeReduction(Init_Pairs)
            self.PrintNums(ListFinal)
            Init_Pairs = ListFinal
        return

if __name__ =="__main__":

    n = options.n
    t_start = time.time()


    if n < 0:
        print >> sys.stderr, "Please Enter a positive integer"
        sys.exit(1)
    print "Generating factors for %d" % n
    print "###############################################"
    GenerateFactors(n)
    print "###############################################\n"
    t_end = time.time()

    delta = t_end - t_start
    print "Execution time = %f secs" % delta

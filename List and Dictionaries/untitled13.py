# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:04:47 2021

@author: Riku
"""


def repToDecimal(n, fromBase):
    
    toNumber = 0

    power = 0

    for i in range((len(n)),0, -1):

            toNumber += conversionLibrary[n[i-1]] * (int(fromBase) ** power)

            power += 1

    return(toNumber)

def main():
    print(repToDecimal(n, fromBase))



main()


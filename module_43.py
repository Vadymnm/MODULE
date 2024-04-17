# -*- coding: utf-8 -*-

def fact_(n):
     if n ==1:
         result = 1
         return 1
     result = fact_(n-1)
     return n * result

def fibonacci_(i):
     if i in (1, 2):
         return 1
     return fibonacci_(i - 1) + fibonacci_(i - 2)

def round_(a,b,n):
    print(a/b)
    print(round(a/b,n))
    print(f"{(a/b):.3f}")
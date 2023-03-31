import sys
import math as m
input = sys.stdin.readline

A, B, V = map(int, input().split())

print(m.ceil((V-B) / (A-B)))
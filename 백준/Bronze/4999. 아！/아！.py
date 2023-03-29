import sys
input = sys.stdin.readline

jh = input().rstrip()
doctor = input().rstrip()

if jh.count("a") >= doctor.count("a"):
    print("go")
else:
    print("no")
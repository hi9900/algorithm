import sys
input = sys.stdin.readline

data = {
"NLCS": "North London Collegiate School",
"BHA": "Branksome Hall Asia",
"KIS": "Korea International School",
"SJA": "St. Johnsbury Academy",
}

school = input().rstrip()

print(data[school])

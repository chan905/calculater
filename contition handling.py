import sys

type = sys.argv[1]

if type == "t2.micro":
    print("this will charge u 2 $ per day")
elif type == "t2.medium":
    print("this will charge u 4 $ per day")
elif type == "t2.large":
    print("this will change u 8 $ per day")
else:
    print("please provid a valid instance type")
      
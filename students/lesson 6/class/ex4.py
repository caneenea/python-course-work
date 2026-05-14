"""
Build a function that takes the time from the user and builds a countdown that prints the seconds 0:0:0.
"""
def countdown(h,m,s):
 while h>=0:
        while m >= 0:

            while s >= 0:
                 print(f"{h} : {m} : {s}")
                 s = s - 1
            s = 59

            m = m - 1
        m = 59

        h = h - 1


h = int(input("Enter the hours:"))
m = int(input("Enter the minutes:"))
s = int(input("Enter the seconds:"))
countdown(h,m,s)


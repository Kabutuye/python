math = int(input("math: "))
if math > 100:
    print("invalid score")
elif math < 0 :
    print("invalid score")

eng = int(input("eng: "))
if eng > 100:
    print("invalid score")
elif eng < 0 :
    print("invalid score")

phy = int(input("phy: "))
if phy > 100:
    print("invalid score")
elif phy < 0 :
    print("invalid score")

kis = int(input("kis: "))
if kis > 100:
    print("invalid score")
elif kis < 0 :
    print("invalid score")

bio = int(input("bio: "))
if bio > 100:
    print("invalid score")
elif bio < 0 :
    print("invalid score")

total = math + eng +phy + kis +bio
print(total)

average = total/5
print("YOUR GRADE IS")

if average <40 :
    print("E")

elif average <50 :
    print("D")

elif average <60 :
    print("C")

elif average <70 :
    print("B")

else:print("A")




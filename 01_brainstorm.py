print "Welcome to a rip-off of Scattegories!"

cat_list = ["Animals", "Food", "Household"]

import random
for x in range(1):
	cat_num = random.randint(1,3)

if cat_num == 1:
	category = cat_list[0]
if cat_num == 2:
	category = cat_list[1]
if cat_num == 3:
	category = cat_list[2]

anslist = []

print "Your category is: " + category
import time


start = time.time()
end = time.time()

response1 = raw_input(category + ':')
anslist.append(response1)
response2 = raw_input(category + ':')
anslist.append(response2)
response3 = raw_input(category + ':')
anslist.append(response3)
response4 = raw_input(category + ':')
anslist.append(response4)
response5 = raw_input(category + ':')
anslist.append(response5)
response6 = raw_input(category + ':')
anslist.append(response6)
response7 = raw_input(category + ':')
anslist.append(response7)
response8 = raw_input(category + ':')
anslist.append(response8)
response9 = raw_input(category + ':')
anslist.append(response9)
print "What is your last item?"
response10 = raw_input(category + ':')
anslist.append(response10)


for x in anslist:
	print(x.center(80,' '))
	print(overall_time.center(80,' '))

Overall_time = end-start
str(Overall_time)

for x in anslist:
	print(x.center(40, ' '))
	print "You took " + Overall_time + "seconds."

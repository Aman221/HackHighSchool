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
new_start = int(start)


response1 = "|            " +  raw_input(category + ':') + "             |"
anslist.append(response1)
response2 = "|            " +  raw_input(category + ':') + "             |"
anslist.append(response2)
response3 = "|            " +  raw_input(category + ':') + "             |"
anslist.append(response3)
response4 = "|            " +  raw_input(category + ':') + "             |"
anslist.append(response4)
response5 = "|            " +  raw_input(category + ':') + "             |"
anslist.append(response5)
response6 = "|            " + raw_input(category + ':') + "             |"
anslist.append(response6)
response7 = "|            " + raw_input(category + ':') + "             |"
anslist.append(response7)
response8 = "|            " + raw_input(category + ':') + "             |"
anslist.append(response8)
response9 = "|            " +  raw_input(category + ':') + "             |"
anslist.append(response9)
print "What is your last item?"
response10 = "|            " +  raw_input(category + ':') + "             |"
anslist.append(response10)
end = time.time()
new_end = int(end)
Overall_time = new_end-new_start
new_overall_time = str(Overall_time)
box_top = "----------------------------"
box_bottom = "----------------------------"
box_fills = "|                            |"
print(box_top.center(80,' '))
for x in anslist:
	print(x.center(80,' '))
	print(box_fills.center(80,' '))
Elapsed_time =  "|    You took " + new_overall_time + " seconds     |" 
print(Elapsed_time.center(80,' '))
print(box_bottom.center(80,' '))

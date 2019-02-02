print "Who goes there?"
memey_answer = raw_input('State your name: ')
acceptable_input = "DHTFHNUQARFMQMKGSPRLRSKBCMD"
other_acceptable_input = """Daenerys of the House Targaryen, the First of Her Name, 
The Unburnt, Queen of the Andals, the Rhoynar and the First Men, 
Queen of Meereen, Khaleesi of the Great Grass Sea, Protector of the Realm, 
Lady Regnant of the Seven Kingdoms, Breaker of Chains and Mother of Dragons"""
so_so_input = "Dany"

if memey_answer == acceptable_input:
	print "Welcome Daenerys"
elif memey_answer == other_acceptable_input:
	print "Weclome Daenerys"
elif memey_answer == so_so_input:
	print "Dany who?"
else:
	print "Move along now."
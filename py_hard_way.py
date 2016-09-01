def cric_world():
	print "which one u like btting or bowling"
	b=raw_input("enter here:")
	if b=="batting":
		print "great choice"
	else:
		print "good for u"
		
def foot_world():
	print "I don't think we will get along well"


def choose_game():
	print "which one u like 1.cricet 2.football"
	choice=raw_input("enter ur choice:")
	if "cricket" in choice:
		cric_world()
	elif "football" in choice:
		foot_world()
	else:
		print "i think u didn't understand the choices"
		
choose_game()
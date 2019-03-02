from player import Player

class RB(Player):
	def run_play(self, play):
		if play == self.Playbook[0]:
			print "RB: I'll head far right and bolt down the field."
		elif play == self.Playbook[1]:
			print "RB: I'll get the ball and dive through the middle."
		else:
			print "RB: I don't know that play..."
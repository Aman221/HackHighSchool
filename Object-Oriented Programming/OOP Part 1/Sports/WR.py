from player import Player

class WR(Player):
	def run_play(self, play):
		if play == self.Playbook[0]:
			print "WR: I'll head as far down the field as I can."
		elif play == self.Playbook[1]:
			print "WR: I'll block the cornerbacks."
		else:
			print "WR: I don't know that play..."
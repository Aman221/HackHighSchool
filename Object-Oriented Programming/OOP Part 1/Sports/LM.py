from player import Player

class LM(Player):
	def run_play(self, play):
		if play == self.Playbook[0]:
			print "LM: I'll block the defense as long as I can."
		elif play == self.Playbook[1]:
			print "LM: I'll block the cornerbacks."
		else:
			print "LM: I don't know that play..."
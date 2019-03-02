from player import Player

class QB(Player):
	def run_play(self, play):
		if play == self.Playbook[0]:
			print "QB: I'll wait and pass it to whoever's open farthest down the field."
		elif play == self.Playbook[1]:
			print "QB: I'll pump fake to the WR then handoff to RB."
		else:
			print "QB: I don't know that play..."







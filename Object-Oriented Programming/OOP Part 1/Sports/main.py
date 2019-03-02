from player import Player
from QB import QB
from RB import RB
from WR import WR
from LM import LM

def main():
	QBZ = QB()
	RBZ = RB()
	WRZ = WR()
	LMZ = LM()
	QBZ.run_play("Hail Mary")
	RBZ.run_play("Hail Mary")
	WRZ.run_play("Hail Mary")
	LMZ.run_play("Hail Mary")
	QBZ.run_play("Dive")
	RBZ.run_play("Dive")
	WRZ.run_play("Dive")
	LMZ.run_play("Dive")
	QBZ.run_play("Flash")
	RBZ.run_play("Flash")
	WRZ.run_play("Flash")
	LMZ.run_play("Flash")

if __name__ == "__main__":
	main()
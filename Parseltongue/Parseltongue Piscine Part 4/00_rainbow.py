i = 0

Black = 30
Red = 31
Green = 32
Yellow = 33
Blue = 34
Purple = 35
Cyan = 36
White = 37

Default = 0
Bold = 1
Faded = 2
Italics = 3
Underlined = 4
Blinking = 5
TT = 6
Negative = 7

BG_Black = 40
BG_Red = 41
BG_Green = 42
BG_Yellow = 43
BG_Blue = 44
BG_Purple = 45
BG_Cyan = 46
BG_White = 47

def write_colorful_text(string, style, foreground_color, background_color):
	if style in range(8):
		if foreground_color in range(30,38):
			if background_color in range(40,48):
				global i
				while i < len(string):
					print "\033[" + str(style) + ";" + str(foreground_color) + ";" + str(background_color) + "m " + string[i] + " \n"
					i = i + 1
					return

write_colorful_text("RAINBOW", Bold, Red, BG_Black)
write_colorful_text("RAINBOW", Bold, Yellow, BG_Black)
write_colorful_text("RAINBOW", Bold, Green, BG_Black)
write_colorful_text("RAINBOW", Bold, Cyan, BG_Black)
write_colorful_text("RAINBOW", Bold, Blue, BG_Black)
write_colorful_text("RAINBOW", Bold, Purple, BG_Black)
write_colorful_text("RAINBOW", Bold, White, BG_Black)
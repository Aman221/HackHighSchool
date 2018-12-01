def print_format_table():
	"""
	prints table of formatted text format options
	"""
	for style in range(8):
		for foreground_color in range(30,38):
			s1 = ''
			for background_color in range(40,48):
				format = ';'.join([str(style), str(foreground_color), str(background_color)])
				s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
			print(s1)
		print('\n')

print_format_table()
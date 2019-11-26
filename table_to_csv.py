import csv
import re

def main():
	#string to be parsed
	s = ''
	while True:
		try:
			s += input() + '\n'
		except EOFError:
			break

	#replaces all white space including new lines with one space
	s = re.sub('\s+', ' ', s, flags=re.IGNORECASE)

	#removes the </table...>
	s = re.sub('</table.*?>', '', s, flags=re.IGNORECASE)
	#splits on <table...>
	s = re.split('<table.*?>', s, flags=re.IGNORECASE)
	#removes the first element of the list because it is always blank or useless
	s = s[1:]
	
	for j in range(len(s)):
		#removes the </tr...>
		s[j] = re.sub('</tr.*?>', '', s[j], flags=re.IGNORECASE)
		#splits on <tr...>
		s[j] = re.split('<tr.*?>', s[j], flags=re.IGNORECASE)
		#removes the first element of the list because it is always blank or useless
		s[j] = s[j][1:]
		
		#splits each table row up into its cells
		for i in range(len(s[j])):
			s[j][i] = re.sub('</td.*?>', '', s[j][i], flags=re.IGNORECASE)
			s[j][i] = re.split('<td.*?>', s[j][i], flags=re.IGNORECASE)
			s[j][i] = s[j][i][1:]

	print(s)

if __name__ == '__main__':
	main()
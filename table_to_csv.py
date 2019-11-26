import csv
import re

def main():
	#string to be parsed
	s = input()
	#removes the </tr...>
	s = re.sub('</tr.*?>', '', s, flags=re.IGNORECASE | re.DOTALL)
	#splits on <tr...>
	s = re.split('<tr.*?>', s, flags=re.IGNORECASE | re.DOTALL)
	#removes the first element of the list because it is always blank
	s = s[1:]
	
	#splits each table row up into its cells
	for i in range(len(s)):
		s[i] = re.sub('</td.*?>', '', s[i], flags=re.IGNORECASE | re.DOTALL)
		s[i] = re.split('<td.*?>', s[i], flags=re.IGNORECASE | re.DOTALL)
		s[i] = s[i][1:]

	print(s)

if __name__ == '__main__':
	main()
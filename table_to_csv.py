import re
import sys
from csv import writer

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

	#splits on <table...> creatig a list of tables
	s = re.split('<table.*?>', s, flags=re.IGNORECASE)
	#removes the first element of the list because it is always blank or useless
	s = s[1:]
	
	#splits up each table into its rows
	for j in range(len(s)):
		#removes the </table...> and everything after it too
		s[j] = re.sub('</table.*?>', '', s[j], flags=re.IGNORECASE)
		
		#TODO: add something here to find the amount of <td or <th flags max function? findall maybe?

		s[j] = re.split('<tr.*?>', s[j], flags=re.IGNORECASE)
		s[j] = s[j][1:]

		#finds the maximum row size so each row can have the same length by:
		# finding the number of <td>s or <th>s in each row
		# finding the maximum among them
		# then using findall again to find the amount of <td>s and <th>s in it
		max_row_size = len(re.findall('<td.*?>|<th.*?>', max(s[j], key=lambda x: len(re.findall('<td.*?>|<th.*?>', x, flags=re.IGNORECASE))), flags=re.IGNORECASE))
		
		#splits each table row up into its cells
		for i in range(len(s[j])):
			#removes the </tr like the </table above
			s[j][i] = re.sub('</tr.*', '', s[j][i], flags=re.IGNORECASE)

			s[j][i] = re.split('<td.*?>|<th.*?>', s[j][i], flags=re.IGNORECASE)
			s[j][i] = s[j][i][1:]

			#removes the </td or </th like the </table above and trims trailing or leading whitespace
			for k in range(len(s[j][i])):
				s[j][i][k] = re.sub('</td.*|</th.*', '', s[j][i][k], flags=re.IGNORECASE).strip()

			#adds empty cells to each row so that they all have the same size
			while len(s[j][i]) < max_row_size:
				s[j][i].append('')

	my_writer = writer(sys.stdout)
	for i in range(len(s)):
		print('TABLE ' + str(i + 1) + ':')
		my_writer.writerows(s[i])
		print()

if __name__ == '__main__':
	main()
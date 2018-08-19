file = open('selected_lines.txt','w')
for line in open('to_use.txt'):
	if 'chapterId' in line and 'chapterName' in line:
		file.write(line)

file.close()



def pascal(n):
	prev_row = []
	pascal = []

	for row_number in range(n):
		current_row_width = row_number + 1
		if row_number == 0:
			row = [1]
		else:
			row = []
			for i in range(current_row_width):
                # 1's
				if i == current_row_width-1 or  i == 0:
					row.append(1)
				else:
					# calc total
					row.append(prev_row[i-1] + prev_row[i])

		prev_row = row
		pascal.append(row)
	return pascal

if __name__ == '__main__':
    p = pascal(10)
    width = len('-'.join(['%s' % num for num in p[-1]]))
    
    #each line add seperation
    for l in p:
        print str.center(' '.join(['%s' % n for n in l]), width)

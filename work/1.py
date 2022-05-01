file = open('books.txt', 'r')
for book in file:
	words = book.split()
	enc = ''.join(w[0] for w in words)
	print(enc)
file.close()

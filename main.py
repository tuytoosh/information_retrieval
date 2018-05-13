import operator

def tag_remove(text) :
	while True:
		index1 = text.find("<");
		if index1 == -1:
			break;
		index2 = text.find(">");
		text = text[: index1] + text[index2 + 1 :]
	return text;

def get_number(number) :
	if number > 999 :
		return str(number);
	elif number > 99:
		return "0" + str(number);
	elif number > 9 :
		return "00" + str(number);
	else :
		return "000" + str(number);

freq = {};
size_of_corpus = 0;
for count in range(1, 1400) :
	f = open('cranfieldDocs/cranfield' + get_number(count),'r')
	message = f.read()
	f.close()
	text = tag_remove(message);

	# replace with space char
	text = text.replace('\n', ' ');
	text = text.replace('.', ' ');

	# remove this chars
	text = text.replace('/', '');
	text = text.replace('(', '');
	text = text.replace(')', '');

	# remove all empty arrays
	items = text.split(' ');
	while '' in items : items.remove('')


	for item in items :
		size_of_corpus += 1;
		if item in freq :
			freq[item] = freq[item] + 1;
		else :
			freq[item] = 1;


print("size of vocab : ", len(freq));

sorted_freq = sorted(freq.items(), key = operator.itemgetter(1), reverse = True )

# print(sorted_freq)

print("size of corpus : ", size_of_corpus);
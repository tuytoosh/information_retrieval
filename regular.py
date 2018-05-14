import operator
from classes.Main import Main
main = Main()

freq = {};
size_of_corpus = 0;
for count in range(1, 1400) :
	f = open('cranfieldDocs/cranfield' + main.get_number(count),'r')
	message = f.read()
	f.close()
	text = main.tag_remove(message);
	items = main.tokenize(text);

	for item in items :
		size_of_corpus += 1;
		if item in freq :
			freq[item] = freq[item] + 1;
		else :
			freq[item] = 1;


vocab_size = len(freq);
print("size of vocab : ", vocab_size);

sorted_freq = sorted(freq.items(), key = operator.itemgetter(1), reverse = True )

# print(sorted_freq)

print("size of corpus : ", size_of_corpus);

# print(sorted_freq[0][1])


count = 0
size = 0
for item in sorted_freq :
	if size < (size_of_corpus / 2) :
		size = size + item[1];
		count = count + 1;
	else : 
		break;

print("the most ... : ", count)



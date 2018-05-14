import operator
from classes.Main import Main
from classes.PorterStemmer import PorterStemmer
main = Main()
p = PorterStemmer();

freq = {};
size_of_corpus = 0;

for count in range(1, 1400) :
	f = open('cranfieldDocs/cranfield' + get_number(count), 'r');
	message = f.read();
	f.close();
	text = main.tag_remove(message);
	itmes = main.tokenize(text);

	for item in items :
		word = p.stem(item, 0,len(item)-1)
		size_of_corpus += 1;
		if word in freq :
			freq[word] = freq[word] + 1;
		else :
			freq[word] = 1;

vocab_size = len(freq);
print("size of vocab : ", vocab_size);

sorted_freq = sorted(freq.items(), key = operator.itemgetter(1), reverse = True )

# print(sorted_freq)

print("size of corpus : ", size_of_corpus);

# print(sorted_freq[0][1])

count = 0;
size = 0;
for item in sorted_freq :
	if size < (size_of_corpus / 2) :
		size = size + item[1];
		count = count + 1;
	else : 
		break;

print("the most ... : ", count);


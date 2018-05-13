def tag_remove(text) :
	while True:
		index1 = text.find("<");
		if index1 == -1:
			break;
		index2 = text.find(">");
		text = text[: index1] + text[index2 + 1 :]
	return text;


f = open('cranfieldDocs/cranfield0001','r')
message = f.read()

text = tag_remove(message);

items = text.split(' ')

print(items)


f.close()
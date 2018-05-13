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
# print(message)
f.close()

# text = "<a>hello world!</a><apan>test is here!</span>"
print(tag_remove(message));
# for i in range(1, 1500) :
	
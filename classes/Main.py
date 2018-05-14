class Main :
	def tag_remove(self, text) :
		while True:
			index1 = text.find("<");
			if index1 == -1:
				break;
			index2 = text.find(">");
			text = text[: index1] + text[index2 + 1 :]
		return text;

	def tokenize(self, text) :
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
		return items;

	def get_number(self, number) :
		if number > 999 :
			return str(number);
		elif number > 99:
			return "0" + str(number);
		elif number > 9 :
			return "00" + str(number);
		else :
			return "000" + str(number);
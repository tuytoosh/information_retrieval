
class StopWordEliminater :

	stopwords = {
		'a',
		'about',
		'an',
		'are',
		'as',
		'at',
		'be',
		'by',
		'for',
		'from',
		'how',
		'i',
		'in',
		'is',
		'it',
		'of',
		'on',
		'or',
		'that',
		'the',
		'this',
		'to',
		'was',
		'what',
		'when',
		'where',
		'who',
		'will',
		'with',
	};

	def eliminate(self, words) :
		for word in self.stopwords :
			while word in words :
				words.remove(word);
		return words;

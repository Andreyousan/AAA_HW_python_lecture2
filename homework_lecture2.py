class CountVectorizer:
    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Returns a document-term matrix from a list of strings.
        All strings mustn't contain any punctuation for perfect results.
        Word order in the matrix can be obtained via get_feature_names().
        """
        words = []
        for line in corpus:
            words.extend(line.lower().split())
        self._feature_names = set(words)
        term_doc_matrix = []
        for line in corpus:
            term_doc_matrix.append([
                line.lower().count(word) for word in self._feature_names
            ])
        return term_doc_matrix

    def get_feature_names(self) -> list[str]:
        """
        Returns list of unique words in previously given corpus.
        """
        try:
            return self._feature_names
        except AttributeError:
            raise AttributeError(
                'No corpus was given yet. Try using fit_transform() first.'
                )


if __name__ == '__main__':
    corpus = [
            'Crock Pot Pasta Never boil pasta again',
            'Pasta Pomodoro Fresh ingredients Parmesan to taste',
             ]
    vectorizer = CountVectorizer()
    vectorizer.get_feature_names()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
class TextAnalyzer:
    def analyze(self, text: str) -> dict:
        """Analyze text for various metrics."""
        words = text.split()
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        
        word_count = len(words)
        sentence_count = len(sentences)
        avg_word_length = sum(len(word) for word in words) / word_count if word_count > 0 else 0
        unique_words = len(set(word.lower() for word in words))
        
        return {
            'word_count': word_count,
            'sentence_count': sentence_count,
            'avg_word_length': avg_word_length,
            'unique_words': unique_words
        } 
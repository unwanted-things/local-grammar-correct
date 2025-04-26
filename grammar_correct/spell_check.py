from spellchecker import SpellChecker as PySpellChecker

class SpellChecker:
    def __init__(self):
        self.spell = PySpellChecker()
        self.corrections = {}
    
    def correct(self, text: str) -> str:
        """Correct spelling in the given text."""
        words = text.split()
        corrected_words = []
        
        for word in words:
            # Check if word is misspelled
            if self.spell.unknown([word]):
                # Get the most likely correction
                correction = self.spell.correction(word)
                if correction and correction != word:
                    self.corrections[word] = correction
                    corrected_words.append(correction)
                else:
                    corrected_words.append(word)
            else:
                corrected_words.append(word)
        
        return ' '.join(corrected_words) 
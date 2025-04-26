from typing import List, Tuple, Dict
import re

class GrammarRules:
    def __init__(self):
        # Articles
        self.articles = {'a', 'an', 'the'}
        
        # Prepositions
        self.prepositions = {
            'about', 'above', 'across', 'after', 'against', 'along', 'among', 'around',
            'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond',
            'by', 'down', 'during', 'except', 'for', 'from', 'in', 'inside', 'into',
            'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside', 'over', 'past',
            'since', 'through', 'throughout', 'till', 'to', 'toward', 'under', 'underneath',
            'until', 'up', 'upon', 'with', 'within', 'without'
        }
        
        # Common irregular verbs
        self.irregular_verbs = {
            'be': ['am', 'is', 'are', 'was', 'were', 'been'],
            'have': ['has', 'had'],
            'do': ['does', 'did', 'done'],
            'go': ['went', 'gone'],
            'see': ['saw', 'seen'],
            'come': ['came', 'come'],
            'take': ['took', 'taken'],
            'give': ['gave', 'given'],
            'find': ['found', 'found'],
            'think': ['thought', 'thought']
        }
        
        # Common contractions
        self.contractions = {
            "don't": "do not",
            "doesn't": "does not",
            "isn't": "is not",
            "aren't": "are not",
            "wasn't": "was not",
            "weren't": "were not",
            "haven't": "have not",
            "hasn't": "has not",
            "hadn't": "had not",
            "won't": "will not",
            "wouldn't": "would not",
            "shouldn't": "should not",
            "couldn't": "could not",
            "can't": "cannot"
        }
        
        # Common homophones
        self.homophones = {
            'there': ['their', 'they\'re'],
            'your': ['you\'re'],
            'its': ['it\'s'],
            'to': ['too', 'two'],
            'then': ['than'],
            'affect': ['effect'],
            'accept': ['except'],
            'complement': ['compliment']
        }
    
    def check_articles(self, sentence: str) -> List[str]:
        """Check proper use of articles."""
        issues = []
        words = sentence.lower().split()
        
        for i, word in enumerate(words):
            if word in self.articles:
                next_word = words[i + 1] if i + 1 < len(words) else None
                if next_word:
                    if word == 'a' and next_word[0] in 'aeiou':
                        issues.append(f"Use 'an' before '{next_word}'")
                    elif word == 'an' and next_word[0] not in 'aeiou':
                        issues.append(f"Use 'a' before '{next_word}'")
        return issues
    
    def check_prepositions(self, sentence: str) -> List[str]:
        """Check proper use of prepositions."""
        issues = []
        words = sentence.lower().split()
        
        for i, word in enumerate(words):
            if word in self.prepositions:
                if i == 0 or i == len(words) - 1:
                    issues.append(f"Preposition '{word}' at sentence boundary")
                elif not words[i-1].isalpha() or not words[i+1].isalpha():
                    issues.append(f"Preposition '{word}' not properly connected")
        return issues
    
    def check_contractions(self, sentence: str) -> List[str]:
        """Check for proper use of contractions."""
        issues = []
        words = sentence.split()
        
        for word in words:
            if word.lower() in self.contractions:
                issues.append(f"Consider using '{self.contractions[word.lower()]}' instead of '{word}'")
        return issues
    
    def check_homophones(self, sentence: str) -> List[str]:
        """Check for common homophone mistakes."""
        issues = []
        words = sentence.split()
        
        for word in words:
            word_lower = word.lower()
            if word_lower in self.homophones:
                alternatives = self.homophones[word_lower]
                issues.append(f"Possible homophone error: '{word}' could be confused with {', '.join(alternatives)}")
        return issues
    
    def check_verb_tense(self, sentence: str) -> List[str]:
        """Check for verb tense consistency."""
        issues = []
        words = sentence.split()
        time_indicators = {
            'past': ['yesterday', 'last', 'ago', 'before', 'earlier'],
            'present': ['today', 'now', 'currently', 'always', 'usually'],
            'future': ['tomorrow', 'next', 'will', 'going to', 'soon']
        }
        
        # Find time indicators in the sentence
        sentence_time = None
        for word in words:
            for tense, indicators in time_indicators.items():
                if word.lower() in indicators:
                    sentence_time = tense
                    break
            if sentence_time:
                break
        
        if sentence_time:
            # Check verbs against the time indicator
            for word in words:
                for base_verb, forms in self.irregular_verbs.items():
                    if word.lower() in forms:
                        if sentence_time == 'past' and not any(form in ['was', 'were', 'had', 'did'] for form in forms):
                            issues.append(f"Verb '{word}' might need past tense form")
                        elif sentence_time == 'present' and not any(form in ['am', 'is', 'are', 'has', 'does'] for form in forms):
                            issues.append(f"Verb '{word}' might need present tense form")
        return issues
    
    def check_run_on_sentences(self, sentence: str) -> List[str]:
        """Check for run-on sentences."""
        issues = []
        if len(sentence.split()) > 40:  # Simple check for long sentences
            issues.append("Possible run-on sentence detected")
        return issues
    
    def check_sentence_fragments(self, sentence: str) -> List[str]:
        """Check for sentence fragments."""
        issues = []
        words = sentence.split()
        if len(words) < 3:  # Very basic check
            issues.append("Possible sentence fragment detected")
        return issues
    
    def check_comma_splices(self, sentence: str) -> List[str]:
        """Check for comma splices."""
        issues = []
        if ',' in sentence:
            parts = sentence.split(',')
            if len(parts) > 1:
                for part in parts[1:]:
                    if part.strip() and part.strip()[0].isupper():
                        issues.append("Possible comma splice detected")
        return issues
    
    def check_all_rules(self, sentence: str) -> Dict[str, List[str]]:
        """Check all grammar rules and return a dictionary of issues."""
        return {
            'articles': self.check_articles(sentence),
            'prepositions': self.check_prepositions(sentence),
            'contractions': self.check_contractions(sentence),
            'homophones': self.check_homophones(sentence),
            'verb_tense': self.check_verb_tense(sentence),
            'run_ons': self.check_run_on_sentences(sentence),
            'fragments': self.check_sentence_fragments(sentence),
            'comma_splices': self.check_comma_splices(sentence)
        } 
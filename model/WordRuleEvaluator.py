from spacy.matcher import Matcher, DependencyMatcher
import re

class WordRuleEvaluator():

    def __init__(self):
        pass

    def evaluate_word_repetitions(self, doc):
        all_tokens_in_text = []
        for token in doc:
            if token.pos_ == "NOUN" or token.pos_ == "VERB":
                all_tokens_in_text.append(token.lemma_)
        all_tokens_in_text_no_duplicates = list(dict.fromkeys(all_tokens_in_text))
        for i in all_tokens_in_text:
            if all_tokens_in_text.count(i) <= 2:  # remove tokens that are unique or repeated just once
                all_tokens_in_text.remove(i)
        sentence_with_duplicates = []
        for number, sent in enumerate(doc.sents):
            duplicates_per_sentence = 0
            for token in sent:
                if token.lemma_ in all_tokens_in_text_no_duplicates:
                    duplicates_per_sentence += 1
            if duplicates_per_sentence >= 1:
                sentence_with_duplicates.append(1)
            else:
                sentence_with_duplicates.append(0)
        return sentence_with_duplicates

    def evaluate_long_words(self, doc):
        long_tokens_results = []
        for number, sent in enumerate(doc.sents):
            long_token_counter = 0
            for token in sent:
                if len(token) >= 10:
                    long_token_counter += 1
            if long_token_counter >= 1:
                long_tokens_results.append(0)
            else:
                long_tokens_results.append(1)
        return long_tokens_results

    def evaluate_existing_hyphens_in_long_words(self, doc):
        hyphens_in_long_words_results = []
        for number, sent in enumerate(doc.sents):
            no_hyphen_counter = 0
            for token in sent:
                if len(token) >= 10:
                    if "-" not in token.text:
                        no_hyphen_counter += 1
            if no_hyphen_counter >= 1:
                hyphens_in_long_words_results.append(0)
            else:
                hyphens_in_long_words_results.append(1)
        return hyphens_in_long_words_results

    def evaluate_abbreviations(self, doc):
        abbreviation_results = []
        for number, sent in enumerate(doc.sents):
            abbreviation_counter = 0
            if re.search("(([A-z]\.){2,})|(([A-z]\. ){2,})", sent.text):
                abbreviation_counter += 1
            if abbreviation_counter >= 1:
                abbreviation_results.append(0)
            else:
                abbreviation_results.append(1)
        return abbreviation_results

    def evaluate_nominalisations(self, doc, nlp):
        matcher = Matcher(vocab=nlp.vocab)
        article_noun = [{"POS": "DET"}, {"POS": "NOUN"}]
        matcher.add("article_noun", patterns=[article_noun])

        nominalisations_results = []
        for number, sent in enumerate(doc.sents):
            nominalised_verb_counter = 0

            # 1st search for nominalisations
            morph_results = matcher(sent, as_spans=True)
            for result in morph_results:
                if result.text.endswith("ung") or result.text.endswith("ungen"):
                    nominalised_verb_counter += 1

            # 2nd search for nominalisations
            for token in sent:
                if token.text.istitle():
                    if token.text.endswith("ung"):
                        verbform = token.text.lower()
                        verbform = verbform.replace("ung", "en")
                        if verbform in nlp.vocab:
                            nominalised_verb_counter += 1
                    elif token.text.endswith("ungen"):
                        verbform = token.text.lower()
                        verbform.replace("ungen", "en")
                        if verbform in nlp.vocab:
                            nominalised_verb_counter += 1
            if nominalised_verb_counter >= 1:
                nominalisations_results.append(0)
            else:
                nominalisations_results.append(1)
        return nominalisations_results

    def evaluate_passive_constructions(self, doc, nlp):
        # match all verbforms of "werden" and an additional participle verb
        dep_matcher = DependencyMatcher(vocab=nlp.vocab)
        dep_pattern = [{"RIGHT_ID": "werden_verb", "RIGHT_ATTRS": {"LEMMA": "werden"}},
                       {"LEFT_ID": "werden_verb", "REL_OP": ">", "RIGHT_ID": "auxverb",
                        "RIGHT_ATTRS": {"MORPH": "VerbForm=Part"}}]
        dep_matcher.add("passive_verbs", patterns=[dep_pattern])
        passive_constructions_results = []
        for number, sent in enumerate(doc.sents):
            dep_matches = dep_matcher(sent)
            passive_construct_counter = 0
            for match in dep_matches:
                passive_construct_counter += 1
            if passive_construct_counter >= 1:
                passive_constructions_results.append(0)
            else:
                passive_constructions_results.append(1)
        return passive_constructions_results

    def evaluate_genitive_constructions(self, doc):
        genitive_constructions_results = []
        for number, sent in enumerate(doc.sents):
            genitive_counter = 0
            for token in sent:
                token_dict = token.morph.to_dict()
                morph_case_genitive = ("Case", "Gen")
                if morph_case_genitive in token_dict.items():
                    genitive_counter += 1
            if genitive_counter >= 1:
                genitive_constructions_results.append(0)
            else:
                genitive_constructions_results.append(1)
        return genitive_constructions_results

    def evaluate_subjunctive_sentences(self, doc):
        infinitive_verbs_for_subjunctive_clauses = ["können", "müssen", "dürfen", "möchten", "werden", "sein", "haben"]
        subjunctive_sentences_results = []
        for number, sent in enumerate(doc.sents):
            subjunctive_word_counter = 0
            morph_mood_sub = ("Mood", "Sub")
            for token in sent:
                token_dict = token.morph.to_dict()
                if morph_mood_sub in token_dict.items() and token.lemma_ in infinitive_verbs_for_subjunctive_clauses:
                    subjunctive_word_counter += 1
            if subjunctive_word_counter >= 1:
                subjunctive_sentences_results.append(0)
            else:
                subjunctive_sentences_results.append(1)
        return subjunctive_sentences_results

    def evaluate_negations(self, doc):
        negative_constructs_results = []
        for number, sent in enumerate(doc.sents):
            negation_counter = 0
            for token in sent:
                if token.lemma_ == "kein":
                    negation_counter += 1
                elif token.text == "nicht" or token.text == "Nicht":
                    negation_counter += 1
            if negation_counter >= 1:
                negative_constructs_results.append(0)
            else:
                negative_constructs_results.append(1)
        return negative_constructs_results

    def evaluate(self, doc, nlp):
        word_repetitions = self.evaluate_word_repetitions(doc)
        long_words = self.evaluate_long_words(doc)
        hyphens_in_words = self.evaluate_existing_hyphens_in_long_words(doc)
        abbreviations = self.evaluate_abbreviations(doc)
        nominalisations = self.evaluate_nominalisations(doc, nlp)
        passive_constructs = self.evaluate_passive_constructions(doc, nlp)
        genitive_constructs = self.evaluate_genitive_constructions(doc)
        subjunctive_constructs = self.evaluate_subjunctive_sentences(doc)
        negative_constructs = self.evaluate_negations(doc)
        return word_repetitions, long_words, hyphens_in_words, abbreviations, nominalisations, passive_constructs, \
               genitive_constructs, subjunctive_constructs, negative_constructs

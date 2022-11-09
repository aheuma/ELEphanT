from spacy.matcher import DependencyMatcher


class SentenceRuleEvaluator:

    def __init__(self):
        pass

    def evaluate_sentence_length(self, doc):
        sentence_length_results = []
        for number, sent in enumerate(doc.sents):
            word_per_sent_counter = 0
            for token in sent:
                if token.pos_ != "PUNCT":
                    word_per_sent_counter += 1
            if word_per_sent_counter >= 9:
                sentence_length_results.append(0)
            else:
                sentence_length_results.append(1)
        return sentence_length_results

    def evaluate_statements(self, doc):
        multiple_statements_results = []
        for number, sent in enumerate(doc.sents):
            # Option 1: All sentences with direct speech are considered as rule-breakers
            if "“," in sent.text:
                multiple_statements_results.append(0)
            # Option 2: If no direct speech: All sentences with two verbs with two subjects are considered as rule-breakers
            else:
                verb_counter = 0
                subject_counter = 0
                for token in sent:
                    if token.pos_ == "VERB":
                        verb_counter += 1
                    elif token.dep_ == "sb":
                        subject_counter += 1
                if verb_counter >= 2 and subject_counter >= 2:  # excludes sentences such as "Anna and I go ..."; as well as sents as "I go and walk".
                    multiple_statements_results.append(0)
                else:
                    multiple_statements_results.append(1)
        return multiple_statements_results

    def evaluate_sentence_structure(self, doc, nlp):
        # Match subject-verb constructions
        dep_matcher = DependencyMatcher(vocab=nlp.vocab)
        dep_pattern = [{"RIGHT_ID": "verb", "RIGHT_ATTRS": {"POS": "VERB"}},
                       {"LEFT_ID": "verb", "REL_OP": ">", "RIGHT_ID": "subject", "RIGHT_ATTRS": {"DEP": "sb"}}]
        dep_matcher.add("nsubj_verb", patterns=[dep_pattern])
        sentence_structure_results = []
        for number, sent in enumerate(doc.sents):
            # If there is a subordinate clause, the sentence structure is considered complex
            if "," in sent.text:
                sentence_structure_results.append(1)
            else:
                dep_matches = dep_matcher(sent)
                # sentences with no dep-matches (and no comma) are considered easy
                if len(dep_matches) == 0:
                    sentence_structure_results.append(0)
                else:
                    # counter is important for cases in which there is more than 1 dep-match
                    complicated_phrase_in_sent_counter = 0
                    for match in dep_matches:
                        matches = match[1]
                        if matches[0] < matches[1]:
                            # if chronology is wrong: sent is complicated
                            complicated_phrase_in_sent_counter += 1
                    if complicated_phrase_in_sent_counter >= 1:
                        sentence_structure_results.append(0)
                    else:
                        sentence_structure_results.append(1)
        return sentence_structure_results

    def evaluate_sentence_beginnings(self, doc):
        allowed_sentence_beginnings = ["Oder", "Wenn", "Weil", "Und", "Aber"]
        sentence_beginnings_results = []
        for number, sent in enumerate(doc.sents):
            loop_end_variable = True
            while loop_end_variable:
                for token in sent:
                    # exclude sentences that start with verbatim speech
                    if token.text != "„":
                        if token.text in allowed_sentence_beginnings:
                            sentence_beginnings_results.append(1)
                            loop_end_variable = False
                            break
                        else:
                            sentence_beginnings_results.append(0)
                            loop_end_variable = False
                            break
                    else:
                        pass
        return sentence_beginnings_results

    def evaluate(self, doc, nlp):
        sentence_length = self.evaluate_sentence_length(doc)
        multiple_statements = self.evaluate_statements(doc)
        sentence_structure = self.evaluate_sentence_structure(doc, nlp)
        allowed_sentence_beginnings = self.evaluate_sentence_beginnings(doc)
        return sentence_length, multiple_statements, sentence_structure, allowed_sentence_beginnings

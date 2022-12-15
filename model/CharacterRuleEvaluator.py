import re


class CharacterRuleEvaluator:

    def evaluate_high_numbers(self, doc):
        pattern_high_numbers = "[0-9]+([1-9]0$)|[1-9][0-9]+[1-9]$|\\d{5,}"
        high_numbers_results = []
        for number, sent in enumerate(doc.sents):
            if re.search(pattern_high_numbers, sent.text):
                high_numbers_results.append(0)
            else:
                high_numbers_results.append(1)
        return high_numbers_results

    def evaluate_percentages(self, doc):
        pattern_percentage_numbers = "([0-9]+\\%)|([0-9]+ \\%)"
        percentages_results = []
        for number, sent in enumerate(doc.sents):
            if re.search(pattern_percentage_numbers, sent.text):
                percentages_results.append(0)
            else:
                percentages_results.append(1)
        return percentages_results

    def evaluate_written_out_numbers(self, doc):
        pattern_written_out_numbers = "\\W[Ee]ins\\W|\\W[Zz]wei\\W|\\W[Dd]rei\\W|\\W[Vv]ier\\W|\\W[Ff]ünf\\W|\\W[Ss]echs\\W|\\W[Ss]ieben\\W|\\W[Aa]cht\\W|\\W[Nn]eun\\W|\\W[Zz]ehn\\W|\\W[Nn]ull\\W|\\W[Zz]wanzig\\W|\\W[Dd]reißig\\W|\\W[Vv]ierzig\\W|\\W[Ff]ünfzig\\W|\\W[Ss]echzig\\W|\\W[Ss]iebzig\\W|\\W[Aa]chtzig\\W|\\W[Nn]eunzig\\W|\\W[Hh]undert\\W|\\W[Tt]ausend\\W"
        written_out_numbers_results = []
        for number, sent in enumerate(doc.sents):
            if re.search(pattern_written_out_numbers, sent.text):
                written_out_numbers_results.append(0)
            else:
                written_out_numbers_results.append(1)
        return written_out_numbers_results

    def evaluate_special_characters(self, doc):
        list_special_characters = ["„", "%", "…", ";", "&", "(", "§"]
        special_characters_results = []
        for number, sent in enumerate(doc.sents):
            special_character_counter = 0
            for token in sent:
                if token.text in list_special_characters:
                    special_character_counter += 1
            if special_character_counter >= 1:
                special_characters_results.append(0)
            else:
                special_characters_results.append(1)
        return special_characters_results

    def evaluate(self, doc):
        high_numbers = self.evaluate_high_numbers(doc)
        percentage_numbers = self.evaluate_percentages(doc)
        written_out_numbers = self.evaluate_written_out_numbers(doc)
        special_characters = self.evaluate_special_characters(doc)
        return high_numbers, percentage_numbers, written_out_numbers, special_characters

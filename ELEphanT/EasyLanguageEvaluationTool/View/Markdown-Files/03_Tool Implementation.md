#### Easy Language Rules
For ELEphanT, the rulebook by [Netzwerk Leichte Sprache]("https://www.leichte-sprache.org/wp-content/uploads/2017/11/Regeln_Leichte_Sprache.pdf") has been chosen, due to its popularity, among other things. This rulebook is intended to be used by Easy Language translators. At
the same time, it is not targeted to be automatically assessed by computer programs. Thus, many
rules are not automatically assessable and excluded. To give an example, all rules from the level of
„design and pictures“ were dismissed because rules such as „Use one single, large font“ or „Do not
use hyphenation“ are simply not applicable for automatic assessment. Due to the project’s time
limitation, the rules were separated into must-have and nice-to-have rules. This was decided mainly
on the basis of feasibility – there are rules which require more elaborate methods such as web
scraping. These rules were marked as optional because web scraping exceeds the author’s current
abilities.

**Rule Selection, Concretization and Implementation** \
The following paragraph presents the list of all rules that have been implemented in ELEphanT.
They have been translated by the author on the basis of the rulebook by Netzwerk Leichte Sprache.
The rule descriprtion itself is followed by a deeper explanation on how the rule is interpreted to
make it applicable for automatic assessment and on how the rule is implemented. In example, the
interpretation often means defining in what case a rule is considered broken or what „not easy“means. The concretization strongly orients on the rulebook by Netzwerk Leichte Sprache which
always gives good and bad examples for each rule. Overall, there are 16 implemented rules.

To achieve a more differentiated result, it was decided to track the degree of Easy Language
on sentence level. This means that for every sentence it is evaluated if it
complies to a rule or violates it. This is tracked in a binary way, by 1 (rule is fulfilled) or 0 (rule is violated). Please note that the tool doesn’t track how often a rule is violated per sentence; instead, it is evaluated if a rule is broken or not. This could be further developed in future. With a look on some questions and the text being a literary text, this may be even more important because there are rules that a literary text violates very often, i.e. rule nr. 4.

***Character Rules***
1. Avoid high numbers.
This rule is implemented using regex. High numbers are defined in two ways: 1. Multi-digit
numbers that do not end in 0; 2. five-digit numbers in any case. If the sentence contains at least one high number, the tool returns 0 (rule is violated).

2. Avoid percentage numbers.
This rule is implemented using regex. A percentage number is defined as the combination of a digit
with the percentage sign, either with a space in between or without. If the sentence contains at least one percentage number, the tool returns 0 (rule is violated).

3. Prefer digits to written out numbers.
This rule is implemented using regex. The tool is given a pre-specified list of the most common
German written-out numbers (such as „eins“, „zwei“ etc.). If the sentence contains at least one
written out number, the tool returns 0 (rule is violated).

4. Avoid special characters.
This rule is implemented using regex. The rulebook by Netzwerk Leiche Sprache defines the
following special characters as being complicated: quotation marks, percentage sign, ellipsis,
semicolon, ampersand, opening round bracket, paragraph sign. Quotation marks and round brackets
are tracked by using the opening sign, respectively. If the sentence contains at least one special
character, the tool returns 0 (rule is violated).

***Word Rules***

5. Always use the same words for the same things.
This rule is implemented by counting word repetitions. To do so, the text is parsed with spaCy and
tokens are counted. Only nouns and verbs are considered for this rule. At first, a list of repetitive words is created (at least 2 repetitions). If a sentence contains one of these repetitive words, the rule is fulfilled and the tool returns 1.6. Use short words. If this is not possible: Separate long words by a hyphen. \
This rule is implemented by counting the length of words. Words with 10 or more characters are
considered as long because an average German word in the Duden series has a length of roughly 10
characters. Next, it is evaluated if the long word is separated by a hyphen. If this is the case, the tool returns 1 (rule fulfilled). If it doesn’t contain a hyphen, the tool returns 0 (rule violated). If there is no long word in the sentence at all, the rule is fulfilled (tool returns 1).

7. Avoid abbreviations.
This rule is implemented using regex. This search finds only 2 sequential and with period
abbreviated characters (with and without space). If a sentence contains at least on abbreviation, the tool returns 0 (rule is violated).

8. Use verbs.
This rule is implemented with spaCy. The rule is interpreted (on the basis of the examples) as
„avoid nominalized verbs“. As there is no list of all German nominalisations, this rule is
approximated as follows: Generally, a search for nominalisations with ending „ung“ is performed.
Then, a spaCy matcher object is used to find nouns ending on „ung“ with a preceding article. A
second approach searches for titlecase tokens ending on „ung“ or „ungen“ (plural). If their ending
can be replaced by the German verb ending „en“ and if this results in a word that is part of the
language model’s vocabulary, the found word is considered as being a nominalisation. Overall, if a
sentence contains at least one nominalisations, the rule is considered violated (tool returns 0).

9. Use active words.
This rule is implemented with spaCy. The rule is interpreted as „avoid passive voice“. To find
passive voice in a sentence, a spaCy matcher object is used. The matcher searchs for the lemma of
the verb „werden“ (to be) and another verb in participle form. If a sentence contains at least one
passive voice phrase, the tool returns 0 (rule violated).

10. Avoid genitive case.
This rule is implemented with spaCy. With the help of spaCy’s token attributes and the morph tag, a
search for morph = „Case: Gen“ is performed. If a sentence contains at least one word in genitive
case, the tool returns 0 (rule violated).

11. Avoid subjunctive case.
This rule is implemented with spaCy. SpaCy offers a token-tag for subjunctive case but the first test showed poor results and a high number of false-positive matches. To find subjunctive case, a list with the lemma of German verbs that build unique forms in subjunctive is created. These verbs are i.e. „können“ („can“), „müssen“ („must“) or „dürfen“ („may“). To define the results of the formerly named tag, a search for the morph tag „Mood: Sub“ is performed. Then, it is checked whether the word is part of the former list. This comparison is based on the words’ lemmata. If a sentence contains a subjunctive form, the tool returns 0 (rule is violated).

12. Use positive language.
This rule is implemented with spaCy. According to the rulebooks’ examples, negations should be
avoided. To track this, a search for tokens with the lemma „kein“ („no“) or „nicht“ („not“) is
performed. If a sentence contains a negation, the tool returns 0 (rule is violated).

***Sentence Rules***

13. Write short sentences.
This rule is implemented with spaCy. A long sentence is interpreted as containing 9 or more words.
This decision goes back to a study by Best (2002) who states that the minimum sentence length
amounts to 6 and the maximum length to 12 words per sentence for children’s and youth’ literature.
To track the compliance, the number of words per sentence (all tokens that are not punctuation) is
counted. If the sentence contains 9 or more words, the tool returns 0 (rule violated).

14. Use one statement per sentence.
This rule is implemented using spaCy. There are two definitions of „one statement per sentence“: 1.
All sentences containing a direct speech phrase (i.e.: „The weather is nice“, he said.) are considered as having multiple statements. To track this, the sentence is searched for a closing quotation mark that is followed by a comma. If this is the case, the rule is considered violated and returns 0. If not, the 2nd search is performed: 2. POS-tagging. All sentences with at least 2 verbs (token.pos_ == „VERB“) and 2 associated subjects (token.dep_ == „sb“) are considered as violating the rule. If this is the case, the tool returns 0; if not, the tool returns 1.

15. Use a simple sentence structure.
This rule is implemented using spaCy. There are two considerations for defining a „simple sentence
structure“: 1. All sentences with a subordinate clause are considered complicated. To track this, the sentence is searched for existing commas. If this is the case, the rule is considered violated and the tool returns 0. 2. The rulebook’s example focuses on the chronology of subject and verb. If the verb precedes the corresponding subject, the sentence is considered complex. This is picked up. To evaluate the chronology of subject and verb in a sentence, a spaCy dependency matcher object is
created. If the verb precedes the subject, the tool returns 0 (rule is violated).

16. The sentences may begin with: Or, If, Because, And, But.
This rule is implemented with spaCy. It is checked, whether the first word (not token!) in a sentence equals one of the allowed sentence beginnings. If this is the case, the rule is considered fulfilled and the tool returns 1.

#### Easy Language Results
After ELEphanT has evaluated all Easy Language rules, these results are saved in an excel file – if
multiple text files are evaluated, an excel file for each text file is created. These files contain all rule results on sentence level – one excel sheet row equals one sentence of the input text. In addition, another excel file is created that summarizes all single text results. This is especially interesting if you plan to compare multiple texts.

***Sentence Level Results*** \
This excel file contains multiple information about the analyzed text file: the number of tokens,
words, and characters per sentence, the average word length per sentence in characters, the number
of satisfied rules per sentence (absolute), the number of satisfied rules per sentence (in %), and the results of the 16 Easy Language rules. Rule nr. 6 is implemented in two different functions (long words and long words with hyphens) and then merged. Thus, there are three different associated
columns for this rule.

***Text Level Results*** \
Independently from the number of input text files, the tool always creates one summarizing excel
file on text level. This contains the following information: the total number of sentences, tokens,
characters and words per text, the average sentence length per text (in words), the 16 rule
evaluations, each in absolute and relative numbers, and 3 different Easy Language scores. The 1.
Easy Language score is calculated in building the average number of satisfied rules per text
(absolute and relative score). The latter relative score is also called „unweighted Easy Language
score“. The 2. score is a weighted Easy Language score. The weighting builds on a reference test
corpus of 10 Easy Language texts, mostly from German public authorities (see below). The tool
was applied to the corpus and average rule compliance scores were extracted as thresholds for the
weighting. The 3. score counts the number of „perfect“ sentences per text in absolute and relative
numbers. A perfect sentence is defined as a sentence that violates 1 rule at maximum. This score is
also given both in absolute and relative numbers.

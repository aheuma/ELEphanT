#### Gold Standard: Easy Language Reference Texts
To be able to verify the tool’s results, two groups of texts were collected. The first group is a corpus of 10 Easy Language texts. These texts have been randomly selected from the Internet when
searching for „Leichte Sprache Beispiele“ („Easy Language examples“). The texts were processed
by the tool: According to preprocessing rules, the texts were modified and separately saved. Then,
the Easy Language scores were evaluated for each text.
On the basis of the summarizing text_level_result.xlsx-file, the rules’ average scores were
calculated and then used to implement the 2. Easy Language score (the weighted score). Assuming
that a low average score of a single rule means that this rule is not very important for Easy
Language, the weighted score is created in multiplying the relative rule results with the average
score. In example: On average, the first two rules are never violated in the Easy Language reference
corpus. This leads to the assumption that these rules are very important. On the contrary, rule nr. 16 is violated very often in all texts. Therefore, it is assumed that this rule is not of high importance for Easy Language. \
These sample texts are mainly non-fictional Easy Language texts by public authorities. One
text is a fairy tale translation. The 2nd group consists of only two texts: a 1:1 translation, meaning a standard German and Easy Language version of the same text: the general terms and conditions by the Bundeszentrale für politische Bildung (bpb) (for the original texts cf.: [standard]("https://www.bpb.de/shop/186122/allgemeine-geschaeftsbedingungen-mit-gesetzlichen-informationen/") and [Easy Language]("https://www.bpb.de/shop/201038/allgemeine-geschaefts-bedingungen-der-bpb-in-leicht-verstaendlicher-sprache/")).

#### Degree of Easy Language in Easy Language Texts
For both the Easy Language Reference Corpus and the 1:1 parallel translation, the average scores of
the three Easy Language scores were calculated. The following table presents the results of
ELEphanT on real-world Easy Language texts.

|     | Unweighted | Weighted | Perfect Sentences |
| ---- | ----| -----| -----|
| Easy Language Corpus | 0.84 | 0.76 | 0.13 |
| 1:1 Easy Language | 0.798 | 0.721 | 0.059 |
| 1:1 Standard German | 0.697 | 0.646 | 0.005 |

#### Discussion
It may seem strange that even the Easy Language texts from the corpus have an Easy Language
score of 0.84 (for the terms and conditions-text the unweighted EL-score is 0.798), whereas
logically one would expect a higher score. There are multiple possible explanations for this
interesting result:

1. Even Easy Language texts do not always adhere to all rules which is even more interesting because Easy Language is known to be firmly rule-based and one would expect it to strictly stick to all rules.

2. When collecting the Easy Language texts, in most cases it was not possible to find out to which rulebook the texts adhere to. In 2015, the German researcher Maaß highlighted that although different rulebooks show some intersections, there are many rules that are unique in one set of rules. This results in a situation where the choice of a rulebook highly effects the results of ELEphanT. Even more, because ELEphanT focuses on one specific rulebook. If a text from the corpus follows other rules, this may cause lower Easy Language scores.

3. Even if the corpus texts adhere to the same rulebook as ELEphanT, they may have been implemented differently. As has been noted in section IV.I, concretization is necessary for many rules. If the translator of one of the EL corpus texts used a different definition for the rules – or a different priority –, this may also cause lower Easy Language scores with ELEphanT. To give an example: For rule nr. 13, I decided that a long sentence is defined as containing 9 or more words. But this threshold is not determined by the rulebook, and if the translator decides differently, this effects the results.

4. Of course, ELEphanT doesn't evalaute all rules that are part of the rulebook by Netzwerk Leichte Sprache. At the same time, some rules can be evaluated approximatively only. In example, not all nominalisations are found with ELEphanT’s implementation. If the tool returns a score of 1, this simply means that a word ending on „ung“ hasn’t been found. But there are other nominalisated word forms that are not tracked by ELEphanT.

Thus, the tool's Easy Language score should not be interpreted as an absolute score but
rather as an approximation. Still, this tendency may be valuable for assessing a text’s complexity. At the same time, the single results for the rules may be helpful in determining where to improve a text to make it more accessible.

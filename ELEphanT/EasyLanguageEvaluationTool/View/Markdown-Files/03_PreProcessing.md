Due to our use case – literary children’s books – some of the preprocessing steps suit better for
literature than for non-fiction texts. At the same time, there are probably some missing steps
necessary for non-fiction texts (such as enumerations which are common in non-fiction but rare in
literature). This will become visible especially when evaluating the tool on non-fiction texts later.
Many preprocessing steps are about removing redundant whitespaces or paragraphs etc. When testing
spaCy’s sentence segmentation, it became evident that the parser has problems with french
quotation marks (which are commonly used in German literature). These are replaced by the
„normal“ German quotations. Also, it was necessary to modify spaCy’s sentence boundaries
because there were cases where spaCy separated the sentence although not necessary. This was
modified, i.e. for semicolons or commas.

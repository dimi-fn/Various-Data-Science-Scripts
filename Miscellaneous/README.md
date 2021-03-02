**(Under construction*)**

# Miscellaneous

## Contents

* [Search Engine Optimization (SEO) & Information Retrieval (IR)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#search-engine-optimization-seo--information-retrieval-ir)

---

# Search Engine Optimization (SEO) & Information Retrieval (IR)

**Contents**

* [General & Metrics](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#general--metrics)
  * [Relevance & Authenticity](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#relevance--authenticity)
    * [Relevance](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#relevance)
    * [Authenticity](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#authenticity)
  * [Metrics](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#metrics)
    * [Pagerank](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#pagerank)
    * [Precision](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#precision)
    * [Recall](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#recall)
* [Keywords](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keywords)
  * [Keyword Attributes](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keyword-attributes)
  * [Keywords Research](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keywords-research)
    * [Data Science](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#data-science)
    * [Machine Learning](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#machine-learning)
    * [Artificial Intelligence](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#artificial-intelligence)
    * [Data Science vs Machine Learning vs AI](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#data-science-vs-machine-learning-vs-ai)
  * [Keyword Distribution](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keyword-distribution)
    
* [Content Optimization](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#content-optimization)
* [Terminologies](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#terminologies)
* [Rules of thumb](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#rules-of-thumb)

----

# General & Metrics

A successful SEO strategy can be achieved by optimizing both for the `search engine` and the surfers/.

* **search engine** ==> technical perspective ==> `Information Retrieval`

* **consumers** ==> human perspective ==> `Information Seeking`


**Information Seeking & Behaviour**:

* How do people start a search?
* How people seek information and how do they utilize it?
* What makes people search differently?





## Relevance & Authenticity
Two important topics that determine *Search Engine Resuts Pages* (`SERPs`) and consequently a website's **pagerank** are: `relevance` and `authenticity`, i.e. if the results that websites produce are relevant and authenticative.

### Relevance
It is determined by various factors such as:
* content and code implementation
* thematic and semantic (metadata) connections between query and your website

A tricky concept about relevance in IR is that `we want at the same time a document to have a good description regarding its content (description), but also to be discriminated from other documents (discrimination)`.

Some of the main `relevance levels` categories are: System, Topical, and Cognitive relevance levels:

* **System relevance level**: the relationship between query and document

* **Topical relevance levels**: the relationship between topic of query and topic of document (i.e. not just keyword matching)

* **Cognitive relevance level**: the relationship between user's state of knowledge and texts (i.e. the ability to undestand the information given)


### Authenticity
* links pointing to you from other websites
* reviews - sentiment



-----

## Metrics
### Pagerank

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/pagerank.PNG" alt="Pagerank"/>
</p>

* `PR(p)`: pagerank score of page p
* `d`: the probability a surfer will continue clicking from this current website (85%), rather than jumping to new location (15%).
I.e., the user will go from website x to website y via the website x (website x recommended that) with a probability of 85%, rather than visiting website y directly by
navigating to another page of the browser (15%)
* `N`: total number of pages in collection
* `pjEM(p)`: set of all pages linked to p
* `L(pj)`: total number of links from page j


### Precision
Precision in the context of Information Retrieval:

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/precision_IR.PNG" alt="Precision"/>
</p>

* It tells us how **useful** the results are (*homogeneity* of results).
* A perfect precision score of 1 means that every result retrieved was relevant, but <ins>it says nothing about if all relevant docs were retrieved</ins>.
* Preference for higher precision than recall: e.g. legal and medical queries where there is a substantial need for high precision and correct results.


### Recall
Recall in the context of Information Retrieval:
<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/recall_IR.PNG" alt="Recall in Information Retrieval"/>
</p>


* It tells us how **complete** the results are (*completeness*).
* A perfect recall score of 1 means that all relevant docs were retrieved, but <ins>it says nothing about how many irrelevant docs were also retrieved</ins>.
* Preference for higher recall than precision: e.g. youtube recommendations, online library collections/scientific articles: There is need for plethora of information/documents/results retrieved even if some of them might be irrelevant to some point.
-----

# Keywords
* Understanding the user's `intent` is important for constructing the right keywords. What the user would type to the search query box in order to find you?

## Keyword Attributes
Keywords *research plan* regarding: `search volume`, `relevance`, and `competition`.

**1) Relevance**: Relevant Keywords: Put yourself in the customer's shoes to discover their *intent* and understand their *customer behaviour*. In this way you will find out which keywords might be relevante to your product/service. E.g. if you sell cars, don't just focus on the keyword "car" (this is what everybody includes in the car websites). You should write about the specific brands you sell and other car attributes. Successfully targeted descriptive keywords will help rank your website highter than the generic ones.

<br>

**2) Search volume**: The number of searches of a particular keyword per month. One tricky fact here is that on the one hand, some keywords might theoritically lead to your website targetfully and successfully, however, they might not be popular queries. Tools for researching the **potential monthly search volume** of keywords: [moz explorer](https://moz.com/explorer), [wordstream](https://www.wordstream.com/), [ahrefs](https://ahrefs.com/keywords-explorer), [semrush.com](https://www.semrush.com/analytics/keywordmagic/start), [google trends](https://trends.google.com/trends/?geo=US)

<br>

**3) Competition / Difficulty**: Keyword competition/difficulty: if what you are selling is already on the web and sold by others as well, this inevitably means that there is already a lot of content around a group of keywords describing your product. When **difficulty** is **low** => competition low => the product that users are typing (query) to find does not lead to many websites, i.e. there are not so many sellers available for that product. It is like "I am typing it but I'm not finding it anywhere". The opposite happens when the difficulty rate is **high**, this means there is a lot of competition around that query as well as availability about the respective product/service that query is referring to.

**SERP**(Search Engine Results Page) **Analysis** Report: It is the process of analyzing the top web pages that rank for a specific keyword or topic. For instance, let's say you sell cars and you think that if someone types "buy a car" will find you. You can type that at the SERP Report and find out. How your website would rank bases on a series of given keywords?

For example, if for a group of keywords at moz.com the search volume is high but the difficulty grade is low, this means that a lot of users have searched for that query but not too many websites are suitably responding to that. 

<br>

## Keywords Research
**1) Brainstorming** : *What products/services do you offer?* ==> Do it from the customer's perspective (and not business's)

* Getting **insights** about your website: [Google Search Console](https://search.google.com/search-console/about)

* **Keyword expansion tools**: The can give potentially useful keywords regarding a topic. E.g. How people are searching for products/services on the web and what keywords are they using for finding out a specifim item? In this way you can get to know your target audience better, and generate a list of *potential keywords*. Tools: [Google Trends](https://trends.google.com/trends/?geo=US), [Answer the Public](https://answerthepublic.com/), [moz.com](https://moz.com/)

<br>

**2) Search Volume Metrics**: *What is the current state of **demand** for those keywords?* ==> Long tail keywords, descriptive keywords.

For example, if you sell cars then it would be quite hard for you to be ranked first at search results when the user searches for "car". But users do not type only "cars" when they want to buy one. They also type many other queries (longer and more descriptive), e.g. bmw black cars, sports fast cars, electric cars, cars for sale in germany, red ferrari in netherlands etc. Focusing on those *long tail keywords* might give you better probabilities of higher ranking than focusing on the very competitive query "car".

<br>

**3) Keyword Categorization**: *Clustering* of your keywords by categorizing them into topics/themes in order to group them.

----
<br>The following twelve images (derived from https://answerthepublic.com/) depict three search queries examples with four images per query, giving analytics insights in the context of SEO. The first four photos are with regard to the search query "**Data Science**", the following four regarding "**Machine Learning**", and the rest of the images with respect to query "**Artificial Intelligence**". For every search query there are four analytics insights: questions, prepositions, comparisons, and related. 
* `Questions`: how users ask a question
* `Prepositions`: what prepositions users use for aksing that query
* `Comparisons`: what comparisons do users think of when they type their query
* `Related`: Related queries to the main query's subject

The last graph (derived from [Google Trends](https://trends.google.com/trends/?geo=US)) illustrates the **search interest** rate with regard to the same three queries above. A value of 100 is the peak popularity for the term, a value of 50 means that the term is half as popular, and a score of 0 means that there was not enough data for this term.

### Data Science 
<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/Data_Science_Questions__answer_the_public.PNG" alt="How users ask about Data Science: questions"/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Questions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/Data_Science_Prepositions__answer_the_public.PNG" alt="How users ask about Data Science: Prepositions"/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Prepositions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/Data_Science_Comparisons__answer_the_public.PNG" alt="How users ask about Data Science: comparisons "/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Comparisons</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/Data_Science_Related__answer_the_public.PNG" alt="How users ask about Data Science: related "/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Related</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

### Machine Learning

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/ML_Questions_answer_the_public.png" alt="How users ask about Machine Learning: Questions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Questions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/ML_Prepositions_answer_the_public.png" alt="How users ask about Machine Learning: Prepositions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Prepositions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/ML_Comparisons_answer_the_public.png" alt="How users ask about Machine Learning: Comparisons">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Comprarisons</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/ML_Related_answer_the_public.png" alt="How users ask about Machine Learning: Related">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Related</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

### Artificial Intelligence

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/AI_Questions_answerthepublic.png" alt="How users ask about Artificial Intelligence: Questions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Questions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/AI_Prepositions_answerthepublic.png" alt="How users ask about Artificial Intelligence: Prepositions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Prepositions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

-----

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/AI_Comparisons_answerthepublic.png" alt="How users ask about Artificial Intelligence: Comparisons">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Comprarisons</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

-----

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/answerthepublic/AI_Related_answerthepublic.png" alt="How users ask about Artificial Intelligence: Related">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Related</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

-----
<br>

### Data Science vs Machine Learning vs AI

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/google_trends/google_trends.PNG" alt="Search Interest Rate among Data Science, Machine Learning, and Artificiall Intelligence, Google Trends">
</p>
<p align="center">
<span><font size="-2"><i>Search Interest Rate: Data Science (blue) vs Machine Learning (red) vs AI (yellow), Worldwide, Jan 2004 - Feb 2021, Credits:</i> </font><a href="https://trends.google.com/trends/?geo=US" target="_blank"><font size="1.8">Google Trends</font></a></span>
</p>

-----

<br>


## Keyword Distribution

----

## Content Optimization
How search engines and consumers view webpages
















## Technical Content Optimization

## Content Planning

## Links Strategy

## SEO Effectiveness Metrics






----

# Terminologies

`Paid Listing`: e.g. to pay google and be displayed in search results as a sponsored link

`Intent`: what users are looking for and how they search

`Web Analytics`: Web analytics let you see how successful you are in attracting users, and the return on your financial investment

# Rules of thumb

* You probably won't have your webpage optimized if you first don't know at which group of keywords you should be focusing on (through keywords research)

* If search volume is high and competition/difficulty is low ==> large potential traffic at the lowest levels of competition ==> demand is high and supply is low ==> market opportunity



-----

### Sources

[1] https://www.linkedin.com/learning/seo-foundations/

[2] Various notes from the *CS976 Information Retrieval* class at Strathclyde University during the academic year 2019-2020: https://www.strath.ac.uk/courses/postgraduatetaught/informationmanagement/#coursecontent

[3] https://answerthepublic.com/

[4] https://medium.com/@bloghands/5-serp-analysis-tools-that-help-you-get-on-page-one-92b9b4e4df3a#:~:text=SERP%20(Search%20Engine%20Results%20Page,ranking%20for%20a%20Google%20search.
# Miscellaneous

## Contents

* [Search Engine Optimization (SEO)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#search-engine-optimization-seo)

---

# Search Engine Optimization (SEO)

**Contents**

* [General & Metrics](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#general--metrics)
* [Keywords](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keywords)
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* []()
* [Terminologies](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#terminologies)

----

## General & Metrics

A successful SEO campaign can be achieved by optimizing for both a `search engine` and surfers/`consumers`.

Two important topics that determine *Search Engine Resuts Pages* (`SERPs`) and consequently a website's **pagerank** are: `relevance` and `authenticity`, i.e. if the results that websites give are relevant and authenticative.

**Relevance**: 
It is determined by various factors such as:
* content and code implementation
* thematic and semantic (metadata) connections between query and your website

**Authenticity**:
* links pointing to you from other websites
* reviews - sentiment


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

## Keywords
* Understanding the user's intent is important for constructing the right keywords. What the user would type to the search query box in order to find you?
* Keywords research plan regarding: `volume`, `relevance`, `competition`
* Getting insights about your website: [Google Search Console](https://search.google.com/search-console/about)
* **Keyword expansion tools**: The can give potentially useful keywords regarding a topic. E.g. what keywords have users been using for finding out a specifim item? In this way you can get to know your target audience better: [Google Trends](https://trends.google.com/trends/?geo=US), [Answer the Public](https://answerthepublic.com/) 


The following twelve images depict three search queries examples with four images per query, giving analytics insights in the context of SEO. The first four photos are with regard to the search query "**Data Science**", the following four regarding "**Machine Learning**", and the rest of the images with respect to query "**Artificial Intelligence**". For every search query there are four analytics insights: questions, prepositions, comparisons, and related. 
* `Questions`: how users ask a question
* `Prepositions`: what prepositions users use for aksing that query
* `Comparisons`: what comparisons do users think of when they type their query
* `Related`: 


<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/Data_Science_Questions__answer_the_public.PNG" alt="How users ask about Data Science: questions"/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Questions</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/Data_Science_Prepositions__answer_the_public.PNG" alt="How users ask about Data Science: Prepositions"/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Prepositions</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/Data_Science_Comparisons__answer_the_public.PNG" alt="How users ask about Data Science: comparisons "/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Comparisons</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/Data_Science_Related__answer_the_public.PNG" alt="How users ask about Data Science: related "/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Related</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>



---

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/ML_Questions_answer_the_public.png" alt="How users ask about Machine Learning: Questions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Questions</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/ML_Prepositions_answer_the_public.png" alt="How users ask about Machine Learning: Prepositions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Prepositions</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>


<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/ML_Comparisons_answer_the_public.png" alt="How users ask about Machine Learning: Comparisons">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Comprarisons</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>


<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/ML_Related_answer_the_public.png" alt="How users ask about Machine Learning: Related">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Related</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----


<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/AI_Questions_answerthepublic.png" alt="How users ask about Artificial Intelligence: Questions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Questions</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/AI_Prepositions_answerthepublic.png" alt="How users ask about Artificial Intelligence: Prepositions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Prepositions</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>


<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/AI_Comparisons_answerthepublic.png" alt="How users ask about Artificial Intelligence: Comparisons">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Comprarisons</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>


<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/AI_Related_answerthepublic.png" alt="How users ask about Artificial Intelligence: Related">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Related</code>, Image from</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>



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

`Web Analytics`: Web analytics let you see how successful you are in attracting users, and the return on your financial investment.


-----

### Sources

[1] https://www.linkedin.com/learning/seo-foundations/

[2] Various notes from the *CS976 Information Retrieval* class at Strathclyde University during the academic year 2019-2020: https://www.strath.ac.uk/courses/postgraduatetaught/informationmanagement/#coursecontent




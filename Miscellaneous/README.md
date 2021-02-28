# Miscellaneous

## Contents

* [Search Engine Optimization (SEO)]()

---

## Search Engine Optimization (SEO)

A successful SEO campaign can be achieved by optimizing for both a `search engine` and surfers/`consumers`

Two important topics that determine *Search Engine Resuts Pages* (`SERPs`) and consequently a website's **pagerank** are: `relevance` and `authenticity`, i.e. if the results that websites give are relevant and authenticative.

**Relevance**: 
It is determined by various factors such as:
* content and code implementation
* thematic and semantic (metadata) connections between query and your website



**Authenticity**
* links pointing to you from other websites
* reviews - sentiment



--------------------------------------------------------------------------
### Pagerank

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/pagerank.PNG" alt="Pagerank"/>
</p>

* `PR(p)`: pagerank score of page p
* `d`: probability a surfer will continue clicking from this current website (85%) rather than jumping to new location (15%)
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
* Preference for higher recall than precision: e.g. youtube, seeking scientific articles: There is need for quantity of information/documents/results even if some of may be irrelevant more or less.


----

### Terminologies

`Paid Listing`: e.g. to pay google and be displayed in search results as a sponsored link

`Intent`: what users are looking for and how they search

`Web Analytics` Web analytics let you see how successful you are in attracting users, and the return on your financial investment.


-----

### Sources

[1] https://www.linkedin.com/learning/seo-foundations/

[2] Various notes from the *CS976 Information Retrieval* class at Strathclyde University during the academic year 2019-2020: https://www.strath.ac.uk/courses/postgraduatetaught/informationmanagement/#coursecontent
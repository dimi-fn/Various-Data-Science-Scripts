**Work on progress*

# Miscellaneous

## Contents

* [Search Engine Optimization (SEO) & Information Retrieval (IR)](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#search-engine-optimization-seo--information-retrieval-ir)

---

# Search Engine Optimization (SEO) & Information Retrieval (IR)

**Contents**

* [Acronyms](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#acronyms)
* [SEO in the context of IR](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#seo-in-the-context-of-ir)
  * [Information Behaviour & Indexing](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#information-behaviour--indexing)   
  * [Zipfian Distribution - Stopwords - Stemming](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#zipfian-distribution---stopwords---stemming)
  * [Relevance & Authenticity](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#relevance--authenticity)
  * [Recommender Systems Evaluation Metrics](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#recommender-systems-evaluation-metrics)
    * [PageRank](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#pagerank)
    * [Precision](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#precision)
    * [Recall](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#recall)

    
* [Organic Search vs. PPC](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#organic-search-vs-ppc)
* [Keywords](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keywords)
  * [Keyword Attributes](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keyword-attributes)
  * [Keyword Research](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keyword-research)
    * [Query: Data Science](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#query-data-science)
    * [Query: Machine Learning](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#query-machine-learning)
    * [Query: Artificial Intelligence](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#query-artificial-intelligence)
    * [Query: Data Science vs Machine Learning vs AI](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#query-data-science-vs-machine-learning-vs-ai)

  * [Keyword Distribution](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#keyword-distribution)


* [Content Optimization](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#content-optimization)
  * [Optimizing Text & Non-Text Elements](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#optimizing-textual-elements)


* [Terminologies](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#terminologies)
* [Rules of thumb](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/Miscellaneous#rules-of-thumb)

----

# Acronyms

| Acronym  | Description |
|------| -------------------------|
| CPC| Cost-Per-Click|
| IR| Information Retrieval|
|PPC |Pay-Per-Clicking|
|SEO |Search Engine Optimization |
|SERP |Search Engine Resuts Page|

# SEO in the context of IR

A successful SEO strategy can be achieved by optimizing both for the `search engine` and the surfers/`consumers`.

* **search engine** ==> technical perspective ==> `Information Retrieval`

* **consumers** ==> human perspective ==> `Information Seeking`


## Information Behaviour & Indexing
### Information Seeking & Behaviour
<i><b>Information Behaviour</b></i> describes the ways through which people seek and utilize information. It is a broader term than that of <i><b>Information Seeking</b></i> because through Information Behaviour we want to give answers to questions such as:

* How do people start a search?
* How people seek information and how do they utilize it?
* What makes people search differently?
* What types of search engines require different solutions?


## Zipfian Distribution - Stopwords - Stemming


<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/zipfian_distrib_law/zipf.PNG" alt="Zipfian Distribution of words">
</p>
<p align="center">
<span><font size="-2"><i>Zipfian Distribution (Zipf's Law), Credits:</i> </font><a href="https://eclecticlight.co/2015/07/11/zipfs-law-deep-and-meaningful/" target="_blank"><font size="1.8">eclecticlight.co</font></a></span>
</p>


<br>Words are not evenly distributed across documents, and English and other languages follow a *Zipfian distribution*. By that, it is meant that:

* A small number of words appear <u>each</u> in a lot of documents (`high-frequency words`)
  * This is where the so-called **stopword** list takes place: stopwords are useless in finding an individual document ==> they offer little *semantic* content
    * **Stopwords** removal achieves <i><b>discrimation</b></i>: procedure of words removal that are common to most of the docs (words like "and", "are", "do", "am", "but")
    * While stopwords removal emphasizes on discrimination, **stemming** emphasizes on document's <i><b>description</b></i> ==> stemming algorithms help us achieve a common concept of the words that can take different forms, by adding all variants of the corresponding words to document descriptions (e.g. information -> inform, political -> polit)

* A medium number of words appear <u>each</u> in a medium number of documents (`medium-frequency words`) 
  * These are the "**best**" words in the IR context ==> they represent some recognisable concept (satisfactory *description* level) that doesn't seem to be meaningless (satisfactory *discrimination* level)

* A large number of words appear <u>each</u> in a small number of documents (`low-frequency words`)

-----

<br>Other main terminlogies, topics, and sections around the above contents are:
* Term Weighting (t<sub>w</sub>)
  * term frequency (t<sub>f</sub>), inverse document frequency (idf)
* Retrieval Models
  * Boolean model
    * Best match retrieval
  * Vector space models
    * Simple Matching
    * Cosine coefficient and Cosine Matching
  * Language models


## Relevance & Authenticity
Two important topics that determine *search engine rankings* and *Search Engine Resuts Pages* (`SERPs`), and consequently a website's **pagerank** are: `relevance` and `authenticity`, i.e. if the results that websites produce are relevant and authenticative.

### Relevance
It is determined by various factors such as:
* content and code implementation
* thematic and semantic (metadata) connections between query and your website

A tricky concept about *relevance* in IR is that `we want our document to have a good description regarding its content (description), but at the same time we also want that document to be discriminated from other documents (discrimination)`. The problem here is that if we tried to describe our document with 'common sense' (i.e. in the way everybody would describe it) then we would probably not achive a satisfactory document descrimination because this is how everybody described similar documents as well!


**Relevance Levels**:

Some of the main relevance level categories comprised of the: System, Topical, and the Cognitive relevance level (*Tefko Saracevic*):

* **System relevance level**: the relationship between query and document

* **Topical relevance levels**: the relationship between topic of query and topic of document (i.e. not just keyword matching)

* **Cognitive relevance level**: the relationship between user's state of knowledge and texts (i.e. the ability to undestand the information given)


### Authenticity
Authenticity in the context of SEO is know as <i>**Domain Authority**</i>. Essentially, it is a measure of how authoritative your domain is. 

Contributing factors include:
* the quantity and quality of links (hyperlinks) pointing to you from other websites (third-party domains), known as **inbound links**
* reviews - sentiment



-----

## Recommender Systems Evaluation Metrics
### PageRank

PageRank measures how likely a surfer is to visit a web page:

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

* It tells us how **useful** the results are (*effectiveness* in terms of the given results).
  * A perfect precision score of 1 means that every result retrieved was relevant, but <ins>it says nothing about if all relevant docs were retrieved</ins>.
  * Preference for higher precision than recall: e.g. legal and medical queries where there is a substantial need for high precision and correct results.


### Recall
Recall in the context of Information Retrieval:
<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/recall_IR.PNG" alt="Recall in Information Retrieval"/>
</p>

* It tells us how **complete** the results are (*completeness* in terms of the given results).
  * A perfect recall score of 1 means that all relevant docs were retrieved, but <ins>it says nothing about how many irrelevant docs were also retrieved</ins>.
  * Preference for higher recall than precision: e.g. youtube recommendations, seeking online library collections/scientific articles: There is need for plethora of information/documents/results retrieved even if some of them might be irrelevant to some extent.

<br><br>

Further research on Recommender System metrics include: Mean Average Precision at K (MAP@K), Mean Average Recall at K (MAR@K), Coverage, Personalization, and Intra-list Similarity.

-----

# Organic Search vs. PPC

* **Organic search** (*natural search*) refers to unpaid search results which are generated based on: inbound links targeting your website, your domain authority, the relevance to user's search query, and other organic ranking factors

* **Pay-per-click** advertising (*PPC*) generates paid search results, it belongs to *paid search marketing* approach, and one of its basic performance metrics is cost-per-click (CPC) evaluation. Examples: Google ads, Google Product Listing Ads, Google Shopping Ads, Bing Ads)


# Keywords
* Understanding user's `intent` is important for constructing the right keywords. 
What keywords would the user have to type in order to find your specific web page?

What the user would type to the search query box in order to find you?

## Keyword Attributes
Keywords *research plan* regarding: `search volume`, `relevance`, and `competition`.

**1) Relevance**: Relevant Keywords: Put yourself in the customer's shoes to discover their *intent* and understand their *customer behaviour*. In this way you will find out which keywords might be relevant to your product/service. E.g. if you sell cars, don't just focus on the keyword "car" (this is what everybody includes in the car websites). You should write about the specific brands you sell and other car attributes. Successfully targeted descriptive keywords will help rank your website highter than the generic ones.

<br>

**2) Search volume**: The number of searches of a particular keyword per month. One tricky fact here is that on the one hand, some keywords might theoritically lead to your website targetfully and successfully, however, they might not be popular queries. I.e., it does not matter if your website can be found by some specific query as long as this query is a "strange" query that nobody would really type it to find your product.
Tools for researching the **potential monthly search volume** of keywords: [moz explorer](https://moz.com/explorer), [wordstream](https://www.wordstream.com/), [ahrefs](https://ahrefs.com/keywords-explorer), [semrush.com](https://www.semrush.com/analytics/keywordmagic/start), [google trends](https://trends.google.com/trends/?geo=US)

<br>

**3) Competition / Difficulty**: Keyword competition/difficulty: if what you are selling is already on the web and sold by others as well, this inevitably means that there is already a lot of content around a group of keywords describing your product. When **difficulty** is **low** => competition low => the product that users are typing (query) to find does not lead to many websites, i.e. there are not so many sellers available for that product. It is like "I am googling it but I can't find it anywhere". The opposite happens when the difficulty rate is **high**, this means there is a lot of competition around that query as well as availability about the respective product/service that query is referring to.

**SERP**(Search Engine Results Page) **Analysis** Report: It is the process of analyzing the top web pages that rank for a specific keyword or topic. For instance, let's say you sell cars and you think that if someone types "buy a car" will find you. You can type that at the SERP Report and find out. How your website would rank bases on a series of given keywords?

For example, if for a group of keywords at moz.com the search volume is high but the difficulty grade is low, this means that a lot of users have searched for that query but not too many websites are suitably responding to that. 

<br>

## Keyword Research

Keyword research has to be conducted iteratively through the year, and *keyword performance <b>evaluation</b>* comes at the end of each keyword research iteration. The only thing you cannot pre-define and predict is the conversion rate (success or not) of your keywords.

**1) Brainstorming** : *What products/services do you offer?* ==> Do it from the customer's perspective (and not business's), think like a customer.

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

### Query: Data Science 
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

### Query: Machine Learning

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

### Query: Artificial Intelligence

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

### Query: Data Science vs Machine Learning vs AI

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/Miscellaneous/img/google_trends/google_trends.PNG" alt="Search Interest Rate among Data Science, Machine Learning, and Artificiall Intelligence, Google Trends">
</p>
<p align="center">
<span><font size="-2"><i>Search Interest Rate: Data Science (blue) vs Machine Learning (red) vs AI (yellow), Worldwide, Jan 2004 - Feb 2021, Credits:</i> </font><a href="https://trends.google.com/trends/?geo=US" target="_blank"><font size="1.8">Google Trends</font></a></span>
</p>

-----

<br>

## Keyword Distribution
It is the procedure of how you will asign and distribute your specific keywords across your website's pages.

In this way:
* you can <i>**map**</i> keywords to pages: you can enhance your targeted keywords by figuring out which keywords you should asign to which pages
* you can <i>**keep track**</i> of keywords that need pages (or pages that need keyword if there was no keyword asignment)
* you can detect and avoid keyword <i>**duplicates**</i> (search engine algorithms "prefer" unique and relevant information across your pages)
* you can reverse engineer the <i>**creation of the content**</i> of a new page to your website by first filling out the keyword distribution file. In this way, you would first decide on 
what keyword you are targeting on, and then you would write the relevant content based on that keyword. In such a way, your content is more likely to be SEO successful.
* you can <i>**adapt**</i> quickly: you can come back to this speadsheet and add or redefine your keywords, as well as review the other metadata.

## Keyword Distribution Diagram

| Structure  | Keywords | URL (of specific page)| The title tag| Meta-description| the h1 header title|
|---------| -------------------------|----------|--------|-----------------|-------------------------|
| **home**  |  || ||  |
| *Cars*  |  || ||  |
| Mercedes  | mercedes-benz |/home/mercedes.html| Find and buy the best mercedes-benz cars in the world| Here is why you will find the best mercedes-benz cars in the world on my website (..)|  Best Mercedes-Benz in Germany|
| BMW | bmw car |/home/bmw.html| Find and buy the best bwm cars in the world| Here is why you will find the best BMW cars in the world on my website (..) | Fastest BMW cars in Austria |
| AUDI | audi car |/home/audi.html|  Find and buy the best audi cars in the world| Here is why you will find the audi BMW cars in the world on my website (..)| Best Audi cars in Italia |

----



# Content Optimization

It is all about how search engines and consumers view webpages, including yours.

There is a need for:
* Clarity and quality: people tend to share with other people content that they *like*, find *useful* and *relevant*, and content that they *trust*

* Good website **structure** and layout: categorize and clarify your content in and across your web pages clearly both from business's and customer's perspective

## Optimizing Text & Non-Text Elements

Focus on URL, title, description, headers, body text, and images:


* <i>**URL**</i>: the keyword phrase that you are targeting should be included in URL if that is possible 
  * construction of a *good URL*: descriptive but short, and concise as possible

* metadata
  * *meta* <i>**title**</i> *tag* optimization
    * make sure your <title_description> tag is successful (*"title" tag in html"*), and that it contains (some of) your target keywords for the best SEO results
  * <i>**headers**</i>: html `h1` tag: give good descriptions (not very long or very short) that encompass your target keywords and your target content

* optimize your content (<i>**body text**</i>) first for your *customers* and then for *search engines* (since the Natural Language Progress (NLP) has tremendously improved, search engines can comprehend text like human beings better and better over time). 

* make search engines understand your <i>**images**</i>: while NLP focuses on text and search engines can take advantage of that, not much help is given to them regarding images (all they can "see" is pixels), video or audio clips, unless specified:   
  * improve your `"src"` and `"alt"` html attributes with reference to your *images*
  * embrace [**structured data**](https://developers.google.com/search/docs/guides/intro-structured-data) with [*JSON-LD*](https://json-ld.org/) to mark up your code with specific and rich range of metadata of specific content for *images, video, and audio*. You can use websites like [schema.org](https://schema.org/docs/gs.html) to enhane ycour schema of your mark up code, and then test the effectiveness of your code with e.g. the [google structure data testing tool](https://search.google.com/test/rich-results?utm_campaign=sdtt&utm_medium=message).




<br>

**Tools**: https://moz.com/learn/seo/title-tag































































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

* Use a specific group of keywords that have a meaningful *search volume*, are *relevant*, and are not too competitive (since it would be difficult for you to be discriminated if there is a lot of competition around those keywords).

* If a specific keyword is being aggressively bid on in CPC markets, this is an indicator of how difficult it will be organically. I.e., If a keyword is being aggressively bid on, this means that a significant competition from paid ads exists, and developing an alternative keyword might be necessary.


-----

### Sources

[1] https://www.linkedin.com/learning/seo-foundations/

[2] Dr Martin Halvey, 2019, *CS976 Information Retrieval*, lecture notes, University of Strathclyde, delivered at the 1st semester of the academic year 2019-2020, https://www.strath.ac.uk/courses/postgraduatetaught/informationmanagement/#coursecontent

[3] https://answerthepublic.com/

[4] https://medium.com/@bloghands/5-serp-analysis-tools-that-help-you-get-on-page-one-92b9b4e4df3a#:~:text=SERP%20(Search%20Engine%20Results%20Page,ranking%20for%20a%20Google%20search.

[5] https://eclecticlight.co/2015/07/11/zipfs-law-deep-and-meaningful/

[6] https://www.ranks.nl/stopwords

[7] http://infolab.stanford.edu/~backrub/google.html

[8] https://www.researchgate.net/publication/227634540_RELEVANCE_A_Review_of_and_a_Framework_for_the_Thinking_on_the_Notion_in_Information_Science

[9] https://towardsdatascience.com/evaluation-metrics-for-recommender-systems-df56c6611093

[10] https://www.wordstream.com/domain-authority

[11] https://www.wordstream.com/inbound-links

[12] https://econsultancy.com/what-paid-search-ppc/

[13] https://www.wordstream.com/organic-search

[14] https://developers.google.com/search/docs/guides/intro-structured-data

[15] https://search.google.com/test/rich-results?utm_campaign=sdtt&utm_medium=message
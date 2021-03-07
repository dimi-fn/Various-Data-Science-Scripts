**Work on progress*

# SEO

---

# Search Engine Optimization (SEO) & Information Retrieval (IR)

## Contents

* [Acronyms](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#acronyms)
* [SEO in the context of IR](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#seo-in-the-context-of-ir)
  * [Information Behaviour & Indexing](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#information-behaviour--indexing)   
  * [Zipfian Distribution - Stopwords - Stemming](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#zipfian-distribution---stopwords---stemming)
  * [Relevance & Authenticity](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#relevance--authenticity)
  * [Recommender Systems Evaluation Metrics](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#recommender-systems-evaluation-metrics)
    * [PageRank](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#pagerank)
    * [Precision](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#precision)
    * [Recall](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#recall)
* [Organic Search vs. PPC](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#organic-search-vs-ppc)
* [Ranking Factors on Search Results](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#ranking-factors-on-search-results)
* [Keywords](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keywords)
  * [Keyword Attributes](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keyword-attributes)
  * [Keyword Research](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keyword-research)
    * [Query: Data Science](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#query-data-science)
    * [Query: Machine Learning](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#query-machine-learning)
    * [Query: Artificial Intelligence](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#query-artificial-intelligence)
    * [Query: Data Science vs Machine Learning vs AI](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#query-data-science-vs-machine-learning-vs-ai)
  * [Keyword Distribution](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keyword-distribution)
* [Content Optimization](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content-optimization)
  * [Optimizing Text & Non-Text Elements](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#optimizing-text--non-text-elements)
  * [Technical Content Optimization](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#technical-content-optimization)
    * [Content & Links](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content--links)
    * [Server-side](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#server-side)
    * [Google Search Console](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#google-search-console)
  * [Content Planning & Strategy](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content-planning--strategy)
    * [Content Strategy](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content-strategy)
      * [Links Strategy](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#links-strategy)
* [SEO Performance Evaluation](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#seo-performance-evaluation)
  * [E-Commerce](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#e-commerce)
* [Rules of thumb](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#rules-of-thumb)
* [More to Read](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#more-to-read)
* [Appendix: Table of Useful Links](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#more-to-read)



* [Sources](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#sources)

----

# Acronyms

| Acronym  | Description |
|------| -------------------------|
| CDN| Content Delivery Network|
| CTR|Click-Through Rate |
| CPC| Cost-Per-Click|
| IDF| Inverse Document Frequency|
| IR| Information Retrieval|
|JSON-LD |JavaScript Object Notation for Linked Data|
|KPI |Key Performance Indicator|
|PPC |Pay-Per-Clicking|
|RDFa|Resource Description Framework in Attributes|
|SEO |Search Engine Optimization |
|SERP |Search Engine Resuts Page|
|TF|Term Frequency|
|TLD|Top Level Domains|


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
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/zipfian_distrib_law/zipf.PNG" alt="Zipfian Distribution of words">
</p>
<p align="center">
<span><font size="-2"><i>Zipfian Distribution (Zipf's Law), Credits:</i> </font><a href="https://eclecticlight.co/2015/07/11/zipfs-law-deep-and-meaningful/" target="_blank"><font size="1.8">eclecticlight.co</font></a></span>
</p>


<br>Words are not evenly distributed across documents, and English and other languages follow a *Zipfian distribution*. By that, it is meant that:

* A small number of words appear <ins>each</ins> in a lot of documents (`high-frequency words`)
  * This is where the so-called **stopword** list takes place: stopwords are useless in finding an individual document ==> they offer little *semantic* content
    * **Stopwords** removal achieves <i><b>discrimation</b></i>: procedure of words removal that are common to most of the docs (words like "and", "are", "do", "am", "but")
    * While stopwords removal emphasizes on discrimination, **stemming** emphasizes on document's <i><b>description</b></i> ==> stemming algorithms help us achieve a common concept of the words that can take different forms, by adding all variants of the corresponding words to document descriptions (e.g. information -> inform, political -> polit)

* A medium number of words appear <ins>each</ins> in a medium number of documents (`medium-frequency words`) 
  * These are the "**best**" words in the IR context ==> they represent some recognisable concept (satisfactory *description* level) that doesn't seem to be meaningless (satisfactory *discrimination* level)

* A large number of words appear <ins>each</ins> in a small number of documents (`low-frequency words`)

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
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/pagerank.PNG" alt="Pagerank"/>
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
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/precision_IR.PNG" alt="Precision"/>
</p>

* It tells us how **useful** the results are (*effectiveness* in terms of the given results).
  * A perfect precision score of 1 means that every result retrieved was relevant, but <ins>it says nothing about if all relevant docs were retrieved</ins>.
  * Preference for higher precision than recall: e.g. legal and medical queries where there is a substantial need for high precision and correct results.


### Recall
Recall in the context of Information Retrieval:
<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/recall_IR.PNG" alt="Recall in Information Retrieval"/>
</p>

* It tells us how **complete** the results are (*completeness* in terms of the given results).
  * A perfect recall score of 1 means that all relevant docs were retrieved, but <ins>it says nothing about how many irrelevant docs were also retrieved</ins>.
  * Preference for higher recall than precision: e.g. youtube recommendations, seeking online library collections/scientific articles: There is need for plethora of information/documents/results retrieved even if some of them might be irrelevant to some extent.

<br><br>

Further research on Recommender System metrics include: Mean Average Precision at K (MAP@K), Mean Average Recall at K (MAR@K), Coverage, Personalization, and Intra-list Similarity.

-----

# Organic Search vs. PPC

* **Organic search** (*natural search*) refers to unpaid search results which are generated based on: inbound links pointing to your website, your domain authority, the relevance to user's search query, and other organic ranking factors

* **Pay-per-click** advertising (*PPC*) generates paid search results, it belongs to *paid search marketing* approach, and one of its basic performance metrics is cost-per-click (CPC) evaluation. Examples: Google ads, Google Product Listing Ads, Google Shopping Ads, Bing Ads)

# Ranking Factors on Search Results

Following the [Relevance & Authenticity](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#relevance--authenticity) section, and although search ranking algorithms change over time, it can be safely claimed that good ranking results align with **high quality** and **relevant information**. Hence, some of the most important ranking factors can be found aggregately and hierarchically on importance as followed:


| `Ranking Factor` | `Description/Examples` |
|---------------|----------------------|
| **Domain-Level & Link Authority Features** | quantity of links to the domain, quality of links to domain, domain-level PageRank |
| **Page-Level Link Features**| PageRank, TrustRank, quantity of link links, anchor text distribution, quality of link sources|
| **Page-Level Keywords & Content Features**| Term Weighting ( TF * IDF), topic modelling content score, content relevance|
| **Page-Level Keyword Agnostic Features**| content length, load speed, readability, uniqueness vs dublicate content|
| **Domain-level Brand Features**| offline usage of domain name/brand, mentions of domain name in news|
| **Traffic & Query Data**| usage signals from browsers, clickstream, CTR of queries|
| **Social Metrics**| quantity and quality of links and sharings from social media|
| **Domain-level Keyword Usage**| exact and partial keyword matches|
| **Domain-level Keyword-Agnostic Features**| domain name length, TLD, HTTP responses|

# Keywords
* Understanding user's (commercial) `intent` (what users are looking for and how they search) is important for constructing the right keywords. 
What keywords would the user have to type in order to find your specific web page?

What the user would type to the search query box in order to find you?

## Keyword Attributes
Keywords *research plan* regarding: `search volume`, `relevance`, and `competition`.

**1) Relevance**: Relevant Keywords: Put yourself in the customers' shoes to discover their *intent* and understand their *customer behaviour*. In this way you will find out which keywords might be relevant to your product/service. E.g. if you sell cars, don't just focus on the keyword "car" (this is what everybody includes in the car websites). You should write about the specific brands you sell and other car attributes. Successfully targeted descriptive keywords will help rank your website highter than the generic ones.

<br>

**2) Search volume**: The number of searches of a particular keyword per month. One tricky fact here is that on the one hand, some keywords might theoritically lead to your website targetfully and successfully, however, they might not be popular queries. I.e., it does not matter if your website can be found by some specific query as long as this query is a "strange" query that nobody would really type it to find your product.
Tools for researching the **potential monthly search volume** of keywords: [moz explorer](https://moz.com/explorer), [wordstream](https://www.wordstream.com/), [ahrefs](https://ahrefs.com/keywords-explorer), [semrush.com](https://www.semrush.com/analytics/keywordmagic/start), [google trends](https://trends.google.com/trends/?geo=US)

<br>

**3) Competition / Difficulty**: Keyword competition/difficulty: if what you are selling is already on the web and sold by others as well, this inevitably means that there is already a lot of content around a group of keywords describing your product. When **difficulty** is **low** => competition low => the product that users are typing (query) to find does not lead to many websites, i.e. there are not so many sellers available for that product. It is like "I am googling it but I can't find it anywhere". The opposite happens when the difficulty rate is **high**, this means there is a lot of competition around that query as well as availability about the respective product/service that query is referring to.

<br>

<ins>**SERP**(Search Engine Results Page) **Analysis** Report</ins>: It is the process of analyzing the top web pages that rank for a specific keyword or topic. For instance, let's say you sell cars and you think that if someone types "buy a car" will find you. You can type that at the SERP Report and find out. How your website would rank bases on a series of given keywords?

For example, if for a group of keywords at moz.com the search volume is high but the difficulty grade is low, this means that a lot of users have searched for that query but not too many websites are suitably responding to that. 

<br>

## Keyword Research

Keyword research has to be conducted iteratively through the year, and *keyword performance <b>evaluation</b>* comes at the end of each keyword research iteration. The only thing you cannot pre-define and predict is the conversion rate (success or not) of your keywords.

**1) Brainstorming** : *What products/services do you offer?* ==> Do it from the customer's perspective (and not business's), think like a customer.

* Getting **insights** about your website: [Google Search Console](https://search.google.com/search-console/about) (former Google Webmaster Tools)

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

Lastly, the data describing the images can be integrated into [CSV files](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO/csv) that are provided by both respective sources.

### Query: Data Science 
<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/Data_Science_Questions__answer_the_public.PNG" alt="How users ask about Data Science: questions"/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Questions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/Data_Science_Prepositions__answer_the_public.PNG" alt="How users ask about Data Science: Prepositions"/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Prepositions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/Data_Science_Comparisons__answer_the_public.PNG" alt="How users ask about Data Science: comparisons "/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Comparisons</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/Data_Science_Related__answer_the_public.PNG" alt="How users ask about Data Science: related "/>
</p>
<p align="center">
<span><font size="-2"><i>"<b>Data Science</b>" Search Queries: <code>Related</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

---

### Query: Machine Learning

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/ML_Questions_answer_the_public.png" alt="How users ask about Machine Learning: Questions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Questions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/ML_Prepositions_answer_the_public.png" alt="How users ask about Machine Learning: Prepositions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Prepositions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/ML_Comparisons_answer_the_public.png" alt="How users ask about Machine Learning: Comparisons">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Comprarisons</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/ML_Related_answer_the_public.png" alt="How users ask about Machine Learning: Related">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Machine Learning</b>" Search Queries: <code>Related</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

### Query: Artificial Intelligence

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/AI_Questions_answerthepublic.png" alt="How users ask about Artificial Intelligence: Questions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Questions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

----

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/AI_Prepositions_answerthepublic.png" alt="How users ask about Artificial Intelligence: Prepositions">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Prepositions</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

-----

<br><p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/AI_Comparisons_answerthepublic.png" alt="How users ask about Artificial Intelligence: Comparisons">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Comprarisons</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

-----

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/answerthepublic/AI_Related_answerthepublic.png" alt="How users ask about Artificial Intelligence: Related">
</p>
<p align="center">
<span><font size="-2"><i>"<b>Artificial Intelligence</b>" Search Queries: <code>Related</code>, Credits:</i> </font><a href="https://answerthepublic.com/" target="_blank"><font size="1.8">answerthepublic.com</font></a></span>
</p>

-----
<br>

### Query: Data Science vs Machine Learning vs AI

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/google_trends/google_trends.PNG" alt="Search Interest Rate among Data Science, Machine Learning, and Artificiall Intelligence, Google Trends">
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

It is about how search engines and consumers view webpages, including yours.

There is a need for:
* **Clarity** and **quality**: people tend to share with other people content that they *like*, find *useful* and *relevant*, and content that they *trust*

* Good website **structure** and layout: categorize and clarify your content in and across your web pages clearly both from business's and customer's perspective

## Optimizing Text & Non-Text Elements

Focus on URL, title, description, headers, body text, and images:


* <i>**URL**</i>: the keyword phrase that you are targeting should be included in URL if that is possible 
  * construction of a *good URL*: descriptive but short, and concise as possible

* <i>**Metadata**</i>
  * *meta* <i>**title**</i> *tag* optimization
    * make sure your <title_description> tag is successful (*"title" tag in html"*), and that it contains (some of) your target keywords for the best SEO results
  * <i>**headers**</i>: html `h1` tag: give good descriptions (not very long or very short) that encompass your target keywords and your target content
      * Although this might not impact your rankings, optimizing the meta description can improve your current click-through rate since it is often used in search engine results listing.

* Optimize your content (<i>**body text**</i>) first for your *customers* and then for *search engines* (since the Natural Language Progress (NLP) has tremendously improved, search engines can comprehend text like human beings better and better over time). 

* Make search engines understand your <i>**images**</i>: while NLP focuses on text and search engines can take advantage of that, not much help is given to them regarding images (all they can "see" is pixels), video or audio clips, unless specified:   
  * improve your `"src"` and `"alt"` html attributes with reference to your *images*
  * embrace [**structured data**](https://developers.google.com/search/docs/guides/intro-structured-data) with [*JSON-LD*](https://json-ld.org/) (JavaScript Object Notation for Linked Data) to mark up your code with specific and rich range of metadata of specific content for *images, video, and audio*. In this way, you can optimize the descriptions closer to the keywords and phrases. Implementation of structured data allows you to display information about specific content, location, dates, pricing content, and more.
    * You can use websites like [schema.org](https://schema.org/docs/gs.html) to enhance ycour schema of your mark up code, and then test the effectiveness of your code with e.g. the [google structure data testing tool](https://search.google.com/test/rich-results?utm_campaign=sdtt&utm_medium=message).

<br>

**Tools**: https://moz.com/learn/seo/title-tag

<br>

## Technical Content Optimization

### Content & Links

Ways to leverage SEO from a technical perspective:

* Construct HTML and <i>**XML sitemap**</i>: https://www.sitemaps.org/index.html
  * A sitemap is a file where you provide information about the pages, videos, and other files on your site, and the relationships between them.

* Control how easy or difficult is your site to be crawled: Have a "[<i>**robots.txt**</i>]((http://www.robotstxt.org/))" file on your main root directory for content you don't want to be discovered by search engines by setting *rules* of how the search engine will crawl, read, and navigate your web page.
  * However, if you don't want that "hidden" content to affect your ranking (i.e. to be ranked higher because of that undesired content that might crosscheck you with undesired user queries), then instead of robots.txt use "`meta name="robots" content="noindex"`"

* Although every seperate page of your website should have a <i>**unique URL**</i> (i.e. /main.html, /contact.html) to discriminate content, <ins>you do not want different url adresses to provide the same content</ins> because this would lead to *confusions* for search engines and you might end up competing with yourself. This confusion can happen when we try to store *session ids* or *tracking parameters* in which case the URL can be different but the content remains exactly the same.
  * Use `link rel="canonical"` before href=" ", to resolve the issue on the occurrence of providing the same content but with different URL links. The `canonical tag` can be used to 
  indicate which is the primary URL for dublicate content across you website pages.
    * Another way to indicate that is directly via the *crawl URL paremeters* section of the Google Search Console](https://search.google.com/search-console/about), and also at [Bing Webmaster Tools](https://www.bing.com/webmasters/about)

* <i>**Redirect issues**</i>: It happens when you use some content of your website to another location of your website, e.g. to another page of your website, however this might not update directly the search engines. These kind of issues might be either <ins>temporary</ins> or <ins>permanent</ins>, and you should use `redirect rules` after moving content across your web page:
  * Temporary redirections: e.g. when you want to display a temporaral content for users to view while you are maintaining your website ==> use `302 (Temporary Redirect)` so that you tell the search engine not to take into consideration the content appearing now and which does not express you. Be careful as this might be interpreted as 301 (see below) if you keep that for too long
  * Permanent redirections: e.g. when you moved a part of your content to another location ==> use `301 (Permanent Redirect)`. In this way you tell search engines to apply all the necessary tranformations to the content that moved from the old URL to the new one.

* When redirecting URLs with *JavaScript* or *meta refresh tags* this may not be suitably processed by search engines.

* <i>**Microformats**</i> and <i>**Microdata**</i> with `schema`: `Semantic` attributes of content can be more efficiently translated by search engines with microdata ==> [schema.org Microdata markup](https://schema.org/docs/gs.html) ==> it provides documentation for specific mark up code syntax for several types of content that can be used in order to help search engines identify specific content as well as the characteristic attributes and metadata of that content across your web pages.
  * **Microformatting**:
    * `JSON-LD` (JavaScript Object Notation for Linked Data)
    * `Embedded or inline Microdata`
    * `RDFa` (Resource Description Framework in Attributes)

### Server-side   
Serving up your website's pages fast and reliably => *quality experience*

* <i>**Visibility**</i> of your website: physical `location` of the web server that hosts your website ==> loading time for visitors that are far away from that location
  * you want to geographically locate your web server to a place that would be relatively near to the majority of your clients
    * if your clients are spead all-over the world relatively equally: use a web host that can distribute requests for your website pages globally
      * You can use `Content Delivery Network (CDN)` which minimizes the loading time delays (*latency*) which are due to the physical distance between the server and users.


* <i>**Cashing**</i>: *Enable server-side cashing* to minimize the increased time load of the *database* workload. This would make the server and the database interact only once to generate the given pages (the servel will "remember" the content for a period of time at a future and subsequent load request)

* Server <i>**reliability**</i>: prefer `HTTPs` and not the HTTP protocol, not only because it is safer but also because it can boost your ranking compared to using http ([http deprecation](https://www.chromium.org/Home/chromium-security/marking-http-as-non-secure))

### Google Search Console

https://search.google.com/search-console/about


* add property => URL prefix => verification of domain => website verification

* through the "*Search results*" you can view your *total clicks, total imperssions, average clickthrough rate (CTR)*, and much more

* via the tools provided by the google search console, you can reduce search engine crawl errors, adress your SEO and [optimize your content](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content-optimization), by finding out various errors/bugs or non-optimal features that exist at your website. This can be achieved either from a technical perspective (e.g. [301 and 302 redirects](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content--links)) or from a non-technical perspective (e.g. duplicate content, block content, content no more relevant).

* via the "`Sitemaps`" section, you can upload your XML site maps

* via [Removals](https://support.google.com/webmasters/answer/9689846?hl=en) you can put the website parts of your websites that you do not want to be indexed by search engines (see about *robots.txt* or *noindex meta tag* [here](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content--links))
  * submit specified directories: do not put your root domain URL as this will make your whole website gone from the search indexing perspective
  * the removal lasts 6 months, hence after that period you should refresh the "removal" section


## Content Planning & Strategy
It is about *planning*, *creating*, and *managing* a useful and usable content.

1. `Planning`: To whom customers you are referring to. You should target a specific portion of customers that might be interested to your product/services


2. `Creating`: Quality of content > quantity of content, and with relevant and useful sources to provide

3. `Managing`: Through [keyword attributes planning](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keyword-attributes), [keyword research](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keyword-research), [keyword distribution](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keyword-distribution), and [content optimization](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content-optimization)

### Content Strategy

* Clear <ins>definition</ins> of **goals** and **objectives**
  * what *keywords* you chose to target
  * what your customers are *searching* for
  * how you want them to *behave* when they *visit your website*

* Comprehend your customers' **needs**
  * demographic and psychographic information, interests, behaviours

* Monitoring **trends**
  * your customer audience and competitors might change rapidly
    * this also means reviewing, redefining, and refining your keywords research 

* Make an editorial calendar (who writes what content in which page and section page at your website and social media)

<br>

**Content types**:
* text, files (word, pdf, ppt), infographics, newsletters, images, videos, Augmented Reality, Virtual Reality

<br>

**Subject content**:
* Educational
* Statistical
* Technical / Procedurar 
* Informational 
* News

<br>

**Content Measurement**
* *popular content*: what content do your customers view and like the most? 
* *customer engagement*: do your customer share your content?
  * Tools to analyze customers' behaviour upon your content, e.g.: [Google Analytics](https://analytics.google.com/analytics/web/provision/#/provision)

<br>

**Customer Engagement Metrics**:
* Average time on site 
* Pages view per visit
* Bounce rate (when a customer visits your website but leaves right away without engaging) / the lower the bounce rate the better

<br>

### Links Strategy
* Use anchor *text links* instead of just "click here" links, with meaningful text upon the links

* You want qualitative links pointing back to your website, i.e. from authoritative and popular websites
  * however, the more relative those links to your content are, the better (*thematic connections*), i.e. it would not make much sence a non-relative website to provide a link towards your website

#### External vs. Internal Links

**Internal Links**

Via the internal links of your website, search engines can get a good idea of the structure of your web pages across your website.

1. <i>**Navigational Links**</i>:
* The links for your main sections (pages) and subsections of your website


2. <i>**Contextual Links**</i>:
* When e.g. a viewer clicks to a link embedded in some content, and jumbs e.g. from page one to the second page, i.e. when the content of some page references content of another page from the same website

<br>

**External Links**

Links that point towards your website.

* web directories (selectively and trustworthy, after an approved review) / local business directories / social media / websites with <ins>relevant</ins> content (e.g. when you reference another website along with some of your content) / links pointing to your website from other websites
  * e.g. links from non-profit or educational organizations can be quite trustworthy

**Link-building**: [moz link explorer for backlink checker](https://moz.com/link-explorer), and other tools like: [majestic.com](https://majestic.com/), [ahrefs.com](https://ahrefs.com/), [raven tools](https://raventools.com/), [semrush](https://www.semrush.com/)
* you want backlinks with high page and domain authority
  * you can examine the backlinks of other popular websites with similar content to you
  * by filling content gaps with your own content, you can build a series of websites network pointing at your website and referencing your product/services

----

# SEO Performance Evaluation

SEO effectiveness can be evaluated both from the traffic derived from the **organic search traffic** and the **business outcomes** after defining your business objectives and *Key Performance Indicators (**KPIs**)*, and with regard to your SEO strategies. For instance, you may designate as a *conversion action* the occurrence of your contact form being filled out and submitted by customers, and as a *coversion rate* the number of times that this happens. (But first of all, you should define your business goals and KPIs)

<br>

Indicative **KPIs**:
* The delta rate in organic search over time
* Keyword (branded or not) search queries and ranking
  * you can merge your [Google Analytics 360](https://marketingplatform.google.com/about/) account along with your [Google Search Console](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#google-search-console), and get various insights from that combination.
* Number of newsletters subscribers and various signups
* Social followers

<br>

* Tools: [Google Analytics 360](https://marketingplatform.google.com/about/), [Adobe Analytics](https://www.adobe.com/analytics/adobe-analytics.html), [Webtrends](https://www.webtrends.com/), [IBM Data Analytics](https://www.ibm.com/analytics)


## E-Commerce

If your business organization is <ins>E-commerce</ins>, then other KPIs might be:
* Revenue
* Average order values
* Transcactions


* In e-commerce it is even more necessary to take advantage of the [schema.org Microdata markup](https://schema.org/docs/gs.html) at your website's code, [details](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#optimizing-text--non-text-elements
)
  * also to take care of the mobile navigation of your website: good search functionality, mobile-friendly UI/UX design, filters, swipeable photos, enabling voice search for queries

* [Google business listing](https://www.google.com/business/) for enhancing local business SEO (e.g. to appear on maps locally)

----


# Rules of thumb

* You probably won't have your webpage optimized if you first don't know at which group of keywords you should be focusing on (through [keywords research](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keyword-research) and more).


* If you have high *impression rate* but low *click-through-rates (CTRs)* this means you are showing up at the search results but viewers don't click your website.

* If search volume is high and competition/difficulty is low, this means there is large potential traffic at the lowest levels of competition, i.e. demand is high and supply is low, a fact which may suggest market opportunity.

* Use a specific group of keywords that have a meaningful *search volume*, are *relevant*, and are not too competitive (since it would be difficult for you to be discriminated if there is a lot of competition around those keywords).

* If a specific keyword is being aggressively bid on in CPC markets, this is an indicator of how difficult it will be organically. I.e., If a keyword is being aggressively bid on, this means that a significant competition from paid ads exists, and developing an alternative keyword might be necessary.

----

# More to Read



[How Google Search Works (Google)](https://www.google.com/search/howsearchworks/)

[How Search Engines Work: Crawling, Indexing, and Ranking (moz.com)](https://moz.com/beginners-guide-to-seo/how-search-engines-operate)

[Moz.com Community](https://moz.com/community)

[The Art of SEO, Mastering Search Engine Optimization (book)](https://www.amazon.com/Art-SEO-Mastering-Search-Optimization/dp/1491948965)

[How to improve SEO with web design](https://www.editorx.com/shaping-design/article/how-to-improve-seo-with-design)


----

# Appendix: Table of Useful Links

----

[Go to contents](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#contents)

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

[16] https://developers.google.com/search/docs/advanced/sitemaps/overview

[17] https://schema.org/docs/gs.html

[18] https://www.akamai.com/us/en/cdn/what-is-a-cdn.jsp

[19] https://support.google.com/webmasters/answer/9689846?hl=en

[20] https://www.editorx.com/shaping-design/article/how-to-improve-seo-with-design

[21] https://www.wordstream.com/blog/ws/2015/04/30/seo-basics#_What_is_SEO

<i>And various hyperlinks that can be found across the script.</i>

-----

[Go to main page](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO)
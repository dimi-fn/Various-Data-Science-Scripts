**Work on progress*

----

# Search Engine Optimization (SEO) Handbook

## Contents

* [Acronyms](#acronyms)
* [SEO in the context of Information Retrieval (IR)](#seo-in-the-context-of-information-retrieval-ir)
  * [Information Behaviour & Indexing](#information-behaviour--indexing)   
  * [Zipfian Distribution - Stopwords - Stemming](#zipfian-distribution---stopwords---stemming)
  * [Relevance & Authenticity](#relevance--authenticity)
  * [Recommender Systems Evaluation Metrics](#recommender-systems-evaluation-metrics)
    * [PageRank](#pagerank)
    * [Precision](#precision)
    * [Recall](#recall)
* [Organic Search vs. PPC](#organic-search-vs-ppc)
* [Ranking Factors on Search Results](#ranking-factors-on-search-results)
* [Keywords](#keywords)
  * [Keyword Attributes](#keyword-attributes)
  * [Keyword Research](#keyword-research)
    * [Query: Data Science](#query-data-science)
    * [Query: Machine Learning](#query-machine-learning)
    * [Query: Artificial Intelligence](#query-artificial-intelligence)
    * [Query: Data Science vs Machine Learning vs AI](#query-data-science-vs-machine-learning-vs-ai)
  * [Keyword Distribution](#keyword-distribution)
* [Content Optimization](#content-optimization)
  * ["Inner" vs. "External" SEO](#inner-vs-external-seo)
  * [Optimizing Text & Non-Text Elements](#optimizing-text--non-text-elements)
  * [Technical Content Optimization](#technical-content-optimization)
    * [Content & Links](#content--links)
    * [Server-side](#server-side)
    * [Google Search Console](#google-search-console)
  * [Content Planning & Strategy](#content-planning--strategy)
    * [Content Strategy](#content-strategy)
      * [Links Strategy](#links-strategy)
* [SEO Performance Evaluation](#seo-performance-evaluation)
  * [E-Commerce](#e-commerce)
* [Rules of thumb](#rules-of-thumb)
* [Recommended Reading & Additional Research](#recommended-reading--additional-research)
* [Appendix: Table of Useful Links](#appendix-table-of-useful-links)
* [Sources](#sources)

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


# SEO in the context of Information Retrieval (IR)

A successful SEO strategy can be achieved by optimizing both for the `search engine` and the surfers/`consumers`.

* **search engine** ==> technical perspective ==> `Information Retrieval`

* **consumers** ==> human perspective ==> `Information Seeking`


## Information Behaviour & Indexing
### Information Seeking & Behaviour
<i><b>Information Behaviour</b></i> describes the ways through which people seek and utilize information. It is a broader term than that of <i><b>Information Seeking</b></i> because through Information Behaviour we want to give answers to questions such as:

* How do people start a search?
* How do users seek information and how do they utilize it?
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
    * **Stopwords** removal achieves <i><b>discrimination</b></i>: it is the removal of words that are common to most of the documents (words like "and", "are", "do", "am", "but")
    * While stopwords removal emphasizes on discrimination, **stemming** emphasizes on document's <i><b>description</b></i> ==> stemming algorithms help us achieve a common concept of the words that can take different forms, by adding all variants of the corresponding words to document descriptions (e.g., information -> inform, political -> polit)

* A medium number of words appear <ins>each</ins> in a medium number of documents (`medium-frequency words`) 
  * These are the "**best**" words in the IR context ==> they represent some recognizable concept (satisfactory *description* level) that does not seem to be meaningless (satisfactory *discrimination* level)

* A large number of words appear <ins>each</ins> in a small number of documents (`low-frequency words`)

-----

<br>Other main terminologies, topics, and sections around the above contents are:
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
Two important topics that determine *search engine rankings* and *Search Engine Resuts Pages* (`SERPs`), and consequently a website's **PageRank** are: `relevance` and `authenticity`, i.e. if the results that websites produce are relevant and authenticated.

### Relevance
It is determined by various factors such as:
* content and code implementation
* thematic and semantic (metadata) connections between the query and website's content

A tricky concept about *relevance* in IR is that `we want our document to have a good description regarding its content (description), but at the same time we also want that document to be discriminated against other documents (discrimination)`. The problem here is that if we tried to describe our document with 'common sense' (i.e. in the way everybody would describe it) then we would probably not achieve satisfactory document discrimination because this is how everybody described similar documents as well!


**Relevance Levels**:

Some of the main relevance level categories comprised of the: System, Topical, and the Cognitive relevance level (*Tefko Saracevic*):

* **System relevance level**: the relationship between query and document

* **Topical relevance levels**: the relationship between the topic of query and topic of document (i.e. not just keyword matching)

* **Cognitive relevance level**: the relationship between user's state of knowledge and texts (i.e. the ability to understand the information given)


### Authenticity
Authenticity in the context of SEO is known as <i>**Domain Authority**</i>. Essentially, it is a measure of how authoritative your domain is. 

Contributing factors include:
* the quantity and quality of links (hyperlinks) pointing to you from other websites (third-party domains), known as **inbound links** (or else **backlinks)
* reviews - sentiment

-----

## Recommender Systems Evaluation Metrics
### PageRank

PageRank measures how likely a surfer is to visit a web page:

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/pagerank.PNG" alt="Pagerank"/>
</p>

* `PR(p)`: PageRank score of page p
* `d`: the probability a surfer will continue clicking from this current website (85%), rather than jumping to a new location (15%).
i.e. the user will go from website x to website y via the website x (website x recommended that) with a probability of 85%, rather than visiting website y directly by
navigating to another page of the browser (15%)
* `N`: total number of pages in the collection
* `pjEM(p)`: set of all pages linked to p
* `L(pj)`: total number of links from page j


### Precision
Precision in the context of Information Retrieval:

<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/precision_IR.PNG" alt="Precision"/>
</p>

* It tells us how **useful** the results are (*effectiveness* in terms of the given results).
  * A perfect precision score of 1 means that every result retrieved was relevant, but <ins>it says nothing about if all relevant documents were retrieved</ins>
  * Preference for higher precision than recall: e.g., legal and medical queries where there is a substantial need for high precision and correct results


### Recall
Recall in the context of Information Retrieval:
<p align="center">
  <img src="https://github.com/dimi-fn/Various-Data-Science-Scripts/blob/main/SEO/img/recall_IR.PNG" alt="Recall in Information Retrieval"/>
</p>

* It tells us how **complete** the results are (*completeness* in terms of the given results).
  * A perfect recall score of 1 means that all relevant documents were retrieved, but <ins>it says nothing about how many irrelevant documents were also retrieved</ins>
  * Preference for higher recall than precision: e.g., youtube recommendations, seeking online library collections/scientific articles: There is a need for a plethora of information/documents/results retrieved even if some of them might be irrelevant to some extent

<br><br>

Further research on Recommender System metrics may include: Mean Average Precision at K (MAP@K), Mean Average Recall at K (MAR@K), Coverage, Personalization, and Intra-list Similarity.

-----

# Organic Search vs. PPC

* **Organic search** (*natural search*) refers to unpaid search results which are generated based on: inbound links pointing to your website, your domain authority, the relevance to the user's search query, and other organic ranking factors

* **Pay-per-click** advertising (*PPC*) generates paid search results, it belongs to *paid search marketing* approach, and one of its basic performance metrics is cost-per-click (CPC) evaluation. Examples: Google ads, Google Product Listing Ads, Google Shopping Ads, Bing Ads)

# Ranking Factors on Search Results

Following the [Relevance & Authenticity](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#relevance--authenticity) section, and although search ranking algorithms change over time, it can be safely claimed that good ranking results align with **high quality** and **relevant information**. Hence, some of the most important ranking factors can be found aggregately and hierarchically on importance as followed:


| `Ranking Factor` | `Description/Examples` |
|---------------|----------------------|
| **Domain-Level & Link Authority Features** | quality of links to domain, domain-level PageRank |
| **Page-Level Link Features**| PageRank, TrustRank, quantity of link links, anchor text distribution, quality of link sources|
| **Page-Level Keywords & Content Features**| Term Weighting ( TF * IDF), topic modelling content score, content relevance|
| **Page-Level Keyword Agnostic Features**| content length, load speed, readability, uniqueness vs dublicate content|
| **Domain-level Brand Features**| offline usage of domain name/brand, mentions of domain name in news|
| **Traffic & Query Data**| usage signals from browsers, clickstream, CTR of queries|
| **Social Metrics**| quantity and quality of links and sharings from social media|
| **Domain-level Keyword Usage**| exact and partial keyword matches|
| **Domain-level Keyword-Agnostic Features**| domain name length, Top Level Domains (TLD), HTTP responses|

# Keywords
Understanding user's (commercial) `intent` (what users are looking for and how they search) is important for constructing the right keywords. 

What would a user type to find a product/service similar to that that you are selling?
What keywords would the user have to type in order to find your specific web page? 

## Keyword Attributes
Keywords *research plan* regarding: `search volume`, `relevance`, and `competition`.

**1) Relevance**: Relevant Keywords: Put yourself in the customers' shoes to discover their *intent* and understand their *customer behaviour*. In this way, you will find out which keywords might be relevant to your product/service. e.g., if you sell cars, don't just focus on the keyword "car" (this is what everybody includes in the car websites). You should write about the specific brands you sell and other car attributes. Successfully targeted descriptive keywords will help rank your website higher than the generic ones.

<br>

**2) Search volume**: The number of searches of a particular keyword per month. One tricky fact here is that on the one hand, although some specific keywords or groups of keywords might theoretically lead to your website successfully, they might not be popular queries from users. i.e. it does not matter if your website can be found by some specific query as long as this query is a "strange" query that nobody would really type it to find your product.
Tools for researching the **potential monthly search volume** of keywords: [moz explorer](https://moz.com/explorer), [wordstream](https://www.wordstream.com/keywords), [ahrefs](https://ahrefs.com/keywords-explorer), [semrush.com](https://www.semrush.com/analytics/keywordmagic/start), [google trends](https://trends.google.com/trends/?geo=US).

<br>

**3) Competition / Difficulty**: Keyword competition/difficulty: if what you are selling is already on the web and sold by others as well, this inevitably means that there is already a lot of content around a group of keywords describing your product. When the "**difficulty**" feature in the analytics elements is **low** => competition low => the product that users are typing to find (query) does not lead to many websites, i.e. there are not so many sellers available for that product. It is like "I am googling it but I can't find it anywhere". The opposite scenario happens when the difficulty rate is **high**, i.e. when there is a lot of competition around that query as well as availability about the respective product/service that the users' query is referring to.

<br>

<ins>**SERP** (Search Engine Results Page) **Analysis** Report</ins>: It is the process of analyzing the top web pages that rank for a specific keyword or topic. For instance, let's say you sell cars and you think that if someone types "buy a car" will find you. You can type that at the SERP Report and find out. How your website would rank bases on a series of given keywords?

For example, if for a group of keywords at moz.com the search volume is high but the difficulty grade is low, this means that a lot of users have searched for that query but not too many websites are suitably responding based on that query. 

<br>

## Keyword Research

Keyword research has to be conducted iteratively through the year, and *keyword performance <b>evaluation</b>* comes at the end of each keyword research iteration. The only thing you cannot pre-define and predict is the conversion rate (success or not) of your keywords.

**1) Brainstorming**: *What products/services do you offer?* ==> Do it from the customer's perspective (and not business's), think like a customer.

* Getting **insights** about your website: [Google Search Console](https://search.google.com/search-console/about) (former Google Webmaster Tools)

* **Keyword expansion tools**: They can give potentially useful keywords regarding a topic. e.g., How people are searching for products/services on the web and what keywords are they using for finding out a specific item? In this way, you can get to know your target audience better, and generate a list of *potential keywords*. Tools: [Google Trends](https://trends.google.com/trends/?geo=US), [Answer the Public](https://answerthepublic.com/), [moz.com](https://moz.com/)

<br>

**2) Search Volume Metrics**: *What is the current state of **demand** for those keywords?*

You should also focus on long-tail keywords, i.e. the descriptive keywords.

For example, if you sell cars then it would be quite hard for you to be ranked first at search results when the user searches for "car". But users do not type only "cars" when they want to buy one. They also type many other queries (longer and more descriptive), e.g., BMW black cars, sports fast cars, electric cars, cars for sale in Germany, red Ferrari in the Netherlands, etc. Focusing on those long-tail keywords might give you better probabilities of higher ranking than focusing on the very competitive query "car".

<br>

**3) Keyword Categorization**: *Clustering* of your keywords by categorizing them into topics/themes in order to group them.

----

<br>The following twelve images (derived from https://answerthepublic.com/) depict three search query examples with four images per query, giving analytics insights in the context of SEO. The first four photos are with regard to the search query "**Data Science**", the following four regarding "**Machine Learning**", and the rest of the images with respect to query "**Artificial Intelligence**". For every search query, there are four analytics insights: questions, prepositions, comparisons, and related. 
* `Questions`: how users ask a question
* `Prepositions`: what prepositions users use for asking that query
* `Comparisons`: what comparisons do users think of when they type their query
* `Related`: Related queries to the main query's subject (e.g., in Google they would be the top suggestions marked as "Related Searches")

The last graph (derived from [Google Trends](https://trends.google.com/trends/?geo=US)) illustrates the **search interest** rate with regard to the same three queries aforementioned. A value of 100 is the peak popularity for the term, a value of 50 means that the term is half as popular, and a score of 0 means that there was not enough data for this term.

Lastly, the data describing the images can be integrated into [CSV files](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO/csv) that are provided by both respective sources.
* Ιn the CSV directory, a [CSV file provided by Moz.com](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO/csv/moz) can additionally be found with regard to the query "Artificial Intelligence", and how Moz aggregates the keyword results and metrics.

<br>

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


<br>

The above images can depict a range of analytics insights. One of the ways you can utilize them is by matching those keywords related to your product/services with the headlines of your articles on your website. However, you should be aware of the high competition of those popular keywords. Ideally, you would focus on keywords that have high search volume (the greener the dot the higher the search volume) with medium or low competition (i.e. the case in which users are looking for something that does not seem to be provided by many sellers).
* * [How to use AnswerThePublic](https://searchlistening.com/how-to-use-answerthepublic-com-become-an-expert-with-search-listening/?utm_source=convertkit&utm_medium=email&utm_campaign=%5BLesson+1+AnswerThePublic.com+course%5D+Do+you+really+know+your+target+audience%3F%20-%202215116)

-----

<br><br>

## Keyword Distribution
It is the procedure of how you will assign and distribute your specific keywords across your website's pages.

In this way:
* you can <i>**map**</i> keywords to pages: you can enhance your targeted keywords by figuring out which keywords you should assign to which pages
* you can <i>**keep track**</i> of keywords that need pages (or pages that need keyword if there was no keyword assignment)
* you can detect and avoid keyword <i>**duplicates**</i> (search engine algorithms "prefer" unique and relevant information across your pages)
* you can reverse engineer the <i>**creation of the content**</i> of a new page to your website by first filling out the keyword distribution file. In this way, you would first decide on 
what keyword you are targeting, and then you would write the relevant content based on that keyword. In such a way, your content is more likely to be SEO successful
* you can <i>**adapt**</i> quickly: you can come back to this spreadsheet and add or redefine your keywords, as well as review the other metadata

## Keyword Distribution Diagram - Example

| Structure  | Keywords | URL (of specific page)| The title tag| Meta-description| the h1 header title|
|---------| -------------------------|----------|--------|-----------------|-------------------------|
| **home**  |  || ||  |
| *Cars*  |  || ||  |
| Mercedes  | mercedes-benz |/home/mercedes.html| Find and buy the best mercedes-benz cars in the world| Here is why you will find the best mercedes-benz cars in the world on my website (..)|  Best Mercedes-Benz in Germany|
| BMW | bmw car |/home/bmw.html| Find and buy the best bwm cars in the world| Here is why you will find the best BMW cars in the world on my website (..) | Fastest BMW cars in Austria |
| AUDI | audi car |/home/audi.html|  Find and buy the best audi cars in the world| Here is why you will find the best audi cars in the world on my website (..)| Best Audi cars in Italy |

----

# Content Optimization

It is about how search engines and consumers view webpages, including yours.

There is a need for:
* **Clarity** and **quality**: people tend to share with other people content that they *like*, find *useful* and *relevant*, and content that they *trust*

* Good website **structure** and layout: categorize and clarify your content in and across your web pages clearly both from business's and customer's perspective

## "Inner" vs. "External" SEO

The SEO procedures could generally be categorized into actions taken inside the website (*on-page SEO*), and optimizations that are undertaken off-page so that the website can get traffic.

<br>

**On-Page SEO features**:
* Title tag of page
* Headings (h1..h5)
* Keyword Optimization
* Eliminating duplicate content ([Google Search Central](https://developers.google.com/search/docs/advanced/guidelines/duplicate-content))
* Images (e.g., using good alt descriptions)
* Meta tags and meta descriptions
* URL (good descriptive URL but not too long)
* Header Response Code (HTTP statuses)
* Loading time of website (page speed)
* Mobile Friendliness
* Quality of content and informativeness (to keep your content up-to-date)
* Internal Links

<br>

**Off-Page SEO**:
* Social Media
* Link Building: getting backlinks from other sources (authoritative and popular)
* Creating quality and sharable content regularly

## Optimizing Text & Non-Text Elements

Focus on URL, title, description, headers, body text, and images:


* <i>**URL**</i>: the keyword phrase that you are targeting should be included in the URL if that is possible 
  * construction of a *good URL*: descriptive but short, and concise as possible

* <i>**Metadata**</i>
  * *meta* <i>**title**</i> *tag* optimization
    * make sure your <title_description> tag is successful (*"title" tag in HTML"*), and that it contains (some of) your target keywords for the best SEO results
  * <i>**headers**</i>: HTML `h1` tag: give good descriptions (not very long or very short) that encompass your target keywords and your target content
      * Although this might not impact your rankings, optimizing the meta description can improve your current click-through rate since it is often used in search engine results listing

* Optimize your content (<i>**body text**</i>) first for your *customers* and then for *search engines* (since the Natural Language Progress (NLP) has tremendously improved, search engines can comprehend text like human beings better and better over time)

* Make search engines understand your <i>**images**</i>: while NLP focuses on text and search engines can take advantage of that, not much help is given to them regarding images (all they can "see" is pixels), video or audio clips, unless specified:   
  * improve your `"src"` and `"alt"` HTML attributes with reference to your *images*
  * embrace *structured data* with [*JSON-LD*](https://json-ld.org/) (JavaScript Object Notation for Linked Data) to mark up your code with a specific and rich range of metadata of specific content for *images, video, and audio*. In this way, you can optimize the descriptions closer to the keywords and phrases. Implementation of structured data allows you to display information about specific content, location, dates, pricing content, and more
    * You can use websites like [schema.org](https://schema.org/documents/gs.html) to enhance your schema of your mark up code, and then test the effectiveness of your code with e.g., the [google structure data testing tool](https://search.google.com/test/rich-results?utm_campaign=sdtt&utm_medium=message)

<br>

**Tools**: https://moz.com/learn/seo/title-tag

<br>

## Technical Content Optimization

### Content & Links

Ways to leverage SEO from a technical perspective:

* Construct HTML and <i>**XML sitemap**</i>: https://www.sitemaps.org/index.html, https://www.xml-sitemaps.com/, [Google Code Sitemap](https://code.google.com/archive/p/sitemap-generators/wikis/SitemapGenerators.wiki), [Best Practises for Sitemaps from Google](https://developers.google.com/search/blog/2014/10/best-practices-for-xml-sitemaps-rssatom)
  * A sitemap is a file where you provide information about the pages, videos, and other files on your site, and the relationships between them
    * Alternatively, use [meta noindex](https://developers.google.com/search/docs/advanced/crawling/block-indexing) / [meta nofollow tags](https://searchengineland.com/google-explains-the-noindex-nofollow-noarchive-nosnippet-meta-tags-10595)

* Control how easy or difficult is your site to be crawled: Have a [robots.txt](http://www.robotstxt.org/) file on your main root directory for content you don't want to be discovered by search engines by setting *rules* of how the search engine will crawl, read, and navigate your web page
  * However, if you don't want that "hidden" content to affect your ranking (i.e. to be ranked higher because of that undesired content that might crosscheck you with undesired user queries), then instead of robots.txt use "`meta name="robots" content="noindex"`"

* Although every separate page of your website should have a <i>**unique URL**</i> (i.e. /main.html, /contact.html) to discriminate content, <ins>you do not want different URL addresses to provide the same content</ins> because this would lead to *confusion* for search engines and you might end up competing with yourself. This confusion can happen when we try to store *session ids* or *tracking parameters* in which case the URL can be different but the content remains exactly the same.
  * Use `link rel="canonical"` before href=" ", to resolve the issue on the occurrence of providing the same content but with different URL links. The `canonical tag` can be used to 
  indicate which is the primary URL for duplicate content across your website pages
    * Another way to indicate that is directly via the *crawl URL parameters* section of the Google Search Console](https://search.google.com/search-console/about), and also at [Bing Webmaster Tools](https://www.bing.com/webmasters/about)

* <i>**Redirect issues**</i>: It happens when you use some content of your website to another location of your website, e.g., to another page of your website, however, this might not update directly the search engines. These kinds of issues might be either <ins>temporary</ins> or <ins>permanent</ins>, and you should use `redirect rules` after moving content across your web page:
  * Temporary redirections: e.g., when you want to display a temporary content for users to view while you are maintaining your website ==> use `302 (Temporary Redirect)` so that you tell the search engine not to take into consideration the content appearing now and which does not express you. Be careful as this might be interpreted as 301 (see below) if you keep that for too long
  * Permanent redirections: e.g., when you moved a part of your content to another location ==> use `301 (Permanent Redirect)`. In this way, you tell search engines to apply all the necessary transformations to the content that moved from the old URL to the new one
    * `Apart from the above 301 and 302 redirect issues you always want your pages to return the status code of 200, and you never want the status code of 403 (page is forbidden), 404 (page not found), and 500 (application error)`

* When redirecting URLs with *JavaScript* or *meta refresh tags* this may not be suitably processed by search engines

* <i>**Microformats**</i> and <i>**Microdata**</i> with `schema`: `Semantic` attributes of content can be more efficiently translated by search engines with microdata ==> [schema.org Microdata markup](https://schema.org/docs/gs.html) ==> it provides documentation for specific mark up code syntax for several types of content that can be used in order to help search engines identify specific content as well as the characteristic attributes and metadata of that content across your web pages.
  * **Microformatting**:
    * `JSON-LD` (JavaScript Object Notation for Linked Data)
    * `Embedded or inline Microdata`
    * `RDFa` (Resource Description Framework in Attributes)

### Server-side   
Serving up your website's pages fast and reliably => *quality experience*

* <i>**Visibility**</i> of your website: physical `location` of the web server that hosts your website ==> loading time for visitors that are far away from that location
  * you want to geographically locate your web server to a place that would be relatively near to the majority of your clients
    * if your clients are spread all-over the world relatively equally: use a web host that can distribute requests for your website pages globally
      * You can use `Content Delivery Network (CDN)` which minimizes the loading time delays (*latency*) which are due to the physical distance between the server and users

* <i>**Cashing**</i>: *Enable server-side cashing* to minimize the increased time load of the *database* workload. This would make the server and the database interact only once to generate the given pages (the server will "remember" the content for a period of time at a future and subsequent load request)

* Server <i>**reliability**</i>: prefer `HTTPS` and not the HTTP protocol, not only because it is safer but also because it can boost your ranking compared to using HTTP ([HTTP deprecation](https://www.chromium.org/Home/chromium-security/marking-http-as-non-secure))

### Google Search Console

https://search.google.com/search-console/about


* add property => URL prefix => verification of domain => website verification

* through the "*Search results*" you can view your *total clicks, total impressions, average clickthrough rate (CTR)*, and much more

* via the tools provided by the Google search console, you can reduce search engine crawl errors, address your SEO and [optimize your content](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content-optimization), by finding out various errors/bugs or non-optimal features that exist on your website. This can be achieved either from a technical perspective (e.g., [301 and 302 redirects](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content--links)), or from a non-technical perspective (e.g., [duplicate content](https://developers.google.com/search/docs/advanced/guidelines/duplicate-content), block content, content no more relevant)

* via the "`Sitemaps`" section, you can upload your XML site maps

* via [Removals](https://support.google.com/webmasters/answer/9689846?hl=en), you can put the website parts of your websites that you do not want to be indexed by search engines (see about *robots.txt* or *noindex meta tag* [here](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#content--links))
  * submit specified directories: do not put your root domain URL as this will make your whole website gone from the search indexing perspective
  * the removal lasts 6 months, hence after that period you should refresh the "removal" section

## Content Planning & Strategy
It is about *planning*, *creating*, and *managing* a useful and usable content.

1. `Planning`: To whom customers you are referring to. You should target a specific portion of customers that might be interested in your product/services
   * [Persona Templates for customers' segmentation](https://offers.hubspot.com/persona-templates)

2. `Creating`: Quality of content should be greater than the quantity of content, the latter of which should be relevant and with useful sources to provide

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
* Technical / Procedural 
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

* Use **anchor text** at the links instead of just "click here" links, with meaningful text description upon the links

* You want qualitative links pointing back to your website, i.e. from authoritative and popular websites
  * however, the more relative those links to your content are, the better (*thematic connections*), i.e. it would not make much sense for a non-relative website to provide a link towards your website

#### External vs. Internal Links

**Internal Links**

Via the internal links of your website, search engines can get a good idea of the structure of your web pages across your website.

1. <i>**Navigational Links**</i>:
* The links for your main sections (pages) and subsections of your website


2. <i>**Contextual Links**</i>:
* When a viewer clicks on a link embedded in some content and jumps e.g., from page one to the second page, i.e. when the content of some page references the content of another page from the same website.

<br>

**External Links**

Links from external sources that point towards your website are perceived as confidence votes by the search engines.

* web directories (selectively and trustworthy, after an approved review) / local business directories / social media/ websites with <ins>relevant</ins> content (e.g., when you reference another website along with some of your content) / links pointing to your website from other websites
  * e.g., links from non-profit or educational organizations can be quite trustworthy

**Link-building**: [moz link explorer for backlink checker](https://moz.com/link-explorer), and other tools like: [majestic.com](https://majestic.com/), [ahrefs.com](https://ahrefs.com/), [raven tools](https://raventools.com/), [semrush](https://www.semrush.com/)
* you want **backlinks** with high page and domain authority
  * you can examine the backlinks of other popular websites with similar content to you
  * by filling content gaps with your own content, you can build a series of websites network pointing at your website and referencing your product/services

----

# SEO Performance Evaluation

SEO effectiveness can be evaluated both from the traffic derived from the **organic search traffic** and the **business outcomes** after defining your business objectives and *Key Performance Indicators (**KPIs**)*, and with regard to your SEO strategies. For instance, you may designate as a *conversion action* the occurrence of your contact form being filled out and submitted by customers, and as a *coversion rate* the number of times that this happens. (But first of all, you should define your business goals and KPIs).

<br>

Indicative **KPIs**:
* The delta rate in organic search over time
* Keyword (branded or not) search queries and ranking
  * you can merge your [Google Analytics 360](https://marketingplatform.google.com/about/) account along with your [Google Search Console](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#google-search-console) and get various insights from that combination.
* Number of newsletters subscribers and various signups
* Social followers

<br>

* Tools: [Google Analytics 360](https://marketingplatform.google.com/about/), [Adobe Analytics](https://www.adobe.com/analytics/adobe-analytics.html), [Webtrends](https://www.webtrends.com/), [IBM Data Analytics](https://www.ibm.com/analytics)


## E-Commerce

If your business organization is E-commerce, then other KPIs might be:
* Revenue
* Average order values
* Transactions

<br>

In E-commerce, it is even more necessary to take advantage of the [schema.org Microdata markup](https://schema.org/documents/gs.html) at your website's code, [details here](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#optimizing-text--non-text-elements).
* take, also, care of the mobile navigation of your website, e.g.: good search functionality, mobile-friendly UI/UX design, filters, swipeable photos, enabling voice search for queries

* [Google business listing](https://www.google.com/business/) for enhancing local business SEO (i.e. to appear on maps locally)

----


# Rules of thumb

* You probably won't have your webpage optimized if you first don't know which group of keywords you should be focusing on (through [keywords research](https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#keyword-research) and more).

* If you have a high *impression rate* but low *click-through-rates (CTRs)* this means you are showing up at the search results but viewers don't click your website.

* If search volume is high and competition/difficulty is low, this means there is large potential traffic at the lowest levels of competition, i.e. demand is high and supply is low, a fact which may suggest a market opportunity.

* Use a specific group of keywords that have a meaningful *search volume*, are *relevant*, and are not too competitive (since it would be difficult for you to be discriminated against others if there is a lot of competition around those keywords).

* If a specific keyword is being aggressively bid on in Cost-Per-Click (CPC) markets, this is an indicator of how difficult it will be organically. i.e. If a keyword is being aggressively bid on, this means that significant competition from paid ads exists, and developing an alternative keyword might be necessary.

----

# Recommended Reading & Additional Research

* [Beginner's Guide to SEO by Moz](https://moz.com/beginners-guide-to-seo)

* [Moz.com Community](https://moz.com/community)

* [How Search Engines Work: Crawling, Indexing, and Ranking (moz.com)](https://moz.com/beginners-guide-to-seo/how-search-engines-operate)

* [Link Explorer by Moz](https://moz.com/help/link-explorer?utm_campaign=092020-kwecomm&utm_medium=email&_hsmi=95404343&_hsenc=p2ANqtz-8DbmX5rwCWo95rHRGS_3BqRkIeFdmOjoxeJsqpvleA39qpYnox2oAu8d8BHNLkaUhhw51zT46MKMl_m6YJPck5wP8WtH1KAEnVd3zM2uqlvzvswA4&utm_source=hubspot)

* [How Google Search Works (Google)](https://www.google.com/search/howsearchworks/)

* [How to use AnswerThePublic](https://searchlistening.com/how-to-use-answerthepublic-com-become-an-expert-with-search-listening/?utm_source=convertkit&utm_medium=email&utm_campaign=%5BLesson+1+AnswerThePublic.com+course%5D+Do+you+really+know+your+target+audience%3F%20-%202215116)

* [Learn SEO from Google Developers, Documentation by Google Search Central](https://developers.google.com/search/docs)

* [Information Architecture for SEO](https://moz.com/blog/information-architecture-for-seo-whiteboard-friday)

* [Keyword Research Strategies, backlinko.com](https://backlinko.com/hub/seo/keyword-difficulty)

* [How to Get Backlinks in 2020](https://moz.com/blog/how-to-get-backlinks?utm_source=hubspot&utm_medium=email&utm_campaign=092020-lecomm&_hsenc=p2ANqtz-823A8ZW8O9t9fVqxD86PvO3B1-wtOR8QYvCB5Kt5jbIRWBGO-TobZhLmHzx5sPItyRXvTSxi9aMI2_mDR4ZsZ8IpZu2wChUwV4ioQDvCGhjrM_TSU&_hsmi=95404439&hsCtaTracking=70f2af25-e7ff-4e53-8219-5f55252903a3%7C11308ab0-9c32-4a47-9350-e627f04fc501)

* [The Art of SEO, Mastering Search Engine Optimization (book)](https://www.amazon.com/Art-SEO-Mastering-Search-Optimization/dp/1491948965)

* [How to improve SEO with web design](https://www.editorx.com/shaping-design/article/how-to-improve-seo-with-design)

----

# Appendix: Table of Useful Links

| Content| Link |
|------|------|
| **Keywords Explorer** | [Moz explorer](https://moz.com/explorer), [Answerthepublic](https://answerthepublic.com/), [Google Trends](https://trends.google.com/trends/?geo=US), [Wordstream](https://www.wordstream.com/keywords), [Ahrefs](https://ahrefs.com/keywords-explorer), [Semrush](https://www.semrush.com/analytics/keywordmagic/start), [Ubersuggest](https://neilpatel.com/ubersuggest/) |
| **Search Volume** | [Moz Pro explorer](https://analytics.moz.com/pro/keyword-explorer), [Wordstream](https://www.wordstream.com/keywords), [Ahrefs](https://ahrefs.com/keywords-explorer), [Semrush](https://www.semrush.com/analytics/keywordmagic/start), [Google Trends](https://trends.google.com/trends/?geo=US) |
| **Measure Site's Search Traffic & Performance** | [Google Search Console](https://search.google.com/search-console/about) |
|**SEO Performance Evaluation** | [Google Analytics 360](https://marketingplatform.google.com/about/), [Adobe Analytics](https://www.adobe.com/analytics/adobe-analytics.html), [Webtrends](https://www.webtrends.com/), [IBM Data Analytics](https://www.ibm.com/analytics) |
|**Schema Markup - Microdata**| [schema.org documentation](https://schema.org/docs/gs.html), [Schema at Wordstream](https://www.wordstream.com/blog/ws/2014/03/20/schema-seo), [test your Schema at Google](https://search.google.com/test/rich-results?utm_campaign=sdtt&utm_medium=message), [JSON for Linking Data](https://json-ld.org/), [Guide to JSON-LD, microdata and schema.org](https://builtvisible.com/micro-data-schema-org-guide-generating-rich-snippets/) |
| **Construct Sitemaps** | [sitemaps.org](https://www.sitemaps.org/index.html), [xml-sitemaps](https://www.xml-sitemaps.com/), [Code Google](https://code.google.com/archive/p/sitemap-generators/wikis/SitemapGenerators.wiki), [Best Practises for Sitemaps by Google](https://developers.google.com/search/blog/2014/10/best-practices-for-xml-sitemaps-rssatom) |
| **Robots.txt, Meta NoIndex, Meta NoFollow** | * [robots.txt](http://www.robotstxt.org/) <hr> * [meta NoIndex](https://developers.google.com/search/docs/advanced/crawling/block-indexing),  [meta NoFollow](https://searchengineland.com/google-explains-the-noindex-nofollow-noarchive-nosnippet-meta-tags-10595)    | 
| **Link Building** | [Moz Link Explorer for Backlink Checker](https://moz.com/link-explorer), [Majestic](https://majestic.com/), [Ahrefs](https://ahrefs.com/), [Raven tools](https://raventools.com/), [Semrush](https://www.semrush.com/)|
| **Page Speed** | [PageSpeed Insights by Google Dev.](https://developers.google.com/speed/pagespeed/insights/) |
| **Mobile Friendliness Checker** | [Test Mobile by Search Google](https://search.google.com/test/mobile-friendly?utm_source=mft&utm_medium=redirect&utm_campaign=mft-redirect) |
| **HTTP Status**  | [httpstatus.io](https://httpstatus.io/)|
| **How to Segment your Customers** | [Persona Templates](https://offers.hubspot.com/persona-templates) |
|**Search your Competitors' Keywords and other Attributes via their URL** | [Spyfu](https://www.spyfu.com/) |
| **Miscellaneous**|  * [Content Research by Frase](https://www.frase.io/content/)<hr>* [Image Optimization](https://ahrefs.com/blog/image-seo/) / [Automate Meta Descriptions](https://www.searchenginejournal.com/titles-meta-descriptions-automatically-python-javascript/360108/#close)<hr>* [Video Generation by Lumen5](https://lumen5.com/)<hr>* [Auto Transcribe - Speech to Text by AWS](https://aws.amazon.com/transcribe/)|
----

<br><p align="center">
<a href="https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO#contents">Go to Contents</a>
</p><br>

-----

### Sources

[1] https://www.linkedin.com/learning/seo-foundations/

[2] Dr Martin Halvey, 2019, *CS976 Information Retrieval*, lecture notes, University of Strathclyde, delivered at the 1st semester of the academic year 2019-2020, https://www.strath.ac.uk/courses/postgraduatetaught/informationmanagement/#coursecontent

[3] https://answerthepublic.com/

[4] https://www.wordstream.com/blog/ws/2015/04/30/seo-basics#_What_is_SEO

[5] https://medium.com/@bloghands/5-serp-analysis-tools-that-help-you-get-on-page-one-92b9b4e4df3a#:~:text=SERP%20(Search%20Engine%20Results%20Page,ranking%20for%20a%20Google%20search.

[6] https://eclecticlight.co/2015/07/11/zipfs-law-deep-and-meaningful/

[7] https://www.ranks.nl/stopwords

[8] http://infolab.stanford.edu/~backrub/google.html

[9] https://www.researchgate.net/publication/227634540_RELEVANCE_A_Review_of_and_a_Framework_for_the_Thinking_on_the_Notion_in_Information_Science

[10] https://towardsdatascience.com/evaluation-metrics-for-recommender-systems-df56c6611093

[11] https://www.wordstream.com/domain-authority

[12] https://www.wordstream.com/inbound-links

[13] https://econsultancy.com/what-paid-search-ppc/

[14] https://www.wordstream.com/organic-search

[15] https://developers.google.com/search/documents/guides/intro-structured-data

[16] https://search.google.com/test/rich-results?utm_campaign=sdtt&utm_medium=message

[17] https://developers.google.com/search/docs/advanced/sitemaps/overview

[18] https://schema.org/documents/gs.html

[19] https://www.akamai.com/us/en/cdn/what-is-a-cdn.jsp

[20] https://support.google.com/webmasters/answer/9689846?hl=en

[21] https://www.editorx.com/shaping-design/article/how-to-improve-seo-with-design

[22] https://www.wordstream.com/blog/ws/2018/06/13/off-page-seo

[23] https://www.gsqi.com/marketing-blog/hidden-seo-danger-wrong-header-response-code/

<i>And various other sources found on hyperlinks across the script.</i>

--------

<br><p align="center">
<a href="https://github.com/dimi-fn/Various-Data-Science-Scripts/tree/main/SEO">Go to Main Page</a>
</p><br>
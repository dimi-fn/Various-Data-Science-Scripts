# BI - Business Intelligence


Contents
=======================

* [Microsoft Power BI](#microsoft-power-bi)
    * [Elements/Parts of Power BI](##elementsparts-of-power-bi)
    * [Concepts](#concepts)
        * [Capacities](#capacities)
        * [Workspaces](#workspaces)
        * [Apps](#apps)
    * [Data Modelling & Visualizations](#data-modelling--visualizations)
        * [Types of visualizations](#types-of-visualizations)
        * [Filtering](#filtering)
    * [Miscellaneous](#miscellaneous)
* [Sources](#sources)

----

# Microsoft Power BI

----- 

## Elements/Parts of Power BI

1) Power BI `Desktop`: Microsoft Windows desktop application, [download-install](https://docs.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop#download-power-bi-desktop-directly)
    * It also includes a *Query Editor* which helps you transform data for visualizations
        * how to launch it: via PowerBI Desktop > Transform Data, or navigator window > Power Query Editor
2) Power BI `service`: online SaaS (Software as a Service)
3) `Mobile apps`: available on phones and tablets

## Concepts

Building blocks of PowerBI:
* `datasets`
* `reports`
* `dashboards`

Those are organized into **workspaces** and they are created on **capacities**

### Capacities

`Capacities`: set of resources used to host and deliver the PowerBI content. They are either *shared* or *dedicated*
* **Dedicated**: capacity is fully committed to a single customer. It requires a <u>subscription</u>
* **Shared**: shared with other customers. By <u>default</u>, workspaces are created under this a shared capacity.

### Workspaces

Staging areas and containers for datasets, reports, dashboards, and dataflows.

There are two types:
1) `My workspace`: personal workspace for any PowerBI customer to collaborate with your content. Only you have access to "my workspace".
2) `Workspaces`: they are used to collaborate and share content with colleagues. Requirement: workspace members need PowerBI Pro licenses.

### Apps

* Collection of dashboards and reports to deliver *key metrics* to PowerBI consumers

* Although apps are interactive, consumers (and colleagues who have access to those) cannot edit them. However they do not need Pro licenses to access the apps.

-----

## Data Modelling & Visualizations

PowerBI Desktop > Report view:

1) **Ribbon**: tasks with respect to reports and visualizations

2) **Report view - Canvas**: visualizations
* *Data view*: view data of report, check data types and validate data
* *Model view*: set the relationship between tables or elements in order to run queries for related data across multiple tables

3) **Pages tab**: bottom of the page. Select or add a report page

4) **Visualizations pane**: Interact with visualizations, customize colours or axes, apply filters, drag fields, and etc.

5) **Fields pane**: Query elements and filters can be dragged onto the Report view or dragged to the Filters area of the Visualizations pane

<br>

### Types of visualizations

* Area charts
* Bar and column charts
* Pie charts
    * donut charts
    * gauge charts
* KPIs
* Line charts
* Maps
* Q&A visual
* Tables
* Treemaps
* Waterfall charts

### Filtering

* Filtering only applies to reports, not to dashboards.

* Filter pane contains filters that are added by the report designer

* Filter types:
    * *report*: applies to all report
    * *page*: applies to current page
    * *visual*: applies to a single visual of the report page
    * *drillthrough*: allows a more detailed exploration of a single visual

-----

# Miscellaneous

* [Create a template app in Power BI](https://docs.microsoft.com/en-us/power-bi/connect-data/service-template-apps-create)

* [AppSource](https://appsource.microsoft.com/en/marketplace/apps?product=power-bi-visuals)
------



























# Sources

https://powerbi.microsoft.com/en-us/learning/
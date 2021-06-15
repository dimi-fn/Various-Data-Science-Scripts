# BI - Business Intelligence


Contents
=======================

* [Microsoft Power BI](#microsoft-power-bi)
    * [Documentation & Courses](#documentation--courses)
    * [Usage - Applications](#usage---applications)
    * [Elements/Parts of Power BI](#elementsparts-of-power-bi)
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

Power BI is designed for self-service business intelligence, it is built on Azure Microsoft's cloud computing infrastructure and platform, and it can be used for powerful analysis and visualization.

------

## Documentation & Courses

* [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)

* [MS courses](https://docs.microsoft.com/en-us/learn/browse/)

------

## Usage - Applications

* create/view reports and dashboards
    * (*report vs dashboard*: reports provide more pieces of information regarding the dashboard, i.e. reports include a more detailed collection of tables and charts, while dashboards are mostly used for monitoring what is going on)

* use a Power BI phone app to monitor progress on a targeted variable



------

## Elements/Parts of Power BI

1) Power BI `Desktop`: Microsoft Windows desktop application, [download-install](https://docs.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop#download-power-bi-desktop-directly). Mostly useful for modeling and creating Power BI reports.
    * It also includes a *Query Editor* which helps you transform data for visualizations
        * how to launch it: via Power BI Desktop > Transform Data, or navigator window > Power Query Editor
        * [Using Power Query in Power BI Desktop](https://docs.microsoft.com/en-us/power-query/power-query-ui)
2) Power BI `service`: online SaaS (Software as a Service), i.e. the cloud-based service. Mostly useful for sharing and collaboration
3) `Mobile apps`: available on phones and tablets

## Concepts

Building blocks of Power BI:
* `datasets`
* `reports`
* `dashboards`

Those are organized into **workspaces** and they are created on **capacities**

### Capacities

`Capacities`: set of resources used to host and deliver the Power BI content. They are either *shared* or *dedicated*
* **Dedicated**: capacity is fully committed to a single customer. It requires a <u>subscription</u>
* **Shared**: shared with other customers. By <u>default</u>, workspaces are created under this a shared capacity.

### Workspaces

Staging areas and containers for datasets, reports, dashboards, and dataflows.

There are two types:
1) `My workspace`: personal workspace for any Power BI customer to collaborate with your content. Only you have access to "my workspace".
2) `Workspaces`: they are used to collaborate and share content with colleagues. Requirement: workspace members need Power BI Pro licenses.

### Apps

* Collection of dashboards and reports to deliver *key metrics* to Power BI consumers

* Although apps are interactive, consumers (and colleagues who have access to those) cannot edit them. However they do not need Pro licenses to access the apps.

-----

## Data Modelling & Visualizations

Power BI Desktop > Report view:

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
* Q&A viual
* Tabless
* Treemaps
* Waterfall charts

### Filtering

* Filtering only applies to reports, not to dashboards

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

## Sources

[1] [Main source: Microsoft Power BI](https://Power BI.microsoft.com/en-us/learning/)

[2] https://spreadsheeto.com/power-bi-desktop-vs-online/

[3] https://chartio.com/blog/dashboards-vs-reports-how-theyre-the-same-how-theyre-different/
# Business Intelligence (BI)


Contents
=======================

* [Microsoft Power BI](#microsoft-power-bi)
    * [Usage - Applications](#usage---applications)
    * [Elements/Parts of Power BI](#elementsparts-of-power-bi)
    * [Workflow](#workflow)
    * [Documentation & Courses - Various Links](#documentation--courses---various-links)
    * [Concepts](#concepts)
        * [Building Blocks of Power BI ](#building-blocks-of-power-bi)
        * [Capacities](#capacities)
        * [Workspaces](#workspaces)
        * [Apps](#apps)
    * [Data Modelling & Visualizations](#data-modelling--visualizations)
        * [Types of visualizations](#types-of-visualizations)
        * [Filtering](#filtering)
    * [Import Data & Analysis](#import-data--analysis)
        * [Getting Data](#getting-data)
    * [Miscellaneous](#miscellaneous)
    * [Sources](#sources)

----

# Microsoft Power BI

Power BI is designed for self-service business intelligence, it is built on Azure Microsoft's cloud computing infrastructure and platform, and it can be used for powerful analysis and visualization.

------

## Usage - Applications

Showcases:

* create/view reports and dashboards
    * (*report vs dashboard*: reports provide more pieces of information regarding the dashboard, i.e. reports include a more detailed collection of tables and charts, while dashboards are mostly used for monitoring what is going on and for a quick overview)

* use a Power BI phone app to monitor progress on a targeted variable

* view inventory and manufacturing progress in a real-time dashboard in the service

------

## Elements/Parts of Power BI

1) Power BI `Desktop`: Microsoft Windows desktop application, [download-install](https://docs.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop#download-power-bi-desktop-directly). Mostly useful for modeling and creating Power BI reports.
    * It also includes a *Query Editor* which helps you transform data for visualizations
        * how to launch it: via Power BI Desktop > Transform Data, or navigator window > Power Query Editor
        * [Using Power Query in Power BI Desktop](https://docs.microsoft.com/en-us/power-query/power-query-ui)
2) Power BI `service`: **online** SaaS (Software as a Service), i.e. the cloud-based service. Mostly useful for sharing and collaboration
3) `Mobile apps`: available on phones and tablets

## Workflow

1) Fetch data to Power BI Desktop and create a report
2) Publish to Power BI SaaS (Power BI online), create new visualizations and/or build dashboards
3) Share dashboards with others and interact with shared dashboards
4) Power BI Mobile apps can be used for no3 workflow

## Documentation & Courses - Various Links

[Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)

[MS courses](https://docs.microsoft.com/en-us/learn/browse/)

* Various Links
    * [Quick Insights, Types of insights supported by Power BI](https://docs.microsoft.com/en-us/power-bi/consumer/end-user-insight-types)

    * [Sharing Methods](https://radacad.com/power-bi-sharing-methods-comparison-all-in-one-review)

-----

## Concepts

### Building Blocks of Power BI 

* `datasets`
    * can be multiple datasets from multiple sources integrated into one, which can accept filtering, queries and etc.
    * Power BI built-in data connectors for connection to databases (e.g., Microsoft SQL Server Database, Azure/Oracle, etc)

* `reports`
    * collection of visualizations that appear together on one or more pages
    * can be created in desktop & online

* `dashboards` files: **.pbix**
    * quick overview of a collection of visuals
    * should be fit on a single page --> **canvas**, where you put the visuals

* `visualizations` also called visuals

* `tiles`
    * single visuals displayed on dashboards or reports
    * while creating the dashboard, you can customize the height, width, and position of the tiles

<br>

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

<br>

* [Create the new workspaces in Power BI](https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-create-the-new-workspaces)

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

<b>

also:
* [key influencers visualizations](https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-influencers#considerations-and-troubleshooting)

### Filtering

* Filtering only applies to reports, not to dashboards

* Filter pane contains filters that are added by the report designer

* Filter types:
    * *report*: applies to all report
    * *page*: applies to current page
    * *visual*: applies to a single visual of the report page
    * *drillthrough*: allows a more detailed exploration of a single visual

-------

## Import Data & Analysis

### Getting Data

You can get data from:

1. `Services` (apps from online services that you already use
    * e.g.: github, google analytics, dynamics 365

2. `Local Files`
    * e.g.: excel, csv files, power BI desktop

When improting data from excel: first make it a table before inserting it into power BI (excel sheet>insert>table) so that power BI can understand the headers and columns

<br>

3. `Databases`
    * connect to databases, e.g. Azure SQL Database, SQL Server Analysis Services, Spark




-------

# Miscellaneous

* [Create a template app in Power BI](https://docs.microsoft.com/en-us/power-bi/connect-data/service-template-apps-create)

* [AppSource](https://appsource.microsoft.com/en/marketplace/apps?product=power-bi-visuals)
------

## Sources

[1] [Main source: Microsoft Power BI](https://docs.microsoft.com/en-us/power-bi/)

[2] https://spreadsheeto.com/power-bi-desktop-vs-online/

[3] https://chartio.com/blog/dashboards-vs-reports-how-theyre-the-same-how-theyre-different/
# Business Intelligence (BI)

[Microsoft Power BI](#microsoft-power-bi)

------

Contents
=======================

* [Microsoft Power BI](#microsoft-power-bi)
* [Usage - Applications](#usage---applications)
* [Elements/Parts of Power BI](#elementsparts-of-power-bi)
* [Workflow](#workflow)
* [Documentation & Resources - Various Links](#documentation--resources---various-links)
    * [SharePoint](#sharepoint)
* [Concepts](#concepts)
    * [Building Blocks of Power BI ](#building-blocks-of-power-bi)
    * [Capacities](#capacities)
    * [Workspaces](#workspaces)
    * [Apps](#apps)
* [Import Data & Analysis](#import-data--analysis)
    * [Getting Data](#getting-data)
    * [Analysis](#analysis)
        * [Quick Insights](#quick-insights)
    * [Data Modeling](#data-modeling)
* [Data Visualization](#data-visualization)
    * [Types of visualizations](#types-of-visualizations)
    * [Filtering](#filtering)
    * [Visuals](#visuals)
* [Miscellaneous](#miscellaneous)
* [Sources](#sources)

----

# Microsoft Power BI

Power BI is designed for self-service business intelligence, it is built on Azure Microsoft's cloud computing infrastructure and platform, and it can be used for powerful analysis and visualization.

------

# Usage - Applications

Showcases:

* create/view reports and dashboards
    * (*report vs dashboard*: reports provide more pieces of information regarding the dashboard, i.e. reports include a more detailed collection of tables and charts, while dashboards are mostly used for monitoring what is going on and for a quick overview)
    * you can pin various reports onto one dashboard. Clicking upon a dashboard's visual will navigate you to the respective report where you might have created other reports/visuals as well

* use a Power BI phone app to monitor progress on a targeted variable

* view inventory and manufacturing progress in a real-time dashboard in the service

------

# Elements/Parts of Power BI

1) Power BI `Desktop`: Microsoft Windows desktop application, [download-install](https://docs.microsoft.com/en-us/power-bi/fundamentals/desktop-get-the-desktop#download-power-bi-desktop-directly). Mostly useful for modeling and creating Power BI reports.
    * It also includes a *Query Editor* which helps you transform data for visualizations
        * how to launch it: via Power BI Desktop > Transform Data, or navigator window > Power Query Editor
        * [Using Power Query in Power BI Desktop](https://docs.microsoft.com/en-us/power-query/power-query-ui)

2) Power BI `service`: **online** SaaS (Software as a Service), i.e. the cloud-based service. Mostly useful for sharing and collaboration
    * also for reporting and creating dashboards
    * set **data refresh times**, share data, and create customized apps

3) `Mobile apps`: available on phones and tablets

# Workflow

1) Fetch data to Power BI Desktop and create a report
2) Publish to Power BI SaaS (Power BI online), create new visualizations and/or build dashboards
3) Share dashboards with others and interact with shared dashboards
4) Power BI Mobile apps can be used for no3 workflow

# Documentation & Resources - Various Links

[Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)

[MS courses](https://docs.microsoft.com/en-us/learn/browse/)

* Various Links
    * [Types of insights supported by Power BI](https://docs.microsoft.com/en-us/power-bi/consumer/end-user-insight-types)

    * [Sharing Methods](https://radacad.com/power-bi-sharing-methods-comparison-all-in-one-review)

## Sharepoint

* [Integrate Power BI reports in SharePoint Online](https://powerbi.microsoft.com/en-us/blog/integrate-power-bi-reports-in-sharepoint-online/)
* [How To Connect Power BI To SharePoint Online List | Refresh Power BI Datasets using Power Automate](https://www.youtube.com/watch?v=1YmyN8OFDp0&ab_channel=LernenTech)
    * Power BI online: file > embed in SharePoint -> copy the link
    * paste the link onto sharepoint (pages > new site page > add a new web part > powerbi > paste the link from above)
        * at sharepoint, the report will be fully interactive

-----

# Concepts

## Building Blocks of Power BI 

* `datasets`
    * can be multiple datasets from multiple sources integrated into one, which can accept filtering, queries and etc.
    * Power BI built-in data connectors for connection to databases (e.g., Microsoft SQL Server Database, Azure/Oracle, etc)

* `reports` **.pbix**
    * collection of visualizations that appear together on one or more pages
    * can be created in desktop & online

* `dashboards` files: 
    * quick overview of a collection of visuals
    * should be fit on a single page --> **canvas**, where you put the visuals

* `visualizations` also called visuals

* `tiles`
    * single visuals displayed on dashboards or reports
    * while creating the dashboard, you can customize the height, width, and position of the tiles

<br>

Those are organized into **workspaces** and they are created on **capacities**

## Capacities

`Capacities`: set of resources used to host and deliver the Power BI content. They are either *shared* or *dedicated*
* **Dedicated**: capacity is fully committed to a single customer. It requires a <u>subscription</u>
* **Shared**: shared with other customers. By <u>default</u>, workspaces are created under this a shared capacity.

## Workspaces

Staging areas and containers for datasets, reports, dashboards, and dataflows.

There are two types:
1) `My workspace`: personal workspace for any Power BI customer to collaborate with your content. Only you have access to "my workspace".
2) `Workspaces`: they are used to collaborate and share content with colleagues. Requirement: workspace members need Power BI Pro licenses.

<br>

* [Create the new workspaces in Power BI](https://docs.microsoft.com/en-us/power-bi/collaborate-share/service-create-the-new-workspaces)

## Apps

* Collection of dashboards and reports to deliver *key metrics* to Power BI consumers

* Although apps are interactive, consumers (and colleagues who have access to those) cannot edit them. However they do not need Pro licenses to access the apps.

-----

# Import Data & Analysis

## Getting Data

You can get data from:

1. `Services` (apps from online services that you already use
    * e.g.: github, google analytics, dynamics 365

2. `Local Files`
    * e.g.: excel, csv files, power BI desktop, OneDrive, SharePoint - Team Sites

* you can sync by version controlling your files by using checkpoints    

* You can also setup `Scheduled Refresh` to automatically connect right to the data source and get updates (e.g. when using workbooks in .xlsx or .xlsm)
    * restrictions:  some features might be available only in later versions of Excel
    * file should be less than 1 GB
    * https://docs.microsoft.com/en-us/power-bi/connect-data/service-excel-workbook-files

* When improting data from excel: first make it a table before inserting it into power BI (excel sheet>insert>table) so that power BI can understand the headers and columns

<br>

3. `Databases`
    * connect to databases, e.g. Azure SQL Database, SQL Server Analysis Services, Spark, Access database

## Analysis

**Transform Data**:
* Use Query Editor to transform data
    * e.g. extract the day of the week from a set of dates using Power Query editor

**Clean Data**:
* Power Query Editor > Transpose data
* you can also change data types, and apply various transformations (transpose, put rows into headers, use "Fill" to replace null values, pivot/unpivot columns)

<br>

### Quick Insights

When uploading a dataset or creating a report, you can also get `quick insights` (right-click the **report** file and choose "quick insights")
* They are about applying various algorithms on the background which can potentially give various insights with regard to: category `outliers`, `correlations`, "`majority`" (prevalence of variable categories across features), and `trends`

Specifically:  

| | Insight          | Description    | 
| ------------- |-------------|-----------------|
|1| `Category outliers (top/bottom)`      | Highlights cases where one or two categories have much larger values than other categories|             
|2|`Change points in a time series`| Significant changes in trends in a time series of data|
|3|`Correlation`| Patter or trend detection of a measurement against a category or value|
|4|`Low Variance`| It detects cases where data points for a dimension aren't far from the mean, i.e. when the variance is low|
|5|`Majority (Major factors)`|It finds cases where a majority of a total value can be attributed to a single factor when broken down by another dimension|
|6|`Outliers`| Clustering model to find outliers in non-time series data|
|7|`Overall trends in time series`|Detects upward or downward trends in time series data|
|8|`Seasonality in time series`|Finds periodic patterns in time series data, such as weekly, monthly, or yearly seasonality|
|9|`Steady share`|Highlights cases where there is a parent-child correlation between the share of a child value in relation to the overall value of the parent across a continuous variable|
|10|`Time series outliers`|Detects when there are specific dates or times with values significantly different than the other date/time values|

<b>

[Types of insights supported by Power BI](https://docs.microsoft.com/en-us/power-bi/consumer/end-user-insight-types)

[Apply insights in Power BI Desktop to explain fluctuations in visuals](https://docs.microsoft.com/en-us/power-bi/create-reports/desktop-insights)

## Data Modeling

* create `relationships` to create a logical connection between different data sources

* Create a new field with `calculated columns` to establish a relationship between tables when no unique fields exist
    * combine data using *"new column"*, use *DAX* (Data Analysis Expressions) language to apply a desired function, e.g. newColumn = data[column1] & ", " & data[column2] will give a combination of the respective data, seperated by commas
    * the column which contains the combined data can then be used as a unique key to establish a relationship between the two tables
    
* Create `measures` to perform calculations on data
    * basically, they are similar to *calculated columns*, but here you apply functions and expressions to introduce new columns based on those <u>calculations</u>
    * Modeling > New Measure (Measure = "")

* Create `calculated table` to create a relationship between two tables
    * function within DAX: create data that you want them stored as part of the model rather than as part of a query
    * Modeling > New Table --> NewTable = ()

<b>

* use `Model View` in Power BI Desktop to set the relationship between tables or elements
    * Home tab > `"Manage Relationships"`: create an *Entity Relationship Diagram* (ERD)
        * **Cardinality** (1:1, 1:M, M:1, M:M), **Cross filter direction**: single or both, i.e. if you want to filter from both sides (both) or not (single)

    * [Create and manage relationships in Power BI Desktop](https://docs.microsoft.com/en-us/power-bi/transform-model/desktop-create-and-manage-relationships)
    * [Bi-directional relationship guidance](https://docs.microsoft.com/en-us/power-bi/guidance/relationships-bidirectional-filtering)

------

# Data Visualization

Power BI Desktop > Report view:

1) **Ribbon**: tasks with respect to reports and visualizations

2) **Report view - Canvas**: visualizations
* *Data view*: view data of report, check data types and validate data
* *Model view*: set the relationship between tables or elements in order to run queries for related data across multiple tables

3) **Pages tab**: bottom of the page. Select or add a report page

4) **Visualizations pane**: Interact with visualizations, customize colours or axes, apply filters, drag fields, and etc.

5) **Fields pane**: Query elements and filters can be dragged onto the Report view or dragged to the Filters area of the Visualizations pane

<br>

## Types of visualizations

* Area charts
* Bar and column charts
* Pie charts
    * donut charts
    * gauge charts
* KPIs
* Line charts
* Maps
    * bubble map: it places a bubble over a geographic point
    * shape map: it shows the outline of the area that you want to visualize
* Q&A viual
* Tabless
* Treemaps
* Waterfall charts

## Filtering

* Filtering only applies to reports, not to dashboards

* Filter pane contains filters that are added by the report designer

* Filter types:
    * *report*: applies to all report
    * *page*: applies to current page
    * *visual*: applies to a single visual of the report page
    * *drillthrough*: allows a more detailed exploration of a single visual

## Visuals

* [key influencers visualizations](https://docs.microsoft.com/en-us/power-bi/visuals/power-bi-visualization-influencers#considerations-and-troubleshooting)

**Compare 2 different measures**:
* scatter, waterfall, and funnel charts

    * `scatter plots`: "*play axis*": create animations based on the variable entered at play axis, e.g. animation based on time/date

    * `waterfalls`: show changes in a specific value over time
        * Category and y Axis. Drag a time-based field, such as month/day, to the "category" bucket, and drag the value that you want to track to the y axis bucket. Time periods where an increase in value occurred are displayed in green by default, while periods with a decrease in value are displayed in red

    * `Funnel charts`: typically used to show changes over a specific process or segment, such as a sales pipeline or website retention rate monitoring

-------


# Miscellaneous

* [Create a template app in Power BI](https://docs.microsoft.com/en-us/power-bi/connect-data/service-template-apps-create)

* [AppSource](https://appsource.microsoft.com/en/marketplace/apps?product=power-bi-visuals)
------

# Sources

[1] [Main source: Microsoft Power BI](https://docs.microsoft.com/en-us/power-bi/)

[2] https://spreadsheeto.com/power-bi-desktop-vs-online/

[3] https://chartio.com/blog/dashboards-vs-reports-how-theyre-the-same-how-theyre-different/
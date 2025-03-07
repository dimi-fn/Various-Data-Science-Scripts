# Data Engineering


Contents
========================
* [Data Engineering Foundations](#data-engineering-foundations)
* [Partitioning & Clustering](#partitioning--clustering)
* [Best Practises](#best-practices)
   * [Data Pipelines](#data-pipelines)
      * [Best Practices for Data Retention and Storage in ETL Platforms](#best-practices-for-data-retention-and-storage-in-etl-platforms)
      * [Future-Proof Your Data Pipelines](#future-proof-your-data-pipelines)      
      * [Best Practices for Optimizing Data Processing Jobs](#best-practices-for-optimizing-data-processing-jobs)
      * [Best Practices for Scalable Data Pipelines](#best-practices-for-scalable-data-pipelines)
      * [Best Practices for API Calls](#best-practices-for-api-calls)
   * [Code](#best-practices-in-general-code)
* [Data Lakehouse Architecture](#data-lakehouse-architecture)
* [Shuffling in ETL and Distributed Systems](#shuffling-in-etl-and-distributed-systems)
* [Joins](#joins)
* [Data Modeling](#data-modeling)
* [Evaluation of Data Observability Tools](#evaluation-of-data-observability-tools)
* [The 3Vs in Big Data](#the-3vs-in-big-data)

------------------------------------------------------------------------------------------------------------------

# Data Engineering Foundations

* `Segmentation of Tools`
1) `Storage`: **databases**
   * SQL vs. NoSQL
2) `Processing Frameworks`
   * For data cleaning, aggregation, clustering, batch and stream processing
      * Spark, Hive, Flink and Kafka
3) `Automation`: **Scheduling**
   * In order to set up and manage workflows
   * Plan jobs with specific intervals
   * Resolve dependency requirements of jobs
      * Scheduling: Airflow (Apache Airflow), Oozie, Luigi

<br>

* `Data`
   * **Structured data**
      * relational databases
   * **Semi-structured data**
      * e.g. JSON files of the format {"key":"value"}
   * **Unstructured data**
      * Video, images, text files

-------------------------------------------------------------------

# Partitioning & Clustering

## Partitioning
Partitioning divides a large table into smaller, more manageable segments (partitions) based on a specific column, such as date, region, or category. Queries can then scan only the relevant partitions instead of the entire table, improving performance and reducing costs.

<br>

`Types of Partitioning`:
* Time-based partitioning (ingestion time partitioning; based on when a particular record was added to the table) (e.g., created_at or event_date)
* Integer-range partitioning (e.g., customer_id in ranges like 1-1000, 1001-2000)
* Column-based partitioning (e.g., country_code)
* Manually-defined partitions (static partitioning based on business logic)


```
CREATE TABLE sales_data  
PARTITION BY DATE(order_date)  
AS SELECT * FROM raw_sales
```

* **Benefits**:
   * Faster queries (only scans relevant partitions)
   * Reduced storage and cost (querying fewer rows)
   * Efficient data pruning

## Clustering
Clustering organizes data within each partition by sorting it based on one or more columns. This helps optimize queries that filter or group by those columns, reducing scan times even further (the clustering field value can also be of text data type, which is not allowed in partitioning).

**Example Use Case**:
A sales table partitioned by order_date can be clustered by customer_id, product_category to speed up customer- or product-specific queries.

**Example in BigQuery**:

```
CREATE TABLE sales_data  
PARTITION BY DATE(order_date)  
CLUSTER BY customer_id, product_category  
AS SELECT * FROM raw_sales;
```

* **Benefits**:
   * Speeds up filtering and grouping queries
   * Improves compression and storage efficiency
   * Works well when query patterns involve multiple columns
      * However, the benefits may become apparent only when the table or partition is > 1GB

-------------------------------------------------------------------

# Best Practices 
## Data Pipelines

1. **Modular Design**
   - **Summary:** Break down the pipeline into small, reusable, and independent components.
   - **Benefit:** Easier maintenance, testing, and debugging.

2. **Data Validation**
   - **Summary:** Implement checks to ensure data quality at each stage.
   - **Benefit:** Prevents errors and ensures reliability and accuracy of data.

3. **Scalability**
   - **Summary:** Design the pipeline to handle increasing volumes of data efficiently. (eg by configurating cluster pools in ETL)
   - **Benefit:** Future-proofs the pipeline and avoids performance bottlenecks.

4. **Error Handling and Logging**
   - **Summary:** Incorporate robust error handling and comprehensive logging.
   - **Benefit:** Facilitates troubleshooting and improves the reliability of the pipeline.

5. **Version Control**
   - **Summary:** Use version control systems for code and configuration management.
   - **Benefit:** Tracks changes, facilitates collaboration, and allows rollback to previous versions if needed.

6. **Documentation**
   - **Summary:** Maintain clear and comprehensive documentation for the pipeline.
   - **Benefit:** Enhances understanding and onboarding, and aids in maintenance and troubleshooting.

7. **Security**
   - **Summary:** Implement appropriate security measures, such as encryption and access controls.
   - **Benefit:** Protects sensitive data and ensures compliance with regulations.

8. **Monitoring and Alerts**
   - **Summary:** Set up monitoring and alerting mechanisms to track the pipeline's performance and health.
   - **Benefit:** Enables proactive maintenance and quick resolution of issues.

### Best Practices for Data Retention and Storage in ETL Platforms

Efficient data retention and storage strategies are vital for ETL pipelines to ensure data is handled securely, cost-effectively, and in compliance with regulatory requirements. Below are key considerations and best practices:

A. `Data Retention`:
Data retention refers to how long data is stored before being archived or deleted, based on business, legal, or regulatory requirements.

**Best Practices**:

* **Define Clear Retention Policies**:
   * Retain data only as long as necessary. Set specific timeframes for retaining data, such as 3 months, 6 months, or a year, depending on business or regulatory needs.
   * Classify data (e.g., raw data, processed data, reporting data) and assign different retention rules based on its importance.
* **Automated Data Purging**:
   * Implement automated deletion or archiving jobs that run regularly to remove or move older data. For example, you can create cron jobs or use cloud lifecycle management policies (such as in S3 or Google Cloud Storage) to manage data retention automatically.
* **Cold and Hot Data Segregation**:
   * Hot data: Frequently accessed or recent data that needs to be kept readily available.
   * Cold data: Older data that is rarely accessed but still needs to be retained for compliance or historical purposes.
   * Use low-cost storage for cold data (e.g., Glacier in AWS, or Archive Storage in GCP), while keeping hot data in fast access storage (e.g., SSDs, in-memory storage).
* **Compliance and Audit Trails**:
   * Ensure retention policies comply with legal frameworks such as GDPR, HIPAA, or industry-specific standards.
   * Keep proper audit trails of when data was ingested, processed, and deleted.

B. `Data Storage`:
Efficient storage strategies ensure that the ETL pipeline runs cost-effectively, and that data is easy to access and scalable.

**Best Practices**:
* **Partitioning**:
   * Organize and partition data by time (e.g., day, month, year), customer, or region. This speeds up access to relevant data in ETL processes and reduces costs by avoiding unnecessary scans of large datasets.
   In platforms like Hadoop or Spark, partitioning can also improve query performance by reducing the amount of data shuffled and read.
* **Compression**:
   * Use compression formats such as Parquet, Avro, or ORC for large datasets. These formats not only reduce storage costs but also optimize data processing performance by reading only the necessary parts of the data.
   * Ensure that compression codecs used are compatible with the ETL framework for efficient reading (e.g., Snappy with Spark).
* **Data Versioning**
   * Maintain version control of data, especially in raw and transformed datasets. This helps in debugging ETL pipelines and provides the ability to reproduce historical results.
   * For versioning, tools like Delta Lake (on Databricks), Apache Hudi, or Apache Iceberg can manage large-scale data lakes with versioned data.
* **Data Lake or Data Warehouse**:
   * Choose an appropriate storage type based on the ETL needs:
      * Data Lake: Suitable for unstructured or semi-structured data. Use it to store raw, large-scale datasets.
      * Data Warehouse: Use structured formats for querying and reporting. Suitable for processed data.
   * Modern architectures (e.g., lakehouse) combine the flexibility of a data lake with the structured querying capabilities of a data warehouse.
* **Metadata Management**:
   * Store metadata about datasets (e.g., schema information, partitioning, lineage) to track how data is processed across the pipeline. Use tools like Apache Atlas or AWS Glue Data Catalog for managing metadata.
   * Metadata improves traceability and helps organize large-scale datasets across the ETL pipeline.
* **Monitoring and Alerts**:
   * Implement storage usage monitoring and set up alerts for cost thresholds or retention breaches.
   * Use cloud provider services like AWS Cost Explorer or Google Cloud Monitoring to keep an eye on storage costs and optimize accordingly.

C. `Data Security and Governance:`
* **Data Encryption**:
   * Encrypt sensitive data at rest and in transit to ensure that it remains secure. Use tools like AWS KMS or Google Cloud’s encryption services.
* **Access Control**:
   * Implement role-based access control (RBAC) and enforce data access policies to prevent unauthorized access.
   * Regularly audit permissions and access logs for compliance.
* **Data Masking and Anonymization**:
   * If you're handling personally identifiable information (PII), apply anonymization or masking techniques to protect sensitive data.
   * This is especially important when sharing or retaining data for reporting or analytics purposes while complying with regulations like GDPR.

### Future-Proof Your Data Pipelines
* [How To Future-Proof Your Data Pipelines](https://www.ascend.io/blog/how-to-future-proof-your-data-pipelines/)   

### Best Practices for Optimizing Data Processing Jobs
* `Partitioning`: Break large datasets into smaller chunks for parallel processing.
* `Efficient File Formats`: Use optimized formats like Parquet or ORC for faster read/write operations.
* `Indexing`: Create indexes on frequently queried columns.
* `Push Down Filters`: Apply filters at the source to reduce data transfer.
* `Caching`: Cache intermediate results to avoid redundant computations.
* `Resource Allocation`: Right-size cluster resources (CPU, memory) for job needs.
* `Code Optimization`: Minimize joins, shuffles, and unnecessary computations.
* `Monitoring`: Use tools like Spark UI or Datadog to track and optimize performance bottlenecks.
* `Compression`: Compress data to reduce storage and transfer costs.
* `Incremental Processing`: Process only new or updated data.

### Best Practices for Scalable Data Pipelines
Scalability in data pipelines is essential to handle increasing data volumes, velocity, and complexity effectively. Below are best practices to ensure scalable and robust data pipelines:

1. `Design for Modularity`
* Break pipelines into smaller tasks: Use modular components for ingestion, transformation, and storage, which can be scaled independently.
* Reusable components: Create generic and reusable functions or templates for common tasks, such as data validation or transformation.

2. `Use Distributed Processing Frameworks`
* Leverage distributed processing tools like Apache Spark, Apache Flink, or Google Dataflow to process large data volumes in parallel.
* Opt for batch or streaming processing based on workload and latency requirements.

3. `Optimize Data Storage`
* Choose scalable storage solutions like cloud object stores (e.g., S3, GCS, Azure Blob Storage) or distributed databases (e.g., Snowflake, BigQuery, Redshift).
* Use efficient data formats like Parquet or Avro to reduce storage costs and speed up processing.

4. `Leverage Cloud-native Tools`
* Use managed services (e.g., AWS Glue, Google Cloud Dataflow, Azure Data Factory) that automatically scale with demand.
* Embrace serverless computing where applicable to handle variable workloads.

5. `Build for Fault Tolerance`
Idempotency: Ensure pipelines can handle retries without causing duplication or corruption.
Implement checkpointing and job recovery mechanisms to resume processing from failure points.
Use monitoring tools to detect and respond to failures quickly.

6. `Adopt Parallelism and Partitioning`
* Partition large datasets by keys (e.g., time, region) to allow parallel processing.
* Use sharding or dynamic scaling for write-heavy or read-heavy systems.

7. `Prioritize Scalability in Transformations`
* Push computation to the database or distributed system where possible.
* Avoid using single-threaded or resource-intensive transformations.

8. `Optimize Resource Management`
* Use autoscaling clusters to scale up or down based on workload.
* Allocate resources dynamically to different pipeline stages based on priority and workload size.

9. `Monitor and Benchmark`
* Use monitoring tools (e.g., Datadog, Prometheus, CloudWatch) to track resource utilization, latency, and throughput.
* Benchmark your pipeline under expected peak loads and optimize bottlenecks.

10. Automate Pipeline Orchestration
* Use orchestration tools (e.g., Apache Airflow, Prefect, Dagster) to manage dependencies and schedule jobs efficiently.
* Implement event-driven triggers for real-time or near-real-time pipelines.

11. Decouple Components
* Use message brokers (e.g., Kafka, RabbitMQ, Pub/Sub) to decouple producers and consumers.
* This approach enables independent scaling of ingestion and processing systems.

12. `Use Infrastructure as Code (IaC)`
* Manage infrastructure using tools like Terraform or CloudFormation to ensure consistency and scalability.
* Automate pipeline deployment and scaling using CI/CD pipelines.

13. `Enforce Data Quality at Scale`
* Implement automated data validation and anomaly detection.
* Use tools like Great Expectations or dbt tests to ensure consistent data quality.

14. `Archive and Purge Old Data`
* Periodically archive or delete unused data to reduce storage costs and improve performance.
* Use tiered storage for cold data (e.g., Glacier, Nearline Storage).

15. `Optimize Query and Indexing`
* For query-heavy pipelines, optimize indexing in relational databases and distributed warehouses.
* Leverage materialized views or pre-aggregated data for frequent queries.

16. `Security and Compliance`
* Implement scalable access control policies using roles and permissions.
* Ensure pipelines comply with data regulations (e.g., GDPR, HIPAA).

## Best Practices for API Calls
`When parsing data from an API, here are some high-level best practices to ensure efficiency, maintainability, and reliability:`
1. `Understand the API Documentation`
Review the API documentation to understand the available endpoints, request/response formats, authentication methods, rate limits, and error handling guidelines.
2. `Use Robust Error Handling`
Handle different HTTP response codes (e.g., 200 OK, 404 Not Found, 500 Internal Server Error).
Implement retries for transient errors (e.g., timeouts or server unavailability).
Ensure graceful error handling for malformed or unexpected API responses.
3. `Implement Pagination and Rate Limiting`
Many APIs return data in pages, so make sure to handle pagination properly (e.g., using page or offset parameters).
Be mindful of API rate limits to avoid hitting throttling or bans. Implement backoff strategies (e.g., exponential backoff) when necessary.
4. `Use Caching for Repeated Requests`
Cache the API responses where appropriate to avoid unnecessary repeated requests. This can improve performance and reduce load on the API.
Use cache expiration strategies to ensure the data stays fresh (e.g., ETags, Last-Modified).
5. Parse Responses Efficiently
Ensure that the API responses are parsed in a memory-efficient way, especially when dealing with large datasets (e.g., using streaming parsing instead of loading the entire response into memory).
Validate the response structure to ensure it matches expected formats, and handle any discrepancies gracefully.
6. Be Mindful of `Security`
Secure API keys and authentication credentials (e.g., use `environment variables` or a secrets manager, not hard-code them).
Use HTTPS for encrypted communication and avoid sending sensitive information in URLs (e.g., API keys or passwords).
7. Rate-Limited or Batch Requests
If an API allows batch processing (e.g., sending multiple requests in a single call), use it to reduce the number of requests and optimize performance.
9. Respect API Terms of Service
Always respect the API's terms of service regarding usage, rate limits, data usage, and any other restrictions to avoid penalties.
10. Monitoring and Logging
Implement proper logging and monitoring to track API usage, errors, and performance. This helps in debugging and identifying potential issues early.
By adhering to these best practices, you can ensure that your API parsing is efficient, secure, and maintainable, even as the data or complexity scales.

## Best Practices in General Code

1. **Clean Code**
   - **Summary:** Write clear, readable, and maintainable code using meaningful variable names and consistent formatting.
   - **Benefit:** Improves readability and ease of maintenance.

2. **DRY Principle (Don’t Repeat Yourself)**
   - **Summary:** Avoid code duplication by abstracting repetitive logic into functions or modules.
   - **Benefit:** Reduces redundancy and potential for errors, and simplifies updates.

3. **Unit Testing**
   - **Summary:** Write tests for individual components to ensure they work as expected.
   - **Benefit:** Detects issues early and facilitates reliable refactoring.

4. **Code Reviews**
   - **Summary:** Conduct regular peer reviews of the codebase.
   - **Benefit:** Ensures code quality, catches bugs, and encourages knowledge sharing.

5. **Performance Optimization**
   - **Summary:** Write efficient code and optimize performance-critical sections.
   - **Benefit:** Enhances the speed and efficiency of applications.

6. **Modularity**
   - **Summary:** Organize code into modules with clear interfaces and responsibilities.
   - **Benefit:** Promotes reusability and simplifies understanding and maintenance.

7. **Refactoring**
   - **Summary:** Regularly improve the structure of existing code without changing its behavior.
   - **Benefit:** Keeps the codebase clean and adaptable to new requirements.

8. **Documentation**
   - **Summary:** Document the codebase, including usage instructions and design decisions.
   - **Benefit:** Assists in understanding, maintaining, and extending the code.


-----------------------------------------------------------------------


# Data Lakehouse Architecture

* `Bronze, Silver, and Gold Layers`
   * Bronze Layer: 
      * **Description**: Raw, unprocessed data directly ingested from various sources.
      * **Purpose**: Stores data in its native form to ensure traceability and provide a complete history.
   * Silver Layer:
      * **Description**: Cleaned and transformed data that has undergone standardization and enrichment.
      * **Purpose**: Provides more refined datasets that are ready for analysis or further processing.
   * Gold Layer:
      * **Description**: Fully processed, aggregated, and business-ready data.
      * **Purpose**: Used for final reporting, dashboards, and high-level business analytics.

<br>

* `Medallion Architecture`
   * **Description**: A layered approach similar to the Bronze, Silver, and Gold layers, but more flexible in how layers are defined and processed.
   * **Purpose**: Allows for more customized intermediate steps, with each layer serving a specific purpose in the data processing pipeline. This architecture can be adapted to the specific needs of the organization and the complexity of its data workflows.

<br>   

* `Delta Lake`
   * **Description**: An open-source storage layer that brings ACID (Atomicity, Consistency, Isolation, Durability) transactions to data lakes. It allows for scalable, reliable, and high-performance data pipelines.
   * **Purpose**: Provides structured streaming and batch processing with data versioning, ensuring consistency and reliability in data pipelines.

<br>

* `Unified Batch and Streaming (Lambda or Kappa within Lakehouse)`
   * **Description**: Integrates both batch and real-time data processing into the Lakehouse, either by maintaining separate layers (Lambda) or processing everything as a stream (Kappa).
   * **Purpose**: Supports use cases where real-time data processing and historical data analysis are both required. This design helps organizations handle both low-latency needs and comprehensive historical analytics within a single architecture.

<br>

* `Delta Engine`
   * **Description**: An optimized query engine built on top of Delta Lake, designed to deliver high performance for complex analytics and machine learning workloads.
   * **Purpose**: Enhances the performance of the Lakehouse architecture, making it suitable for large-scale data analytics and AI/ML tasks.

<br>   

* `Lakehouse Metadata Layer`
   * **Description**: Centralized management of metadata to ensure governance, data quality, and easy data discovery. It often integrates with cataloging systems like Apache Hive or AWS Glue.
   * **Purpose**: Enables better data management, ensuring that data is consistently described, discoverable, and secure across the Lakehouse.

<br>

* `Data Mesh within Lakehouse`
   * **Description**: Decentralized data management architecture where different teams own and manage their data products within a shared Lakehouse environment.
   * **Purpose**: Promotes scalability and flexibility by allowing domain teams to control their data while still benefiting from centralized infrastructure and governance provided by the Lakehouse.

<br>   

* `Time Travel`
   * **Description**: A feature provided by Delta Lake that allows users to query previous versions of data. It facilitates auditing, debugging, and data recovery.
   * **Purpose**: Supports the analysis of historical data states, improving transparency and allowing for rollback if errors occur.

-----------------------------------------------------------------------

# Joins
`Bucket Joining` and `Broadcast Join` are both strategies used in distributed computing frameworks (like Spark) to optimize the performance of joins. They differ from typical SQL-style joins (like left join, inner join, etc.) in terms of how the join is executed rather than the join logic itself.

<br>

Bucket Joining and Broadcast Join are both strategies used in distributed computing frameworks (like Spark) to optimize the performance of joins. They differ from typical SQL-style joins (like left join, inner join, etc.) in terms of how the join is executed rather than the join logic itself.

1. `Bucket Join (Bucketed Join)`
Concept: A bucket join is used when tables are pre-partitioned or bucketed on the join key. Each bucket contains a subset of data corresponding to specific hash values of the join key.
How it works: When tables are bucketed on the join key and have the same number of buckets, each worker can handle only a small subset of the data (corresponding to a bucket), making the join more efficient since it doesn’t need to shuffle large amounts of data across the network.
Benefit: This reduces the amount of data shuffling, which improves the performance of the join operation, especially with large datasets.
Use Case: Works best when both tables are large and are partitioned based on the same key.
2. `Broadcast Join`
Concept: In a broadcast join, the smaller dataset is broadcast (i.e., copied) to all nodes/workers in the cluster, so each node can perform the join operation locally without the need to shuffle the smaller dataset.
How it works: One of the tables is small enough to fit into the memory of the worker nodes, so the smaller table is sent to every worker node, and the join is performed locally.
Benefit: This is much faster for joins involving a large table and a small table, as it avoids the need to shuffle data.
Use Case: Works well when one table is much smaller than the other.
3. `SQL-style Joins (e.g., Left Join, Inner Join, Right Join)`
Concept: These are logical join operations that define how data from two tables should be combined:
Left Join: Returns all rows from the left table, and the matched rows from the right table. If there's no match, NULL values are returned from the right table.
Inner Join: Returns only the rows that have matching values in both tables.
Right Join: Returns all rows from the right table and the matched rows from the left table.
How it works: These joins are based on the values in specified columns and don’t specify how the join should be performed by the underlying system.
Benefit: These joins are flexible and used to express how you want to combine data logically. However, performance can vary depending on the size of the datasets and the join algorithm chosen by the query engine.
Key Differences:
Execution Strategy vs. Logical Operation:

Bucket and Broadcast joins are execution strategies used to optimize performance when joining large datasets in distributed systems.
Left Join, Inner Join, etc., are logical SQL operations that define how two tables should be combined based on conditions.
Data Shuffling:

Bucket Join minimizes shuffling by partitioning data in advance.
Broadcast Join avoids shuffling by sending a small dataset to every worker node.
SQL-style joins often involve shuffling data across nodes if the data isn't partitioned or broadcasted appropriately.
Use Cases:

Use Bucket Join for joining two large bucketed datasets.
Use Broadcast Join for joining a large dataset with a small one.
Use SQL-style joins when defining the relationship between the tables logically.
In summary, Bucket Join and Broadcast Join are performance optimization strategies used in distributed systems, while Left Join, Inner Join, etc., are ways to specify how tables should be combined based on data relationships.

-----------------------------------------------------------------------

# Shuffling in ETL and Distributed Systems

`Shuffling` is the process of redistributing or exchanging data across nodes in a distributed system to group data by a certain key or ensure that the necessary data for a computation (such as a join, sort, or aggregation) is present on the same node. It's a key aspect of distributed computing frameworks like Apache Spark, Hadoop, and other ETL platforms, but it’s also an expensive operation because of the following reasons:

Data Movement: Data is transferred across the network between nodes.
Disk and Memory Usage: Intermediate data often needs to be written to disk or cached in memory during shuffling, consuming resources.
Latency: The time required to perform shuffling can significantly slow down the ETL process.
Example of Shuffling:
In a join operation, if two tables are distributed across different nodes, shuffling ensures that all records with the same join key are brought to the same node so the join can be executed correctly.
Minimizing Shuffling:
To improve the performance of ETL jobs, reducing shuffling is crucial. Here are some best practices:

Partitioning/Clustering: Pre-partition your data on commonly used join or group-by keys. This avoids the need for shuffling by ensuring that data for a particular key is already colocated.
Broadcast Joins: For joins involving large and small datasets, use broadcast joins to avoid shuffling large amounts of data.
Caching and Reuse: Cache frequently accessed intermediate results to avoid repeating shuffling operations across different stages of an ETL job.
Avoid Wide Transformations: Wide transformations (like groupByKey) require shuffling of data between nodes. Use more efficient operations like reduceByKey, which minimizes data movement.

-----------------------------------------------------------------------

# Data Modeling
Data modeling in the context of data engineering is the process of designing the structure and organization of data to ensure it’s stored, retrieved, and processed efficiently. It’s essential for ETL (Extract, Transform, Load) platforms, where data is moved from source systems to data warehouses or data lakes.

Key components include:

* `Conceptual, Logical, and Physical Models`: Conceptual models define high-level relationships between entities, logical models outline the detailed structure (tables, columns, relationships), and physical models map this to actual database structures.
* `Schema Design`: Involves structuring the data into schemas like Star or Snowflake for analytical workloads, optimizing for query performance.
* `Normalization/Denormalization`: Normalization reduces redundancy in relational databases, while denormalization is often used in ETL processes to optimize performance for read-heavy analytical tasks.
* `Data Types and Constraints`: Careful selection of data types and enforcing constraints (e.g., primary keys, foreign keys) ensures data integrity and reduces storage costs.
* `Handling Slowly Changing Dimensions (SCD)`: Used in ETL pipelines to track historical data changes in dimensions (e.g., customer data).
* `Data Partitioning and Indexing`: Critical for large-scale ETL systems, partitioning data (by time, region, etc.) and indexing speeds up query performance in warehouses like BigQuery or Redshift.
* `Data Lake vs. Data Warehouse Modeling`: Data lakes often store raw, unstructured data in various formats (e.g., Parquet), while data warehouses are optimized for structured data and faster queries.
* Data modeling is crucial for ensuring scalability, maintainability, and efficient querying in ETL pipelines, enabling businesses to derive insights from their data effectively.

-----------------------------------------------------------------------

# Evaluation of Data Observability Tools
* [Evaluating Data Observability Tools: A Comprehensive Guide](https://www.dataengineeringweekly.com/p/evaluating-data-observability-tools?publication_id=73271&post_id=149037505&isFreemail=true&r=i0gax&triedRedirect=true&utm_source=substack&utm_medium=email)

-----------------------------------------------------------------------

# The 3Vs in Big Data

| Aspect |  Description | Example | Key Challenge |
|-----------|------------|----------------------|------|
| `Volume`  | The scale of data (amount) | Terabytes of web logs, petabytes of videos| Storing and processing large datasets|
| `Velocity`  | The speed of data flow and processing  | Real-time IoT sensor data, stock transactions | Processing and analyzing data in real-time |
| `Variety`  | The diversity of data formats and types  | JSON logs, images, relational tables | Integrating, analyzing, and storing diverse data |

# DE_Fundamentals_ETL_Pipeline

This project demonstrates a fundamental ETL (Extract, Transform, Load) pipeline implemented entirely in Python, designed to process Medicare yearly enrollment and beneficiary data. It provides a hands-on example of how to extract, clean, and store data in a structured format for further analysis.

Pipeline Overview
Extraction:

The pipeline connects to a public API to retrieve Medicare enrollment and beneficiary data.
The extracted data is retrieved in a raw format, which is prepared for transformation.
Transformation:

The raw data is cleaned and filtered to focus on specific fields and columns relevant to the analysis.
Irrelevant or redundant data is removed, ensuring the dataset is concise and meaningful.
This step ensures the data adheres to a standardized structure suitable for loading into a database.
Loading:

The transformed data is loaded into a SQLite database, a lightweight and efficient database system.
The database provides a structured and queryable format, enabling further exploration and analysis.
Key Features
Single-Script Implementation:
The entire pipeline is built within a single Python script, showcasing simplicity and modularity.

Data Engineering Fundamentals:
This project highlights foundational data engineering concepts, including API interaction, data transformation, and database integration.

SQLite Integration:
The choice of SQLite ensures ease of use, portability, and compatibility, making it ideal for small-to-medium datasets.

Use Case
This ETL pipeline serves as a practical example for anyone looking to understand data engineering workflows. It is particularly suited for those working with healthcare data or similar structured datasets.

Feel free to explore the script, customize it for your needs, or extend its functionality to incorporate additional data sources or transformations. This project provides a solid foundation for building more complex ETL pipelines in Python.

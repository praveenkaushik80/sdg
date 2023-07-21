# Description: Synthetic Data Generator(sdg)

The Synthetic Data Generator is a web application developed using Streamlit, designed to facilitate the generation of synthetic data based on a Bayesian Network. The application allows users to upload a sample data CSV file, and through the power of Bayesian modeling, it generates new synthetic data that shares statistical similarities with the original dataset. This tool is particularly useful for researchers, data scientists, and machine learning practitioners who require larger datasets for testing statistical models or training machine learning algorithms without compromising sensitive or real-world data.

# Key Features:

# Data Upload and Visualization:
The application allows users to upload a CSV file containing the sample data they wish to analyze and generate synthetic data from. Once the data is uploaded, the initial rows of the sample dataset are displayed, providing users with a quick overview of the data.

# Missing Value Analysis:
For a thorough data assessment, the application includes a checkbox that allows users to view missing values in the uploaded sample data. This feature helps identify any missing data points and ensures data integrity during the generation of synthetic data.

# Synthetic Data Generation:
The core functionality of the project lies in generating synthetic data. Using Bayesian Networks, the application analyzes the structure of the uploaded data and estimates Conditional Probability Distributions (CPDs) through Maximum Likelihood Estimation. The Bayesian Network is then used to generate synthetic data points based on the statistical patterns observed in the original dataset.

# Descriptive Statistics Comparison:
To validate the effectiveness of the synthetic data generation, the application provides a side-by-side comparison of descriptive statistics between the original data and the generated synthetic data. This comparison helps users assess the similarity of statistical characteristics, such as mean, standard deviation, and quartiles, ensuring the generated data closely reflects the properties of the original dataset.

# Download of Synthetic Data:
Once the synthetic data is generated and its statistics are compared, users have the option to download the generated synthetic data as a CSV file. This feature allows users to use the synthetic data for further analysis, model testing, or machine learning tasks.

Overall, the Synthetic Data Generator project empowers users to confidently work with large datasets without privacy concerns, as it generates synthetic data that accurately preserves the statistical properties of the original dataset. By leveraging the Bayesian modeling approach, the application provides a reliable and privacy-preserving solution for researchers and data professionals seeking to enhance their data analysis and model-building capabilities.

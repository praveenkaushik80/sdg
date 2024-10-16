import streamlit as st
import pandas as pd
import base64
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.sampling import BayesianModelSampling

def generate_samples_bayesian(df, n):
    try:
        # Define the Bayesian network structure
        model = BayesianNetwork()
        for col in df.columns:
            model.add_node(col)

        # Estimate the CPDs from the data using Maximum Likelihood Estimation
        estimator = MaximumLikelihoodEstimator(model, df)
        cpds = estimator.get_parameters()

        # Add the CPDs to the model
        for cpd in cpds:
            model.add_cpds(cpd)

        # Check if the model is valid
        model.check_model()

        # Sample from the Bayesian network
        sampler = BayesianModelSampling(model)
        samples = sampler.forward_sample(size=n, seed=42)

        # Convert the generated samples to a Pandas DataFrame
        generated_data = pd.DataFrame(samples)

        return generated_data
    
    except Exception as e:
        st.error("Error occurred: " + str(e))

# Streamlit app code
st.sidebar.write()
st.sidebar.write("Synthetic data refers to information that is artificially generated, rather than coming \
                 from real-world events. It is commonly used to validate mathematical models and train machine\
                  learning models. Synthetic data is often created using algorithms and can be generated by \
                 computer simulations. It is used in various fields as a substitute for sensitive data that \
                 cannot be released to the public. This allows researchers to analyze and work with data\
                  without compromising privacy or confidentiality.")
st.title('Synthetic Data Generator')
st.write()
st.write('The data generator tool takes a sample data DataFrame as input and generates new data based on the statistics\
          of the original data. Users can specify how many rows of data they want to generate and the tool \
         compares the statistics of the generated data with the original data to ensure similarity. This tool is\
          useful for creating larger datasets for testing statistical models or machine learning algorithms.')

# Ask the user to upload a CSV file
uploaded_file = st.file_uploader("Upload the sample data (CSV file)")

# If a file was uploaded, read it into a DataFrame
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Ask the user how many rows they want to see
    num_rows = st.number_input("Number of rows to display:", min_value=1, max_value=len(df), value=5)

    # Show the specified number of rows
    st.write("## Sample Data")
    st.write(df.head(num_rows))
    st.write()

    # Add a checkbox to show/hide missing values
    if st.checkbox("Show missing values"):
        st.write(df.isna().sum())

    # Ask the user how many rows of synthetic data they want to generate
    num_synthetic_rows = st.number_input("Number of synthetic rows to generate (max=9999999):", min_value=len(df), max_value=9999999, value=len(df))

    # Generate synthetic data
    synthetic_data = generate_samples_bayesian(df, num_synthetic_rows)

    # Show the synthetic data
    st.write("## Generated Synthetic Data based on the given sample dataset")
    st.write(synthetic_data)

    # Compare the statistics for the original and generated data side by side
    st.write("## Comparison of Descriptive Statistics")
    st.write()
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Original Data")
        st.write(df.describe())
    with col2:
        st.write("### Generated Data")
        st.write(synthetic_data.describe())

    # Allow the user to download the synthetic data as a CSV file
    csv = synthetic_data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="synthetic_data.csv">Download synthetic data</a>'
    st.markdown(href, unsafe_allow_html=True)

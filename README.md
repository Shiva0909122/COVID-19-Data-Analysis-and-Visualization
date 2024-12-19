# COVID-19 Data Analysis and Visualization

This project provides an in-depth analysis and interactive visualization of COVID-19 global data. The goal of the project is to understand the trends and patterns in the spread of the virus, its impact across countries, and the effectiveness of various measures like vaccination.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Analysis and Visualizations](#analysis-and-visualizations)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
This project leverages the [Johns Hopkins University COVID-19 dataset](https://github.com/CSSEGISandData/COVID-19) and other sources to perform data cleaning, exploratory data analysis (EDA), and create interactive visualizations using Plotly.

### Key Features:
- Time series analysis of COVID-19 cases globally and by country
- Geographical heatmaps to visualize case distribution
- Trend analysis to compare cases, deaths, and recoveries across different countries
- Interactive plots for better insights into the data

## Data Sources
- [Johns Hopkins University COVID-19 Dataset](https://github.com/CSSEGISandData/COVID-19)
- [Our World in Data](https://github.com/owid/covid-19-data)
- Kaggle datasets (if applicable)

## Installation Instructions
To run this project locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://shiva0909122/COVID-19-Data-Analysis-and-Visualization.git
   cd COVID-19-Data-Analysis-and-Visualization
   ```

2. Set up a Python virtual environment:
   ```bash
   python -m venv venv
   ```


## Usage
Once the environment is set up, you can run the analysis and generate the visualizations.

### Running the Jupyter Notebook:
1. Install Jupyter Notebook (if not already installed):
   ```bash
   pip install jupyter
   ```

2. Start the Jupyter Notebook server:
   ```bash
   jupyter notebook
   ```

3. Open the notebook file `analysis_notebook.ipynb` in your browser, and execute the code blocks to see the data analysis and visualizations.

### Running the Interactive Plot:
If you want to run the interactive Plotly graph:
1. Ensure Plotly is installed:
   ```bash
   pip install plotly
   ```

2. Run the Python script `interactive_visualization.py` to view the plot:
   ```bash
   python interactive_visualization.py
   ```

## Analysis and Visualizations
- **Time Series Plot**: Shows the trend of confirmed cases over time.
- **Geographical Distribution**: Displays COVID-19 cases on a world map.
- **Top 10 Countries**: A bar chart comparing the total number of confirmed cases by country.
- **Vaccination Rates**: Analyzes the correlation between vaccination rates and case numbers.

### Output

![image](https://github.com/user-attachments/assets/00194369-aa7a-496c-9eb9-6c8dd708d695)


### Example of Interactive Plot:
- A line plot showing global COVID-19 confirmed cases over time. You can interact with the plot to zoom in, hover for exact values, and filter data by country.

## Contributing
Contributions are welcome! If you would like to improve this project, please fork the repository, make your changes, and submit a pull request.

### How to Contribute:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a pull request


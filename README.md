# What is it?
This repository contains a machine learning model designed to predict whether a bank customer will respond positively or negatively to a marketing campaign. The model leverages various data science techniques, including:

Exploratory Data Analysis (EDA): In-depth analysis to understand the data, identify patterns, and handle missing values.
Data Ingestion and Transformation: Efficiently loading and preprocessing the dataset for modeling.
Machine Learning: Utilizing appropriate algorithms to build a predictive model.
Flask Web App: Developing a user-friendly web interface using Flask, HTML, and CSS to interact with the model.

# Table Of Content 
#### [Purpose](#Purpose)
#### [Target Audience](#TargetAudience)
#### [Usage](#Usage)
#### [File Structure](#FileStructure)
#### [Configuration](#Configuration)
#### [Issues and Contributing](#IssuesandContributing1)
#### [License](#License)
#### [Author](#Author)

<a name="purpose"></a># Purpose:
The primary goal of this repository is to provide a hands-on learning experience for individuals interested in exploring the field of machine learning. By studying and experimenting with the code, users can gain a deeper understanding of end-to-end projects solutions for best practices.


<a name="TargetAudience"></a> # Target Audience:
This repository is suitable for a wide range of individuals, including:
-Data scientists
-Machine learning enthusiasts
-Students and researchers
-Developers working on data-driven projects

<a name="Usage"></a># Usage
Installation:
Clone the repository:
```
git clone https://github.com/MuhammadUmer241/Non-Genrative-AI.git
```
Use code with caution.

Install dependencies:
Ensure you have the necessary Python libraries installed. You can use a requirements.txt file or install them individually:

```
pip install -r requirements.txt
```

Run ```app.py``` in your IDE

Got to this link to your local machine
```http://127.0.0.1:5000/```

<a name="FileStructure"></a> # File Structure 
Artifacts/
  - Train/ (contains training data)
  - Test/ (contains testing data)
  - Raw_Data/ (contains raw data)
  - model.pkl (trained model)
  - preprocessor.pkl (preprocessor object)
src/
  - ```utils.py``` (common functions)
  - ```Logger.py``` (logging functionality)
  - ```exceptions.py``` (custom exception handling)
  - notebook/
    -```EDA.ipynb``` (EDA to understand Data)
  - components/
    - ```data_ingestion.py``` (data loading and splitting)
    - ```data_transformation.py``` (data transformation logic)
    - ```model_trainer.py``` (to train the model)
  - pipeline/
    - ```predict_pipeline.py``` (prediction pipeline)
  - templates/
    - ```index.html``` (GET request template)
    - ```home.html``` (POST request template)
  - static/
    - ```styles.css``` (stylesheets)
```app.py``` (Flask application)

-It is not recomended to change the structures and names of Directories and Files



<a name="Configuration"></a># Configuration
This repository currently doesn't require any specific configuration. However, if you plan to use external services or modify the code, you might need to set up environment variables or configure certain parameters.


<a name="IssuesandContributing1"></a># Issues and Contributing
If you encounter any issues or have suggestions for improvements, please feel free to open an issue on the repository's GitHub page. Contributions are welcome! To contribute:

#### 1.Fork the repository.
#### 2.Create a new branch for your feature or bug fix.
#### 3.Make your changes and commit them.  
#### 4.Submit a pull request to the main repository.

<a name= "License"></a># License
This repository is licensed under the MIT License.  

<a name= "Author"></a># Author
##### Muhammad Umer
Linkdln:
-```https://www.linkedin.com/in/muhammad-umer-881466293/```

Email:
-```umernadeem241@gmail.com```


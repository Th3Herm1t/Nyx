# Nyx: MBTI Personality Prediction
This Django web application predicts MBTI (Myers-Briggs Type Indicator) personality types based on user input text. The project integrates a machine learning model trained on MBTI data, allowing users to explore and interact with personality predictions.

   - Kaggle Notebook: https://www.kaggle.com/code/abdelkarimbsalah/notebook18d15ca57a
   - Original dataset: https://www.kaggle.com/datasets/datasnaek/mbti-type
   - Inspiration: https://pdfs.semanticscholar.org/6399/91916d01f962aef01d117dbe33dc3e11852e.pdf

## Objective and Goals
Nyx aims to provide a practical MBTI personality predictor with real-world applications in marketing, content suggestion, job matching, and more.


## Planning and Timeline
1. **ML Model Refinement:**
   - Explored various algorithms and techniques to perfect the ML model.
   - Iterative testing and improvement.

2. **Django Web App Development:**
   - Constructed a Django web app as a wrapper around the chosen ML model.
   - Ensured seamless integration of the model into the app.

3. **Integration and Optimization:**
   - Successfully integrated the ML model into the app.
   - Optimization for real-world applications.

## Communication and Engagement
Engaged extensively with the instructor and the AI community:
- Sought advice on ML model improvement.
- Collaborated for insights into effective deployment and applications.

## Problem Definition and Innovative Solution
The challenge: Build a highly accurate ML model for better insight into the human psyche. The innovation lies in predicting personality types from authentic text-based input, a departure from traditional assessment methods.

## Data Collection
Utilized a Kaggle dataset:
- Selected data aligned with computational power constraints.
- Ensured relevance for accurate personality predictions.

## Dataset Exploration
- Conducted statistical analysis.
- Visualized key insights for better understanding.

## User Interaction
1. **Simple Input Mechanism:**
   - Users input text.
   - Press the predict button.

2. **Output Information:**
   - Receive predicted personality type.
   - Access detailed personality profile.
   - View prediction accuracy.

## ML Model Details
**Data Preprocessing:**
1. Text cleaning:
   - Tokenization, stop word removal, punctuation removal, stemming/lemmatization.

2. Label encoding:
   - Convert categorical personality types into numerical values.

**Feature Engineering:**
- Convert text data into numerical vectors using TF-IDF or word embeddings.

**Model Selection:**
- SVM model was selected as the highest-performing among various tried algorithms.

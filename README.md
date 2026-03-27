Premier League Result Prediction using Machine Learning
A machine learning project that predicts the outcome of Premier League football matches (Home Win / Away Win / Draw) using historical match data and team form features.

📌 Project Overview
This project uses Logistic Regression to predict Premier League match results based on each team's recent performance. Given two teams, the model returns the predicted winner or a draw.

🗂️ Dataset

Source: Historical Premier League match data (e.g. from Kaggle / football-data.co.uk)
Contains match results, home/away teams, and goals scored per match
Covers multiple Premier League seasons


⚙️ Features Used
FeatureDescriptionhome_encodedHome team encoded as a numberaway_encodedAway team encoded as a numberhome_goals_avgHome team's average goals scored in last 5 home matchesaway_goals_avgAway team's average goals scored in last 5 away matcheshome_conceded_avgHome team's average goals conceded in last 5 home matchesaway_conceded_avgAway team's average goals conceded in last 5 away matches

🛠️ Tech Stack

Python
Pandas
Scikit-learn
Jupyter Notebook


🔄 Project Pipeline
1. Data Loading & Cleaning
        ↓
2. Feature Engineering (5-match rolling averages)
        ↓
3. Label Encoding (teams + results)
        ↓
4. Train/Test Split (80/20)
        ↓
5. Model Training (Logistic Regression)
        ↓
6. Evaluation & Prediction

📊 Model Performance

Accuracy: 48%
Baseline (random guess): 33%
The model outperforms random guessing by 15% on a 3-class classification problem


Note: Football is inherently unpredictable. 48% accuracy is consistent with published sports prediction benchmarks.


🔮 Predict a Match
pythonpredict_match('Arsenal', 'Chelsea')
# Output: Predicted Winner: Arsenal

🚀 How to Run

Clone the repo

bashgit clone https://github.com/yourusername/premier-league-predictor.git

Install dependencies

bashpip install pandas scikit-learn jupyter

Open the notebook

bashjupyter notebook premier_league_predictor.ipynb

Run all cells in order


📈 Future Improvements

Add head-to-head record between teams
Include current league standings as a feature
Try Random Forest or XGBoost for better accuracy
Extend rolling window from 5 to 10 matches

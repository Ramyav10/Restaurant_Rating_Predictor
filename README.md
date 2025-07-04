# Restaurant Rating Prediction System

This project is a **Machine Learning-based Restaurant Rating Prediction System** that predicts restaurant ratings based on multiple factors such as location, cuisine, cost, and other key attributes. It features a **Streamlit web app** that allows users to input restaurant details and receive predicted ratings instantly.

---
##  Key Features

* Predicts restaurant ratings using a trained **Random Forest Regressor** model.
* Simple & interactive **Streamlit web interface** for easy predictions.
* Robust data preprocessing pipeline with feature encoding and scaling.
* Automatic loading of encoders, scaler, and model for seamless predictions.

---

##  Technologies Used

* **Python 3**
* **Machine Learning:**

  * Random Forest Regressor
  * Scikit-learn (Modeling, Preprocessing)
* **Data Handling:**

  * Pandas, Numpy
* **Visualization:**

  * Matplotlib, Seaborn (EDA)
* **Web Application:**

  * Streamlit
* **Serialization:**

  * joblib (for saving models, encoders, scalers)

---

## How It Works

1. **Data Preprocessing:**

   * Cleaning missing values, duplicates, and garbage entries.
   * Label encoding for categorical variables.
   * Scaling numeric fields.

2. **Model Training:**

   * Random Forest Regressor trained on preprocessed dataset.
   * Model evaluated using Mean Squared Error (MSE).
   * Trained model, encoders, scaler, and feature columns are saved.

3. **Web App Flow (Streamlit):**

   * User selects restaurant attributes through the app UI.
   * Inputs are encoded and scaled automatically.
   * Model predicts rating, which is displayed in the app.

---

##  Getting Started (Local Setup)

### 1️ Install Dependencies:

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**

```
numpy
pandas
scikit-learn
matplotlib
seaborn
streamlit
joblib
```

### 2️ Run Streamlit App:

```bash
python -m streamlit run app.py
```

### 3️ Usage:

* Input restaurant details in the app form.
* Click **Predict Rating**.
* Get the predicted rating instantly.

---

##  Model Performance:

* **Model:** Random Forest Regressor
* **Target Metric:** Rating (range 0 to 5)
* Model is trained with optimized preprocessing for enhanced accuracy.

---

##  Future Enhancements

* Hyperparameter tuning for better accuracy.
* Additional models for comparison.
* Cloud-based deployment.
* User feedback integration for model refinement.

---

##  License

This project is intended for educational and demonstration purposes only.

---


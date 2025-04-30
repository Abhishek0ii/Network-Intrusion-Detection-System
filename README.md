# Network Intrusion Detection System Using Reinforcement Learning and Automated Audit Reporting

This project implements an advanced **Network Intrusion Detection System (NIDS)** that combines traditional Machine Learning (ML) and Reinforcement Learning (RL) techniques to identify and classify network threats such as **SQL Injection** and **Distributed Denial of Service (DDoS)** attacks. Additionally, it includes **automated audit reporting** capabilities that generate insightful visualizations and performance metrics in PDF format.

---

## 🧠 Project Objective

The goal is to develop a **robust**, **adaptive**, and **intelligent IDS** that can:
- Continuously learn and improve from real-time feedback.
- Detect both known and novel attack types using a hybrid learning framework.
- Provide comprehensive audit trails and performance visualizations for evaluation and compliance purposes.

---

## 📌 Key Features

### 1. **Hybrid Learning Framework**
- **Supervised Learning** (for known threats):
  - Models used: `Random Forest`, `Decision Tree`, `KNN`, `Logistic Regression`, `Naive Bayes`.
  - Evaluated using accuracy, F1-score, precision, recall, and confusion matrix.

- **Unsupervised Learning** (for anomaly detection):
  - Uses `K-Means Clustering` with PCA.
  - Detects deviations in unlabeled data using distance from cluster centroids.

- **Reinforcement Learning** (for dynamic threat learning):
  - Uses **Deep Q-Learning (DQN)** and **Actor-Critic** algorithms.
  - Agent receives real-time rewards (+1 for correct, -1 for incorrect classification).
  - Adapts to evolving attack strategies via policy updates.

---

### 2. **Automated Audit Report Generation**
- Generates PDF reports using `ReportLab` library.
- Includes:
  - Confusion matrices
  - ROC curves
  - Reward progression over episodes
  - Cluster plots
  - Summary of test results and evaluation metrics

---

### 3. **Statistical Validation**
- Uses hypothesis testing and statistical analysis to validate model performance and feature relevance:
  - `Chi-Square`, `T-Test`, `ANOVA`, `Kruskal-Wallis`
  - Visualization using seaborn (violin plots, heatmaps, boxplots)

---

## 📊 Datasets Used

- **SQL Injection Dataset** (Kaggle): Simulates structured query manipulation attacks.
  - Link: [SQL Injection Dataset](https://www.kaggle.com/datasets/syedsaqlainhussain/sql-injection-dataset)

- **CICDDoS2019 Dataset** (UNB): Realistic DDoS traffic for testing IDS performance.
  - Link: [CICDDoS2019 Dataset](https://www.unb.ca/cic/datasets/ddos-2019.html)

Each dataset undergoes cleaning, encoding, and scaling before being used in training and evaluation.

---

## ⚙️ How It Works

1. **Data Preprocessing**
   - Missing value handling, duplicate removal
   - Label encoding for categorical features (e.g., `protocol_type`, `flag`)
   - MinMax scaling of numerical features
   - Feature elimination for low-variance columns

2. **Exploratory Data Analysis (EDA)**
   - Statistical summaries and visual plots
   - Heatmaps for correlation analysis
   - KDE, boxplots, countplots, and violin plots

3. **Model Training and Testing**
   - All models are trained on processed data and evaluated on a held-out test set.
   - RL agents (DQN, Actor-Critic) are trained over multiple episodes with reward optimization.

4. **Visualization and Reporting**
   - Generates plots for learning curves, confusion matrices, clustering, and RL rewards.
   - Creates a PDF report summarizing the model's behavior and performance.

---

## 🛠️ Technologies Used

- **Programming Language**: Python 3.8+
- **Libraries**:
  - Data: `pandas`, `numpy`
  - ML/DL: `scikit-learn`, `PyTorch`, `Keras`
  - Visualization: `seaborn`, `matplotlib`
  - Statistical Tests: `pingouin`, `scipy`
  - PDF Report: `reportlab`

---

## 📈 Evaluation Metrics

- **Classification**: Accuracy, Precision, Recall, F1-Score
- **Clustering**: Elbow Method, Silhouette Score
- **Reinforcement Learning**: Cumulative Reward over Episodes, Policy Convergence
- **Statistical Testing**: P-values from hypothesis tests, ANOVA results

---

## 🧪 Testing Strategy

- **Unit Tests**: Each preprocessing and model function tested independently.
- **Integration Tests**: Entire pipeline from preprocessing to model output validated.
- **Model Validation**: 80-20 train-test split, cross-validation (5-fold), GridSearchCV for tuning.
- **RL Evaluation**: Reward trend visualization, policy improvement tracking.

---

## 📤 Deployment & Scalability

- Future plan to deploy via **Flask API** or **Docker container**.
- System is compatible with **GPU acceleration** for DQN/Actor-Critic models.
- Designed to scale with larger datasets and allow modular updates (e.g., plugging in new models).

---

## 🔭 Future Enhancements

- ✅ Integrate autoencoders or LSTMs for time-series traffic patterns.
- ✅ Enable semi-supervised learning with manual analyst validation.
- ✅ Use **Federated Learning** for privacy-preserving distributed training.
- ✅ Add SHAP or LIME for **Explainable AI** support.
- ✅ Validate system on NSL-KDD and CICIDS2017 datasets for generalizability.

---

## 👨‍💻 Author

**Abhishek Kumar**  
Final Year B.Tech - Computer Science and Engineering  
Vellore Institute of Technology (VIT)  
Supervisor: Prof. Anisha M. Lal

---

## 📜 License

This project was developed as part of the B.Tech Final Year Capstone Project at **Vellore Institute of Technology (VIT)**.  
All rights reserved. Distribution or reproduction of this work or its components is prohibited without prior permission from the author and the university.

© 2025 Abhishek Kumar. All rights reserved.

---

## thankyou 

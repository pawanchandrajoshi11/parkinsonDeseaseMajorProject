
# Detection of Parkinson's Disease using Machine Learning

This project uses machine learning to diagnose Parkinson's disease through speech analysis. It explores different machine learning models and their accuracy in predicting Parkinson's disease based on speech metadata.

## Project Report
[Parkinsons_Disease_Detection_report.pdf](https://github.com/pawanchandrajoshi11/parkinsonDeseaseMajorProject/files/13256398/Parkinsons_Disease_Detection_report.pdf)

## Abstract

Diagnosing Parkinson's disease is a complex task that comprises examining various aspects of the body, mind, and nervous system. Researchers have discovered a new way to use speech metadata to diagnose people with Parkinson's disease by extracting features from people's voices. Naive Bayes, Logistic Regression, Gradient Boosting, Random Forest, Multilayer Perceptron, and Stacked Classifiers were used to evaluate different learning models for this task. The Stacked Classifier and Gradient Boosted models reached the highest accuracy with 89.47% and 88.15%, respectively. The multilayer sensor model has the lowest accuracy with 84.21%. Therefore, the Stacking Classifier and Gradient Boosting models were found to be optimal for similar data. This study provides insight into the selection of appropriate machine learning models for accurate prediction.

**Keywords:** Parkinson's disease, machine learning model

## Introduction

Parkinson's disease (PD) is a mental disorder that affects the body's motor function. This condition is recognized by the degeneration of brain cells that produce neurotransmitters such as dopamine, acetylcholine, and serotonin. It is the second most frequent mental illness worldwide, next to Alzheimer's disease. It is a serious disease that influences the central nervous system, usually seen in people over 60 years of age. The identification of PS is difficult, especially in the early stages, and is often based on movement analysis. Speech problems affect up to 89% of people with PS, usually caused by a deficiency in laryngeal function, facial expression, lung capacity, and speech power.

The use of artificial intelligence (AI) algorithms and its subcategory machine learning (ML) in medicine is gaining momentum. This is because they can create the necessary patterns that enable early detection and diagnosis of many diseases. Parkinson's disease (PD) is an area where ML is used to develop predictive models for early detection, enabling doctors to make better decisions when diagnosing the disease, thereby improving patient outcomes.

## Machine Learning Methods

1. **Naïve Bayes Classifier**
   Naive Bayes is a popular algorithm based on Bayes Theorem. It is known for its simplicity, speed, and accuracy, particularly for large files. The algorithm assumes independence among features and calculates probabilities to estimate class probability.

2. **Logistic Regression**
   Logistic regression is a classifier employed for tasks that include binary classification. It uses logistic functions to predictively model the outcome of a binary response variable. Logistic regression is powerful and works on both small and large datasets.

3. **Random Forest**
   Random Forest is a popular machine learning algorithm for classification and regression tasks that uses learning methods to combine multiple decision trees. The algorithm evaluates significance to identify important predictors.

4. **Gradient Boosting**
   Gradient Boosting is a useful machine learning technique for recovery and classification tasks that create models in the previous step with each new model to correct errors from previous models. The algorithm uses the failure rate to determine the error at each stage and adjusts the weight of the analysis to draw more attention to the results that were underestimated in the previous model.

5. **Stacking Classifier**
   The Stacked Classifier is an ML algorithm that enhances prediction accuracy by combining multiple models. It falls under cluster learning, where several models are merged to improve overall prediction accuracy.

6. **Multilayer Perceptron**
   The Multilayer Perceptron (MLP) is a widely-used neural network for regression and classification tasks.

## Literature Review

As an important part of educational research, data analysis is an important tool that allows researchers to identify gaps in existing knowledge and develop new questions. By referring to the relevant literature, researchers can understand the state of knowledge in their field and identify areas that require further research.

## Methodology

To generate a resilient and precise model, a well-defined process is necessary. This includes gathering and pre-processing relevant data, normalizing it to ensure consistency, selecting the appropriate algorithm, training the model on the pre-processed data, and evaluating its accuracy using various metrics.

## Result

The accuracy scores of six machine learning models between training and testing datasets are as follows:

| Algorithm          | Type   | Scores     |
|--------------------|--------|------------|
| MultiLayer Perceptron | Train  | 81.03%     |
| MultiLayer Perceptron | Test   | 84.21%     |
| Naïve Bayes        | Train  | 78.38%     |
| Naïve Bayes        | Test   | 85.53%     |
| Logistic Regression | Train  | 84.85%     |
| Logistic Regression | Test   | 85.53%     |
| Gradient Boosting  | Train  | 96.47%     |
| Gradient Boosting  | Test   | 89.47%     |
| Random Forest      | Train  | 92.35%     |
| Random Forest      | Test   | 85.53%     |
| Stacked Classifier  | Train  | 96.03%     |
| Stacked Classifier  | Test   | 88.16%     |

These scores are based on MLP training accuracy, MLP test accuracy, Naive Bayesian training accuracy, Naive Bayesian accuracy testing, Logistic Regression training accuracy, Logistic regression test accuracy, Gradient Boosting training accuracy, Gradient Boosting test accuracy training Forest, Forest Test Accuracy, Stacked Classifier Training Accuracy, Stacked Classifier Test Accuracy.

## Conclusion

This project explores machine learning models for diagnosing Parkinson's disease based on speech analysis. Stacked Classifier and gradient boosting are effective classification methods for this task. Overall, speech analysis has shown promise as a non-invasive method for Parkinson's disease diagnosis.

## Acknowledgment

We thank Graphic Era Hill University in Dehradun for providing the resources and assistance for this research. Special thanks to the teachers for their guidance and support in this project.

## References

[1] Tarigoppula, V. S. Sriram et al (2008) "Intelligent Parkinson Disease Prediction Using Machine Learning Algorithms."

[2] Geeta Yadav, Yugal Kumar, and G Sahoo (2012). "Prediction of Parkinson's disease using Data Mining Methods: a comparative analysis of tree, statistical and support vector machine classifiers."

[3] Mostafa, Salama A., et al. (2018) "Evaluating the Performance of Three Classification Methods in Diagnosis of Parkinson’s Disease."

[4] Haq, A.U., Li, J.,
# Detection of Parkinson's Disease using Machine Learning

This project uses machine learning to diagnose Parkinson's disease through speech analysis. It explores different machine learning models and their accuracy in predicting Parkinson's disease based on speech metadata.

## Abstract

Diagnosing Parkinson's disease is a complex task that comprises examining various aspects of the body, mind, and nervous system. Researchers have discovered a new way to use speech metadata to diagnose people with Parkinson's disease by extracting features from people's voices. Naive Bayes, Logistic Regression, Gradient Boosting, Random Forest, Multilayer Perceptron, and Stacked Classifiers were used to evaluate different learning models for this task. The Stacked Classifier and Gradient Boosted models reached the highest accuracy with 89.47% and 88.15%, respectively. The multilayer sensor model has the lowest accuracy with 84.21%. Therefore, the Stacking Classifier and Gradient Boosting models were found to be optimal for similar data. This study provides insight into the selection of appropriate machine learning models for accurate prediction.

**Keywords:** Parkinson's disease, machine learning model

## Introduction

Parkinson's disease (PD) is a mental disorder that affects the body's motor function. This condition is recognized by the degeneration of brain cells that produce neurotransmitters such as dopamine, acetylcholine, and serotonin. It is the second most frequent mental illness worldwide, next to Alzheimer's disease. It is a serious disease that influences the central nervous system, usually seen in people over 60 years of age. The identification of PS is difficult, especially in the early stages, and is often based on movement analysis. Speech problems affect up to 89% of people with PS, usually caused by a deficiency in laryngeal function, facial expression, lung capacity, and speech power.

The use of artificial intelligence (AI) algorithms and its subcategory machine learning (ML) in medicine is gaining momentum. This is because they can create the necessary patterns that enable early detection and diagnosis of many diseases. Parkinson's disease (PD) is an area where ML is used to develop predictive models for early detection, enabling doctors to make better decisions when diagnosing the disease, thereby improving patient outcomes.

## Machine Learning Methods

1. **Naïve Bayes Classifier**
   Naive Bayes is a popular algorithm based on Bayes Theorem. It is known for its simplicity, speed, and accuracy, particularly for large files. The algorithm assumes independence among features and calculates probabilities to estimate class probability.

2. **Logistic Regression**
   Logistic regression is a classifier employed for tasks that include binary classification. It uses logistic functions to predictively model the outcome of a binary response variable. Logistic regression is powerful and works on both small and large datasets.

3. **Random Forest**
   Random Forest is a popular machine learning algorithm for classification and regression tasks that uses learning methods to combine multiple decision trees. The algorithm evaluates significance to identify important predictors.

4. **Gradient Boosting**
   Gradient Boosting is a useful machine learning technique for recovery and classification tasks that create models in the previous step with each new model to correct errors from previous models. The algorithm uses the failure rate to determine the error at each stage and adjusts the weight of the analysis to draw more attention to the results that were underestimated in the previous model.

5. **Stacking Classifier**
   The Stacked Classifier is an ML algorithm that enhances prediction accuracy by combining multiple models. It falls under cluster learning, where several models are merged to improve overall prediction accuracy.

6. **Multilayer Perceptron**
   The Multilayer Perceptron (MLP) is a widely-used neural network for regression and classification tasks.

## Literature Review

As an important part of educational research, data analysis is an important tool that allows researchers to identify gaps in existing knowledge and develop new questions. By referring to the relevant literature, researchers can understand the state of knowledge in their field and identify areas that require further research.

## Methodology

To generate a resilient and precise model, a well-defined process is necessary. This includes gathering and pre-processing relevant data, normalizing it to ensure consistency, selecting the appropriate algorithm, training the model on the pre-processed data, and evaluating its accuracy using various metrics.

## Result

The accuracy scores of six machine learning models between training and testing datasets are as follows:

| Algorithm          | Type   | Scores     |
|--------------------|--------|------------|
| MultiLayer Perceptron | Train  | 81.03%     |
| MultiLayer Perceptron | Test   | 84.21%     |
| Naïve Bayes        | Train  | 78.38%     |
| Naïve Bayes        | Test   | 85.53%     |
| Logistic Regression | Train  | 84.85%     |
| Logistic Regression | Test   | 85.53%     |
| Gradient Boosting  | Train  | 96.47%     |
| Gradient Boosting  | Test   | 89.47%     |
| Random Forest      | Train  | 92.35%     |
| Random Forest      | Test   | 85.53%     |
| Stacked Classifier  | Train  | 96.03%     |
| Stacked Classifier  | Test   | 88.16%     |

These scores are based on MLP training accuracy, MLP test accuracy, Naive Bayesian training accuracy, Naive Bayesian accuracy testing, Logistic Regression training accuracy, Logistic regression test accuracy, Gradient Boosting training accuracy, Gradient Boosting test accuracy training Forest, Forest Test Accuracy, Stacked Classifier Training Accuracy, Stacked Classifier Test Accuracy.

## Conclusion

This project explores machine learning models for diagnosing Parkinson's disease based on speech analysis. Stacked Classifier and gradient boosting are effective classification methods for this task. Overall, speech analysis has shown promise as a non-invasive method for Parkinson's disease diagnosis.

## Acknowledgment

We thank Graphic Era Hill University in Dehradun for providing the resources and assistance for this research. Special thanks to the teachers for their guidance and support in this project.


## Project Images (one with input value and one with the output)
<img width="1201" alt="Screenshot 2023-11-04 at 16 21 47" src="https://github.com/pawanchandrajoshi11/parkinsonDeseaseMajorProject/assets/73007506/0aa9f5eb-9552-4ee2-8c81-609a22a877c3">
<img width="1206" alt="Screenshot 2023-11-04 at 16 21 23" src="https://github.com/pawanchandrajoshi11/parkinsonDeseaseMajorProject/assets/73007506/84280c65-73a9-4ecf-8aab-f8970c7cc520">



## References
[1] Tarigoppula, V. S. Sriram et al (2008) "Intelligent Parkinson Disease Prediction Using Machine Learning Algorithms."

[2] Geeta Yadav, Yugal Kumar, and G Sahoo (2012). "Prediction of Parkinson's disease using Data Mining Methods: a comparative analysis of tree, statistical and support vector machine classifiers."

[3] Mostafa, Salama A., et al. (2018) "Evaluating the Performance of Three Classification Methods in Diagnosis of Parkinson’s Disease."

[4] Haq, A.U., Li, J.,

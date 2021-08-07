



{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "58096c58",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import imblearn\n",
    "from sklearn.model_selection import train_test_split\n",
    "from imblearn.under_sampling import RandomUnderSampler\n",
    "from imblearn.over_sampling import SMOTE\n",
    "from imblearn.over_sampling import ADASYN\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn import tree\n",
    "from sklearn.metrics import accuracy_score, recall_score, precision_score\n",
    "from sklearn.naive_bayes import MultinomialNB, BernoulliNB\n",
    "from sklearn import metrics\n",
    "import matplotlib.pyplot as plt\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "from sklearn.linear_model import LogisticRegression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a86bf307",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HCJ\\anaconda3\\envs\\SMOTE_ENC\\lib\\site-packages\\sklearn\\utils\\validation.py:761: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\HCJ\\anaconda3\\envs\\SMOTE_ENC\\lib\\site-packages\\sklearn\\utils\\validation.py:761: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    }
   ],
   "source": [
    "# 데이터 불러오기\n",
    "data=pd.read_csv(\"C:/Users/HCJ/Desktop/2021_Summer/Finance_data/bank.csv\")\n",
    "\n",
    "# 데이터 전처리\n",
    "Y=data[['TARGET']]\n",
    "X=data.drop(['Unnamed: 0','TARGET'],axis=1)\n",
    "\n",
    "X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.3,random_state=1004)\n",
    "\n",
    "# 데이터 샘플링\n",
    "\n",
    "X_undersampled, Y_undersampled = RandomUnderSampler(random_state=0).fit_resample(X_train,Y_train)\n",
    "X_smote, Y_smote = SMOTE(random_state=0).fit_resample(X_train,Y_train)\n",
    "X_ada, Y_ada = ADASYN(random_state=0).fit_sample(X_train,Y_train)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "61dc64a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Undersampling DT \n",
      "Accuracy :  0.8733164161624049 \n",
      "Precision, Recall, Fscore :  (array([0.99865164, 0.04477929]), array([0.87359582, 0.83399209]), array([0.93194721, 0.08499496]), array([35608,   253], dtype=int64))\n",
      "Smote DT \n",
      "Accuracy :  0.7498396586821338 \n",
      "Precision, Recall, Fscore :  (array([0.99857747, 0.0235024 ]), array([0.74912941, 0.84980237]), array([0.85605173, 0.04573981]), array([35608,   253], dtype=int64))\n",
      "Adasyn DT \n",
      "Accuracy :  0.8113828392961713 \n",
      "Precision, Recall, Fscore :  (array([0.99854812, 0.03043416]), array([0.8112222 , 0.83399209]), array([0.89519028, 0.0587253 ]), array([35608,   253], dtype=int64))\n"
     ]
    }
   ],
   "source": [
    "# DT 모델 형성 및 결과\n",
    "# undersampling\n",
    "DT1 = DecisionTreeClassifier(max_depth=4, min_samples_split=50, min_samples_leaf=25)\n",
    "DT1.fit(X_undersampled,Y_undersampled)\n",
    "y_pred1=DT1.predict(X_test)\n",
    "\n",
    "under_DT_accuracy=metrics.accuracy_score(Y_test,y_pred1)\n",
    "under_DT_score=metrics.precision_recall_fscore_support(Y_test,y_pred1)\n",
    "print(\"Undersampling DT\",\"\\n\"+\"Accuracy : \", under_DT_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", under_DT_score)\n",
    "\n",
    "# Smote\n",
    "DT2=DecisionTreeClassifier(max_depth=4, min_samples_split=50, min_samples_leaf=25)\n",
    "DT2.fit(X_smote,Y_smote)\n",
    "y_pred2=DT2.predict(X_test)\n",
    "\n",
    "smote_DT_accuracy=metrics.accuracy_score(Y_test,y_pred2)\n",
    "smote_DT_score=metrics.precision_recall_fscore_support(Y_test,y_pred2)\n",
    "print(\"Smote DT\",\"\\n\"+\"Accuracy : \", smote_DT_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", smote_DT_score)\n",
    "# Adasyn\n",
    "DT3=DecisionTreeClassifier(max_depth=4, min_samples_split=50, min_samples_leaf=25)\n",
    "DT3.fit(X_ada,Y_ada)\n",
    "y_pred3=DT3.predict(X_test)\n",
    "\n",
    "ada_DT_accuracy=metrics.accuracy_score(Y_test,y_pred3)\n",
    "ada_DT_score=metrics.precision_recall_fscore_support(Y_test,y_pred3)\n",
    "print(\"Adasyn DT\",\"\\n\"+\"Accuracy : \", ada_DT_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", ada_DT_score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "26f95347",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HCJ\\anaconda3\\envs\\SMOTE_ENC\\lib\\site-packages\\sklearn\\utils\\validation.py:761: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Undersampling NB \n",
      "Accuracy :  0.6363737765260311 \n",
      "Precision, Recall, Fscore :  (array([0.99512944, 0.01086374]), array([0.63690744, 0.56126482]), array([0.77670468, 0.02131492]), array([35608,   253], dtype=int64))\n",
      "Smote NB \n",
      "Accuracy :  0.7196118345835308 \n",
      "Precision, Recall, Fscore :  (array([0.99592439, 0.01465637]), array([0.72056841, 0.58498024]), array([0.8361604 , 0.02859627]), array([35608,   253], dtype=int64))\n",
      "Adasyn NB \n",
      "Accuracy :  0.7681603970887594 \n",
      "Precision, Recall, Fscore :  (array([0.99712225, 0.02069212]), array([0.76873175, 0.68774704]), array([0.86815731, 0.04017548]), array([35608,   253], dtype=int64))\n"
     ]
    }
   ],
   "source": [
    "# NB 모델 형성 및 결과\n",
    "# undersamling\n",
    "multiNB1=MultinomialNB()\n",
    "multiNB1.fit(X_undersampled,Y_undersampled)\n",
    "y_pred4=multiNB1.predict(X_test)\n",
    "\n",
    "under_naive_accuracy=metrics.accuracy_score(Y_test,y_pred4)\n",
    "under_naive_score=metrics.precision_recall_fscore_support(Y_test,y_pred4)\n",
    "print(\"Undersampling NB\",\"\\n\"+\"Accuracy : \", under_naive_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", under_naive_score)\n",
    "\n",
    "# Smote\n",
    "multiNB2=MultinomialNB()\n",
    "multiNB2.fit(X_smote,Y_smote)\n",
    "y_pred5=multiNB2.predict(X_test)\n",
    "\n",
    "smote_naive_accuracy=metrics.accuracy_score(Y_test,y_pred5)\n",
    "smote_naive_score=metrics.precision_recall_fscore_support(Y_test,y_pred5)\n",
    "print(\"Smote NB\",\"\\n\"+\"Accuracy : \", smote_naive_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", smote_naive_score)\n",
    "\n",
    "# Adasyn\n",
    "multiNB3=MultinomialNB()\n",
    "multiNB3.fit(X_ada,Y_ada)\n",
    "y_pred6=multiNB3.predict(X_test)\n",
    "\n",
    "ada_naive_accuracy=metrics.accuracy_score(Y_test,y_pred6)\n",
    "ada_naive_score=metrics.precision_recall_fscore_support(Y_test,y_pred6)\n",
    "print(\"Adasyn NB\",\"\\n\"+\"Accuracy : \", ada_naive_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", ada_naive_score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ce3d5c24",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HCJ\\anaconda3\\envs\\SMOTE_ENC\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n",
      "C:\\Users\\HCJ\\anaconda3\\envs\\SMOTE_ENC\\lib\\site-packages\\sklearn\\utils\\validation.py:761: DataConversionWarning: A column-vector y was passed when a 1d array was expected. Please change the shape of y to (n_samples, ), for example using ravel().\n",
      "  y = column_or_1d(y, warn=True)\n",
      "C:\\Users\\HCJ\\anaconda3\\envs\\SMOTE_ENC\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Undersampling Logi \n",
      "Accuracy :  0.8469925545857617 \n",
      "Precision, Recall, Fscore :  (array([0.99857649, 0.03714185]), array([0.84711301, 0.83003953]), array([0.91662995, 0.07110208]), array([35608,   253], dtype=int64))\n",
      "Smote Logi \n",
      "Accuracy :  0.8479406597696663 \n",
      "Precision, Recall, Fscore :  (array([0.99824857, 0.03571429]), array([0.84834869, 0.79051383]), array([0.91721447, 0.06834102]), array([35608,   253], dtype=int64))\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\HCJ\\anaconda3\\envs\\SMOTE_ENC\\lib\\site-packages\\sklearn\\linear_model\\logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adasyn Logi \n",
      "Accuracy :  0.8474108362845431 \n",
      "Precision, Recall, Fscore :  (array([0.99828042, 0.03575876]), array([0.84778701, 0.7944664 ]), array([0.91689953, 0.06843718]), array([35608,   253], dtype=int64))\n"
     ]
    }
   ],
   "source": [
    "# logistic 모델 형성 및 결과\n",
    "# optimization\n",
    "'''\n",
    "Y = data[['TARGET']]\n",
    "X = data.drop(['TARGET'], axis=1)\n",
    "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=1004\n",
    "X = MinMaxScaler().fit_transform(X) \n",
    "# 뭔가 이상함. 테스트데이터 스플릿 이전에 optimization 해야하는 것 같은데 스플릿 이후에 optimization 하는게 필요없는 코드 같음\n",
    "'''\n",
    "# under sampling\n",
    "Logi1 = LogisticRegression()\n",
    "Logi1.fit(X_undersampled, Y_undersampled)\n",
    "y_pred7 = Logi1.predict(X_test)\n",
    "\n",
    "under_Logi_accuracy=metrics.accuracy_score(Y_test,y_pred7)\n",
    "under_Logi_score=metrics.precision_recall_fscore_support(Y_test,y_pred7)\n",
    "print(\"Undersampling Logi\",\"\\n\"+\"Accuracy : \", under_Logi_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", under_Logi_score)\n",
    "\n",
    "# Smote\n",
    "Logi2 = LogisticRegression()\n",
    "Logi2.fit(X_smote, Y_smote)\n",
    "y_pred8 = Logi2.predict(X_test)\n",
    "\n",
    "smote_Logi_accuracy=metrics.accuracy_score(Y_test,y_pred8)\n",
    "smote_Logi_score=metrics.precision_recall_fscore_support(Y_test,y_pred8)\n",
    "print(\"Smote Logi\",\"\\n\"+\"Accuracy : \", smote_Logi_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", smote_Logi_score)\n",
    "\n",
    "# Adasyn\n",
    "Logi3 = LogisticRegression()\n",
    "Logi3.fit(X_ada, Y_ada)\n",
    "y_pred9 = Logi3.predict(X_test)\n",
    "\n",
    "ada_Logi_accuracy=metrics.accuracy_score(Y_test,y_pred9)\n",
    "ada_Logi_score=metrics.precision_recall_fscore_support(Y_test,y_pred9)\n",
    "print(\"Adasyn Logi\",\"\\n\"+\"Accuracy : \", ada_Logi_accuracy, \"\\n\"+\"Precision, Recall, Fscore : \", ada_Logi_score)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4dfe3791",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

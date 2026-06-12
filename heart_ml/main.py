import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
LR=LogisticRegression(solver='liblinear')
data_df=pd.read_csv('heart.csv')
x=data_df.drop('target',axis=1)
y=data_df['target']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
LR.fit(x_train,y_train)
y_pred=LR.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy*100)
data_df = pd.read_csv('test_data.csv')
x = data_df.drop('target', axis=1)
y_pred = LR.predict(x)
print(y_pred)


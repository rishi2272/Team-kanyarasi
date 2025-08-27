import pandas as pd

def generateAI():
    dataset = pd.read_csv('data-kits-cse.csv')
    dataset = dataset.dropna()
    X= dataset.iloc[:,1].values
    X= X.reshape(-1,1)
    y=dataset.iloc[:,-1].values

    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

    from sklearn.neighbors import KNeighborsClassifier
    ai = KNeighborsClassifier(n_neighbors=5)

    ai.fit(x_train,y_train)

    import pickle
    pickle.dump(ai,open('model.pkl','wb'))

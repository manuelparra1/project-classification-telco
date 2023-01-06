def get_forest(x_t,x_v,y_t,y_v):
    '''compare accuracy of Train & Validate set'''
    from sklearn.ensemble import RandomForestClassifier

    # create model object and fit it to training data
    rf = RandomForestClassifier(max_depth=4, random_state=123)
    rf.fit(train_X,train_y)

    # print result
    print(f"Accuracy of Random Forest on train is {rf.score(x_t, y_t)}")
    print(f"Accuracy of Random Forest on validate is {rf.score(x_v, y_v)}")

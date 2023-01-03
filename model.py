def split_dataset(df):
    import pandas as pd
    import numpy as np

    from sklearn.model_selection import train_test_split

    '''
    returns train, validate, test (in that order)
    
    uses train_test_split() from SciKit Learn - Model Selection
    
    20% test, 80% train_validate
    then of the 80% train_validate: 30% validate, 70% train.
    '''

    train_validate, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

    return train,validate,test

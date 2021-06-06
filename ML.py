def breast_survival_test(cancer_df):

    # %%
    """
    ## Machine Learning
    """

    # %%
    """
    ### Dependencies
    """

    # %%
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    import pandas as pd

    # %%
    """
    Using dataframe, create independent variables and the dependent variable
    """

    # %%
    """
    ### Preprocessing Data 
    """
    
    # %%
    # Assign y (target) = Dependent variable
    y = cancer_df['diagnosis']
    # %%
    # Assign X (data) = Independent variables
    X = cancer_df.drop("_id", axis=1)
    X = X.drop("diagnosis", axis=1)
    # %%
    """
    Split our data into training and testing
    """

    # %%
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    # %%
    """
    Scale the data
    """

    # %%
    X_scaler = StandardScaler().fit(X_train)
    X_train_scaled = X_scaler.transform(X_train)
    X_test_scaled = X_scaler.transform(X_test)

    # %%
    """
    Create a Logistic Regression Model
    """

    # %%
    from sklearn.linear_model import LogisticRegression
    classifier = LogisticRegression(max_iter=1000000)

    # %%
    """
    Fit (train) the model using the training data
    """

    # %%
    classifier.fit(X_train_scaled, y_train)

    # %%
    """
    Validate the model using the test data
    """

    # %%
    training_data_score = round(classifier.score(X_train_scaled, y_train)*100,4)
    testing_data_score = round(classifier.score(X_test_scaled, y_test)*100,4)
    results = {
        "training_data_score" : training_data_score,
        "testing_data_score": testing_data_score
    }
    return results
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
    stats_dict = X.describe().to_dict()
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

    # Make predictions with the hypertuned model
    predictions = classifier.predict(X_test_scaled)
    # Calculate classification report
    from sklearn.metrics import classification_report
    classification_report_dict = classification_report(y_test, predictions, target_names=["benign","malignant"], output_dict=True)

    results = {
        "training_data_score" : training_data_score,
        "testing_data_score": testing_data_score,
        "stats_dict": stats_dict,
        "classification_report": classification_report_dict
    }
    return results


def cancer_survival_rate(df,race_origin,survival_months,tumour_classification,tumor_size):
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

    def master_dict(le,df,col):
        temp_df = df[[col]].copy()
        temp_df[col +'_encoded'] = le.fit_transform(df[col].values)
        mapping_df = temp_df.drop_duplicates(col).reset_index().drop('index',axis=1).drop(col +'_encoded',axis=1)
        return mapping_df.to_dict()

    def get_encoded_value(le,df,col,value):
        temp_df = df[[col]].copy()
        temp_df[col +'_encoded'] = le.fit_transform(df[col].values)
        mapping_df = temp_df.drop_duplicates(col).reset_index().set_index(col)
        code = mapping_df.loc[value, col +'_encoded']
        return code

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

    # %%
    # Assign X (data) = Independent variables

    transformed_df = df.copy()
    le_race_origin = LabelEncoder()
    transformed_df['race_origin'] = le_race_origin.fit_transform(transformed_df['race_origin'])
    race_origin_master_dict = master_dict(le_race_origin,df,'race_origin')
    le_survival_months = LabelEncoder()
    transformed_df['survival_months'] = le_survival_months.fit_transform(transformed_df['survival_months'])
    le_status = LabelEncoder()
    transformed_df['status'] = le_status.fit_transform(transformed_df['status'])
    le_tumour_classification = LabelEncoder()
    transformed_df['tumour_classification'] = le_tumour_classification.fit_transform(transformed_df['tumour_classification'])
    tumour_classification_master_dict = master_dict(le_tumour_classification,df,'tumour_classification')
    le_death_cause = LabelEncoder()
    transformed_df['death_cause'] = le_death_cause.fit_transform(transformed_df['death_cause'])
    le_death_classification = LabelEncoder()
    transformed_df['death_classification'] = le_death_classification.fit_transform(transformed_df['death_classification'])
    le_tumor_size = LabelEncoder()
    transformed_df['tumor_size'] = le_tumor_size.fit_transform(transformed_df['tumor_size'])
    y = transformed_df["status"].copy()
    X = transformed_df.drop("status", axis=1)
    X = X.drop("_id", axis=1)

    if (race_origin=='0'):
        results = {
            "race_origin_master_dict" : race_origin_master_dict,
            "tumour_classification_master_dict": tumour_classification_master_dict,
            "csr": ""}
        return results
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

    # Make predictions 
    race_origin_encoded = get_encoded_value(le_race_origin,df,'race_origin',race_origin)
    tumour_classification_encoded = get_encoded_value(le_tumour_classification,df,'tumour_classification',tumour_classification)
    data = {'diagnosis_year': 2018, 'race_origin': race_origin_encoded, 'survival_months': survival_months,
        'tumour_classification': tumour_classification_encoded, 'death_cause': 5,
        'death_classification': 0, 'tumor_size': tumor_size}
    X_predict = pd.DataFrame(data,index=[0])
    X_predict_scaled = X_scaler.transform(X_predict)

    predictions = classifier.predict(X_predict_scaled)
    predicted_status = le_status.inverse_transform(predictions)
    if (predicted_status=='Alive'):
        csr = "HIGH"
    else:
        csr = "LOW"
    results = {
        "race_origin_master_dict" : race_origin_master_dict,
        "tumour_classification_master_dict": tumour_classification_master_dict,
        "csr": csr
    }
    return results
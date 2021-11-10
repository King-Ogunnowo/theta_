from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, f1_score, confusion_matrix, recall_score
from sklearn.metrics import plot_confusion_matrix
from imblearn import over_sampling, under_sampling
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

Over = RandomOverSampler(sampling_strategy = 'minority')
Under = RandomUnderSampler(sampling_strategy = 'majority')
pipeline = Pipeline(steps=[('o', Over), ('u', Under)])


def benchmark(x_train, x_test, y_train, y_test, algs = ['list of algs'], choice_metric = 'metric'):
    
    train = []
    test = []
    name = []
    recall = []
    precision = []
    f1 = []
    
    for alg in algs:
        name.append(type(alg).__name__)
        print('\n')
        print('algorithm:', alg)
        
        
        
        training = alg.fit(x_train, y_train)
        training_score = alg.score(x_train, y_train)
        y_pred = alg.predict(x_test)
        test_score = alg.score(x_test, y_test)
        
        f1.append(f1_score(y_test, y_pred))
        recall.append(recall_score(y_test, y_pred))
        precision.append(precision_score(y_test, y_pred))
        tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
        
        if (training_score - test_score) > 0.1:
            print('model likely overfitting, investigate further')
            
        train.append(training_score)
        test.append(test_score)
        
        print('tn, fp, fn, tp:', tn, fp, fn, tp)
    benchmark = pd.DataFrame({'alg_name': name,
                             'train_score':train,
                             'test_score':test,
                             'precision':precision,
                             'recall':recall,
                             'f1':f1}, columns = ['alg_name', 'train_score', 'test_score', 'precision', 'recall', 'f1'])
        
    return benchmark

        
def print_confusion_matrix(model, y_test, y_pred):
    """
    This function prints out the TP, FP, FN and TN
    ARGS:
        y_test - the true values of y
        y_pred - the predicted values of y
    """
    plot_confusion_matrix(model, x_test, y_test, include_values = True)
    cm = confusion_matrix(y_test, y_pred)
    print('True positive = ', cm[0][0])
    print('False positive = ', cm[0][1])
    print('False negative = ', cm[1][0])
    print('True negative = ', cm[1][1])

def class_distr(dataframe = 'df', target_column = 'column', pred_value = '1'):
    
    display(Markdown('##### Class Distribution in Dataset'))
    
    dataframe[target_column].value_counts().plot(kind = 'bar',
                                                xlabel = 'classes',
                                                ylabel = 'frequency',
                                                rot = 0)

    result = (len(dataframe.loc[dataframe['Response'] == pred_value])/len(dataframe)) * 100
    print('class distribution for target variable:',result)
 
    if result < 40 or result > 50:
        print('\n')
        print('***class distribution is imbalanced, employ oversampling or undersampling techniques to rectify***')
    elif result >= 40 and result <=50:
        print('\n')
        print('***class distribution is balanced, proceed***')
   
def class_balancer(dataframe = 'df', target_column = 'y'):
    
    x = dataframe.drop(target_column, axis = 1)
    y = dataframe[target_column]
    
    x_resampled, y_resampled = pipeline.fit_resample(x, y)
    return pd.concat([x_resampled, y_resampled], axis = 1)

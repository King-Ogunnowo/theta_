import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def looped_freq_plot(dataframe = 'df', columns = 'column'):
    for column in columns:
        dataframe[column].value_counts().plot(kind = 'bar',
                                             xlabel = column,
                                             ylabel = 'frequency',
                                             title = 'frequency of {} in dataset'.format(column),
                                             color = 'blue',
                                             grid = True,
                                             rot = 45)
        plt.show()

    

def groupby_plot(dataframe = 'df', pry_column = 'column', sec_column = 'column', title = '### title',
                 figure_size = 'size', plot_color = 'color', plt_args = {}):
    display(Markdown(title))
    dataframe.groupby(pry_column)[sec_column].value_counts().unstack().plot(figsize = figure_size,
                                                                            **plt_args)
    plt.show()



def feature_imp(x_train_set, model = 'model name', num_of_feats = 'number'):
    feature_importance = pd.DataFrame(model.feature_importances_,index=x_train_set.columns.tolist(),
                                      columns=['feat_imp']).reset_index()
    feature_importance.rename(columns={'index': 'feature'}, inplace=True)
    feature_importance['rate'] = np.round((feature_importance['feat_imp']/feature_importance['feat_imp'].sum())*100,2)
    feature_importance = feature_importance.sort_values(by=['rate'], ascending=False).reset_index(drop=True)
    feature_importance.drop(columns=['feat_imp'],inplace=True)
    fig, ax = plt.subplots(figsize=(10, 10),nrows=1,ncols=1)
    sns.barplot(x=feature_importance.loc[0:num_of_feats,'rate'], 
                y=feature_importance.loc[0:num_of_feats,'feature'], 
                color='grey', data=feature_importance)
    plt.xlabel('Percentage')
    plt.ylabel('Feature')
    plt.title('Top {} important features'.format(num_of_feats))
    plt.show()
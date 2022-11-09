import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import seaborn as sns

def create_regplot(df, title):
    sns.set_style("darkgrid")
    fig = sns.regplot(x=df.columns[0], y="4. Wiener Sachtextformel", data=df, scatter_kws={"color": "firebrick"}, line_kws={"color": "seagreen"},  fit_reg=True, ci=None)
    fig.xaxis.label.set_color("maroon")
    fig.yaxis.label.set_color("maroon")
    plt.title(title)
    plt.show()



ls_scores_unweighted_age1 = [0.83, 0.829, 0.793, 0.823, 0.819, 0.78, 0.818, 0.786, 0.807, 0.829, 0.826, 0.799, 0.819, 0.816]
ls_perfect_sents_age1 = [0.186, 0.135, 0.112, 0.157, 0.152, 0.045, 0.13, 0.059, 0.116, 0.169, 0.139, 0.092, 0.121, 0.091]
ls_scores_weighted_age1 = [0.741, 0.743, 0.708, 0.737, 0.737, 0.702, 0.73, 0.707, 0.729, 0.742, 0.735, 0.715, 0.734, 0.734]
readability_scores_wstf_age1 = [3.1, 2.7, 3.6, 3.1, 3.0, 5.3, 2.2, 4.8, 3.8, 2.6, 1.8, 4.1, 2.8, 4.1]
df_unweighted_age1 = pd.DataFrame({"LS unweighted": ls_scores_unweighted_age1, "4. Wiener Sachtextformel": readability_scores_wstf_age1})
df_weighted_age1 = pd.DataFrame({"LS weighted": ls_scores_weighted_age1, "4. Wiener Sachtextformel": readability_scores_wstf_age1})
df_perfect_sents_age1 = pd.DataFrame({"Share of Perfect Sentences": ls_perfect_sents_age1, "4. Wiener Sachtextformel" : readability_scores_wstf_age1})

ls_scores_unweighted_age2 = [0.786, 0.788, 0.805, 0.785, 0.774, 0.789, 0.803, 0.794, 0.799, 0.8, 0.766, 0.782, 0.815, 0.766]
ls_perfect_sents_age2 = [0.083, 0.098, 0.087, 0.101, 0.065, 0.079, 0.082, 0.097, 0.093, 0.11, 0.054, 0.072, 0.114, 0.042]
ls_scores_weighted_age2 = [0.711, 0.71, 0.726, 0.707, 0.7, 0.711, 0.723, 0.714, 0.72, 0.721, 0.691, 0.699, 0.733, 0.69]
readability_scores_wstf_age2 = [5.7, 5.1, 5.2, 5.3, 7.0, 4.6, 4.2, 4.5, 4.9, 4.5, 5.9, 5.0, 4.4, 6.2]
df_unweighted_age2 = pd.DataFrame({"LS unweighted": ls_scores_unweighted_age2, "4. Wiener Sachtextformel": readability_scores_wstf_age2})
df_weighted_age2 = pd.DataFrame({"LS weighted": ls_scores_weighted_age2, "4. Wiener Sachtextformel": readability_scores_wstf_age2})
df_perfect_sents_age2 = pd.DataFrame({"Share of Perfect Sentences": ls_perfect_sents_age2, "4. Wiener Sachtextformel" : readability_scores_wstf_age2})

ls_scores_unweighted_ls_corpus = [0.873, 0.812, 0.825, 0.835, 0.823, 0.812, 0.854, 0.823, 0.824, 0.884]
ls_scores_weighted_ls_corpus = [0.781, 0.749, 0.754, 0.762, 0.756, 0.739, 0.776, 0.756, 0.755, 0.787]
ls_perfect_sents_ls_corpus = [0.284, 0.069, 0.109, 0.056, 0.077, 0.104, 0.183, 0.062, 0.059, 0.367]
readability_scores_wstf_ls_corpus = [0.9, 6.8, 9.6, 6.7, 6.2, 6.9, 4.5, 7.1, 6.7, 3.3]
df_unweighted_ls_corpus = pd.DataFrame({"LS unweighted": ls_scores_unweighted_ls_corpus, "4. Wiener Sachtextformel": readability_scores_wstf_ls_corpus})
df_weighted_ls_corpus = pd.DataFrame({"LS weighted": ls_scores_weighted_ls_corpus, "4. Wiener Sachtextformel": readability_scores_wstf_ls_corpus})
df_perfect_sents_ls_corpus = pd.DataFrame({"Share of Perfect Sentences": ls_perfect_sents_ls_corpus, "4. Wiener Sachtextformel" : readability_scores_wstf_ls_corpus})

'''create_plot(df_unweighted_age1, "Children's Books I \n Age: 6–8")
create_plot(df_weighted_age1, "Children's Books I \n Age: 6–8")
create_plot(df_perfect_sents_age1, "Children's Books I \n Age: 6–8")
create_plot(df_unweighted_age2, "Children's Books II \n Age: 10–12")
create_plot(df_weighted_age2, "Children's Books II \n Age: 10–12")
create_plot(df_perfect_sents_age2, "Children's Books II \n Age: 10–12")
create_plot(df_unweighted_ls_corpus, "LS corpus")
create_plot(df_weighted_ls_corpus, "LS corpus")
create_plot(df_perfect_sents_ls_corpus, "LS corpus")'''

#print("Age 1:", result_age1)
#print("Age 2:", results_age2)

print(pearsonr(ls_scores_weighted_ls_corpus, readability_scores_wstf_ls_corpus))

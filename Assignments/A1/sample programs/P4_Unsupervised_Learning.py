import csv
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

file_path = "/Users/p.mittal/Library/Mobile Documents/com~apple~CloudDocs/Roux/Courses/NLP/Assignments/Assignment 1 BOW/Subset_patient_notes.csv"

df = pd.read_csv(file_path)
print(df.head())

# Convert pn_history column to a list of strings
documents = df['pn_history'].astype(str).tolist()

stop_words = [str(i) for i in range(1, 101)]+['2x', '3x']
stop_words += vectorizer.get_stop_words()

# Create an instance of TfidfVectorizer
vectorizer = TfidfVectorizer(min_df=5, max_df=0.8, max_features=1000, stop_words=stop_words, norm='l2')

# Fit and transform the documents to a DTM using TF-IDF
dtm = vectorizer.fit_transform(documents)

# convert it to a df
dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names())


# Merge dtm_df with the original dataframe and remove pn_history column
df_merged = pd.concat([df.drop('pn_history', axis=1), dtm_df], axis=1)



# apply preprocessing steps such as data standardization to all columns except pon_num and case_num, and PCA to the features
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Standardize the data
scaler = StandardScaler()
scaler.fit(df_merged.drop(['pn_num', 'case_num'], axis=1))
scaled_data = scaler.transform(df_merged.drop(['pn_num', 'case_num'], axis=1))

# Apply PCA to the features
pca = PCA()
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)

# Create a dataframe with the two principal components
df_pca = pd.DataFrame(x_pca)

df_pca.shape

df_pca.head()

# print the variance explained by each principal component in % and the total variance explained by all the principal components
print(pca.explained_variance_ratio_)
print(sum(pca.explained_variance_ratio_))

# print the cumulative variance explained by the principal components
var = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=3)*100)
print(var)

# Keep compontnets that explain 85% of the variance

pca = PCA(n_components=0.85)
pca.fit(scaled_data)
x_pca = pca.transform(scaled_data)
df_pca = pd.DataFrame(x_pca)
df_pca.shape

# print the cumulative variance explained by the principal components
var = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=3)*100)
print(var)

# Perform clustering using K-means and create ten clusters
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=10)
kmeans.fit(df_pca)
y_kmeans = kmeans.predict(df_pca)

# Add the cluster labels to the dataframe
df_pca['cluster'] = y_kmeans
df_pca.head()

# print the number of patients in each cluster
df_pca['cluster'].value_counts()

# print the mean of each feature in each cluster
df_pca.groupby('cluster').mean()

# print the top 10 features in each cluster
n = 10
for i in range(10):
    print(df_pca[df_pca['cluster']==i].mean().sort_values(ascending=False)[:n])

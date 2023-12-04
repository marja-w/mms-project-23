# methods from content_based_recsys.ipynb
import random

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def drop_duplicates(df):
    """
    Drop duplicate songs
    """
    df['artists_song'] = df.apply(lambda row: row['artist_name'] + row['track_name'], axis=1)
    return df.drop_duplicates('artists_song')


def select_cols(df):
    """
    Select useful columns
    """
    return df[['artist_name', 'id', 'track_name', 'danceability', 'energy', 'key', 'loudness', 'mode',
               'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', "artist_pop",
               "genres", "track_pop"]]


def genre_preprocess(df):
    """
    Preprocess the genre data
    """
    df['genres_list'] = df['genres'].apply(lambda x: x.split(" "))
    return df


def generate_playlist_recos(df, features, nonplaylist_features):
    '''
    Generated recommendation based on songs in a specific playlist.
    ---
    Input:
    df (pandas dataframe): spotify dataframe
    features (pandas series): summarized playlist feature (single vector)
    nonplaylist_features (pandas dataframe): feature set of songs that are not in the selected playlist

    Output:
    non_playlist_df_top_40: Top 40 recommendations for that playlist
    '''

    non_playlist_df = df[
        df['id'].isin(nonplaylist_features['id'].values)]  # all songs that are not in selected playlist
    # Find cosine similarity between the playlist and the complete song set
    non_playlist_df['sim'] = cosine_similarity(nonplaylist_features.drop('id', axis=1).values,
                                               features.values.reshape(1, -1))[:, 0]
    non_playlist_df_top_40 = non_playlist_df.sort_values('sim', ascending=False).head(
        40)  # sort values according to cosine similarity to playlist

    return non_playlist_df_top_40


def generate_playlist_feature(complete_feature_set, playlist_df):
    '''
    Summarize a user's playlist into a single vector
    ---
    Input:
    complete_feature_set (pandas dataframe): Dataframe which includes all of the features for the spotify songs
    playlist_df (pandas dataframe): playlist dataframe

    Output:
    complete_feature_set_playlist_final (pandas series): single vector feature that summarizes the playlist
    complete_feature_set_nonplaylist (pandas dataframe):
    '''

    # Find song features in the playlist
    complete_feature_set_playlist = complete_feature_set[complete_feature_set['id'].isin(playlist_df['id'].values)]
    # Find all non-playlist song features
    complete_feature_set_nonplaylist = complete_feature_set[~complete_feature_set['id'].isin(playlist_df['id'].values)]
    complete_feature_set_playlist_final = complete_feature_set_playlist.drop(columns="id")
    return complete_feature_set_playlist_final.sum(axis=0), complete_feature_set_nonplaylist


def get_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function is basically the content_based_recsys script in one function.
    I use it to create features for the test data set as well.
    :param df: the input DataFrame, the data before preprocessing
    :return: the preprocessed DataFrame
    """
    playlist_df = df.drop(columns=["Unnamed: 0", 'Unnamed: 0.1'])  # remove unneccessary columns
    song_df = drop_duplicates(playlist_df)
    song_df = select_cols(song_df)
    song_df = genre_preprocess(song_df)

if __name__ == '__main__':
    # look at data statistics
    df = pd.read_csv("../data/processed_data.csv")
    print(f"We have a dataset of {len(df)} entries")

    # create sorted data
    df.sort_values("name", inplace=True)

    num_playlists = df["name"].nunique()  # count distinct values, this is the number of playlists
    num_tracks = df["track_name"].nunique()  # count distinct values, this is the number of tracks
    print(f"Playlists: {num_playlists} \nTracks: {num_tracks}")

    # group by playlist
    playlists = df.groupby('name')["track_name"].apply(list)

    # divide into 90% train and 10% test data
    test_data_per = 0.1
    train_data = list()
    test_data = list()

    for playlist in list(playlists.index):  # loop through all playlists
        if random.random() > test_data_per:  # in 90% of cases
            for idx, song in df[df["name"] == playlist].iterrows():
                train_data.append(song)
        else:
            for idx, song in df[df["name"] == playlist].iterrows():
                test_data.append(song)

    # convert to dataframes and store
    pd.DataFrame(train_data).to_csv("../data/processed_data_train.csv")
    pd.DataFrame(test_data).to_csv("../data/processed_data_test.csv")

    print(f"Train data points: {len(train_data)}")
    print(f"Test data points: {len(test_data)}")



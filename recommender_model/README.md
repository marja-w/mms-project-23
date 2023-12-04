# Recommender Model Experiment

This folder contains the notebooks and data that implement the collaborative and content-based filtering approaches for 
recommending songs, based on Spotify's redcommendation system. 

## [collaborative_filtering.ipynb](collaborative_filtering.ipynb)

Here, the matrix for making recommendations based on user data is created. Originally, Spotify uses a matrix storing
information about each user and their track counts. Since this data is not publicly available, I used a matrix created 
from the [train data](data/processed_data_train.csv), where each row is a playlist, instead of a user, and each
column is a song, trying to mimic the original data used by Spotify. The idea was that each playlist could be seen as a
user, because each user might have created one of the playlists. Still, the information of the play counts is missing, 
as well as the differentiation of playlists created by one and the same user.

This script creates:

- [matrix.npy](data%2Fmatrix.npy)
- [unique_songs_uris.txt](data%2Funique_songs_uris.txt)
- [playlists.txt](data%2Fplaylists.txt)

which is needed for the [evaluation.ipynb](evaluation.ipynb) script.

## [content_based_recsys.ipynb](content_based_recsys.ipynb)

(The original notebook can be found [here](https://github.com/enjuichang/PracticalDataScience-ENCA/blob/main/notebooks/content_based_recsys.ipynb))
In this notebook, the content-based filtering is applied. The songs are recommended based on the track features, like 
loudness, danceability, and [many more](https://developer.spotify.com/documentation/web-api/reference/get-several-audio-features).
Those are originally retrieved using the python library [spotipy](https://spotipy.readthedocs.io/en/2.22.1/), which can
be seen in the original repository [here](https://github.com/enjuichang/PracticalDataScience-ENCA/blob/main/notebooks/Extract%20Features%20Script.ipynb).
I skipped the preprocessing step and used the final data provided [here](https://github.com/marja-w/mms-project-23/blob/main/recommender_model/data/processed_data.csv).
I then divided the dataset into [train](data/processed_data_train.csv) and [test](data/processed_data_test.csv) data, 
which you can do yourself with the [data_handling.py](scripts/data_handling.py) script. For reproducability, I uploaded 
the train-test split I used. This script uses those files and creates:
- [allsong_data_train.csv](data%2Fallsong_data_train.csv)
- [allsong_data_test.csv](data%2Fallsong_data_test.csv)
- [complete_feature_train.csv](data%2Fcomplete_feature_train.csv)
- [complete_feature_test.csv](data%2Fcomplete_feature_test.csv)

which is needed for the [evaluation.ipynb](evaluation.ipynb) script.

We have a dataset of 67499 entries

- Playlists: 869 
- Tracks: 30046
- Train data points: 60732
- Test data points: 6767

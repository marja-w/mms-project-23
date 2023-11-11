# Multimedia Systems Project Website

- [Proposal](https://github.com/marja-w/mms-project-23/blob/main/README.md#proposal)
- [Documentation](https://github.com/marja-w/mms-project-23/blob/main/README.md#documentation)
- [Schedule](https://github.com/marja-w/mms-project-23/blob/main/README.md#schedule)
- [Updates](https://github.com/marja-w/mms-project-23/blob/main/README.md#updates)
- [Sources](https://github.com/marja-w/mms-project-23/blob/main/README.md#sources)


## Proposal

Music streaming platforms have established themselves as a great way to enjoy music. Especially Spotify, as it is the [world's biggest streaming platform](https://www.businessofapps.com/data/spotify-statistics/#:~:text=Spotify%20is%20the%20world's%20biggest%20music%20streaming%20platform%20by%20number%20of%20subscribers ).


One of the reasons why Spotify is so successful is its recommendation system. It gives users suggestions for the next song and can create whole playlists for them. This makes it possible for the subscribers to listen to music they enjoy, without having to look through the masses of music out there themselves.


On the one side, there are the listeners, but Spotify is also a tool for music creators to showcase their work. The success of new music on Spotify heavily depends on the algorithm that recommends music to a user (2). Yet, the complexity of the recommender system of Spotify might reduce the understandability of the process for new artists.


In my project I want to create an explainable music recommender system, as close to the recommender system by Spotify. The goal is to create a model like the original Spotify recommender system, to be able to explain the algorithm and create a comprehensive summary for artists. I want to evaluate the model on the [Million Playlist Dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge).

## Documentation

**Disclaimer: the notebooks about preprocessing and content based prediction are heavily based off the notebooks
publicly available [here](https://github.com/enjuichang/PracticalDataScience-ENCA/tree/main)**

## Schedule
- 12th – 26th October: Research task and research current Recommender System algorithms
- 26th October – 9th November: train and fine-tune model (using [million playlist dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)) 
- 9th – 23rd November: evaluate model with test data (from [million playlist dataset](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge)) 
- 23rd – 4th December: analyze the important features for better recommendation results 

## Updates

### 26th October Update

- Task Definition: the task the model will be evaluated on is the task of **automatic playlist continuation**. This means, given a set of playlist features, like name or number of including different albums, generate a list of soundtracks that can continue the playlist to the users liking. The Million Playlist Dataset (MLP) is divided into a train and test set, where the test set is incomplete, in order to be able to test the model.
- [Spotify Recommender System Algorithm](https://github.com/marja-w/mms-project-23/blob/main/spotify_recommender_system.md)
- [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/): python client for Spotify Web API which enables fetching data and querying Spotify's catalog for songs

### Project Update

Progress:
- identified Spotifys algorithm: matrix-manipulation+CNN+NLP
- surveyed [existing systems](https://github.com/search?q=music%20recommandation&type=repositories), I did not find a project that performed matrix manipulation and build a CNN with spectrogram information
- settled on task of automatic playlist continuation

Remaining Technical Challenges:
- prepare train and test data using Spotipy and the MLP dataset: how to get audio data for spotify songs and turn into spectrogram input for CNN?
- build models for recommendation using Python: which library to use for matrix manipulation?
- evaluate the build model on MPL dataset

Adjustments requested to proposal:
- raise awareness about which media is used for creating a good recommendation: song attributes of different forms (temporal data like length of song or release date, spectrogram data, artist information, vector data assessed using NLP, ...)
- the goal is to implement the recommender techniques used in Spotify in a python notebook with focus on matrix manipulation and the CNN-based spectrogram analysis
- this notebook should explain the techniques and make them more comprehensible for non-experts
- finally evaluate the model on the MPL dataset on the task of automatic playlist continuation, to provide validity of the used approach

## Sources

(1) https://www.businessofapps.com/data/spotify-statistics/#:~:text=Spotify%20is%20the%20world's%20biggest%20music%20streaming%20platform%20by%20number%20of%20subscribers 

(2) Antonia Saravanou, Federico Tomasi, Rishabh Mehrotra, & Mounia Lalmas. (2021). Multi-Task Learning of Graph-based Inductive Representations of Music Content. Proceedings of the 22nd International Society for Music Information Retrieval Conference, 602–609. https://doi.org/10.5281/zenodo.5624379 

(3) Buket Baran, Guilherme Dinis Junior, Antonina Danylenko, Olayinka S. Folorunso, Gösta Forsum, Maksym Lefarov, Lucas Maystre, and Yu Zhao. 2023. Accelerating Creator Audience Building through Centralized Exploration. In Proceedings of the 17th ACM Conference on Recommender Systems (RecSys '23). Association for Computing Machinery, New York, NY, USA, 70–73. https://doi.org/10.1145/3604915.3608880 

(4) https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge 

(5) Current Challenges and Visions in Music Recommender Systems Research." International Journal of Multimedia Information Retrieval 7 (2018): 95-116.

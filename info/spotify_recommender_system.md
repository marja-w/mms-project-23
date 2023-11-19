# Spotifys Recommender System

- Bandits for Recommendations as Treatments (BaRT)
- collaborative and content-based filtering
- also uses NLP to analyze news, articles, blogs about songs and artists (for weekly playlist)

## Collaborative filtering
This technique uses information about other users in order to create a recommendation. For example, if two users listen to a lot of the same songs, Spotify will recommend songs that one of them listens to the other, if the other user has not listened to that song yet. This is similar to Netflixs' "You may also like" or Amazons' "Customers have also bought" recommendations.

More specifically, Spotify uses one big matrix, where each row is a user and each column is a song, and each entry resembles the amount of times a user has listened to a song. This matrix is called the rating matrix R.

![image](https://github.com/marja-w/mms-project-23/assets/58331624/f3f3be60-534f-4d03-b504-bf68f79ce7f2)

The matrix R is now transformed to two matrices, the preference matrix P and confidence matrix C. The preference matrix P is similar to matrix R, but every entry is 1 if users have listened to the song, and 0 if they have not, disregarding the amount of times the user has listened to a song. The confidence matrix C describes how confident the model is about a certain preference, factoring in the listening count of the user. A higher **listening count** makes the model more confident that the user likes the song, which therefore means this is one attribute that influences the recommender system of Spotify. The problem is, the matrices alone can not give information about songs the user has never listened to before. This is why Spotify uses Weighted Matrix Factorization to approximate matrix R with two other matrices.

![image](https://github.com/marja-w/mms-project-23/assets/58331624/6212aec6-acb3-49e1-a3a5-bc286b66e109)

[Weighted Matrix Factorization](https://tryolabs.com/blog/introduction-to-recommender-systems#:~:text=matrix%20factorization) factorizes the original matrix R into User and Item Matrix. The algorithm tries to approximate the original values in R as close as possible, while it is doing so, it fills empty values in R, which can be used for recommending new songs to users.

To sum it up, Spotify basically uses your listening data and the one of the other users in order to find similarities and recommend songs. The problem with this approach is that no new songs, songs no user has ever listened to, will be recommended, also known as the cold start problem. This is why Spotify uses two additional techniques for recommendation.

## Content based filtering
- analyze song itself (spectrogram, frequencies over time)
- spectrogram is fed into a convolutional neural network (CNN)

## Natural Language Processing
- scan internet to find articles, blogs, and online reviews talking about artists and songs
- use the descriptors used in those to compute importance of artist or song and generate "cultural vectors" with weight
- the terms associated with the cultural vectors for a song or artist are used to compare similarity between artists and songs a user listens to and freshly released music

# Sources
1. [Recommending music on Spotify with deep learning](https://sander.ai/2014/08/05/spotify-cnns.html)
2. [How Spotify’s Algorithm Manages To Find Your Inner Groove](https://analyticsindiamag.com/how-spotifys-algorithm-manages-to-find-your-inner-groove/)
3. [How does Spotify's recommendation system work?](https://www.univ.ai/blog/how-does-spotifys-recommendation-system-work#:~:text=Recommendations%20for%20each%20user%20are,algorithm%20on%20every%20song%20vector.)
4. [How Does Spotify Know You So Well?](https://medium.com/@sophiaciocca/spotifys-discover-weekly-how-machine-learning-finds-your-new-music-19a41ab76efe)
5. [Music Recommendation System using Spotify Dataset](https://www.kaggle.com/code/vatsalmavani/music-recommendation-system-using-spotify-dataset)
6. 

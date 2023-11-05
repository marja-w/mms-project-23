# Spotifys Recommender System

- Bandits for Recommendations as Treatments (BaRT)
- collaborative and content-based filtering
- also uses NLP to analyze news, articles, blogs about songs and artists (for weekly playlist)

## Collaborative filtering
- Based off of other peoples playlists, add songs to your own, if the songs overlap. Similar to Netflixs "You may also like" or Amazons "Customers have also bought"
- Matrix manipulation
- uses your listening data and listening data of others to recommend songs
- does not recommend songs no one has listened to before: cold start problem

## Content based filtering
- anaylze song itself (spectrogram, frequencies over time)
- spectrogram is fed into a convolutional neural network (CNN)

## Natural Language Processing
- scan internet to find articles, blogs, and online reviews talking about artists and songs
- use the descriptors used in those to compute importance of artist or song and generate "cultural vectors" with weight
- the terms associated with the cultural vectors for a song or artist are used to compare similarity between artists and songs a user listens to and freshly released music

# Sources
1. [Recommending music on Spotify with deep learning](https://sander.ai/2014/08/05/spotify-cnns.html)
2. [How Spotify’s Algorithm Manages To Find Your Inner Groove](https://analyticsindiamag.com/how-spotifys-algorithm-manages-to-find-your-inner-groove/)https://analyticsindiamag.com/how-spotifys-algorithm-manages-to-find-your-inner-groove/
3. [How does Spotify's recommendation system work?](https://www.univ.ai/blog/how-does-spotifys-recommendation-system-work#:~:text=Recommendations%20for%20each%20user%20are,algorithm%20on%20every%20song%20vector.)https://www.univ.ai/blog/how-does-spotifys-recommendation-system-work#:~:text=Recommendations%20for%20each%20user%20are,algorithm%20on%20every%20song%20vector.
4. [How Does Spotify Know You So Well?](https://medium.com/@sophiaciocca/spotifys-discover-weekly-how-machine-learning-finds-your-new-music-19a41ab76efe)https://medium.com/@sophiaciocca/spotifys-discover-weekly-how-machine-learning-finds-your-new-music-19a41ab76efe
5. [Music Recommendation System using Spotify Dataset](https://www.kaggle.com/code/vatsalmavani/music-recommendation-system-using-spotify-dataset)
6. 

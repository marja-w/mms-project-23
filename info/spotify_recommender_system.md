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
To overcome the cold start problem, mentioned in the section before, Spotify also analyzes the song itself. Audio analysis can be performed by analyzing a spectrogram of the audio. This is like a picture of a song, it visually encodes the frequencies of the audio signal over time. The x-axis resembles the time dimension, while the y-axis represents the frequency of the signal in kilohertz (kHz), which determines the pitch. The intensity of a pixel resembles loudness in dezibel (dB). The first step when computing spectrograms is applying a Fourier transform (FT) to the soundwave, it maps the time domain of an audio signal to the frequency domain. The FT detangles possibly mixed sounds to the bare signal frequencies by utilizing Fourier's Theorem. In order to detect change in an audio signal over time, the fast FT (FFT) is applied on several specified time windows of the input, resembling the short time FT (STFT). The STFT outputs the spectrogram, the visual representation of the audio clip. This is obtained by stacking the results of the FFTs one after the other, one for every windowIf you are interested to learn more about audio signal processing and how the spectrogram is created, I recommend this video about the Short-Time Fourier Transform: [Short-Time Fourier Transform Explained Easily](https://youtu.be/-Yxj3yfvY-4?si=Vy0dQwBpcpPVVdOW).

![spectrogram](https://github.com/marja-w/mms-project-23/assets/58331624/786c58bf-2582-4bc1-8d3f-d2983e8a6eaa)

Spectrograms are converted to logmel spectrograms by transforming the frequencies of the spectrogram to the mel scale. This scale is non-linear, incorporating the fact that humans can recognize changes of frequency better at lower, than at higher frequencies.  Finally, a logarithmic operation is applied in order to receive logmel spectrograms, which can be used as input for two-dimensional convolution.

![image](https://github.com/marja-w/mms-project-23/assets/58331624/9cd293fb-e015-4e15-ac1c-ec0e4c68ffd9)

The spectrogram is then fed into a convolutional neural network (CNN). A CNN is a neural network architecture that is adapted to work with image data, mostly known for applications like face recognition or object detection. It consists of a feature extraction and a classification component. It extracts features from two dimensional inputs by passing discrete filters with a predefined stride over it. The stride defines how far the filter is pushed each step of the convolution. The features are produced by computing the dot product of the filter and the current region of the image the filter resides on. The filter size, also called kernel size, determines the dimensions of the filter. 

![image](https://github.com/marja-w/mms-project-23/assets/58331624/fea5d6bb-7f1c-434c-b59b-051acd067947)

After the convolution, a pooling layer can be implemented. There are different types of pooling, for example average and max pooling. Using a max pooling layer means that the features are again convolved, but this time the maximum is computed from the current filter zone. Finally, the output matrices of the feature extraction component are flattened and used as input for a fully connected layer, which computes the final output.

Since a spectrogram is essentially an image of the audio, we can use the CNN architecture to analyze it and and predict song features like loudness or beats per minute. More information about the different features that Spotify uses can be found here: [Spotify API - Audio Features](https://developer.spotify.com/documentation/web-api/reference/get-several-audio-features). Since this analysis does not depend on any user data, it can be performed on completely new songs. 

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
6. [Spectrogram](https://en.wikipedia.org/wiki/Spectrogram)
7. [Convolutional Neural Networks - A Beginners Guide](https://towardsdatascience.com/convolution-neural-networks-a-beginners-guide-implementing-a-mnist-hand-written-digit-8aa60330d022)
8. [Convolutional Neural Network | Deep Learning](https://developersbreach.com/convolution-neural-network-deep-learning/)
9. [Understanding the Mel Spectrogram](https://medium.com/analytics-vidhya/understanding-the-mel-spectrogram-fca2afa2ce53)
10. [Convolutional Neural Networks: 1998-2023 Overview](https://www.superannotate.com/blog/guide-to-convolutional-neural-networks)

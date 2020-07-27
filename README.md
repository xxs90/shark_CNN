# Shark-classification-model
Composed of convolutional nueral networks, deep & transfer learning, VGG16 pre-trained model, Keras, and Tensorflow backend

## Introduction
Abundance and distribution data of global shark populations is necessary for effective conservation and management. Direct methods such as surveys and fisheries monitoring are adequate, however they rarely provide species specific indices of population abundance. Yet, there is a plethora of unstructured data that is virtually untapped and can fill this informational gap. Instagram contains over a billion users worldwide and despite the vast amounts of shark images available, there is little research that implements social medias like Instagram for shark conservation. By using this image classification model trained to identify sharks, we can generate inferred shark sightings. Our approach creates abundance and distribution maps that suggest Instagram can be efficiently exploited to reveal spatiotemporal trends in shark populations. Using alternative sources of abundance data is needed for management and conservation of these important data-poor group of marine animals. 
Note -- (This model works best when predicting images originating from Instagram, but is also effective with predicting images from other repositories)

In early trainings, we identified challenges in a binary classification structure that more often than not, pointed to drawings of sharks. After adding a 'drawing' class and increasing the threshold to 0.63, this model can predict shark images with 92% accuracy.

In conjuncture with Instagram web scraping utilizing InstaCrawlR [3] for post collection, this model can be used in a pipeline which maps inferred shark sightings according to predictions and locations mentioned in the post [1]. You can find this repository [here](https://github.com/JeremyFJ/Instagram_sharkSighting)

![image_sample1.png](image_sample1.PNG)

Image examples for the three classes: drawing, not_shark, and shark

## Data
You can download the image repository [here](https://drive.google.com/drive/folders/1ov4wfJUWTLWmqwUbvs8v0L9BUCZed6E4?usp=sharing)

The dataset structure is shown below
```
    ├── dataset                   <- root
        ├── training_set          <- training set folders
        |   ├── drawing        <- image files
        |   ├── not_shark           
        |   ├── shark
        |  
        ├── test_set              <- validation set folders
        |   ├── drawing        <- image files
        |   ├── not_shark           
        |   ├── shark
``` 

## References
- [1] Jenrette J, Liu ZY-C, Hastie T, Ferretti F. Data mining Instagram for tracking global sharkpopulations. Science Advances (TBD). 2020.
- [2] Liu ZY-C, Chamberlin AJ, Shome P, Jones IJ, Riveau G, Jouanard N, Ndione, Sokolow SH, De Leo GA. Identification of snails and parasites of medical importance via convolutional neural network: an application for human schistosomiasis. PLoS neglected tropical diseases. 2019.
- [3] Schroeder J. InstaCrawlR. Crawl public Instagram data using R scripts without API access token. 2018. 

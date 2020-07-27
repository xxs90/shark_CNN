## Run
To run training:
```
python main_train.py
```
Note -- Keep the image directory names static (or make changes to `img_loader.py`)
(1) This script will load images from 7 different directories using csv files listing image designations. These designations specify either training or test set and which class the image is suited for. You can change the configurations within the csv files. 
(2) For fluency, it is easy to add images into the training model once they have been validated. Simply add the images to their designated directories and a list of the files to the csv. 
(3) Once predictions are made on the test set, accuracy and training history is reported in addition to confusion matrix plots for each class.
(4) To view the mistakes during validation, `class_prediction.csv` and `prediction_probability.csv` are generated. You can edit `move_file.py` to identify false negative and false positive labels.

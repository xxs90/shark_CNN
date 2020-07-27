# Inference
To run prediction:
```
python main_inference.py
```
Note -- Add the images you want predicted to `model_predictor/dataset/test_set/shark/` 
(1) Training weights saved as `.h5` are loaded for predictions as well as preprocessed data saved as `.npy` files.
(2) You can adjust the threshold however you want. It is currently set to 0.63.
(3) `class_prediction.csv` is produced and again, `move_file.py` can be run to identify shark and non-shark predictions. You can edit `main_inference.py` to identify drawing predictions as well. 

## Contact
- Data: jjeremy1@vt.edu
- Model: jjeremy1@vt.edu, zacycliu@stanford.edu

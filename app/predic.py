import numpy as np
from skimage.io import imread
from skimage.transform import resize
import joblib
import pickle
import io
from PIL import Image


Categories =  ['bike','car','cup','ice cream cone','pretty sunflower']

def predictFuntion(image_url):
    # test_model = pickle.load(open("Classification_Model.p","rb"))
    test_model = joblib.load("model_joblib")



    flat_data = []
    
    image_bytes = image_url.file.read()
    image = Image.open(io.BytesIO(image_bytes))
    img_array = np.array(image) 
    img_resized = resize(img_array,(150,150,3))
    flat_data.append(img_resized.flatten())
    flat_data = np.array(flat_data) 
    y_output = test_model.predict(flat_data)
    y_output = Categories[y_output[0]] 
    
    return y_output
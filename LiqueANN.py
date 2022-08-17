from tensorflow.keras.models import load_model
import joblib
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def fxn():
    warnings.warn("deprecated", DeprecationWarning)


class LiqueANN():
    
    def __init__(self):
        self.model=load_model('model_and_scaler/LiqueANN.h5')
        self.scaler_filename = "model_and_scaler/LiqueANN_scaler.save"
        self.scaler=joblib.load(self.scaler_filename)
      

    def LiqueANN_run(self,qc_ave,fs_ave,u2_ave,magnitude,pga,gwt):
        inputs=self.scaler.transform([[qc_ave,fs_ave,u2_ave,magnitude,pga,gwt]])
        guess_of_model=np.round(self.model.predict(inputs)).astype(int)
        if guess_of_model == 1:
            print("!! BAD NEWS !! Soil has liquefaction potential under these circumstances")
        else:
            print("!! GOOD NEWS !! Soil has not liquefaction potential under these circumstances")
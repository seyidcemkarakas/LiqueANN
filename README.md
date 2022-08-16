# LiqueANN

ANN model for estimating potential liquefaction of soil.

![alt text](https://cdn.britannica.com/84/152184-050-0C74FF5D/qualities-soil.jpg)

## Model Structure

Inputs:

- qc_ave => Average cone tip resistance (kPa)
- fs_ave => Average sleeve friction resistance (kPa)
- u2_ave => Average pore water pressure (kPa)
- magnitude => Earthquake moment magnitude (Mw)
- pga => Event-specific conditional median peak ground acceleration (g)
- gwt => Groundwater table depth (m)
 
Output:

- manifestation => 0 for "not liquefaction"; 1 for "liquefaction"

## Example Model Usage

Importing necessary libraries.

```
from tensorflow.keras.models import load_model
import joblib
```

Loading ANN Model and Min-Max Scaler from saved files.

```
model = load_model('LiqueANN.h5')
scaler_filename = "LiqueANN_scaler.save"
scaler = joblib.load(scaler_filename) 
```

Entering the values.

```
qc_ave=10333.0
fs_ave=85.0
u2_ave=54.5
magnitude=6.0
pga=0.53
gwt=1.2
```

Scaling entered values with scaler.

```
inputs=scaler.transform([[qc_ave,fs_ave,u2_ave,magnitude,pga,gwt]])
```

Predicting given inputs.

```
guess_of_model=np.round(model.predict(inputs)).astype(int)
Out : array([[1]])
```

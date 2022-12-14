# LiqueANN

ANN model for predicting soil liquefaction potential.
LiqueANN is constructed with 14612 data(11690 data for training, 2922 data for testing). This model is the most data-trained model in the literature.

## What is soil liquefaction ?

The pore water pressure refers to the pressure of the groundwater between the soil grains. Due to the destructive effect of earthquake movements in the earth, the pore water pressure of the soils increases. Liquefaction is the name given to the transition of the soil from the solid state to the liquid state as a result of the increase in pore water pressure in a granular soil in soil mechanics. Due to the increasing water pressure, the contact of the soil particles with each other decreases, with this decrease, the effective stress of the soil decreases and finally a decrease in the bearing capacity occurs.

![alt text](https://cdn.britannica.com/84/152184-050-0C74FF5D/qualities-soil.jpg)

## Model Structure

Inputs:

![alt text](https://ars.els-cdn.com/content/image/1-s2.0-S0013795216301855-gr1.jpg)

 
| Variable  | Explaination |
| ------------- | ------------- |
| qc_ave | Average cone tip resistance (kPa) In the CPT test, the cone is dipped into the ground at a speed of 2 cm/s. As a result of the test, kPa value is recorded at every point where measurement is taken. The average of all these values gives the **qc_ave** value. If there is only the Qc,end value in the available data, half can be taken.  |
| fs_ave | Average sleeve friction resistance (kPa)  |
| u2_ave | Average pore water pressure (kPa)  |
| magnitude | Earthquake moment magnitude (Mw)  |
| pga | Event-specific conditional median peak ground acceleration (g)  |
| gwt | Groundwater table depth (m)  | 



Output:

- manifestation => 0 for "not liquefaction"; 1 for "liquefaction"

## Model Usage

```python
from LiqueANN import LiqueANN
```

Creating model object.
```python
model=LiqueANN()
```

Entering example inputs. Units should be :

| Variable  | Unit |
| ------------- | ------------- |
| qc_ave | kPa  |
| fs_ave | kPa  |
| u2_ave | kPa  |
| magnitude | Mw  |
| pga | g  |
| gwt | m  |



```python
qc_ave=10333.0
fs_ave=85.0
u2_ave=54.5
magnitude=6.0
pga=0.02
gwt=1.2
```

Getting prediction. Output is string. It could be different.
```python
model.LiqueANN_run(qc_ave,fs_ave,u2_ave,magnitude,pga,gwt)
Out : "!! GOOD NEWS !! Soil will not liquefy"
```
## Model Performance

| Metric  | Training data | Testing data |
| ------------- | ------------- |------------- |
| Accuracy | 0.88  | 0.86 |

## Contact

https://www.linkedin.com/in/seyidcem-karaka%C5%9F-534848188/

seyidcemkarakas@gmail.com

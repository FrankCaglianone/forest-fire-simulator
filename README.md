# forest-fire-simulator

Forest fire simulator developed using the Neptyne software, used to build spreadsheets in python.

The code is developed based on the 6 main fire spreading factors in real life:
* Rain🌧️ in mm/h  (+rain -probability)
* Humidity🌫️ in %  (+humidity -probability)
* Temperature🌡️ in celsius  (+temperature +probability)
* Wind💨 in km/h (+wind +probability)
* Wind direction🔀 
* Tree flammability🔥 which depending on the tree type can be
    - Single stem, high flammability, 76%-100%
    - Cluster, medium-high flammability, 51%-75% 
    - Stand, medium flammability, 26%-50%
    - Woodland, low flammability, 1%-25%

From those factors than we calculate the:
*  ### Spreading Time: temperature * wind / rain / humidity
*  ### Burning Time: 1 / tree flammability

## To run the code
Step 1. Copy the python code from forest_fire.py
Step 2. Make an account on [Neptyne.com](https://www.neptyne.com/)
Step 3. Make a new file and paste the code into the code panel in the neptyne simulator
Step 4. Run the code

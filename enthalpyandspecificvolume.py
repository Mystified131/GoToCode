import psychrolib

# Set the unit system, for example to SI (can be either SI or IP) - this needs to be done only once

psychrolib.SetUnitSystem(psychrolib.SI)

# Calculate the dew point temperature for a dry bulb temperature of 25 C and a relative humidity of 80%
TDewPoint = psychrolib.GetTDewPointFromRelHum(25.0, 0.80)
print(f'TDewPoint: {TDewPoint} degree C')

#TDewPoint: 21.309397163661785 degree C
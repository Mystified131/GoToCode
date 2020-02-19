import psychrolib

psychrolib.SetUnitSystem(psychrolib.SI)

print("")

inval = input ("Please enter the dry-bulb temperature: ")
inv = float(inval)

print("")

inval2 = input ("Please enter the pressure: ")
inv2 = float(inval2)

print("")

inval3 = input ("Please enter the humidity ratio: ")
inv3 = float(inval3)

print("")

inval5 = input ("Please enter the kg of dry air and water vapor: ")
totmass = float(inval5)

enth = psychrolib.GetMoistAirEnthalpy(inv, inv3)
ens = str(enth)

vol = psychrolib.GetDryAirVolume(inv, inv2)
ens2 = str(vol)

mvol = psychrolib.GetMoistAirVolume(inv, inv3, inv2)
ens3 = str(mvol)

totvol = float(vol + mvol)
spvol = totvol/totmass

specvol = str(spvol)

print("")

print ("The mpist-air enthalpy is: " + ens)

print("")

print ("The dry-air volume is: " + ens2)

print("")

print ("The moist-air volume is: " + ens3)

print("")

print ("The specific volume is: " + specvol)


#Specific volume is defined as the total volume of dry air and water vapor mixture per kg of dry air and water vapor (SI-units). The specific volume can be expressed as: v = V / ma + mw (11)


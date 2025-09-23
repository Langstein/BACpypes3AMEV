from bacpypes3.object import AnalogValueObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

from bacpypes3.local.cmd import Commandable
from bacpypes3.local.cov import COVIncrementCriteria
from bacpypes3.local.event import OutOfRangeEventAlgorithm
from bacpypes3.local.fault import OutOfRangeFaultAlgorithm
#ToDo Alarm Algorithm

class AV_SW_T_AMEV1(Commandable, AnalogValueObject):
    objectIdentifier=("analogValue", 201)
    objectName="MUSTER_420_VTA01_HZK01_HZ~_EF~01_T~~01_SW~01"
    description="Wärmeversorgungsanlage Verteilanlage Heizkreis Heizwasser Temperatur Sollwert"
    presentValue=0.0
    units="degreesCelsius"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    minPresValue=0.0
    maxPresValue=100.0
    resolution=0.4
    relinquishDefault=2.5
    covIncrement=2.5
    timeDelay=60
    notificationClass=300
    highLimit=65.0
    lowLimit=6.0
    deadband=0.5
    limitEnable=[True, True]
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["Alarm:","Fehler:","Normal:"]
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=0
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    profileName="AV_SW_T_AMEV1 Sollwert Temperatur"
    propertyList=[75,77,79,85,28,111,36,103,81,117,87,104,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,69,65,106,371,168] #,388,389,431,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria

class AV_SN_AMEV1(Commandable, AnalogValueObject):
    objectIdentifier=("analogValue", 201)
    objectName="MUSTER_480_NZA01_TWS01_TW~_WAZ01_ZAE01_SN~01"
    description="GA-Sytem Netzanschluß Trinkwassersystem Trinkwasser Wasserzähler Zähler Seriennummer"
    presentValue=1234567
    units="noUnits"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    minPresValue=1234567
    maxPresValue=1234567
    resolution=1
    relinquishDefault=2.5
    covIncrement=2.5
    timeDelay=0
    notificationClass=300
    highLimit=1234567
    lowLimit=1234567
    deadband=1
    limitEnable=[True, True]
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["Störung:","Fehler:","Normal:"]
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=0
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    profileName="AV_SN_AMEV1 Seriennummer"
    propertyList=[75,77,79,85,28,111,36,103,81,117,87,104,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,69,65,106,371,168] #,388,389,431,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria

class AV_MW_F_AMEV1(Commandable, AnalogValueObject):
    objectIdentifier=("analogValue", 346)
    objectName="MUSTER_480_NZA01_TWS01_TW~_WAZ01_F~~01_MW~01"
    description="GA-Sytem Netzanschluß Trinkwassersystem Trinkwasser Wasserzähler Volumenstrom Messwert"
    presentValue=0.0
    units="cubicMetersPerHour"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    minPresValue=0.0
    maxPresValue=1000.0
    resolution=0.5
    relinquishDefault=0
    covIncrement=25
    timeDelay=0
    notificationClass=300
    highLimit=0.0
    lowLimit=1000.0
    deadband=1.1
    limitEnable=[True, True]
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["Störung:","Fehler:","Normal:"]
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=0
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    profileName="AV_MW_F_AMEV1 Volumenstrom"
    propertyList=[75,77,79,85,28,111,36,103,81,117,87,104,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,69,65,106,371,168] #,388,389,431,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria

class AV_ZW_F_AMEV1(Commandable, AnalogValueObject):
    objectIdentifier=("analogValue", 348)
    objectName="MUSTER_480_NZA01_TWS01_TW~_WAZ01_F~~01_ZW~01"
    description="GA-Sytem Netzanschluß Trinkwassersystem Trinkwasser Wasserzähler Menge Zählwert"
    presentValue=0.0
    units="cubicMeters"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    minPresValue=0.0
    maxPresValue=1000000000.0
    resolution=0.1
    relinquishDefault=0
    covIncrement=1
    timeDelay=0
    notificationClass=300
    highLimit=0.0
    lowLimit=1000000000.0
    deadband=1.1
    limitEnable=[True, True]
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["Störung:","Fehler:","Normal:"]
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=0
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    profileName="AV_ZW_F_AMEV1 Menge Zählwert"
    propertyList=[75,77,79,85,28,111,36,103,81,117,87,104,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,69,65,106,371,168] #,388,389,431,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria
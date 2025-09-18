#from bacpypes3.debugging import ModuleLogger

from bacpypes3.object import AnalogInputObject
from bacpypes3.local.object import Object as _Object
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

from bacpypes3.local.cov import COVIncrementCriteria
from bacpypes3.local.event import OutOfRangeEventAlgorithm
from bacpypes3.local.fault import OutOfRangeFaultAlgorithm
#ToDo Alarm Algorithm

class AI_MW_T_AU_AMEV1(_Object, AnalogInputObject):
    objectIdentifier=("analogInput", 102)
    objectName="MUSTER_GEW_ANLxx°xx_BGRxx_AU~_EF~01_T~~01_MW~01"
    description="MUSTER Gewerk Anlage Baugruppe Medium/Position Aggregat Betriebsmittel Funktion"
    presentValue=0.0
    units="degreesCelsius"
    deviceType="BACtwin AI_MW_T_H_HT_AMEV1 Heizung Hochtemperatur"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    updateInterval=0
    minPresValue=-50.0
    maxPresValue=150.0
    resolution=0.01
    covIncrement=0.2
    timeDelay=1
    notificationClass=300
    highLimit=2
    lowLimit=-20
    deadband=0.2
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
    eventMessageTextsConfig=["Alarm:","Fehler:","Normal"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit, 
    eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="AI_MW_T_H_HT_AMEV1 Temperatur Messung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,118,117,69,65,106,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _event_algorithm: OutOfRangeEventAlgorithm
    _fault_algorithm: OutOfRangeFaultAlgorithm
    _cov_criteria = COVIncrementCriteria
#    _property_monitors = objectIdentifier
    
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        # intrinsic event algorithm
        self._event_algorithm = OutOfRangeEventAlgorithm(None, self)

    def __init__(self, **kwargs):
#        if _debug:
#            AnalogValueObjectFD._debug("__init__ ...")
#            AnalogValueObjectFD._debug("__init__ ...")
        super().__init__(**kwargs)

        # intrinsic fault detection
        #self._fault_algorithm = OutOfRangeFaultAlgorithm(None, self)

class AI_MW_T_H_NT_AMEV1(_Object, AnalogInputObject):
    objectIdentifier=("analogInput", 103)
    objectName="MUSTER_GEW_VTAxx°xx_FBH01_HZ~_EF~01_T~~01_MW~01"
    description="MUSTER Gewerk Verteilanlage Fußbodenheizung Heizwasser Temperatur Messwert"
    presentValue=0.0
    units="degreesCelsius"
    deviceType="BACtwin AI_MW_T_H_NT_AMEV1 Heizung Hochtemperatur"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    updateInterval=0
    minPresValue=-50.0
    maxPresValue=150.0
    resolution=0.01
    covIncrement=0.2
    timeDelay=120
    notificationClass=300
    highLimit=40.0
    lowLimit=6.0
    deadband=0.2
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
    eventMessageTextsConfig=["Alarm:","Fehler:","Normal"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit, 
    eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="AI_MW_T_H_NT_AMEV1 Tem3peratur Messung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,118,117,69,65,106,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,371,168]

    _event_algorithm: OutOfRangeEventAlgorithm
    _fault_algorithm: OutOfRangeFaultAlgorithm
    _cov_criteria = COVIncrementCriteria

class AI_MW_T_H_HT_AMEV1(_Object, AnalogInputObject):
    objectIdentifier=("analogInput", 104)
    objectName="MUSTER_GEW_VTAxx°xx_STH01_HZ~_EF~01_T~~01_MW~01"
    description="MUSTER Gewerk Verteilanlage Statische Heizfläche Heizwasser Temperatur Messwert"
    presentValue=0.0
    units="degreesCelsius"
    deviceType="BACtwin AI_MW_T_H_HT_AMEV1 Heizung Hochtemperatur"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    updateInterval=0
    minPresValue=-50.0
    maxPresValue=150.0
    resolution=0.01
    covIncrement=0.5
    timeDelay=1
    notificationClass=300
    highLimit=90.0
    lowLimit=10.0
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
    eventMessageTextsConfig=["Alarm:","Fehler:","Normal"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit, 
    eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="AI_MW_T_H_HT_AMEV1 Temperatur Messung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,118,117,69,65,106,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,371,168]

    _event_algorithm: OutOfRangeEventAlgorithm
    _fault_algorithm: OutOfRangeFaultAlgorithm
    _cov_criteria = COVIncrementCriteria
#    _property_monitors = objectIdentifier 
    
#    def __init__(self, **kwargs):
#        super().__init__(**kwargs)

        # intrinsic event algorithm
        #self._event_algorithm = OutOfRangeEventAlgorithm(None, self)

    #def __init__(self, **kwargs):
#        if _debug:
#            AnalogValueObjectFD._debug("__init__ ...")
#            AnalogValueObjectFD._debug("__init__ ...")
     #   super().__init__(**kwargs)

        # intrinsic fault detection
      #  self._fault_algorithm = OutOfRangeFaultAlgorithm(None, self)
    
class AI_RW_AMEV1(_Object, AnalogInputObject):
    objectIdentifier=("analogInput", 134)
    objectName="MUSTER_GEW_ANLxx°xx_BGRxx_HZ~_VEN01_MOT01_RW~01"
    description="MUSTER Gewerk Anlage Baugruppe Medium/Position Aggregat Betriebsmittel Funktion"
    presentValue=0.0
    units="percent"
    deviceType="BACtwin AI_RW_AMEV1 Rückführwert"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    updateInterval=1
    minPresValue=0.0
    maxPresValue=100.0
    resolution=0.1
    covIncrement=3
    timeDelay=60
    notificationClass=300
    highLimit=100.0
    lowLimit=0.0
    deadband=3.0
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
    eventMessageTextsConfig=["Alarm:","Fehler:","Normal"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit, 
    eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="AI_RW_AMEV1 Rückführwert"
    propertyList=[75,77,79,85,28,31,111,36,103,81,118,117,69,65,106,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria 

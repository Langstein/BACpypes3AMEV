from bacpypes3.object import AnalogOutputObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *
from bacpypes3.local.cmd import Commandable

from bacpypes3.local.cov import COVIncrementCriteria
from bacpypes3.local.event import CommandFailureEventAlgorithm
from bacpypes3.local.fault import OutOfRangeFaultAlgorithm
#ToDo Alarm Algorithm

class AO_ST_AMEV1(Commandable, AnalogOutputObject):
    objectIdentifier=("analogOutput", 201)
    objectName="MUSTER_420_VTA01_HZK01_HZV_VEN01_MOT01_ST~01"
    description="Wärmeversorgungsanlage Verteilanlage Heizkreis Heizwasser Ventil Stellsignal"
    presentValue=0.0
    units="percent"
    deviceType="BACtwin AO_ST_AMEV1 Stellsignal"
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
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
    ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["","",""]
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=0
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
#    interfaceValue=0
    #valueSource: ValueSource
    #valueSourceArray: ArrayOf(ValueSource, _length=16)
    #lastCommandTime: TimeStamp
    #commandTimeArray: ArrayOf(TimeStamp, _length=16)
    #auditPriorityFilter: OptionalPriorityFilter
    profileName="AO_ST_AMEV1 Stellsignal"
    propertyList=[77,79,85,28,31,111,36,103,81,117,69,65,106,87,104,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,371,431,168] #,387,431,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria 

class AO_SW_F_AMEV1(Commandable, AnalogOutputObject):
    objectIdentifier=("analogOutput", 204)
    objectName="MUSTER_430_VTA01_LKL01_ZU~_VVR01_F~~01_SW~01"
    description="Lufttechnische Anlage Verteilanlage Luftkanal Zuluft Volumenstromregler Volumenstrom Sollwert"
    presentValue=0.0
    units="cubicMetersPerHour"
    deviceType="BACtwin AO_SW_F_AMEV1 Volumenstrom Sollwert"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    minPresValue=0.0
    maxPresValue=100.0
    resolution=0.4
    relinquishDefault=50
    covIncrement=25
    timeDelay=60
    notificationClass=300
    highLimit=5000
    lowLimit=0
    deadband=25
    limitEnable=[True, True]
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
    ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["","",""]
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=0
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
#    interfaceValue=0
    #valueSource: ValueSource
    #valueSourceArray: ArrayOf(ValueSource, _length=16)
    #lastCommandTime: TimeStamp
    #commandTimeArray: ArrayOf(TimeStamp, _length=16)
    #auditPriorityFilter: OptionalPriorityFilter
    profileName="AO_SW_PD_AMEV1 Differenzdruck Sollwert"
    propertyList=[77,79,85,28,31,111,36,103,81,117,69,65,106,87,104,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,371,431,168] #,387,431,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria 

class AO_SW_PD_AMEV1(Commandable, AnalogOutputObject):
    objectIdentifier=("analogOutput", 205)
    objectName="MUSTER_420_VTA01_HZK01_HZV_PPE01_PD~01_SW~01"
    description="Wärmeversorgungsanlage Verteilanlage Heizkreis Heizwasser Pumpe Differenzdruck Sollwert"
    presentValue=0.0
    units="meters"
    deviceType="BACtwin AO_SW_PD_AMEV1 Differenzdruck Sollwert"
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
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
    ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["","",""]
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=0
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
#    interfaceValue=0
    #valueSource: ValueSource
    #valueSourceArray: ArrayOf(ValueSource, _length=16)
    #lastCommandTime: TimeStamp
    #commandTimeArray: ArrayOf(TimeStamp, _length=16)
    #auditPriorityFilter: OptionalPriorityFilter
    profileName="AO_SW_F_AMEV1 Volumenstrom Sollwert"
    propertyList=[77,79,85,28,31,111,36,103,81,117,69,65,106,87,104,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,371,431,168] #,387,431,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria 

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
    deviceType="BACtwin AO_ST_AMEV1 Stellsignal" #geht nicht bei commandable
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
#    currentCommandPriority=16
    #valueSource: ValueSource
    #valueSourceArray: ArrayOf(ValueSource, _length=16)
    #lastCommandTime: TimeStamp
    #commandTimeArray: ArrayOf(TimeStamp, _length=16)
    #auditPriorityFilter: OptionalPriorityFilter
    profileName="AO_ST_AMEV1 Stellsignal"
    propertyList=[77,79,85,28,31,111,36,103,81,117,69,65,106,87,104,22,113,17,45,59,25,52,35,0,72,130,351,352,353,355,354,356,357,371,431,168] #,387,431,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria 

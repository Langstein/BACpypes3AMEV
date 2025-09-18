from bacpypes3.object import BinaryValueObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

from bacpypes3.local.cmd import Commandable
from bacpypes3.local.cov import COVIncrementCriteria
from bacpypes3.local.event import ChangeOfStateEventAlgorithm
from bacpypes3.local.fault import CharacterStringFaultAlgorithm
#ToDo Alarm Algorithm

class BV_SB_NSP_AMEV1(Commandable, BinaryValueObject):
    objectIdentifier=("binaryValue", 614)
    objectName="MUSTER_480_ASP01°01_#####_###_AS~01_#####_REV01"
    description="Gebäudeautomationssystem Automationsschwerpunkt AS Revisionsschalter"
    presentValue=0
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    inactiveText="Normal"
    activeText="Gesperrt"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=600
    alarmValue="active"
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType=1
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
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BV_SB_NSP_AMEV1"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria 


from bacpypes3.object import BinaryValueObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

from bacpypes3.local.cmd import Commandable
from bacpypes3.local.cov import COVIncrementCriteria
from bacpypes3.local.event import ChangeOfStateEventAlgorithm
from bacpypes3.local.fault import CharacterStringFaultAlgorithm
#ToDo Alarm Algorithm

class BV_ENT_AMEV1(Commandable, BinaryValueObject):
    objectIdentifier=("binaryInput", 619)
    objectName="MUSTER_480_ASPxx°xx_ASVxx_###_SSK01_UBE01_ETR01"
    description="Muster Entriegelung"
    presentValue="inactive"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    inactiveText="Inaktiv"
    activeText="Aktiv"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    minimumOffTime=0
    minimumOnTime=1
    timeDelay=0
    notificationClass=500
    alarmValue="active"
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""] #ArrayOf(CharacterString, _length=3),
    eventMessageTextsConfig=["Gefallen:","Fehler:","Normal:"] #ArrayOf(CharacterString, _length=3)
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BV_ENT_AMEV1 Entriegelung UBE"
    propertyList=[75,77,79,85,28,31,111,36,103,81,46,4,16,15,115,33,114,66,67,87,104,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BV_SB_NSP_AMEV1(Commandable, BinaryValueObject):
    objectIdentifier=("binaryInput", 614)
    objectName="MUSTER_480_ASPxx°xx_ASVxx_###_SSK01_UBE01_ETR01"
    description="Muster Nachspeisung"
    presentValue="inactive"
    statusFlags=[False, False, False, False]
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
    minimumOffTime=0
    minimumOnTime=1
    timeDelay=0
    notificationClass=450
    alarmValue="active"
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""] #ArrayOf(CharacterString, _length=3),
    eventMessageTextsConfig=["Gefallen:","Fehler:","Normal:"] #ArrayOf(CharacterString, _length=3)
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BV_SB_NSP_AMEV1 Freigabe Nachspisung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,46,4,16,15,115,33,114,66,67,87,104,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BV_SM_NAF_AMEV1(Commandable, BinaryValueObject):
    objectIdentifier=("binaryInput", 635)
    objectName="MUSTER_410_ASPxx°xx_ASVxx_###_WAZ01_UBE01_ETR01"
    description="Muster Normal|Ausgefallen"
    presentValue="inactive"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    inactiveText="Normal"
    activeText="Ausgefallen"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    minimumOffTime=0
    minimumOnTime=1
    timeDelay=0
    notificationClass=300
    alarmValue="active"
    eventEnable=[True, True, True]
    ackedTransitions=[True,True,True]
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""] #ArrayOf(CharacterString, _length=3),
    eventMessageTextsConfig=["Störung:","Fehler:","Normal:"] #ArrayOf(CharacterString, _length=3)
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BV_SM_NAF_AMEV1 Störmelung Ausgefallen"
    propertyList=[75,77,79,85,28,31,111,36,103,81,46,4,16,15,115,33,114,66,67,87,104,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria


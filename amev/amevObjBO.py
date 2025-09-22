from bacpypes3.object import BinaryOutputObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

from bacpypes3.local.cmd import Commandable
from bacpypes3.local.cov import COVIncrementCriteria
from bacpypes3.local.event import CommandFailureEventAlgorithm
#from bacpypes3.local.fault import *
#ToDo Alarm Algorithm

class BO_SB_AMEV1(Commandable, BinaryOutputObject):
    objectIdentifier=("binaryOutput", 501)
    objectName="MUSTER_430_LTAxx_ERHxx_HZV_PPExx_MOTxx_SB~01"
    description="Muster Lufttechnische Anlagen Lüftungsanlage Erhitzer Heizwasser-Vorlauf Pumpe Motor Schaltbefehl"
    presentValue="inactive"
    deviceType="BACtwin Schaltbefehl"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="normal"
    inactiveText="Aus"
    activeText="Ein"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    minimumOffTime=120
    minimumOnTime=30
    relinquishDefault="inactive"
    timeDelay=60
    notificationClass=600
    feedbackValue="inactive"
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
    #currentCommandPriority=16
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BO_SB_AMEV1 Schaltbefehl"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,431,168]
    _cov_criteria = COVIncrementCriteria     

class BO_SB_KL_AMEV1(Commandable, BinaryOutputObject):
    objectIdentifier=("binaryOutput", 505)
    objectName="MUSTER_420_VTAxx_#####_HZV_VENxx_MOTxx_SB~01"
    description="Muster Wärmeversorgung Verteilanlage Heizwasser-Vorlauf Ventil Motor Schaltbefehl"
    presentValue="inactive"
    deviceType="BACtwin Schaltbefehl"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="normal"
    inactiveText="Auf"
    activeText="Zu"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    minimumOffTime=120
    minimumOnTime=30
    relinquishDefault="inactive"
    timeDelay=60
    notificationClass=300
    feedbackValue="inactive"
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
    #currentCommandPriority=16
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BO_SB_KL_AMEV1 Schaltbefehl"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,431,168]
    _cov_criteria = COVIncrementCriteria     

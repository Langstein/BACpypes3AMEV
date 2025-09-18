from bacpypes3.object import BinaryInputObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

from bacpypes3.local.cov import COVIncrementCriteria
from bacpypes3.local.event import ChangeOfStateEventAlgorithm
from bacpypes3.local.fault import CharacterStringFaultAlgorithm
#ToDo Alarm Algorithm

class BI_GM_BSK_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 402)
    objectName="MUSTER_400_#####°##_#####_###_BSK01_#####_GM~01"
    description="Muster BSK Gefahrmeldung"
    presentValue="inactive"
    deviceType="BACtwin BI_GM_BSK_AMEV1 Gefahrmeldung"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Gefallen"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=150
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
    profileName="BI_GM_BSK_AMEV1 Gefahrmeldung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_SM_NOT_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 403)
    objectName="MUSTER_400_#####°##_#####_###_NTA01_SLT01_GM~01"
    description="Muster Not-Aus Störmeldung"
    presentValue="inactive"
    deviceType="BACtwin BI_SM_NOT_AMEV1 Störmeldung"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Not-Aus"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=150
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
    profileName="BI_SM_NOT_AMEV1 Störmeldung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_AM_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 404)
    objectName="MUSTER_400_#####°##_#####_###_#####_#####_AM~01"
    description="Muster Alarmmeldung"
    presentValue="inactive"
    deviceType="BACtwin BI_AM_AMEV1 Alarmmeldung"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Alarm"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=200
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
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_AM_AMEV1 Alarmmeldung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_AM_ZOF_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 405)
    objectName="MUSTER_400_#####°##_#####_###_FEN01_GS~01_AM~01"
    description="Muster Alarmmeldung Auf"
    presentValue="inactive"
    deviceType="BACtwin BI_AM_ZOF_AMEV1 Alarmmeldung Auf"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Zu"
    activeText="Auf"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=1
    notificationClass=200
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
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_AM_AMEV1 Alarmmeldung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_SM_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 406)
    objectName="MUSTER_400_#####°##_#####_###_#####_#####_SM~01"
    description="Muster Störmeldung"
    presentValue="inactive"
    deviceType="BACtwin BI_SM_AMEV1 Störmeldung"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Störung"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
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
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["Störung:","Fehler:","Normal:"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_SM_AMEV1 Störmeldung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_SM_NAF_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 407)
    objectName="MUSTER_400_#####°##_#####_###_#####_ZAE01_SM~01"
    description="Muster Störmeldung Ausgefallen"
    presentValue="inactive"
    deviceType="BACtwin BI_SM_NAF_AMEV1 Ausgefallen"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Ausgefallen"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
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
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["Ausgefallen:","Fehler:","Normal:"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_SM_NAF_AMEV1 Ausgefallen"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_SM_LU_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 408)
    objectName="MUSTER_400_#####°##_#####_###_BSK01_#####_SM~01"
    description="Muster Störmeldung Ausgelöst"
    presentValue="inactive"
    deviceType="BACtwin BI_SM_LU_AMEV1 Ausgelöst"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Ausgelöst"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
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
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["Ausgelöst:","Fehler:","Normal:"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_SM_LU_AMEV1 Ausgelöst"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_SM_SYS_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 409)
    objectName="MUSTER_480_ASP01°01_#####_###_AS~01_PTB01_SM~01"
    description="Gebäudeautomationssystem Automationsschwerpunkt AS Pufferbaterie Störmeldung"
    presentValue="inactive"
    deviceType="BACtwin BI_SM_SYS_AMEV1 Störmeldung"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Störung"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=600
    alarmValue="active"
    eventEnable=[True,True,True]
    ackedTransitions=[True,True,True]
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""] #ArrayOf(CharacterString, _length=3),
    eventMessageTextsConfig=["Störung:","Fehler:","Normal:"] #ArrayOf(CharacterString, _length=3)
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=ObjectPropertyReference
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_SM_SYS_AMEV1 Störmeldung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_SM_LU_IH_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 410)
    objectName="MUSTER_400_#####°##_#####_###_#####_F~~01_SM~01"
    description="Muster Störmeldung Luftstromüberwachung"
    presentValue="inactive"
    deviceType="BACtwin BI_SM_LU_IH_AMEV1 Luftstromüberwachung"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Luftströmung"
    activeText="KeineLuftströmung"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=200
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
    eventMessageTextsConfig=["Keine Luftströmung:","Fehler:","Normal:"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit #Anlagenschaltbefehl
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_SM_LU_IH_AMEV1 Luftstromüberwachung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_ANO_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 411)
    objectName="MUSTER_400_#####°##_#####_###_TUR01_#####_ANO01"
    description="Muster Anormal"
    presentValue="inactive"
    deviceType="BACtwin BI_ANO_AMEV1 Anormal"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Anormal"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=350
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
    eventMessageTextsConfig=["Anormal:","Fehler:","Normal:"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit #Anlagenschaltbefehl
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_ANO_AMEV1 Anormal"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_SAB_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 412)
    objectName="MUSTER_400_#####°##_#####_###_TUR01_#####_SAB01"
    description="Muster Sabotagealarm"
    presentValue="inactive"
    deviceType="BACtwin BI_SAB_AMEV1 Sabotagealarm"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="reverse"
    inactiveText="Normal"
    activeText="Sabotage"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=350
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
    eventMessageTextsConfig=["Sabotagealarm:","Fehler:","Normal:"]
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit #Anlagenschaltbefehl
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_SAB_AMEV1 Sabotagealarm"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_BM_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 414)
    objectName="MUSTER_###_#####°##_#####_###_#####_#####_BM~01"
    description="Muster Betriebsmeldung"
    presentValue="inactive"
    deviceType="BACtwin BI_BM_AMEV1 Betriebsmeldung"
    statusFlags=[False, False, False, False]
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
    timeDelay=60
    notificationClass=600
    alarmValue="active"
    eventEnable=[True,True,True]
    ackedTransitions=[True,True,True]
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""] #ArrayOf(CharacterString, _length=3),
    eventMessageTextsConfig=["Alarm:","Fehler:","Normal:"] #ArrayOf(CharacterString, _length=3)
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=ObjectPropertyReference
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_BM_AMEV1 Betriebmeldung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria

class BI_RM_AMEV1(BinaryInputObject):
    objectIdentifier=("binaryInput", 442)
    objectName="MUSTER_###_#####°##_#####_###_#####_#####_RM~01"
    description="Muster Rückmeldung"
    presentValue="inactive"
    deviceType="BACtwin BI_RM_AMEV1 Rückmeldung"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    polarity="normal"
    inactiveText="Zu"
    activeText="Auf"
    changeOfStateTime= DateTime(date=Date("2025-01-01")._value,time=(23, 59, 59, 99))
    changeOfStateCount=0
    timeOfStateCountReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    elapsedActiveTime=1
    timeOfActiveTimeReset=DateTime(date=Date().now()._value, time=Time().now()._value)
    timeDelay=60
    notificationClass=600
    alarmValue="active"
    eventEnable=[True,True,True]
    ackedTransitions=[True,True,True]
    notifyType=1
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""] #ArrayOf(CharacterString, _length=3),
    eventMessageTextsConfig=["Alarm:","Fehler:","Normal:"] #ArrayOf(CharacterString, _length=3)
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=ObjectPropertyReference
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    #interfaceValue: OptionalReal
    #faultHighLimit: Real
    #faultLowLimit: Real
    profileName="BI_RM_AMEV1 Rückmeldung"
    propertyList=[75,77,79,85,28,31,111,36,103,81,84,46,4,16,15,115,33,114,113,17,6,35,0,72,130,351,352,353,355,354,356,357,371,168]
    _cov_criteria = COVIncrementCriteria


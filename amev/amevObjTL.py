from bacpypes3.object import TrendLogObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

class TL_AN_P_AMEV1(TrendLogObject):
    objectIdentifier=("trendLog",101)
    objectName="MUSTER_TL~01" 
    description="Muster Datenaufzeichnung analog Polling"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    enable=True
    startTime=DateTime(date=(125,1,1,255), time=(0,0,0,0))
    stopTime=DateTime(date=Date("2050-12-31")._value, time=Time("23:59:59.99")._value)
    logDeviceObjectProperty=DeviceObjectPropertyReference(
        objectIdentifier="analog-input,1",
        propertyIdentifier=PropertyIdentifier.presentValue,
    )
    logInterval=90000
    covResubscriptionInterval=3600
    # FIXME:clientCovIncrement="defaultIncrement"
    stopWhenFull=False
    bufferSize=1000
    #logBuffer=[log_record1,log_record2,log_record3] #Fixme ReadRange
    recordCount=1
    totalRecordCount=1
    loggingType="polled"
    alignIntervals=False
    intervalOffset=2
    trigger=False
    notificationThreshold=401
    recordsSinceNotification=0
    lastNotifyRecord=0
    notificationClass=700
    eventEnable=[0,1,1]
    ackedTransitions=[0,0,0]
    notifyType="event"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["", "", ""]
    eventMessageTexts=ArrayOf(CharacterString)(["","",""])
    eventMessageTextsConfig=ArrayOf(CharacterString)(["Event: TL AN","Fehler: TL AN","Normal: TL AN"])
    eventDetectionEnable=False
    eventAlgorithmInhibit=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    reliabilityEvaluationInhibit=False
    profileName="TL_AN_P_AMEV1 Datenaufzeichnung analog Polling"
    propertyList=ArrayOf(PropertyIdentifier)([75,77,79,28,133,142,143,132,134,128,127,144,126,131,141,145,197,205,111,103,137,140,173,36,17,35,0,72,130,351,352,353,371,168])

class TL_AN_C_AMEV1(TrendLogObject):
    objectIdentifier=("trendLog",102)
    objectName="MUSTER_TL~02" 
    description="Muster Datenaufzeichnung analog COV"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    enable=True
    startTime=DateTime(date=(125,1,1,255), time=(0,0,0,0))
    stopTime=DateTime(date=Date("2050-12-31")._value, time=Time("23:59:59.99")._value)
    logDeviceObjectProperty=DeviceObjectPropertyReference(
        objectIdentifier="analog-input,1",
        propertyIdentifier=PropertyIdentifier.presentValue,
    )
    logInterval=0
    covResubscriptionInterval=3600
    # FIXME:clientCovIncrement="defaultIncrement"
    stopWhenFull=False
    bufferSize=1000
    #logBuffer=[log_record1,log_record2,log_record3] #Fixme ReadRange
    recordCount=1
    totalRecordCount=1
    loggingType="cov"
    alignIntervals=False
    intervalOffset=2
    trigger=False
    notificationThreshold=402
    recordsSinceNotification=0
    lastNotifyRecord=0
    notificationClass=700
    eventEnable=[0,1,1]
    ackedTransitions=[0,0,0]
    notifyType="event"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["", "", ""]
    eventMessageTexts=ArrayOf(CharacterString)(["","",""])
    eventMessageTextsConfig=ArrayOf(CharacterString)(["Event: TL AN","Fehler: TL AN","Normal: TL AN"])
    eventDetectionEnable=False
    eventAlgorithmInhibit=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    reliabilityEvaluationInhibit=False
    profileName="TL_AN_C_AMEV1 Datenaufzeichnung analog COV"
    propertyList=ArrayOf(PropertyIdentifier)([75,77,79,28,133,142,143,132,134,128,127,144,126,131,141,145,197,205,111,103,137,140,173,36,17,35,0,72,130,351,352,353,371,168])

class TL_AN_ZW_AMEV1(TrendLogObject):
    objectIdentifier=("trendLog",103)
    objectName="MUSTER_TL~03" 
    description="Muster Datenaufzeichnung Zählwert"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    enable=True
    startTime=DateTime(date=(125,1,1,255), time=(0,0,0,0))
    stopTime=DateTime(date=Date("2050-12-31")._value, time=Time("23:59:59.99")._value)
    logDeviceObjectProperty=DeviceObjectPropertyReference(
        objectIdentifier="analog-input,1",
        propertyIdentifier=PropertyIdentifier.presentValue,
    )
    logInterval=90000
    covResubscriptionInterval=3600
    # FIXME:clientCovIncrement="defaultIncrement"
    stopWhenFull=False
    bufferSize=1000
    #logBuffer=[log_record1,log_record2,log_record3] #Fixme ReadRange
    recordCount=1
    totalRecordCount=1
    loggingType="polled"
    alignIntervals=False
    intervalOffset=2
    trigger=False
    notificationThreshold=401
    recordsSinceNotification=0
    lastNotifyRecord=0
    notificationClass=700
    eventEnable=[0,1,1]
    ackedTransitions=[0,0,0]
    notifyType="event"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["", "", ""]
    eventMessageTexts=ArrayOf(CharacterString)(["","",""])
    eventMessageTextsConfig=ArrayOf(CharacterString)(["Event: TL AN","Fehler: TL AN","Normal: TL AN"])
    eventDetectionEnable=False
    eventAlgorithmInhibit=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    reliabilityEvaluationInhibit=False
    profileName="TL_AN_ZW_AMEV1 Datenaufzeichnung analog Zählwerte"
    propertyList=ArrayOf(PropertyIdentifier)([75,77,79,28,133,142,143,132,134,128,127,144,126,131,141,145,197,205,111,103,137,140,173,36,17,35,0,72,130,351,352,353,371,168])

class TL_BN_AMEV1(TrendLogObject):
    objectIdentifier=("trendLog",104)
    objectName="MUSTER_TL~04" 
    description="Muster Datenaufzeichnung binär"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    enable=True
    startTime=DateTime(date=(125,1,1,255), time=(0,0,0,0))
    stopTime=DateTime(date=Date("2050-12-31")._value, time=Time("23:59:59.99")._value)
    logDeviceObjectProperty=DeviceObjectPropertyReference(
        objectIdentifier="binary-input,1",
        propertyIdentifier=PropertyIdentifier.presentValue,
    )
    logInterval=0
    covResubscriptionInterval=3600
    # FIXME:clientCovIncrement="defaultIncrement"
    stopWhenFull=False
    bufferSize=1000
    #logBuffer=[log_record1,log_record2,log_record3] #Fixme ReadRange
    recordCount=1
    totalRecordCount=1
    loggingType="cov"
    alignIntervals=False
    intervalOffset=2
    trigger=False
    notificationThreshold=402
    recordsSinceNotification=0
    lastNotifyRecord=0
    notificationClass=700
    eventEnable=[0,1,1]
    ackedTransitions=[0,0,0]
    notifyType="event"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["", "", ""]
    eventMessageTexts=ArrayOf(CharacterString)(["","",""])
    eventMessageTextsConfig=ArrayOf(CharacterString)(["Event: TL AN","Fehler: TL AN","Normal: TL AN"])
    eventDetectionEnable=False
    eventAlgorithmInhibit=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    reliabilityEvaluationInhibit=False
    profileName="TL_AN_BN_AMEV1 Datenaufzeichnung binär"
    propertyList=ArrayOf(PropertyIdentifier)([75,77,79,28,133,142,143,132,134,128,127,144,126,131,141,145,197,205,111,103,137,140,173,36,17,35,0,72,130,351,352,353,371,168])


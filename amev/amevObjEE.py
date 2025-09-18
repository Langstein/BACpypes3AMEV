from bacpypes3.object import EventEnrollmentObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

from bacpypes3.local.event import ChangeOfBitstringEventAlgorithm, ChangeOfValueEventAlgorithm, ChangeOfStateEventAlgorithm
from bacpypes3.local.event import CommandFailureEventAlgorithm, FloatingLimitEventAlgorithm
from bacpypes3.local.fault import *

class EE_CCP_AMEV1(EventEnrollmentObject):
    """
    This is an EventEnrollment Object to monitor CurrentCommandPriority changed to manual of an output Object 
    """
    objectIdentifier=("eventEnrollment", 201)
    objectName="MUSTER_CCP_1"
    description="Test Event Enrollment CurrentCommendPriority"
    statusFlags=[False,False,False,False]
    eventState="normal"
    reliability="noFaultDetected"
    eventParameters=EventParameter(
        changeOfState=EventParameterChangeOfState(
            timeDelay=3,
            listOfValues=[
                PropertyStates(unsignedValue=1),
                PropertyStates(unsignedValue=2),
                PropertyStates(unsignedValue=3),
                PropertyStates(unsignedValue=4),
                PropertyStates(unsignedValue=5),
                PropertyStates(unsignedValue=7),
                PropertyStates(unsignedValue=8),
             ])
    )
    objectPropertyReference=DeviceObjectPropertyReference(
        objectIdentifier="binaryOutput,501",
        propertyIdentifier=PropertyIdentifier.currentCommandPriority,
        #propertyArrayIndex=11,
        #deviceIdentifier=this_device.objectIdentifier,
    )
    notificationClass=300
    eventEnable=[True,True,True]
    ackedTransitions=[True, True, True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=ArrayOf(CharacterString)(["","",""])
    eventMessageTextsConfig=ArrayOf(CharacterString)(["","",""])
    faultType="none"
    #FIXME faultParameters=FaultParameter(["none"])
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    propertyList=[75,77,79,28,37,72,83,78,36,35,0,17,130,351,352,353,355,354,356,111,103,371,168] #,359,358,357,371,486,485,168]
    profileName="EE-CCP Handmeldung"

class EE_COS_AMEV1(EventEnrollmentObject):
    objectIdentifier=("eventEnrollment", 202)
    objectName="Object_202_EE"
    description="Test Event Enrollment ChangeOfState"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    eventParameters=EventParameter(
        changeOfState=EventParameterChangeOfState(
            timeDelay=3,
            listOfValues=[PropertyStates(
                binaryValue="active"
            )]
        )
    )
    objectPropertyReference=DeviceObjectPropertyReference(
        objectIdentifier="binaryInput,3",
        propertyIdentifier=PropertyIdentifier.presentValue,
        #propertyArrayIndex=11,
        #deviceIdentifier=this_device.objectIdentifier,
    )
    notificationClass=300
    eventEnable=[True, True, True]
    ackedTransitions=[True, True, True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["","",""]
    faultType="none"
    #FIXME faultParameters=FaultParameter(["none"])
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    propertyList=[75,77,79,28,37,72,83,78,36,35,0,17,130,351,352,353,355,354,356,111,103,371,168]#,359,358,357,371,486,485,168]
    profileName="EE-COS Meldung"

class EE_OOR_AMEV1(EventEnrollmentObject):
    objectIdentifier=("eventEnrollment",201)
    objectName="MUSTER_eeo1"
    description="test event enrollment"
    eventType="outOfRange"
    notifyType="alarm"  # event, ackNotification
    eventParameters=EventParameter(
        outOfRange=EventParameterOutOfRange(
            timeDelay=10, lowLimit=0.0, highLimit=100.0, deadband=5.0,
        ),
    )
    objectPropertyReference=DeviceObjectPropertyReference(
        objectIdentifier="analog-input,102",
        propertyIdentifier=PropertyIdentifier.presentValue,
    )
    eventState="normal"
    eventEnable=[True,True,True] # toOffNormal, toFault, toNormal
    ackedTransitions=[True,True,True]  # toOffNormal, toFault, toNormal
    notificationClass=300
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["", "", ""]
    eventMessageTextsConfig=["", "", ""]
    eventDetectionEnable=False
    # eventAlgorithmInhibitReference=ObjectPropertyReference
    # eventAlgorithmInhibit=False
    timeDelayNormal=1
    statusFlags=[False, False, False, False]  # inAlarm, fault, overridden, outOfService
    reliability="noFaultDetected"
    # faultType=
    # faultParameters=
    reliabilityEvaluationInhibit=False
    propertyList=[75,77,79,28,37,72,83,78,36,35,0,17,130,351,352,353,355,354,356,111,103,371,168]#,359,358,357,371,486,485,168]
    profileName="EE-OOR Meldung"

class EE_FLIM_AMEV1(EventEnrollmentObject):
    objectIdentifier=("eventEnrollment", 204)
    objectName="MUSTER_FLIM_1"
    description="Test Enrollment Floating Limit"
    eventType="floatingLimit"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
# +++ +++ FIXME +++ +++    
    #eventParameters=EventParameter(changeOfBitstring=ee90_evp_cob)
    eventParameters=EventParameter(
        floatingLimit=EventParameterFloatingLimit(
            timeDelay=60,
            setpointReference = DeviceObjectPropertyReference(
                objectIdentifier="analogInput,134",
                propertyIdentifier=PropertyIdentifier.presentValue,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
            lowDiffLimit = 3,
            highDiffLimit = 3,
            deadband = 0.5
        )
    )
    objectPropertyReference=DeviceObjectPropertyReference(
        objectIdentifier="analogOutput,201",
        propertyIdentifier=PropertyIdentifier.presentValue,
        #propertyArrayIndex=11,
        #deviceIdentifier=this_device.objectIdentifier,
    )
    notificationClass=300
    eventEnable=[True, True, True]
    ackedTransitions=[True, True, True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["","",""]
    faultType="none"
    #FIXME faultParameters=FaultParameter(["none"]),
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    profileName="EE-FLIM Abweichung"
    propertyList=[75,77,79,28,37,72,83,78,36,35,0,17,130,351,352,353,355,354,356,111,103,371,168]#,359,358,357,371,486,485,168]

class EE_COB_AMEV1(EventEnrollmentObject):
    objectIdentifier=("eventEnrollment", 205)
    objectName="Muster_COS1"
    description="Test Event Enrollment ChangeOfBitstring"
    eventType="changeOfBitstring"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    #eventParameters=EventParameter(
    #    changeofbitstring=EventParameterChangeOfBitstring(
    #        timeDelay = 60,
    #        bitmask = [],#[False,False,True,True]
    #        listOfBitstringValues = []#([False,False,True,True])
    #        )
    #    )
    objectPropertyReference=DeviceObjectPropertyReference(
        objectIdentifier="analogOutput,1",
        propertyIdentifier=PropertyIdentifier.statusFlags,
        #propertyArrayIndex=11,
        #deviceIdentifier=this_device.objectIdentifier,
    )
    notifyType="alarm"  # event, ackNotification
    notificationClass=500
    eventEnable=[True, True, True]
    ackedTransitions=[True, True, True]
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["", "", ""]
    eventMessageTextsConfig=["","",""]
    faultType="none"
    #FIXME: faultParameters=FaultParameter(["none"])
    eventDetectionEnable=True
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    profileName="EE-COB Handmeldung"
    propertyList=[75,77,79,28,37,72,83,78,36,35,0,17,130,351,352,353,355,354,356,111,103,371,168]#,359,358,357,371,486,485,168]

class EE_CMDF_AMEV1(EventEnrollmentObject):
    objectIdentifier=("eventEnrollment", 208)
    objectName="Object_208_EE"
    description="Event Enrollment CommandFailture Description 1"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected" 
    eventParameters=EventParameter(
        commandFailure=EventParameterCommandFailure(
            timeDelay=3,
            feedbackPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryInput,1",
                propertyIdentifier=PropertyIdentifier.presentValue,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            )
        )
    )
    objectPropertyReference=DeviceObjectPropertyReference(
        objectIdentifier="binaryOutput,1",
        propertyIdentifier=PropertyIdentifier.presentValue,
        #propertyArrayIndex=11,
        #deviceIdentifier=this_device.objectIdentifier,
    )
    notificationClass=300
    eventEnable=[True, True, True]
    ackedTransitions=[True, True, True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=["","",""]
    eventMessageTextsConfig=["","",""]
    faultType="none"
    #FIXME faultParameters=FaultParameter(["none"])
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    profileName="EE-CMDF Ausführkontrolle"
    propertyList=[75,77,79,28,37,72,83,78,36,35,0,17,130,351,352,353,355,354,356,111,103,371,168]#,359,358,357,371,486,485,168]            


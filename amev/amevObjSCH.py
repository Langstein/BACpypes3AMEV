from bacpypes3.object import ScheduleObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

class SCH_BN_AMEV1(ScheduleObject):
    objectIdentifier=("schedule", 201)
    objectName="MUSTER_400_#####°##_#####_###_#####_#####_SCH01"
    description="Muster Zeitpan binär"
    presentValue=Enumerated(0)
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    eventDetectionEnable=False
    notificationClass=300
    eventEnable=[True, True, True]
    ackedTransitions=[True, True, True]
    notifyType="alarm"
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=ArrayOf(CharacterString)(["","",""])
    eventMessageTextsConfig=ArrayOf(CharacterString)(["Alarm: SCH 1","Fehler: SCH 1","Normal: SCH 1"])
    effectivePeriod=DateRange(
        startDate=(255, 255, 255, 255),
        endDate=(255, 255, 255, 255),
    )
    weeklySchedule=[
        DailySchedule(
            daySchedule=[
                TimeValue(time=(6, 30, 0, 0), value=Enumerated(1)),
                TimeValue(time=(18, 30, 0, 0), value=Null(())),
                #TimeValue(time=(17, 0, 0, 0), value=Integer(42)),
                #TimeValue(time=(0,0,0,0), value=Null()),
                ]
         
            ),
        ]* 7
    #Neujahr=CalendarEntry(date=(255,1,1,255))
    exceptionSchedule=[]
            #SpecialEvent(
                #    calendarEntry = CalendarEntry(date=(255,1,1,255))
                #    )
    priorityForWriting=12
    scheduleDefault=Enumerated(0)
    #weeklySchedule: ArrayOf(DailySchedule, _length=7)
    #exceptionSchedule: ArrayOf(SpecialEvent)
    listOfObjectPropertyReferences=[
        DeviceObjectPropertyReference(
            objectIdentifier="binaryOutput,100",
            propertyIdentifier=PropertyIdentifier.presentValue,
            #propertyArrayIndex=11,
            #deviceIdentifier=this_device.objectIdentifier,
            ),
        DeviceObjectPropertyReference(
            objectIdentifier="binaryOutput,200",
            propertyIdentifier=PropertyIdentifier.presentValue,
            #propertyArrayIndex=11,
            deviceIdentifier="device,200",
            ), # Objekte auf fremden Device
    ]# ListOf(DeviceObjectPropertyReference)
    #reliabilityEvaluationInhibit: Boolean
    propertyList=[75,77,79,85,28,32,123,38,174,54,88,111,103,81,371,168] #,353,17,35,36,0,72,130,351,352,357,371,486,485,168,

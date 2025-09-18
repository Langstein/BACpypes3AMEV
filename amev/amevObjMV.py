from bacpypes3.object import MultiStateValueObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *
from bacpypes3.local.cmd import Commandable

from bacpypes3.local.cov import COVIncrementCriteria
from bacpypes3.local.event import ChangeOfStateEventAlgorithm
#from bacpypes3.local.fault import Chan
#ToDo Alarm Algorithm


class MV_GS_AEM_AMEV1(Commandable, MultiStateValueObject):
    Null = Null()
    objectIdentifier=("multiStateValue", 902)
    objectName="MUSTER_420_VTA01_HZK01_###_####_#####_AST01"
    description="Wärmeversorgungsanlage Verteilanlage Heizkreis Heizwasser Anlagensteuerung"
    presentValue=3
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    numberOfStates=3
    stateText=["Aus","Ein","Auto"]
    #priorityArray=PriorityArray([Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null(),Null()])
    #priorityArray=[Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null]
    relinquishDefault=1
    timeDelay=5
    notificationClass=500
    eventEnable=[True, True, True]
    ackedTransitions=[True, True, True]
    notifyType="alarm"
    alarmValues=ListOf(Unsigned)([1,2])
    faultValues=ListOf(Unsigned)([])
    eventTimeStamps=[
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
        ]
    eventMessageTexts=ArrayOf(CharacterString)(["","",""])
    eventMessageTextsConfig=ArrayOf(CharacterString)(["","",""])
    eventDetectionEnable=False
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit
    #eventAlgorithmInhibit=False
    timeDelayNormal=1
    reliabilityEvaluationInhibit=False
    profileName="MV_GS_AEM_AMEV1 Gesamtanlagensteuerung"
    #currentCommandPriority=12
    propertyList=[75,77,79,85,28,111,36,103,81,74,110,87,104,113,17,7,39,35,0,72,130,351,352,353,355,354,356,357,371,431,168] #,433,434,432,430,486,485,
    _cov_criteria = COVIncrementCriteria 

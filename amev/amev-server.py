"""
Simple example that has a device object and an additional custom object.
"""

import asyncio

from bacpypes3.debugging import ModuleLogger
from bacpypes3.argparse import SimpleArgumentParser
from bacpypes3.ipv4.app import Application

from bacpypes3.object import * #AnalogInputObject, AnalogOutputObject
from bacpypes3.basetypes import * #PropertyIdentifier
from bacpypes3.primitivedata import *
#from bacpypes3.local.object import Object as _Object
from bacpypes3.local.device import DeviceObject as _DeviceObject
from bacpypes3.local.networkport import NetworkPortObject as _NetworkPortObject
#from bacpypes3.local.cov import COVIncrementCriteria

#from bacpypes3.local.cmd import Commandable
#from bacpypes3.local.event import OutOfRangeEventAlgorithm, ChangeOfStateEventAlgorithm
#from bacpypes3.apdu import IAmRequest

from amevTemplate import *

# some debugging
_debug = 0
_log = ModuleLogger(globals())

            
class DeviceObject(_DeviceObject):
    """
    When running as an instance of this custom device, the DeviceObject is
    an extension of the one defined in bacpypes3.local.device (in this case
    doesn't add any proprietary properties).
    """
    objectIdentifier=('device',4222) #Fixme
    #vendorIdentifier = _vendor_id
    #objectName=_dev_name
    description = "Gebäudeautomationssystem Automationsschwerpunkt AS Device"
    modelName = 'Python3 AMEV BACnet Testserver'
    firmwareRevision = '0.1'
    applicationSoftwareVersion = '0.8'
    location = 'wherever'
    timeSynchronizationInterval=3600
    structuredObjectList=[
        #DeviceObjectReference(objectIdentifier=("structured-view",999)),
        #ObjectReference(objectIdentifier=("structured-view",998)),
        #ObjectIdentifier('structured-view',998),
        ]
    #timeSynchronizationRecipients=ListOf(Recipient)([Receipient, Recipient(device=('device',2))])
    daylightSavingsStatus=True
    lastRestoreTime=TimeStamp(dateTime=DateTime(date=Date().now()._value, time=Time().now()._value))
    lastRestartReason='warmstart'
    backupAndRestoreState='idle'
    #restartNotificationRecipients=ListOf(Recipient)([Recipient(device=('device',4194303))]) #Broadcast
    configurationFiles=[('file',1)]
    backupFailureTimeout=10
    backupPreparationTime=11
    restorePreparationTime=12
    restoreCompletionTime=13
    databaseRevision = 1
    alignIntervals=False
    intervalOffset=0
    serialNumber = '1234567'
    profileName='DEV_AMEV1'
    protocolObjectTypesSupported=[
		   True, #AI
		   True, #AO
		   True, #AV
		   True, #BI
		   True, #BO
		   True, #BV
		   True, #CAL
		   False, #CMD
		   True, #DEV
		   True, #EE
		   True, #FIL
		   False, #GRP
		   True, #LP
		   False, #MSI
		   False, #MSO
		   True, #NC
		   False, #PG
		   True, #SCH
		   False, #AVG
		   True, #MSV
		   True, #TL
		   False, #LSP
		   False, #LSZ
		   False, #ACC
		   False, #PC
		   False, #ELOG
		   False, #GGR
		   False, #TLM
		   False, #LC
		   True, #SV
		   False, #ACD
		   False, #NotInUse
		   False, #ACR
		   False, #ACP
		   False, #ACR
		   False, #ACU
		   False, #ACZ
		   False, #CDI
		   False, #NS
		   False, #BSV
		   False, #CSV
		   False, #DTP
		   False, #DV
		   False, #DTPV
		   False, #DTV
		   False, #IV
		   False, #LAV
		   False, #OSV
		   False, #PIV
		   False, #TPV
		   False, #TV
		   False, #NF
		   False, #AE
		   False, #CHN
		   False, #LO
		   False, #BLO FIXME: No Template available
		   True, #NP
		   False, #elevator Group Rev >14
		   False, #escalator Rev >14
		   False, #lift Rev >14
		   False, #staging Rev >14
		   False, #audit-log Rev >14
		   False, #audit-reporter Rev >14
		   False, #
		   False, #
		   ]
        

#class NetworkPortObject(_NetworkPortObject):
class NP_IP1(_NetworkPortObject):
    """
    When running as an instance of this custom device, the NetworkPortObject is
    an extension of the one defined in bacpypes3.local.networkport (in this
    case doesn't add any proprietary properties).
    """
    objectName = "ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NP~01" # Fixme
    description = "Gebäudeautomationssystem Automationsschwerpunkt AS Device Netwerk Anschluß IP"

    #pass

class FIL_AMEV1(FileObject):
    objectIdentifier=("file", 1)
    objectName="MUSTER_480_ASP01°01_#####_###_AS~01_#####_FIL01"
    description="Backup-Datei"
    fileType="testfile"
    fileSize=123
    modificationDate=DateTime(date=Date().now()._value, time=Time().now()._value)
    archive=False
    readOnly=True
    fileAccessMethod="streamAccess"
    recordCount=321
    profileName="FIL Vorlage"
    propertyList=[75,77,79,28,43,42,71,13,99,41,141,371,168] #486,485,
    
class NONAMEV_CSV(CharacterStringValueObject):
    objectIdentifier=("characterstringValue", 1)
    objectName="Link zur Dokumentation"
    description="Beschreibung AMEV BACtwin Siehe https://www.amev-online.de/AMEVInhalt/Planen/Gebaeudeautomation/BACtwin/"
    presentValue="Read.me"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
#    priorityArray: ArrayOf(PriorityValue, _length=16)
#    relinquishDefault: CharacterString
#    timeDelay: Unsigned
##    notificationClass: Unsigned
#   alarmValues: ArrayOf(OptionalCharacterString)
#   faultValues: ArrayOf(OptionalCharacterString)
#   eventEnable: EventTransitionBits
#   ackedTransitions: EventTransitionBits
#   notifyType: NotifyType
#   eventTimeStamps: ArrayOf(TimeStamp, _length=3)
#   eventMessageTexts: ArrayOf(CharacterString, _length=3)
#   eventMessageTextsConfig: ArrayOf(CharacterString, _length=3)
#    eventDetectionEnable: Boolean
#    eventAlgorithmInhibitRef: ObjectPropertyReference
#    eventAlgorithmInhibit: Boolean
#    timeDelayNormal: Unsigned
#   reliabilityEvaluationInhibit: Boolean
#    currentCommandPriority: OptionalUnsigned
#    valueSource: ValueSource
#    valueSourceArray: ArrayOf(ValueSource, _length=16)
#    lastCommandTime: TimeStamp
#    commandTimeArray: ArrayOf(TimeStamp, _length=16)
#    auditPriorityFilter: OptionalPriorityFilter

class NONAMEV_EVL(EventLogObject):
    objectIdentifier=("eventLog", 1)
    objectName="*_EVL01"
    description="Test EventLog für Schulung"
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    enable=True
    startTime=DateTime(date=(125,1,1,255), time=(0,0,0,0))
    stopTime=DateTime(date=Date("2050-12-31")._value, time=Time("23:59:59.99")._value)
    stopWhenFull=False
    bufferSize=100
    LogBuffer=[
    ]
    recordCount=0
    totalRecordCount=0
    notificationThreshold=25
    recordsSinceNotification=0
    lastNotifyRecord=0
    notificationClass=700
    #eventEnable: EventTransitionBits
    #ackedTransitions: EventTransitionBits
    #notifyType: NotifyType
    #eventTimeStamps: ArrayOf(TimeStamp, _length=3)
    #eventMessageTexts: ArrayOf(CharacterString, _length=3)
    #eventMessageTextsConfig: ArrayOf(CharacterString, _length=3)
    #eventDetectionEnable: Boolean
    #eventAlgorithmInhibitRef: ObjectPropertyReference
    #eventAlgorithmInhibit: Boolean
    #reliabilityEvaluationInhibit: Boolean

async def ramp(
    avo: Object, starting_value: float, step_count: int, step_size: float
) -> None:
    """
    Ramp the present value from the starting value up step_size increments
    step_count number of times, then back down again.
    """
    #if _debug:
    #    _log.debug("ramp %r %r %r %r", avo, starting_value, step_count, step_size)

    try:
        while True:
            #if _debug:
                #_log.debug("- reliability %s", avo.reliability)
                #_log.debug("- ID %d", avo.objectIdentifier)
                #_log.debug("- ID %s", avo.objectIdentifier)
            
            #for i in range(step_count):
            if avo.outOfService == False:
                avo.presentValue = avo.presentValue + 0.1 # starting_value + step_size
            await asyncio.sleep(5)

            #if _debug:
            #    _log.debug("- ramp down")
            #for i in range(step_count):
                #avo.presentValue = starting_value + step_count - step_size
                #avo.presentValue = starting_value + step_count - step_size
                #await asyncio.sleep(0.5)
            if avo.presentValue > avo.maxPresValue:
                avo.presentValue = avo.minPresValue
                _log.debug("- ramp minPresValue")

    except KeyboardInterrupt:
        pass

def Test_AMEV_Objekte(app):
        ai10001=AI_MW_T_H_HT_AMEV1(
#            objectIdentifier=("analog-input", 1),
#            objectName="ORTS-BAS_AI",
        )
        app.add_object(ai10001)

        bi402=BI_GM_BSK_AMEV1(
        )
        app.add_object(bi402) 

        bi403=BI_SM_NOT_AMEV1(
        )
        app.add_object(bi403)

        bi404=BI_AM_AMEV1(
        )
        app.add_object(bi404)

        bi405=BI_AM_ZOF_AMEV1(
        )
        app.add_object(bi405)

        bi406=BI_SM_AMEV1(
        )
        app.add_object(bi406)  

        bi407=BI_SM_NAF_AMEV1(
        )
        app.add_object(bi407)

        bi408=BI_SM_LU_AMEV1(
        )
        app.add_object(bi408)

        bi409=BI_SM_SYS_AMEV1(
        )
        #app.add_object(bi409) Benutzt Baseiobjekte

        bi410=BI_SM_LU_IH_AMEV1(
        )
        app.add_object(bi410)
        
        bi411=BI_ANO_AMEV1(
        )
        app.add_object(bi411)
        
        bi412=BI_SAB_AMEV1(
        )
        app.add_object(bi412)
        
        bi414=BI_BM_AMEV1(
        )
        app.add_object(bi414)
        
        bi446=BI_RM_AMEV1(
        )
        app.add_object(bi446)

        bi409=BI_SM_SYS_AMEV1(
        )
        app.add_object(bi409)
        
        bo501=BO_SB_AMEV1(
        )
        app.add_object(bo501)
        bo501.eventMessageTextsConfig[0] = "Alarm: " + bo501.description
        bo501.eventMessageTextsConfig[1] = "Fehler: "+ bo501.description
        bo501.eventMessageTextsConfig[2] = "Normal: "+ bo501.description 
        
        bv614=BV_SB_NSP_AMEV1(
        )
        app.add_object(bv614)

        ee201=EE_CCP_AMEV1(
            objectIdentifier=("eventEnrollment",201),
            objectName="MUSTER_CCP_1",
            description="Test Event Enrollment CurrentCommendPriority",
        )
        app.add_object(ee201)
        ee201.eventMessageTextsConfig[0] = "Alarm: "+ee201.description
        ee201.eventMessageTextsConfig[1] = "Fehler: "+ee201.description
        ee201.eventMessageTextsConfig[2] = "Normal: "+ee201.description
        
        ee202=EE_CCP_AMEV1(
            objectIdentifier=("eventEnrollment",202),
            objectName="MUSTER_COS_1",
            description="Test Event Enrollment ChangeOfState",
        )
        app.add_object(ee202)
        ee202.eventMessageTextsConfig[0] = "Alarm: "+ee202.description
        ee202.eventMessageTextsConfig[1] = "Fehler: "+ee202.description
        ee202.eventMessageTextsConfig[2] = "Normal: "+ee202.description    
            
        ee203=EE_OOR_AMEV1(
            objectIdentifier=("eventEnrollment",203),
            objectName="MUSTER_OOS_1",
            description="Test Event Enrollment OutOfRange",
        )
        app.add_object(ee203)
        ee203.eventMessageTextsConfig[0] = "Alarm: "+ee203.description
        ee203.eventMessageTextsConfig[1] = "Fehler: "+ee203.description
        ee203.eventMessageTextsConfig[2] = "Normal: "+ee203.description 
        
        ee204=EE_FLIM_AMEV1(
            objectIdentifier=("eventEnrollment",204),
            objectName="MUSTER_FLIM_1",
            description="Test Event Enrollment Floating Limit",
        )
        app.add_object(ee204)
        ee204.eventMessageTextsConfig[0] = "Alarm: "+ee204.description
        ee204.eventMessageTextsConfig[1] = "Fehler: "+ee204.description
        ee204.eventMessageTextsConfig[2] = "Normal: "+ee204.description 
        
        ee205=EE_COB_AMEV1(
            objectIdentifier=("eventEnrollment",205),
            objectName="MUSTER_COB_1",
            description="Test Event Enrollment ChangeOfBitstring",
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="analogOutput,1",
                propertyIdentifier=PropertyIdentifier.statusFlags,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ))
        app.add_object(ee205) 
        ee205.eventMessageTextsConfig[0] = "Hand: " +ee205.description
        ee205.eventMessageTextsConfig[1] = "Fehler: "+ee205.description
        ee205.eventMessageTextsConfig[2] = "Normal: "+ee205.description 
        
        ee208=EE_CMDF_AMEV1(
            objectIdentifier=("eventEnrollment",208),
            objectName="MUSTER_CMD_1",
            description="Test Event Enrollment Command Failture",
        )
        app.add_object(ee208)
        ee208.eventMessageTextsConfig[0] = "Alarm: "+ee208.description
        ee208.eventMessageTextsConfig[1] = "Fehler: "+ee208.description
        ee208.eventMessageTextsConfig[2] = "Normal: "+ee208.description
        
        mv902=MV_GS_AEM_AMEV1(
        )
        app.add_object(mv902)

        sv101=SV_ANL_AMEV1(
            #objectIdentifier=("structuredView", 101)
            #objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_SV~01"
            #description="Gebäudeautomationssystem Automationsschwerpunkt AS System"
        )
        app.add_object(sv101)

        sv102=SV_BGP_AMEV1(
            #objectIdentifier=("structuredView", 102)
            #objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_SV~02"
            #description="Gebäudeautomationssystem Automationsschwerpunkt AS Subsystem"
        )
        app.add_object(sv102)
        
        sv103=SV_AGG_AMEV1(
            #objectIdentifier=("structuredView", 103)
            #objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_SV~03"
            #description="Gebäudeautomationssystem Automationsschwerpunkt AS Equipment"
        )
        app.add_object(sv103)

        tvl_lp = LP_AN_AMEV1(
        )   
        #if _debug: _log.info("    - loop: %r", tvl_lp.objectName)
        app.add_object(tvl_lp) 

        sch201=SCH_BN_AMEV1(
        )
        #_log.debug("    - so: %r", sch201)
        app.add_object(sch201)
        
        tl101=TL_AN_P_AMEV1(
        )
        app.add_object(tl101)
        
        tl102=TL_AN_C_AMEV1(
        )
        app.add_object(tl102)  
        
        tl103=TL_AN_ZW_AMEV1(
        )
        app.add_object(tl103)
        
        tl104=TL_BN_AMEV1(
        )
        app.add_object(tl104)
 

def Basisobjekte(app):
        csv1=NONAMEV_CSV(
        )
        app.add_object(csv1)
        
#**************** FIL ***************
        fil1=FIL_AMEV1(
            description="Datensicherungsdatei (fiktiv)"
            )
        app.add_object(fil1)
        
#**************** CAL ***************
        Neujahr=CalendarEntry(date=(255,1,1,255)) #Jahr (255 = jeder),Monat,
        Dreikoenig=CalendarEntry(date=(255,1,6,255)) 
        Maifeiertag=CalendarEntry(date=(255,5,1,255)) 
        Nationalfeiertag=CalendarEntry(date=(255,10,3,255)) 
        #Example heute=Date().now()._value
        Weihnachten=CalendarEntry(dateRange=DateRange(startDate=(255,12,24,255), endDate=(255,12,25,255))) #Fixme
        Weihnachten=CalendarEntry(dateRange=DateRange(startDate=Date("2025-12-25")._value, endDate=Date("2025-12-26")._value))
        #weekdaytest=CalendarEntry(weekNDay=Date(255,255,255,6))
        
        cal101 = CAL_FT_AMEV1(
            dateList = [Neujahr,Dreikoenig,Maifeiertag,Nationalfeiertag,Weihnachten]
            )
        app.add_object(cal101)

        cal102 = CAL_SF_AMEV1(
            )
        app.add_object(cal102)

        cal103 = CAL_BF_AMEV1(
            )
        app.add_object(cal103)
        
        cal104 = CAL_ALG_AMEV1(
            )
        app.add_object(cal104)
        
#**************** NC ***************

        nc100 = NC_GM_PSA_AMEV1(
        )
        app.add_object(nc100)
        
        nc150 = NC_GM_OSA_AMEV1()
        app.add_object(nc150)

        nc200 = NC_AM_GA_AMEV1()
        app.add_object(nc200)
                
        nc250 = NC_VAM_GA_AMEV1()
        app.add_object(nc250)
        
        nc300 = NC_SM_GA_AMEV1()
        app.add_object(nc300)

        nc350 = NC_ANO_GA_AMEV1()
        app.add_object(nc350)

        nc400 = NC_WM_GA_AMEV1()
        app.add_object(nc400)

        nc425 = NC_WM_GAQ_AMEV1()
        app.add_object(nc425)

        nc450 = NC_RVM_GA_AMEV1()
        app.add_object(nc450)

        nc500 = NC_HD_GA_AMEV1()
        app.add_object(nc500)

        nc600 = NC_SYS_GA_AMEV1()
        app.add_object(nc600)

        nc700 = NC_TL_GA_AMEV1()
        app.add_object(nc700)

        nc800 = NC_SO_GA_AMEV1()
        app.add_object(nc800)


#**************** PG ***************

#**************** SV ***************
        sv1 = SV_AGG_AMEV1(
            objectIdentifier=("structuredView", 1),
            objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_SV~01",
            description="Gebäudeautomationssystem Automationsschwerpunkt AS Equipment",
            subordinateList=ArrayOf(DeviceObjectReference)([
                DeviceObjectReference(objectIdentifier=("device",999),),
                DeviceObjectReference(objectIdentifier=("calendar",101),),
                DeviceObjectReference(objectIdentifier=("calendar",102),),
                #DeviceObjectReference(objectIdentifier=("calendar",103),),
                #DeviceObjectReference(objectIdentifier=("calendar",104),),
                DeviceObjectReference(objectIdentifier=("notificationClass",100),),
                DeviceObjectReference(objectIdentifier=("notificationClass",150),),
                DeviceObjectReference(objectIdentifier=("notificationClass",200),),
                DeviceObjectReference(objectIdentifier=("notificationClass",250),),
                DeviceObjectReference(objectIdentifier=("notificationClass",300),),
                DeviceObjectReference(objectIdentifier=("notificationClass",350),),
                DeviceObjectReference(objectIdentifier=("notificationClass",400),),
                DeviceObjectReference(objectIdentifier=("notificationClass",425),),
                DeviceObjectReference(objectIdentifier=("notificationClass",450),),
                DeviceObjectReference(objectIdentifier=("notificationClass",500),),
                DeviceObjectReference(objectIdentifier=("notificationClass",600),),
                DeviceObjectReference(objectIdentifier=("notificationClass",700),),
                DeviceObjectReference(objectIdentifier=("notificationClass",800),),
                DeviceObjectReference(objectIdentifier=("binaryInput",409),),
                ]),
            subordinateAnnotations=([
                "Automationsstation",
                "Kalender Feiertage",
                "Kalender Ferientage",
                "Meldeklasse Gefahr Person",
                "Meldeklasse Gefahr Liegenschaft",
                "Meldeklasse Alarm",
                "Meldeklasse Voralarm",
                "Meldeklasse Störung",
                "Meldeklasse Anormal",
                "Meldeklasse Wartung",
                "Meldeklasse Wartung (quittierbar)",
                "Meldeklasse Revision",
                "Meldeklasse Hand",
                "Meldeklasse System",
                "Meldeklasse Trend",
                "Meldeklasse Sonstiges",
                "Pufferbatterie Störung",
            ]),
            )
        app.add_object(sv1)

def Heizkreis(app):
#Beispiel Heizkreis
#Vorlauffühler
        #Ort_BAS="71157_B6_EG"
        #Ort_KT ="Irgendwo"
        Ort_BAS="ORTS-BAS"
        Ort_KT ="" #"Ortsangabe"
        Gew_BAS="420"
        Gew_KT ="" #"Wärmeversorgungsanlage"
        Anl_BAS="VTA01°01"
        Anl_KT ="Verteilanlage 1"
        Bgp_BAS="###"
        Bgp_KT =""
        MeP_BAS="###"
        MeP_KT =""
        Agg_BAS="#####"
        Agg_KT =""
        Btm_BAS="#####"
        Btm_KT =""
        
        sv998=SV_BGP_AMEV1(
            objectIdentifier=("structured-view", 998),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"",
            #subordinateList=ArrayOf(DeviceObjectReference)([
            subordinateList=[
                DeviceObjectReference(objectIdentifier=("structured-view",999)),
                ],
            subordinateAnnotations=([
                "Baugruppe Heizkreis",
                ]),
            
        )
        app.add_object(sv998)
        
        Bgp_BAS="HZK01"
        Bgp_KT ="Heizkreis 1"

        sv999=SV_BGP_AMEV1(
            objectIdentifier=("structured-view", 999),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"",
            subordinateList=ArrayOf(DeviceObjectReference)([
                DeviceObjectReference(objectIdentifier=("structured-view",1000)),
                DeviceObjectReference(objectIdentifier=("structured-view",1001)),
                DeviceObjectReference(objectIdentifier=("structured-view",1010)),
                DeviceObjectReference(objectIdentifier=("structured-view",1020)),
                ]),
            subordinateAnnotations=([
                "Fühler Vorlauf",
                "Fühler Rücklauf",
                "Ventil",
                "Pumpe",
                ]),
            
        )
        app.add_object(sv999)
        
# Weekday: 8AM–5PM occupied
        weekday_schedule = DailySchedule(
            daySchedule=[
                TimeValue(time=(6, 30, 0, 0), value=Enumerated(1)),
                TimeValue(time=(19, 30, 0, 0), value=Null(())),
            ]
)
        
# Weekend: always off
        weekend_schedule = DailySchedule(
            daySchedule=[
                #TimeValue(time=(0, 0, 0, 0), value=Null(())),  # Midnight OFF              
            ]
        )

# Weekly Schedule (Monday=0 ... Sunday=6)
        weekly_schedule = [
            weekday_schedule,  # Monday
            weekday_schedule,  # Tuesday
            weekday_schedule,  # Wednesday
            weekday_schedule,  # Thursday
            weekday_schedule,  # Friday
            weekend_schedule,  # Saturday
            weekend_schedule,  # Sunday
        ]
        
        sch1000 = SCH_BN_AMEV1(
            objectIdentifier=("schedule", 1000),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SCH01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Zeitplan",
            weeklySchedule=weekly_schedule,
            listOfObjectPropertyReferences=[
                DeviceObjectPropertyReference(
                    objectIdentifier="binaryOutput,501",
                    propertyIdentifier=PropertyIdentifier.presentValue,
                    #propertyArrayIndex=11,
                    #deviceIdentifier=this_device.objectIdentifier,
                ),
            ]
        )
        app.add_object(sch1000)
        
        # MV Anlagensteuerung
        mv1000 = MV_GS_AEM_AMEV1(
            objectIdentifier=("multiStateValue", 1000),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"AST01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Anlagensteuerung",
        )
        #if _debug: _log.info("    - multistateValue: %r", mv1000.objectName)
        app.add_object(mv1000)
        mv1000.eventMessageTextsConfig[0] = "Alarm: " + mv1000.description
        mv1000.eventMessageTextsConfig[1] = "Fehler: "+ mv1000.description
        mv1000.eventMessageTextsConfig[2] = "Normal: "+ mv1000.description 

        MeP_BAS="HZV"
        MeP_KT ="Heizwasser Vorlauf"
        Agg_BAS="EF~01"
        Agg_KT =""
        Btm_BAS="T~~01"
        Btm_KT ="Temperatur 1"
        
        sv1000=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 1000),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"",
            subordinateList=ArrayOf(DeviceObjectReference)([
                DeviceObjectReference(objectIdentifier=("analog-input",1000)),
                DeviceObjectReference(objectIdentifier=("trend-log",1000)),
                ]),
            subordinateAnnotations=([
                "Messwert",
                "Messwert Datenaufzeichnung",
                ]),
            
        )
        app.add_object(sv1000)
        
        ai1000=AI_MW_T_H_HT_AMEV1(
            objectIdentifier=("analog-input", 1000),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Messwert",
        )
        app.add_object(ai1000)
        
        
        tl1000=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 1000),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01_TL",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Messwert Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="analog-input,1000",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl1000)
        
        av1000=AV_SW_T_AMEV1(
            objectIdentifier=("analogValue", 1000), 
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SWC01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Sollwert berechnet",
        )
        app.add_object(av1000)
        
        lp1000 = LP_AN_AMEV1(
            objectIdentifier=("loop", 1000), 
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"LP~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Regler",
            manipulatedVariableReference=ObjectPropertyReference(
                objectIdentifier="analogOutput,1010", propertyIdentifier=PropertyIdentifier.presentValue, propertyArrayIndex=16,
                ),
            controlledVariableReference=ObjectPropertyReference(
                objectIdentifier="analogInput,1000", propertyIdentifier=PropertyIdentifier.presentValue,
                ),
            setpointReference=ObjectPropertyReference(
                objectIdentifier="analogValue,1000", propertyIdentifier=PropertyIdentifier.presentValue,
                ),
            )   
        app.add_object(lp1000) 
        #print(lp1000)
        #print(lp1000.setpointReference)
        #print(lp1000.setpointReference.get_attribute)
        #print(type(lp1000.setpointReference))
        #print(dir(lp1000.setpointReference))

        av1001=AV_SW_T_AMEV1(
            objectIdentifier=("analogValue", 1001), 
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MAX01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Maximalwert",
            presentValue=55,
        )
        app.add_object(av1001)

        av1002=AV_SW_T_AMEV1(
            objectIdentifier=("analogValue", 1002), 
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MIN01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Minimalwert",
            presentValue=20,
        )
        app.add_object(av1002)
        
        av1003=AV_SW_T_AMEV1(
            objectIdentifier=("analogValue", 1003), 
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"KST01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Kennlinie Steilheit",
            presentValue=1.1,
            units=98,
        )
        app.add_object(av1003)
        
        av1004=AV_SW_T_AMEV1(
            objectIdentifier=("analogValue", 1004), 
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"KEX01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Kennlinie Exponent",
            presentValue=1.3,
            units=98,
        )
        app.add_object(av1004)

        av1005=AV_SW_T_AMEV1(
            objectIdentifier=("analogValue", 1005), 
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"KFP01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Kennlinie Fußpunkt",
            presentValue=22,
            units=98,
        )
        app.add_object(av1005)

        av1006=AV_SW_T_AMEV1(
            objectIdentifier=("analogValue", 1006), 
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"KPV01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Kennlinie Parallelverschiebung",
            presentValue=0,
            units='degreesKelvin',
        )
        app.add_object(av1006)


#Rücklauffühler        
        MeP_BAS="HZR"
        MeP_KT ="Heizwasser Rücklauf"

        sv1001=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 1001),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"",
            subordinateList=ArrayOf(DeviceObjectReference)([
                DeviceObjectReference(objectIdentifier=("analog-input",1001)),
                DeviceObjectReference(objectIdentifier=("trend-log",1001)),
                ]),
            subordinateAnnotations=([
                "Messwert",
                "Messwert Datenaufzeichnung",
                ]),
            
        )
        app.add_object(sv1001)

        ai1001=AI_MW_T_H_HT_AMEV1(
            objectIdentifier=("analog-input", 1001),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Messwert",
        )
        app.add_object(ai1001)
        
        tl1001=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 1001),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01_TL",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Messwert Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="analog-input,1001",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl1001)

#Ventil
        MeP_BAS="HZV"
        MeP_KT ="Heizwasser Vorlauf"
        Agg_BAS="VEN01"
        Agg_KT ="Ventil 1"
        Btm_BAS="MOT01"
        Btm_KT =""

        sv1010=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 1010),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"",
            subordinateList=([
                DeviceObjectReference(objectIdentifier=("analog-output",1010)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",10101)),
                DeviceObjectReference(objectIdentifier=("analog-input",1010)),
                DeviceObjectReference(objectIdentifier=("trend-log",1010)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",10102)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",10103)),
                ]),
            subordinateAnnotations=([
                "Stellsignal",
                "Abweichung",
                "Rückführwert",
                "Rückführwert Datenaufzeichnung",
                "UBE Hand",
                "LVB Hand"
                ]),
            
        )
        app.add_object(sv1010)
        
        Btm_BAS="MOT01"
        Btm_KT =""
        
        ao1010 = AO_ST_AMEV1(
            objectIdentifier=("analog-output", 1010),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ST~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Stellsignal",
            statusFlags=[False, False, False, False],
                    )
        app.add_object(ao1010)

        ai1010=AI_RW_AMEV1(
            objectIdentifier=("analog-input", 1010),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"RW~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Rückführwert",
        )
        app.add_object(ai1010)        

        tl1010=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 1010),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01_TL",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Messwert Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="analog-input,1010",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl1010)

        ee10101=EE_FLIM_AMEV1(
            objectIdentifier=("eventEnrollment", 10101),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ABW01_EE",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Abweichung",
            eventParameters=EventParameter(
                floatingLimit=EventParameterFloatingLimit(
                    timeDelay=60,
                    setpointReference = DeviceObjectPropertyReference(
                        objectIdentifier="analogInput,1010",
                        propertyIdentifier=PropertyIdentifier.presentValue,
                        #propertyArrayIndex=11,
                        #deviceIdentifier=this_device.objectIdentifier,
                    ),
                    lowDiffLimit = 3,
                    highDiffLimit = 3,
                    deadband = 0.5
                )
            ),
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="analogOutput,1010",
                propertyIdentifier=PropertyIdentifier.presentValue,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee10101)
        ee10101.eventMessageTextsConfig[0] = "Abweichung: "+ee10101.description
        ee10101.eventMessageTextsConfig[1] = "Fehler: "+ee10101.description
        ee10101.eventMessageTextsConfig[2] = "Normal: "+ee10101.description
        
        Btm_BAS="UBE01"
        Btm_KT ="Bedieneinheit"
        ee10102=EE_CCP_AMEV1(
            objectIdentifier=("eventEnrollment", 10102),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDG01_EE",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Hand stellen",
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
            ),
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="analogOutput,1010",
                propertyIdentifier=PropertyIdentifier.currentCommandPriority,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee10102)
        ee10102.eventMessageTextsConfig[0] = "Hand: "+ee10102.description
        ee10102.eventMessageTextsConfig[1] = "Fehler: "+ee10102.description
        ee10102.eventMessageTextsConfig[2] = "Normal: "+ee10102.description
        
        Btm_BAS="LVB01"
        Btm_KT ="LVB"
        ee10103=EE_COB_AMEV1(
        objectIdentifier=("eventEnrollment", 10103),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDG01_EE",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Hand stellen",
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="analogOutput,1010",
                propertyIdentifier=PropertyIdentifier.statusFlags,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee10103)
        ee10103.eventMessageTextsConfig[0] = "Hand: "+ee10103.description
        ee10103.eventMessageTextsConfig[1] = "Fehler: "+ee10103.description
        ee10103.eventMessageTextsConfig[2] = "Normal: "+ee10103.description

#Pumpe
        MeP_BAS="HZV"
        MeP_KT ="Heizwasser Vorlauf"
        Agg_BAS="PPE01"
        Agg_KT ="Pumpe 1"
        Btm_BAS="#####"
        Btm_KT =""

        sv1020=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 1020),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"",
            subordinateList=([
                DeviceObjectReference(objectIdentifier=("binary-output",1020)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",10201)),
                DeviceObjectReference(objectIdentifier=("binary-input",1020)),
                DeviceObjectReference(objectIdentifier=("trend-log",1020)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",10202)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",10203)),
                ]),
            subordinateAnnotations=([
                "Schaltbefehl",
                "Ausführkontrolle",
                "Betriebsmeldung",
                "Betriebsmeldung Datenaufzeichnung",
                "UBE Hand",
                "LVB Hand"
                ]),
            
        )
        app.add_object(sv1020)

        bo1020=BO_SB_AMEV1(
            objectIdentifier=("binary-output", 1020),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SB~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Schaltbefehl",
        )
        app.add_object(bo1020)

        bi1020=BI_BM_AMEV1(
            objectIdentifier=("binary-input", 1020),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"BM~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Betriebsmeldung",
        )
        app.add_object(bi1020)

        ee10201=EE_CMDF_AMEV1(
            objectIdentifier=("eventEnrollment", 10201),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"AK~01_EE",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Ausführkontrolle",
            eventParameters=EventParameter(
                commandFailure=EventParameterCommandFailure(
                    timeDelay=3,
                    feedbackPropertyReference=DeviceObjectPropertyReference(
                        objectIdentifier="binaryInput,1020",
                        propertyIdentifier=PropertyIdentifier.presentValue,
                        #propertyArrayIndex=11,
                        #deviceIdentifier=this_device.objectIdentifier,
                    )
                )
            ),
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryOutput,1020",
                propertyIdentifier=PropertyIdentifier.presentValue,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee10201)
        ee10201.eventMessageTextsConfig[0] = "Abweichung: "+ee10201.description
        ee10201.eventMessageTextsConfig[1] = "Fehler: "+ee10201.description
        ee10201.eventMessageTextsConfig[2] = "Normal: "+ee10201.description

        tl1020=TL_BN_AMEV1(
            objectIdentifier=("trend-log", 1020),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"BM~01_TL",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Betriebsmeldung Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="binary-input,1020",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl1020)

        Btm_BAS="UBE01"
        Btm_KT ="Bedieneinheit"
        ee10202=EE_CCP_AMEV1(
            objectIdentifier=("eventEnrollment", 10202),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDB01_EE",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Hand schalten",
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
            ),
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryOutput,1020",
                propertyIdentifier=PropertyIdentifier.currentCommandPriority,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee10202)
        ee10202.eventMessageTextsConfig[0] = "Hand: "+ee10202.description
        ee10202.eventMessageTextsConfig[1] = "Fehler: "+ee10202.description
        ee10202.eventMessageTextsConfig[2] = "Normal: "+ee10202.description
        
        Btm_BAS="LVB01"
        Btm_KT ="LVB"
        ee10203=EE_COB_AMEV1(
        objectIdentifier=("eventEnrollment", 10203),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDB01_EE",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Hand schalten",
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryOutput,1020",
                propertyIdentifier=PropertyIdentifier.statusFlags,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee10203)
        ee10203.eventMessageTextsConfig[0] = "Hand: "+ee10203.description
        ee10203.eventMessageTextsConfig[1] = "Fehler: "+ee10203.description
        ee10203.eventMessageTextsConfig[2] = "Normal: "+ee10203.description

def NONAMEV_Objekte(app):
        tim1 = TimerObject(
            #    _required = ("presentValue", "statusFlags", "timerState", "timerRunning")
            objectIdentifier=("timer", 1),
            description="Timer Testobjekt",
            objectName="Timer1",
            presentValue=0,
            statusFlags=[0,0,0,0],
            eventState=0,
            reliability="noFaultDetected",
            outOfService=False,
            timerState=0,
            timerRunning=False,
            updateTime=DateTime(date=Date().now()._value, time=Time().now()._value),
            #lastStateChange: TimerTransition
            expirationTime=DateTime(date=Date("2030-12-31")._value,time=(23, 59, 59, 99)),
            initialTimeout=120,
            defaultTimeout=180,
            minPresValue=0,
            maxPresValue=99999,
            resolution=1,
            #stateChangeValues: ArrayOf(TimerStateChangeValue, _length=7)
            #listOfObjectPropertyReferences: ListOf(DeviceObjectPropertyReference)
            priorityForWriting=12,
            eventDetectionEnable=False,
            notificationClass=700,
            timeDelay=60,
            timeDelayNormal=15,
            #alarmValues: ListOf(TimerState)
            eventEnable=[False,False,False],
            ackedTransitions=[True,True,True],
            notifyType="alarm",
            eventTimeStamps=[
                TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
                TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
                TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
                ],
            eventMessageTexts=["","",""], #ArrayOf(CharacterString, _length=3),
            eventMessageTextsConfig=["Alarm:","Fehler:","Normal"],#ArrayOf(CharacterString, _length=3)
            #eventAlgorithmInhibitRef: ObjectPropertyReference
            #eventAlgorithmInhibit: Boolean
            #reliabilityEvaluationInhibit: Boolean
        )
        
        app.add_object(tim1)
        
        # make a  "program":16
        pg1 = ProgramObject(
             objectIdentifier=("program",16),
             objectName="Object_16_PG", description="Program Description 1",
             programState="idle", programChange="halt",  reasonForHalt="internal",
             descriptionOfHalt="This is only a simulation",  programLocation="Irgendwo in python", instanceOf="Unterprogramm von",
             statusFlags=[False, False, False, False], reliability="noFaultDetected", outOfService=True,
             notificationClass=4194303, 
             eventEnable=[True, True, True], ackedTransitions=[True, True, True], notifyType="alarm",
             eventTimeStamps=[TimeStamp(time=(255, 255, 255, 255)),TimeStamp(time=(255, 255, 255, 255)),TimeStamp(time=(255, 255, 255, 255)),],
             eventMessageTexts=ArrayOf(CharacterString)(["eins","zwei","drei"]),
             eventMessageTextsConfig=ArrayOf(CharacterString)(["Alarm: PG 1","Fehler: PG 1","Normal: PG 1"]),
             eventDetectionEnable=False,reliabilityEvaluationInhibit=False,
             profileName="None AMEV TD PG Profile",
             propertyList=[75,77,79,92,90,100,29,91,28,48,111,103,81,353,17,35,36,0,72,130,351,352,357,371,486,485,168]
             )
        #if _debug: _log.info("    - program: %r", pg1.objectName)
        app.add_object(pg1)
        
        evl1=NONAMEV_EVL(
            logBuffer=[
                EventLogRecord(
                    #timestamp=TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))),
                    #timestamp=TimeStamp(dateTime=DateTime(date=Date().now()._value, time=Time().now()._value)),
                    #logDatum=(
                    #EventLogRecordLogDatum(
                        #logStatus=True
                        #timeChange=2.0
                    #    
                    #),
                )
            ]
    #eventParameters=EventParameter(
    #    outOfRange=EventParameterOutOfRange(
    #        timeDelay=10, lowLimit=0.0, highLimit=100.0, deadband=5.0,
    #    ),
    #)
    #logBuffer: ListOf(EventLogRecord)
    
    #class EventLogRecord(Sequence):
#    _order = ("timestamp", "logDatum")
#    timestamp = DateTime(_context=0)
#    logDatum = EventLogRecordLogDatum(_context=1)

    #class EventLogRecordLogDatum(Choice):
    #logStatus = LogStatus(_context=0)
    #notification = EventNotificationParameters(_context=1)
    #timeChange = Real(_context=2)
#    class EventNotificationParameters(Sequence):
#    _order = (
#        "processIdentifier",
#        "initiatingDeviceIdentifier",
#        "eventObjectIdentifier",
#        "timeStamp",
#        "notificationClass",
#        "priority",
#        "eventType",
#        "messageText",
#        "notifyType",
#        "ackRequired",
#        "fromState",
#        "toState",
#        "eventValues",
#    )
#    processIdentifier = Unsigned(_context=0)
#    initiatingDeviceIdentifier = ObjectIdentifier(_context=1)
#    eventObjectIdentifier = ObjectIdentifier(_context=2)
#    timeStamp = TimeStamp(_context=3)
#    notificationClass = Unsigned(_context=4)
#    priority = Unsigned(_context=5)
#    eventType = EventType(_context=6)
#    messageText = CharacterString(_context=7, _optional=True)
#    notifyType = NotifyType(_context=8)
#    ackRequired = Boolean(_context=9, _optional=True)
#    fromState = EventState(_context=10, _optional=True)
#    toState = EventState(_context=11)
#    eventValues = NotificationParameters(_context=12, _optional=True)
        )
        app.add_object(evl1)

def checkEventState(obj:Object)-> None:
#ToDo
            objectIdentifier=obj.objectIdentifier
            print(f"test: {objectIdentifier}")
            objectName=obj.objectName
            print(f"test: {objectName}")
            description=obj.description
            print(f"test: {description}")
            try:
                reliability=obj.reliability
                print(f"test: {reliability}")
                if obj.reliability > 0:
                    obj.statusFlags[0]=True
                    obj.statusFlags[1]=True
                else:
                    obj.statusFlags[0]=False
                    obj.statusFlags[1]=False
            except:
                pass

def checkFault(obj:Object)-> None:
    try:
        if obj.reliability > 0:
            obj.statusFlags[0]=True
            obj.statusFlags[1]=True
        else:
            #obj.statusFlags[0]=False wird in checkAlarm gesetzt!
            obj.statusFlags[1]=False
    except:
        pass

def checkAlarm(obj:Object)-> None:
    objectType = obj.objectType
    #if objectType == 3:
    #    print(objectType)
    match objectType:
        case 3 | 5: # "binary-input" | "binary-value": GEHT NICHT !!!
            try:
                if obj.alarmValue == obj.presentValue:
                    #print(obj.alarmValue)
                    #print(obj.presentValue)
                    #Fixme with algorithm and timedelay
                    obj.statusFlags[0]=True
                    obj.eventState = 2
                else:
                    obj.statusFlags[0]=False
                    obj.eventState = 0
            except:
                pass
        
def checkOutOfService(obj:Object)-> None:
    try:
        if obj.outOfService == True:
            obj.statusFlags[3]=True
        else:
            obj.statusFlags[3]=False
    except:
        pass

def runPID(obj:Object)-> None:
    try:
        #print(obj.bias)
        sp=obj.setpointReference
        #print(sp.objectType)
        obj.setpoint=sp.presentValue
        #print(obj.setpoint)

    except:
        pass


async def objCheck(app):
    print("objCheck run")
    try:
        while True:
            ol=app.objectIdentifier
            objekte=len(ol)
            #print(objekte)
            #print(list(ol.items())[objekte-1])
            #print(list(ol.keys())[0])
            #print(list(ol.values())[0])
            
            i=0
            while i < objekte:  
            #for index, objects in ol:
                #print(i)                
                objid=list(ol.keys())[i]
                obj=list(ol.values())[i]
                #print(obj)
                checkOutOfService(obj)
                #print("checkOutOfService done")
                checkAlarm(obj)
                checkFault(obj)
                #runPID(obj)
                if obj.objectType == 20:
                    sp=obj.logDeviceObjectProperty
                    #print(sp.presentValue)
                    #spl=len(sp)
                    #print(spl)
                    #print(sp(ObjectIdentifier))
                    #ID=sp->objectIdentifier
                    #prop=sp[1]#.propertyIdentifier             
                i+=1

                                
            await asyncio.sleep(0.5)
                
    except KeyboardInterrupt:
        pass

async def main() -> None:
    try:
        app = None
        parser = SimpleArgumentParser()

        # make sure the vendor identifier is the custom one
        args = parser.parse_args()
        #args.vendoridentifier = _vendor_id
        if _debug:
            _log.debug("args: %r", args)

        # build an application
        app = Application.from_args(args)
        if _debug:
            _log.debug("app: %r", app)
            
#Aggregate
        Basisobjekte(app) #Müssen immer da sein
        #Test_AMEV_Objekte(app)
        #NONAMEV_Objekte(app)
        Heizkreis(app)       
            
        #Test am AMEV Class Object
        ai10=AI_MW_T_AU_AMEV1(
            objectIdentifier=("analogInput", 10), 
            objectName="ORTS-BAS_420_WET01_#####_AU~_EF~01_T~~01_MW~01",
            description="Wetterstation Außen Temperatur Messwert",
            profileName="AI_MW_AU_T_AMEV1 Temperatur Messung",
        )
        app.add_object(ai10)
 
        Meldeschauer_inhibit=ObjectPropertyReference(
            objectIdentifier="binaryValue,614",
            propertyIdentifier=PropertyIdentifier.presentValue,
            propertyArrayIndex=1,
            )

        # nach dem Erstellen und Hinzufügen aller Objekte:
        #asyncio.create_task(send_initial_iam(app))
        #send_initial_iam(app)
        app.i_am()
        wi=app.who_is()
        #print(wi) check for IP address 
        
        
        # ramp up and down
        # Simulator für Werte
        await asyncio.gather(
            ramp(ai10, 4.0, 35, 0.1),
            objCheck(app)

        )

    finally:
        if app:
            app.close()


if __name__ == "__main__":
    asyncio.run(main())

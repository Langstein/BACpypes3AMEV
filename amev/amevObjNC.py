from bacpypes3.object import NotificationClassObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

class NC_GM_PSA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 100)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~10"    
    description="GA-System Automationsschwerpunkt AS Meldeklasse Gefahr Person"
    notificationClass=100
    priority=[10,11,110]
    ackRequired=[True, True, True]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99), 
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_GM_PSA_AMEV1 Meldeklasse Gefahr Person"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_GM_OSA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 150)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~15"    
    description="GA-System Automationsschwerpunkt AS Meldeklasse Gefahr Liegenschaft"
    notificationClass=150
    priority=[15,16,150]
    ackRequired=[True, True, True]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_GM_OSA_AMEV1 Meldeklasse Gefahr Liegenschaft"
    propertyList=[75,77,79,28,17,86,1,102,371,168]    

class NC_AM_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 200)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~20"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Alarm"
    notificationClass=200
    priority=[20,21,120]
    ackRequired=[True,True,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_AM_GA_AMEV1 Meldeklasse Alarm"
    propertyList=[75,77,79,28,17,86,1,102,371,168]
        
class NC_VAM_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 250)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~25"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Voralarm"
    notificationClass=250
    priority=[25,26,125]
    ackRequired=[True,True,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_VAM_GA_AMEV1 Meldeklasse Voralarm"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_SM_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 300)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~30"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Störung"
    notificationClass=300
    priority=[30,31,130]
    ackRequired=[True,True,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_SM_GA_AMEV1 Meldeklasse Störung"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_ANO_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 350)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~35"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Anormal"
    notificationClass=350
    priority=[35,36,135]
    ackRequired=[False,False,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_ANO_GA_AMEV1 Meldeklasse Anormal"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_WM_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 400)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~40"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Wartung"
    notificationClass=400
    priority=[40,41,140]
    ackRequired=[False,False,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_WM_GA_AMEV1 Meldeklasse Wartung"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_WM_GAQ_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 425)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~42"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Wartung (quitierbar)"
    notificationClass=425
    priority=[42,43,142]
    ackRequired=[True,False,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_WM_GAQ_AMEV1 Meldeklasse Wartung (quittierbar)"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_RVM_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 450)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~45"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Revision"
    notificationClass=450
    priority=[45,46,145]
    ackRequired=[False,False,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_RVM_GA_AMEV1 Meldeklasse Revision"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_HD_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 500)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~50"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Hand"
    notificationClass=500
    priority=[50,51,150]
    ackRequired=[False,False,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_HD_GA_AMEV1 Meldeklasse Handeingriff"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_SYS_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 600)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~60"
    description="GA-System Automationsschwerpunkt AS Meldeklasse System"
    notificationClass=600
    priority=[60,61,160]
    ackRequired=[True,False,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_SYS_GA_AMEV1 Meldeklasse System"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_TL_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 700)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~70"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Trend"
    notificationClass=700
    priority=[70,71,170]
    ackRequired=[False,False,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_TL_GA_AMEV1 Meldeklasse Trend"
    propertyList=[75,77,79,28,17,86,1,102,371,168]

class NC_SO_GA_AMEV1(NotificationClassObject):
    objectIdentifier=("notificationClass", 800)
    objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_NC~80"
    description="GA-System Automationsschwerpunkt AS Meldeklasse Sonstiges"
    notificationClass=800
    priority=[80,81,180]
    ackRequired=[True,False,False]
    recipientList=[
        Destination(
            validDays=[1, 1, 1, 1, 1, 1, 1], fromTime=(0, 0, 0, 0), toTime=(23, 59, 59, 99),
            recipient=Recipient(device="device,96"),
            processIdentifier=3, issueConfirmedNotifications=True, transitions=[True, True, True],  # toOffNormal, toFault, toNormal
        )
    ]
    profileName="NC_SO_GA_AMEV1 Meldeklasse Sonstiges"
    propertyList=[75,77,79,28,17,86,1,102,371,168]


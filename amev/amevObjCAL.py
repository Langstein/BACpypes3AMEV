
from bacpypes3.object import CalendarObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *
#ToDo Calendar Algorithm

class CAL_FT_AMEV1(CalendarObject):
            objectIdentifier=("calendar", 101)
            objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_CAL01"
            description="GA-System Automationsschwerpunkt AS Kalender Feiertage"
            presentValue=False
            dateList=[] # ListOf(CalendarEntry)
            profileName='CAL_FT_AMEV1 Jahreskalender Feiertage'
            propertyList=[75,77,79,28,85,23,371,168]

class CAL_SF_AMEV1(CalendarObject):
            objectIdentifier=("calendar", 102)
            objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_CAL02"
            description="GA-System Automationsschwerpunkt AS Kalender Schulferien"
            presentValue=False
            dateList=[] # ListOf(CalendarEntry)           
            profileName='CAL_SF_AMEV1 Jahreskalender Schulferien'
            propertyList=[75,77,79,28,85,23,371,168]

class CAL_BF_AMEV1(CalendarObject):
            objectIdentifier=("calendar", 103)
            objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_CAL03"
            description="GA-System Automationsschwerpunkt AS Kalender Betriebsferien"
            presentValue=False
            dateList=[] # ListOf(CalendarEntry)           
            profileName='CAL_BF_AMEV1 Jahreskalender Betriebsferin'
            propertyList=[75,77,79,28,85,23,371,168]

class CAL_ALG_AMEV1(CalendarObject):
            objectIdentifier=("calendar", 104)
            objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_CAL04"
            description="GA-System Automationsschwerpunkt AS Kalender allgemein"
            presentValue=False
            dateList="",#: ListOf(CalendarEntry            
            profileName='CAL_ALG_AMEV1 Jahreskalender [frei wählbar]'
            propertyList=[75,77,79,28,85,23,371,168]
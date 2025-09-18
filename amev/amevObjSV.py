from bacpypes3.object import StructuredViewObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

class SV_ANL_AMEV1(StructuredViewObject):
    objectIdentifier=("structuredView", 101)
    objectName="MUSTER_480_ASP01°01_#####_###_AS~01_#####_SV~01"
    description="MUSTER_Gebäudeautomationssystem Automationsschwerpunkt AS System"
    nodeType= "system"
    nodeSubtype= "Anlage"
    subordinateList=ArrayOf(DeviceObjectReference)([
        #DeviceObjectReference(objectIdentifier=("device"999)),
        ])
    subordinateAnnotations=([
        "",
        ])
    #subordinateTags: ArrayOf(NameValueCollection)
    #subordinateNodeTypes: ArrayOf(NodeType)
    #subordinateRelationships: ArrayOf(Relationship)
    #defaultSubordinateRelationship: Relationship
    #repesents
    #tags
    #Profile_Location
    profileName="SV_ANL_AMEV1 Anlage"
    propertyList=[75,77,79,28,208,207,211,210,371,168] #210,488,487,489,490,491,486,485,168

class SV_BGP_AMEV1(StructuredViewObject):
    objectIdentifier=("structuredView", 102)
    objectName="MUSTER_480_ASP01°01_#####_###_AS~01_#####_SV~02"
    description="MUSTER_Gebäudeautomationssystem Automationsschwerpunkt AS Subsystem"
    nodeType= "subsystem"
    nodeSubtype= "Baugruppe"
    subordinateList=ArrayOf(DeviceObjectReference)([
        #DeviceObjectReference(objectIdentifier=("device"999)),
        ])
    subordinateAnnotations=([
        "",
        ])
    #subordinateTags: ArrayOf(NameValueCollection)
    #subordinateNodeTypes: ArrayOf(NodeType)
    #subordinateRelationships: ArrayOf(Relationship)
    #defaultSubordinateRelationship: Relationship
    #repesents
    #tags
    #Profile_Location
    profileName="SV_BGP_AMEV1 Baugruppe"
    propertyList=[75,77,79,28,208,207,211,210,371,168] #210,488,487,489,490,491,486,485,168

class SV_AGG_AMEV1(StructuredViewObject):
    objectIdentifier=("structuredView", 103)
    objectName="MUSTER_480_ASP01°01_#####_###_AS~01_#####_SV~03"
    description="MUSTER_Gebäudeautomationssystem Automationsschwerpunkt AS Equipment"
    nodeType= "equipment"
    nodeSubtype= "Aggregat"
    subordinateList=ArrayOf(DeviceObjectReference)([
        #DeviceObjectReference(objectIdentifier=("device"999)),
        ])
    subordinateAnnotations=([
        "",
        ])
    #subordinateTags: ArrayOf(NameValueCollection)
    #subordinateNodeTypes: ArrayOf(NodeType)
    #subordinateRelationships: ArrayOf(Relationship)
    #defaultSubordinateRelationship: Relationship
    #repesents
    #tags
    #Profile_Location
    profileName="SV_AGG_AMEV1 Aggregat"
    propertyList=[75,77,79,28,208,207,211,210,371,168] #210,488,487,489,490,491,486,485,168
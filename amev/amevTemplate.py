from amevObjAI import *
from amevObjAO import *
from amevObjAV import *
from amevObjBI import *
from amevObjBO import *
from amevObjBV import *
from amevObjCAL import *
from amevObjEE import *

from amevObjLP import *
from amevObjNC import *
from amevObjSCH import *

from amevObjMV import *
from amevObjTL import *

from amevObjSV import *

def Test_AMEV_Objekte(app):
        ai10001=AI_MW_T_H_HT_AMEV1(
#            objectIdentifier=("analog-input", 1),
#            objectName="ORTS-BAS_AI",
        )
        app.add_object(ai10001)

        ai102=AI_MW_T_AU_AMEV1(            
        )
        #app.add_object(ai102)

        ai103=AI_MW_T_H_NT_AMEV1(            
        )
        app.add_object(ai103)

        ai104=AI_MW_T_H_HT_AMEV1(            
        )
        #app.add_object(ai104)

        ai114=AI_MW_M_L_RU_AMEV1(            
        )
        app.add_object(ai114)

        ai118=AI_MW_P_AMEV1(            
        )
        app.add_object(ai118)

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
            #description="GA-System Automationsschwerpunkt AS System"
        )
        app.add_object(sv101)

        sv102=SV_BGP_AMEV1(
            #objectIdentifier=("structuredView", 102)
            #objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_SV~02"
            #description="GA-System Automationsschwerpunkt AS Subsystem"
        )
        app.add_object(sv102)
        
        sv103=SV_AGG_AMEV1(
            #objectIdentifier=("structuredView", 103)
            #objectName="ORTS-BAS_480_ASP01°01_#####_###_AS~01_#####_SV~03"
            #description="GA-System Automationsschwerpunkt AS Equipment"
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
 

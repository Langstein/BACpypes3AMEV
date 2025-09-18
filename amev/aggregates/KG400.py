from amevTemplate import *


def AGG_SSK_AMEV1(app):
        Ort_BAS="ORTS-BAS"
        Ort_KT ="" #"Ortsangabe"
        Gew_BAS="480"
        Gew_KT ="GA-System" #"Wärmeversorgungsanlage"
        Anl_BAS="ASP40°01"
        Anl_KT ="ASP 40 Feld 1"
        Bgp_BAS="#####"
        Bgp_KT =""
        MeP_BAS="###"
        MeP_KT =""
        Agg_BAS="SSK01"
        Agg_KT ="Schaltschrank"
        Btm_BAS="#####"
        Btm_KT =""
        sv153=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 138),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"",
            subordinateList=ArrayOf(DeviceObjectReference)([
                DeviceObjectReference(objectIdentifier=("binary-input",139)),
                DeviceObjectReference(objectIdentifier=("binary-input",140)),
                DeviceObjectReference(objectIdentifier=("binary-input",141)),
                DeviceObjectReference(objectIdentifier=("binary-input",142)),
                DeviceObjectReference(objectIdentifier=("binary-input",143)),
                DeviceObjectReference(objectIdentifier=("binary-input",144)),
                DeviceObjectReference(objectIdentifier=("binary-input",145)),
                DeviceObjectReference(objectIdentifier=("binary-input",146)),
                DeviceObjectReference(objectIdentifier=("binary-input",147)),
                DeviceObjectReference(objectIdentifier=("trend-log",148)),
                DeviceObjectReference(objectIdentifier=("binary-value",149)),
                DeviceObjectReference(objectIdentifier=("trend-log",150)),
                DeviceObjectReference(objectIdentifier=("binary-output",151)),
                ]),
            subordinateAnnotations=([
                "Schaltschrank Endschalter Alarmmeldung",
                "Schaltschrank Spannung Störmeldung",
                "Schaltschrank Überspannung Störmeldung",
                "Schaltschrank Phasenwächter Störmeldung",
                "Schaltschrank Gleichspannung 24V Unterspannung Störmeldung",
                "Schaltschrank Gleichspannung 12V Unterspannung Störmeldung",
                "Schaltschrank Unterspannung Störmeldung",
                "Schaltschrank Unterspannung Störmeldung",
                "Schaltschrank Taster Entriegelung",
                "Schaltschrank Taster Entriegelung Datenaufzeichnung",
                "Schaltschrank Bedieneinheit Entriegelung",
                "Schaltschrank Bedieneinheit Entriegelung Datenaufzeichnung",
                "Schaltschrank Lampe Schaltbefehl",
                ]),
            
        )
        app.add_object(sv153)

        Btm_BAS="GS~01"
        Btm_KT ="Endschalter"
        bi139=BI_AM_ZOF_AMEV1(
            objectIdentifier=("binary-input", 139),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"AM~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Alarmeldung",                
        )
        app.add_object(bi139)
        
        Bgp_BAS="ASV01"
        Bgp_KT ="AV Stromversorgung"
        MeP_BAS="AC~"
        MeP_KT ="Wechselspannung"
        Btm_BAS="E~~01"
        Btm_KT ="Spannung"
        bi140=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 140),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Störmeldung",                
        )
        app.add_object(bi140)

        Btm_BAS="EH~01"
        Btm_KT ="Überspannung"
        bi141=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 141),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Störmeldung",                
        )
        app.add_object(bi141)

        Btm_BAS="EHP01"
        Btm_KT ="Phasenwächter"
        bi142=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 142),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Störmeldung",                
        )
        app.add_object(bi142)
        
        MeP_BAS="DC~"
        MeP_KT ="Gleichspannung"
        Btm_BAS="EL~01"
        Btm_KT ="Unterspannung"
        bi143=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 143),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"24V Störmeldung",                
        )
        app.add_object(bi143) 

        MeP_BAS="DC~"
        MeP_KT ="Gleichspannung"
        Btm_BAS="EL~01"
        Btm_KT ="Unterspannung"
        bi144=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 144),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~02",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"12V Störmeldung",                
        )
        app.add_object(bi144)

        MeP_BAS="AC~"
        MeP_KT ="Wechselspannung"
        Btm_BAS="EL~01"
        Btm_KT ="Unterspannung"
        bi145=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 145),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Störmeldung",                
        )
        app.add_object(bi145) 

        MeP_BAS="L1N"
        MeP_KT ="Phase L1-N"
        Btm_BAS="EL~01"
        Btm_KT ="Unterspannung"
        bi146=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 146),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Störmeldung",                
        )
        app.add_object(bi146)

        MeP_BAS="###"
        MeP_KT =""
        Btm_BAS="TAS01"
        Btm_KT =""
        bi147=BI_ENT_AMEV1(
            objectIdentifier=("binary-input", 147),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ETR01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Entriegelung",                
        )
        app.add_object(bi147)  

        tl148=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 148),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ETR01_TL",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Entriegelung Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier=("binary-input", 147),
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl148)   

        MeP_BAS="###"
        MeP_KT =""
        Btm_BAS="UBE01"
        Btm_KT ="Bedieneinheit"
        tl150=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 150),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ETR01_TL",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Entriegelung Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier=("binary-value", 149),
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl150) 

        
        MeP_BAS="###"
        MeP_KT =""
        Btm_BAS="LAM01"
        Btm_KT ="Lampe"
        bo151=BO_SB_AMEV1(
            objectIdentifier=("binary-output", 151),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SB~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Schaltbefehl",                
        )
        app.add_object(bo151)   


def AGG_EF_T_AMEV1(app):
        Ort_BAS="ORTS-BAS"
        Ort_KT ="" #"Ortsangabe"
        Gew_BAS="400"
        Gew_KT ="" #"Wärmeversorgungsanlage"
        Anl_BAS="#####°##"
        Anl_KT =""
        Bgp_BAS="###"
        Bgp_KT =""
        MeP_BAS="###"
        MeP_KT =""
        Agg_BAS="#####"
        Agg_KT =""
        Btm_BAS="#####"
        Btm_KT =""
        sv153=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 153),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"",
            subordinateList=ArrayOf(DeviceObjectReference)([
                DeviceObjectReference(objectIdentifier=("analog-input",154)),
                DeviceObjectReference(objectIdentifier=("trend-log",155)),
                ]),
            subordinateAnnotations=([
                "Messwert",
                "Messwert Datenaufzeichnung",
                ]),
            
        )
        app.add_object(sv153)

        ai154=AI_MW_T_H_HT_AMEV1(
            objectIdentifier=("analog-input", 154),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Messwert",
        )
        app.add_object(ai154)

        tl155=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 155),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01_TL",
            description=Ort_KT+" "+""+Gew_KT+" "+""+Anl_KT+" "+""+Bgp_KT+" "+""+MeP_KT+" "+""+Agg_KT+" "+""+Btm_KT+" "+"Messwert Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier=("analog-input", 154),
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl155)        
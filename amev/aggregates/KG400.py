from amevTemplate import *


def AGG_SSK_AMEV1(app):
        Ort_BAS="ORTS-BAS"
        Ort_Text ="" #"Ortsangabe"
        Gew_BAS="480"
        Gew_Text ="GA-System" #"Wärmeversorgungsanlage"
        Anl_BAS="ASP40°01"
        Anl_Text ="ASP 40 Feld 1"
        Bgp_BAS="#####"
        Bgp_Text =""
        MeP_BAS="###"
        MeP_Text =""
        Agg_BAS="SSK01"
        Agg_Text ="Schaltschrank"
        Btm_BAS="#####"
        Btm_Text =""
        sv153=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 138),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"",
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
        Btm_Text ="Endschalter"
        bi139=BI_AM_ZOF_AMEV1(
            objectIdentifier=("binary-input", 139),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"AM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Alarmeldung",                
        )
        app.add_object(bi139)
        
        Bgp_BAS="ASV01"
        Bgp_Text ="AV Stromversorgung"
        MeP_BAS="AC~"
        MeP_Text ="Wechselspannung"
        Btm_BAS="E~~01"
        Btm_Text ="Spannung"
        bi140=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 140),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Störmeldung",                
        )
        app.add_object(bi140)

        Btm_BAS="EH~01"
        Btm_Text ="Überspannung"
        bi141=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 141),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Störmeldung",                
        )
        app.add_object(bi141)

        Btm_BAS="EHP01"
        Btm_Text ="Phasenwächter"
        bi142=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 142),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Störmeldung",                
        )
        app.add_object(bi142)
        
        MeP_BAS="DC~"
        MeP_Text ="Gleichspannung"
        Btm_BAS="EL~01"
        Btm_Text ="Unterspannung"
        bi143=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 143),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"24V Störmeldung",                
        )
        app.add_object(bi143) 

        MeP_BAS="DC~"
        MeP_Text ="Gleichspannung"
        Btm_BAS="EL~01"
        Btm_Text ="Unterspannung"
        bi144=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 144),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~02",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"12V Störmeldung",                
        )
        app.add_object(bi144)

        MeP_BAS="AC~"
        MeP_Text ="Wechselspannung"
        Btm_BAS="EL~01"
        Btm_Text ="Unterspannung"
        bi145=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 145),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Störmeldung",                
        )
        app.add_object(bi145) 

        MeP_BAS="L1N"
        MeP_Text ="Phase L1-N"
        Btm_BAS="EL~01"
        Btm_Text ="Unterspannung"
        bi146=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 146),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Störmeldung",                
        )
        app.add_object(bi146)

        MeP_BAS="###"
        MeP_Text =""
        Btm_BAS="TAS01"
        Btm_Text =""
        bi147=BI_ENT_AMEV1(
            objectIdentifier=("binary-input", 147),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ETR01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Entriegelung",                
        )
        app.add_object(bi147)  

        tl148=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 148),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ETR01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Entriegelung Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier=("binary-input", 147),
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl148)   

        MeP_BAS="###"
        MeP_Text =""
        Btm_BAS="UBE01"
        Btm_Text ="Bedieneinheit"
        bv149=BI_ENT_AMEV1(
            objectIdentifier=("binary-value", 149),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ETR01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Entriegelung",                
        )
        app.add_object(bv149)         
        tl150=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 150),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ETR01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Entriegelung Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier=("binary-value", 149),
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl150) 

        
        MeP_BAS="###"
        MeP_Text =""
        Btm_BAS="LAM01"
        Btm_Text ="Lampe"
        bo151=BO_SB_AMEV1(
            objectIdentifier=("binary-output", 151),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SB~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Schaltbefehl",                
        )
        app.add_object(bo151)   

def AGG_EF_T_AMEV1(app):
        Ort_BAS="ORTS-BAS"
        Ort_Text ="" #"Ortsangabe"
        Gew_BAS="400"
        Gew_Text ="" #"Wärmeversorgungsanlage"
        Anl_BAS="#####°##"
        Anl_Text =""
        Bgp_BAS="###"
        Bgp_Text =""
        MeP_BAS="###"
        MeP_Text =""
        Agg_BAS="EF~01"
        Agg_Text =""
        Btm_BAS="T~~01"
        Btm_Text ="Temperatur"
        sv153=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 153),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"",
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
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Messwert",
        )
        app.add_object(ai154)

        tl155=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 155),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Messwert Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier=("analog-input", 154),
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl155)

def AGG_EF_QPH_AMEV1(app):
        Ort_BAS="ORTS-BAS"
        Ort_Text ="" #"Ortsangabe"
        Gew_BAS="400"
        Gew_Text ="" #"Wärmeversorgungsanlage"
        Anl_BAS="#####°##"
        Anl_Text =""
        Bgp_BAS="###"
        Bgp_Text =""
        MeP_BAS="###"
        MeP_Text =""
        Agg_BAS="EF~01"
        Agg_Text =""
        Btm_BAS="QPH01"
        Btm_Text ="Leitfähigkeitt"
        sv157=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 157),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"",
            subordinateList=ArrayOf(DeviceObjectReference)([
                DeviceObjectReference(objectIdentifier=("analog-input",158)),
                DeviceObjectReference(objectIdentifier=("trend-log",159)),
                ]),
            subordinateAnnotations=([
                "Messwert",
                "Messwert Datenaufzeichnung",
                ]),
            
        )
        app.add_object(sv157)

        ai158=AI_MW_QPH_AMEV1(
            objectIdentifier=("analog-input", 158),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Messwert",
        )
        app.add_object(ai158)

        tl159=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 159),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Messwert Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier=("analog-input", 158),
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl159)

def AGG_PPE_E1_AMEV1(app):
        Ort_BAS="ORTS-BAS"
        Ort_Text ="" #"Ortsangabe"
        Gew_BAS="430"
        Gew_Text ="Lufttechnische Anlage" #"Wärmeversorgungsanlage"
        Anl_BAS="LTA01°00"
        Anl_Text ="Lüftungsanlage"
        Bgp_BAS="ERH01"
        Bgp_Text ="Erhitzer"
        MeP_BAS="HZV"
        MeP_Text ="Heizwasser Vorlauf"
        Agg_BAS="PPE01"
        Agg_Text ="Pumpe 1"
        Btm_BAS="#####"
        Btm_Text =""

        sv161=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 161),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"",
            subordinateList=([
                DeviceObjectReference(objectIdentifier=("binary-output",162)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",164)),
                DeviceObjectReference(objectIdentifier=("binary-input",163)),
                DeviceObjectReference(objectIdentifier=("trend-log",165)),
                DeviceObjectReference(objectIdentifier=("binary-input",166)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",167)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",168)),
                ]),
            subordinateAnnotations=([
                "Schaltbefehl",
                "Ausführkontrolle",
                "Betriebsmeldung",
                "Betriebsmeldung Datenaufzeichnung",
                "Störmeldung",
                "UBE Hand",
                "LVB Hand"
                ]),
            
        )
        app.add_object(sv161)

        bo162=BO_SB_AMEV1(
            objectIdentifier=("binary-output", 162),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SB~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Schaltbefehl",
        )
        app.add_object(bo162)

        bi163=BI_BM_AMEV1(
            objectIdentifier=("binary-input", 163),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"BM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Betriebsmeldung",
        )
        app.add_object(bi163)

        ee164=EE_CMDF_AMEV1(
            objectIdentifier=("eventEnrollment", 164),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"AK~01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Ausführkontrolle",
            eventParameters=EventParameter(
                commandFailure=EventParameterCommandFailure(
                    timeDelay=3,
                    feedbackPropertyReference=DeviceObjectPropertyReference(
                        objectIdentifier="binaryInput,163",
                        propertyIdentifier=PropertyIdentifier.presentValue,
                        #propertyArrayIndex=11,
                        #deviceIdentifier=this_device.objectIdentifier,
                    )
                )
            ),
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryOutput,162",
                propertyIdentifier=PropertyIdentifier.presentValue,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee164)
        ee164.eventMessageTextsConfig[0] = "Abweichung: "+ee164.description
        ee164.eventMessageTextsConfig[1] = "Fehler: "+ee164.description
        ee164.eventMessageTextsConfig[2] = "Normal: "+ee164.description

        tl165=TL_BN_AMEV1(
            objectIdentifier=("trend-log", 165),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"BM~01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Betriebsmeldung Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="binary-input,163",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl165)

        bi166=BI_SM_AMEV1(
            objectIdentifier=("binary-input", 166),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SM~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Störmeldung",
        )
        app.add_object(bi166)        

        Btm_BAS="UBE01"
        Btm_Text ="Bedieneinheit"
        ee167=EE_CCP_AMEV1(
            objectIdentifier=("eventEnrollment", 167),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDB01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Hand schalten",
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
                objectIdentifier="binaryOutput,162",
                propertyIdentifier=PropertyIdentifier.currentCommandPriority,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee167)
        ee167.eventMessageTextsConfig[0] = "Hand: "+ee167.description
        ee167.eventMessageTextsConfig[1] = "Fehler: "+ee167.description
        ee167.eventMessageTextsConfig[2] = "Normal: "+ee167.description
        
        Btm_BAS="LVB01"
        Btm_Text ="LVB"
        ee170=EE_COB_AMEV1(
        objectIdentifier=("eventEnrollment", 170),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDB01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Hand schalten",
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryOutput,162",
                propertyIdentifier=PropertyIdentifier.statusFlags,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee170)
        ee170.eventMessageTextsConfig[0] = "Hand: "+ee170.description
        ee170.eventMessageTextsConfig[1] = "Fehler: "+ee170.description
        ee170.eventMessageTextsConfig[2] = "Normal: "+ee170.description

def AGG_VEN_SB_AMEV1(app):
        Ort_BAS="ORTS-BAS"
        Ort_Text ="" #"Ortsangabe"
        Gew_BAS="420"
        Gew_Text ="Wärmeversorgung" #"Wärmeversorgungsanlage"
        Anl_BAS="VTA01°00"
        Anl_Text ="Verteilanlage"
        Bgp_BAS="HVT01"
        Bgp_Text ="Heizverteiler 1"
        MeP_BAS="HZV"
        MeP_Text ="Heizwasser Vorlauf"
        Agg_BAS="VEN01"
        Agg_Text ="Ventil 1"
        Btm_BAS="MOT01"
        Btm_Text =""

        sv226=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 226),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"",
            subordinateList=([
                DeviceObjectReference(objectIdentifier=("binary-output",227)),
                DeviceObjectReference(objectIdentifier=("binary-input",228)),
                DeviceObjectReference(objectIdentifier=("binary-input",229)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",230)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",231)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",232)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",233)),
                DeviceObjectReference(objectIdentifier=("trend-log",236)),
                DeviceObjectReference(objectIdentifier=("trend-log",237)),
                DeviceObjectReference(objectIdentifier=("trend-log",238)),
                ]),
            subordinateAnnotations=([
                "Schaltbefehl",
                "Rückmeldung Auf",
                "Rückmeldung Zu",
                "Ausführkontrolle Auf",
                "Ausführkontrolle zu",
                "UBE Hand",
                "LVB Hand",
                "Schaltbefehl Datenaufzeichnung",
                "Rückmeldung Auf Datenaufzeichnung",
                "Rückmeldung Zu Datenaufzeichnung"
                ]),
            
        )
        app.add_object(sv226)
        
        Btm_BAS="MOT01"
        Btm_Text =""

        bo227=BO_SB_AMEV1(
            objectIdentifier=("binary-output", 227),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SB~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Schaltbefehl",
        )
        app.add_object(bo227)

        bi228=BI_RM_A_AMEV1(
            objectIdentifier=("binary-input", 228),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"RMA01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Rückmeldung Auf",
        )
        app.add_object(bi228)

        bi229=BI_RM_A_AMEV1(
            objectIdentifier=("binary-input", 229),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"RMZ01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Rückmeldung Zu",
        )
        app.add_object(bi229)

        ee230=EE_CMDF_AMEV1(
            objectIdentifier=("eventEnrollment", 230),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"AKA01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Ausführkontrolle Auf",
            eventParameters=EventParameter(
                commandFailure=EventParameterCommandFailure(
                    timeDelay=3,
                    feedbackPropertyReference=DeviceObjectPropertyReference(
                        objectIdentifier="binaryInput,228",
                        propertyIdentifier=PropertyIdentifier.presentValue,
                        #propertyArrayIndex=11,
                        #deviceIdentifier=this_device.objectIdentifier,
                    )
                )
            ),
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryOutput,227",
                propertyIdentifier=PropertyIdentifier.presentValue,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee230)
        ee230.eventMessageTextsConfig[0] = "Abweichung: "+ee230.description
        ee230.eventMessageTextsConfig[1] = "Fehler: "+ee230.description
        ee230.eventMessageTextsConfig[2] = "Normal: "+ee230.description

        ee231=EE_CMDF_AMEV1(
            objectIdentifier=("eventEnrollment", 231),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"AKZ01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Ausführkontrolle Zu",
            eventParameters=EventParameter(
                commandFailure=EventParameterCommandFailure(
                    timeDelay=3,
                    feedbackPropertyReference=DeviceObjectPropertyReference(
                        objectIdentifier="binaryInput,229",
                        propertyIdentifier=PropertyIdentifier.presentValue,
                        #propertyArrayIndex=11,
                        #deviceIdentifier=this_device.objectIdentifier,
                    )
                )
            ),
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryOutput,227",
                propertyIdentifier=PropertyIdentifier.presentValue,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee231)
        ee231.eventMessageTextsConfig[0] = "Abweichung: "+ee231.description
        ee231.eventMessageTextsConfig[1] = "Fehler: "+ee231.description
        ee231.eventMessageTextsConfig[2] = "Normal: "+ee231.description

        Btm_BAS="UBE01"
        Btm_Text ="Bedieneinheit"
        ee232=EE_CCP_AMEV1(
            objectIdentifier=("eventEnrollment", 232),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDB01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Hand schalten",
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
                objectIdentifier="binaryOutput,162",
                propertyIdentifier=PropertyIdentifier.currentCommandPriority,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee232)
        ee232.eventMessageTextsConfig[0] = "Hand: "+ee232.description
        ee232.eventMessageTextsConfig[1] = "Fehler: "+ee232.description
        ee232.eventMessageTextsConfig[2] = "Normal: "+ee232.description
        
        Btm_BAS="LVB01"
        Btm_Text ="LVB"
        ee233=EE_COB_AMEV1(
        objectIdentifier=("eventEnrollment", 233),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDB01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Hand schalten",
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="binaryOutput,227",
                propertyIdentifier=PropertyIdentifier.statusFlags,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee233)
        ee233.eventMessageTextsConfig[0] = "Hand: "+ee233.description
        ee233.eventMessageTextsConfig[1] = "Fehler: "+ee233.description
        ee233.eventMessageTextsConfig[2] = "Normal: "+ee233.description

        tl236=TL_BN_AMEV1(
            objectIdentifier=("trend-log", 236),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SB~01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Schaltbefehl Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="binary-output,227",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl236)

        tl237=TL_BN_AMEV1(
            objectIdentifier=("trend-log", 237),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"RMA01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Rückmeldung Auf Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="binary-input,228",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl237)

        tl238=TL_BN_AMEV1(
            objectIdentifier=("trend-log", 238),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"RMZ01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Rückmeldung Zu Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="binary-input,229",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl238)




def AGG_VEN_ST_AMEV1(app):
        Ort_BAS="ORTS-BAS"
        Ort_Text ="" #"Ortsangabe"
        Gew_BAS="430"
        Gew_Text ="Lufttechnische Anlage" #"Wärmeversorgungsanlage"
        Anl_BAS="LTA01°00"
        Anl_Text ="Lüftungsanlage"
        Bgp_BAS="ERH01"
        Bgp_Text ="Erhitzer"
        MeP_BAS="HZV"
        MeP_Text ="Heizwasser Vorlauf"
        Agg_BAS="VEN01"
        Agg_Text ="Ventil 1"
        Btm_BAS="MOT01"
        Btm_Text =""

        sv240=SV_AGG_AMEV1(
            objectIdentifier=("structured-view", 240),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"SV~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"",
            subordinateList=([
                DeviceObjectReference(objectIdentifier=("analog-output",241)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",242)),
                DeviceObjectReference(objectIdentifier=("analog-input",243)),
                DeviceObjectReference(objectIdentifier=("trend-log",244)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",245)),
                DeviceObjectReference(objectIdentifier=("event-enrollment",246)),
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
        app.add_object(sv240)
        
        Btm_BAS="MOT01"
        Btm_Text =""
        
        ao241 = AO_ST_AMEV1(
            objectIdentifier=("analog-output", 241),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ST~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Stellsignal",
            statusFlags=[False, False, False, False],
                    )
        app.add_object(ao241)

        ai243=AI_RW_AMEV1(
            objectIdentifier=("analog-input", 243),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"RW~01",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Rückführwert",
        )
        app.add_object(ai243)        

        tl244=TL_AN_P_AMEV1(
            objectIdentifier=("trend-log", 244),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"MW~01_TL",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Messwert Datenaufzeichnung",
            logDeviceObjectProperty=DeviceObjectPropertyReference(
                objectIdentifier="analog-input,243",
                propertyIdentifier=PropertyIdentifier.presentValue,
            ),
        )
        app.add_object(tl244)

        ee242=EE_FLIM_AMEV1(
            objectIdentifier=("eventEnrollment", 242),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"ABW01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Abweichung",
            eventParameters=EventParameter(
                floatingLimit=EventParameterFloatingLimit(
                    timeDelay=60,
                    setpointReference = DeviceObjectPropertyReference(
                        objectIdentifier="analogInput,243",
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
                objectIdentifier="analogOutput,1024110",
                propertyIdentifier=PropertyIdentifier.presentValue,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee242)
        ee242.eventMessageTextsConfig[0] = "Abweichung: "+ee242.description
        ee242.eventMessageTextsConfig[1] = "Fehler: "+ee242.description
        ee242.eventMessageTextsConfig[2] = "Normal: "+ee242.description
        
        Btm_BAS="UBE01"
        Btm_Text ="Bedieneinheit"
        ee244=EE_CCP_AMEV1(
            objectIdentifier=("eventEnrollment", 244),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDG01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Hand stellen",
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
                objectIdentifier="analogOutput,241",
                propertyIdentifier=PropertyIdentifier.currentCommandPriority,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee244)
        ee244.eventMessageTextsConfig[0] = "Hand: "+ee244.description
        ee244.eventMessageTextsConfig[1] = "Fehler: "+ee244.description
        ee244.eventMessageTextsConfig[2] = "Normal: "+ee244.description
        
        Btm_BAS="LVB01"
        Btm_Text ="LVB"
        ee245=EE_COB_AMEV1(
        objectIdentifier=("eventEnrollment", 245),
            objectName=Ort_BAS+"_"+""+Gew_BAS+"_"+""+Anl_BAS+"_"+""+Bgp_BAS+"_"+""+MeP_BAS+"_"+""+Agg_BAS+"_"+""+Btm_BAS+"_"+"HDG01_EE",
            description=Ort_Text+" "+""+Gew_Text+" "+""+Anl_Text+" "+""+Bgp_Text+" "+""+MeP_Text+" "+""+Agg_Text+" "+""+Btm_Text+" "+"Hand stellen",
            objectPropertyReference=DeviceObjectPropertyReference(
                objectIdentifier="analogOutput,1010",
                propertyIdentifier=PropertyIdentifier.statusFlags,
                #propertyArrayIndex=11,
                #deviceIdentifier=this_device.objectIdentifier,
            ),
        )
        app.add_object(ee245)
        ee245.eventMessageTextsConfig[0] = "Hand: "+ee245.description
        ee245.eventMessageTextsConfig[1] = "Fehler: "+ee245.description
        ee245.eventMessageTextsConfig[2] = "Normal: "+ee245.description       

def KG400_Demo(app):
    AGG_SSK_AMEV1(app)
    AGG_EF_T_AMEV1(app)
    AGG_EF_QPH_AMEV1(app)
    AGG_PPE_E1_AMEV1(app)
    AGG_VEN_SB_AMEV1(app)
    AGG_VEN_ST_AMEV1(app)
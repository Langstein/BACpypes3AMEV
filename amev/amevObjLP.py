from bacpypes3.object import LoopObject
from bacpypes3.basetypes import * 
from bacpypes3.primitivedata import *

class LP_AN_AMEV1(LoopObject):
    objectIdentifier=("loop", 101)
    objectName="MUSTER_420_VTA01_HZK01_HZ~_EF~01_T~~01_LP~01"
    description="Wärmeversorgungsanlage Verteilanlage Heizkreis Heizwasser Temperatur Regler"
    presentValue=5.1
    statusFlags=[False, False, False, False]
    eventState="normal"
    reliability="noFaultDetected"
    outOfService=False
    updateInterval = 1
    outputUnits="percent"
    manipulatedVariableReference=ObjectPropertyReference(
        objectIdentifier="analogOutput,201",
        propertyIdentifier=PropertyIdentifier.presentValue,
        propertyArrayIndex=11,
    )
    controlledVariableReference=ObjectPropertyReference(
        objectIdentifier="analogInput,102",
        propertyIdentifier=PropertyIdentifier.presentValue,
        #propertyArrayIndex=1,
    )
    controlledVariableValue=5.1
    controlledVariableUnits="percent"
    setpointReference=ObjectPropertyReference(
        objectIdentifier="analogValue,201",
        propertyIdentifier=PropertyIdentifier.presentValue,
        #propertyArrayIndex=1,
    )
    setpoint=20
    action="reverse"
    proportionalConstant = 6
    proportionalConstantUnits = "degreesCelsius"
    integralConstant=1
    integralConstantUnits="percent"
    derivativeConstant=1
    derivativeConstantUnits="percent"
    bias=5
    minimumOutput=0
    maximumOutput=100
    priorityForWriting=11
    covIncrement=2
    #timeDelay=5, notificationClass=4194303, errorLimit=20, deadband=0.5,
    #eventEnable=[True, True, True],
    #ackedTransitions=[True, True, True],
    #notifyType="event",
    #eventTimeStamps=[
    #    TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
    #    TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
    #    TimeStamp(dateTime=DateTime(date=(255,255,255,255), time=(255,255,255,255))), 
    #    ],
    #eventMessageTexts=ArrayOf(CharacterString)(["[letzter Meldetext Alarmmeldung]","[letzter Meldetext Fehlermeldung]","[letzter Meldetext Normalisierung]"]),
    #eventMessageTextsConfig=ArrayOf(CharacterString)(["Alarm: LP 1","Fehler: LP 1","Normal: LP 1"]),
    #eventDetectionEnable=False, 
    #eventAlgorithmInhibitRef=Meldeschauer_inhibit,
    #eventAlgorithmInhibit=False, timeDelayNormal=1, reliabilityEvaluationInhibit=False,
    profileName="LP_AN_AMEV1 Regler"
    propertyList=[75,77,79,85,28,111,36,103,81,118,82,60,19,21,20,109,108,2,93,94,49,50,26,27,14,61,68,88,22,113,17,34,25,35,0,72,130,351,352,353,355,354,356,357,371,168] #,390,486,485,

class PID:
    def __init__(self, Kp, Ki, Kd, setpoint=0.0, output_limits=(None, None)):
        self.Kp = Kp  # Proportionalfaktor
        self.Ki = Ki  # Integralfaktor
        self.Kd = Kd  # Differentialfaktor

        self.setpoint = setpoint  # Sollwert

        self._integral = 0.0
        self._last_error = None
        self._last_time = None

        self.output_limits = output_limits  # (min, max)

    def reset(self):
        """Setzt den Regler-Zustand zurück."""
        self._integral = 0.0
        self._last_error = None
        self._last_time = None

    def compute(self, actual_value, current_time):
        """Berechnet den PID-Regelwert."""
        error = self.setpoint - actual_value
        dt = 0.0

        if self._last_time is not None:
            dt = current_time - self._last_time
        else:
            # Beim ersten Aufruf dt auf 0 setzen
            dt = 0.0

        # Integralterm
        if dt > 0.0:
            self._integral += error * dt

        # Differentialterm
        derivative = 0.0
        if self._last_error is not None and dt > 0.0:
            derivative = (error - self._last_error) / dt

        # PID-Ausgabe berechnen
        output = (
            self.Kp * error +
            self.Ki * self._integral +
            self.Kd * derivative
        )

        # Begrenzung der Ausgabe
        min_output, max_output = self.output_limits
        if min_output is not None:
            output = max(min_output, output)
        if max_output is not None:
            output = min(max_output, output)

        # Zustand aktualisieren
        self._last_error = error
        self._last_time = current_time

        return output
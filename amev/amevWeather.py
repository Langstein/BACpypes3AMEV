from bacpypes3.object import * #AnalogInputObject, AnalogOutputObject
import asyncio

import aiohttp

location = "Berlin"

async def wetter_daten(app, tru: Object, mru: Object, wig: Object, wir: Object) -> None:
    try:
        while True:
            try:
                ol=app.objectIdentifier
                locationObj = list(ol.values())[2]
                location=locationObj.presentValue

                print("Start Wetterabfrage")
                print(locationObj.presentValue)

                url = f"https://wttr.in/{location}?format=j1"
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as resp:
                        daten = await resp.json()
                        aktuell = daten["current_condition"][0]
                wetter={
                    "ort": location,
                    "temperatur": aktuell["temp_C"],
                    "feuchte": aktuell["humidity"],
                    "helligkeit": aktuell["weatherDesc"][0]["value"],
                    "windgeschwindigkeit": aktuell["windspeedKmph"],
                    "windrichtung_text": aktuell["winddir16Point"],
                    "windrichtung_grad": aktuell["winddirDegree"],
                }

                tru.presentValue = aktuell["temp_C"]
                mru.presentValue = aktuell["humidity"]
                wig.presentValue = aktuell["windspeedKmph"]
                
                if wig.units == 74:
                    wig.presentValue = wig.presentValue/3.6
                    wig.resolution=1/3.6
                else:
                    wig.resolution=1
                    
                wir.presentValue = aktuell["winddirDegree"]
                tru.reliability = "noFaultDetected"
                mru.reliability = "noFaultDetected"
                wig.reliability = "noFaultDetected"
                wir.reliability = "noFaultDetected"

            except Exception as e:
                tru.presentValue = -5
                tru.reliability = "communicationFailure"
                mru.presentValue = -5
                mru.reliability = "communicationFailure"
                wig.presentValue = -5
                wig.reliability = "communicationFailure"
                wir.presentValue = -5
                wir.reliability = "communicationFailure"
                print("Fehler bei Abfrage Wetterdaten")

            await asyncio.sleep(60)

    except KeyboardInterrupt:
        pass 


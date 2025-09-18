# BACpypes3 - Python library for AMEV BACtwin demonstration

This folk uses BACpypes3 library to create some Demo-Application of the AMEV BACtwin.

See [AMEV BACtwin](https://www.amev-online.de/AMEVInhalt/Planen/Gebaeudeautomation/BACtwin/) for the Documentation.


## System requirements
- python > 3.12
- sudo apt install pipenv

## Usage
- Tested with python 3.12
- Clone this folk
- change into you directory
- Sent Env-Variables:
  >pipenv install --dev

  >pipenv shell
- change into amev directory
- start amev-server.py by using then IP Address
  >python3 amev-server.py --address [ip]/24

#### NOTE: This is under development. The BACnet stack itself does not implement all BACnet algorithms 
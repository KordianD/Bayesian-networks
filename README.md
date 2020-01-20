# Bayesian-networks

The program tries to estimate how likely you are to get into a fight on the way home.

## Setup
- [Get Genie, pysmile wrapper and license from here](https://download.bayesfusion.com/files.html?category=Academia)
- Put `pysmile.pyd` and `pysmile_license.py` into `src`
- Run `python3 ./mma.py`
- To modify network edit `mma.xdsl` with Genie or manually

### Node description:
- TimeOfDay - how late are you going home?
- FootballGame - is there a football game currently going on?
- Bar - are you coming home from a bar, pub or club?
- Sobriety - are you sober or drunk?
- Company - are you alone or with friends?
- Transportation - what means of transportation will you use?
- Neighbourhood - does your way home go through a dangerous or safe neighbourhood?
- RiskOfMMA - the chance to get into a fight

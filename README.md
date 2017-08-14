# The Contraculator

The Contraculator is a Python script for calculating the duration and frequencies of contractions while a mother-to-be is in labor. It determines when you have transitioned from 'early labor' to 'active labor'.

## Screenshots

![The contractions](/images/contraction-shot1.png)

## Getting Started

### Prerequisites

This script was designed using Python 2.7. If using Python 3.0 or above, adjustments will be necessary.

### Installation
```
git clone https://github.com/alexhmontgomery/the-contractulator
cd the-contractulator
python Contraculator.py
```

## Instructions

### Editing the test parameters

The script is set up to determine if 'active labor' has been entered by whether or not the 5-1-1 Rule has occurred. This is a standard rule used by many hospitals to help expecting parents determine if they are in 'active labor'. The rule states that contractions must be at least 1 minute in duration, occurring at a frequency of 5 minutes (or less) for at least one hour.

If you wish to adjust these default parameters, you can change the variable test settings in the script. The screenshot below shows the test parameters on lines 15-18 that would need to be changed if you wish to adjust the settings for 'active labor'.

![test parameters](/images/testparameters.png)

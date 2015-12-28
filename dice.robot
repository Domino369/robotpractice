*** Settings ***
Documentation	Dice tests
...
...				gherkin syntax styled dice tests
Library			dice_library.DiceLibrary

*** Test Cases ***
d6
	When user rolls a "6" sided die
	The result is within 0 and "6"

*** Keywords ****
User rolls a "${die_size}" sided die
	Roll	${die_size}

The result is within 0 and "${die_size}"
	Result should be	${die_size}

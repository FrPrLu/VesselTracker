# VesselTracker

## The Goal is to relate the __AIS__ messages received from the *satellite* to the specific __IMO__ of the *sending ship*.

### How it works:

1. Crontab file to run the script periodically
	1. Reads the *.CSV* file to get MMSI and IMO conversion table and creates a dict.
	2. Reads the all the *.AIS* files sent from the satellite.
	3. For each line in the file:
		1. splits the string
		2. decodes the AIS message
			1. if the MMSI in the decoded messages matches with the conversion table, writes a line appending the original line with the respective IMO number.
			2. else appends IMO:0 to the original line.
	4. Moves all the processed *.AIS* files to the old folder.
	5. Saves one file with all the messages with the respective IMO number appended.


Teste1
test 2
	



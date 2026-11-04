# voter_district_streets
create voter district street lists from Pennsylvania voter export file.

The voting district I (used to) run is in a building shared by four voting districts causing
lots of confusion with people trying to figure out which voting district they need to go to.
To help people figure this out I wrote this script which parses the Allegheny county "full voter
export" to make a list of which streets are assigned to which voting district(s).  This script
has not been made to work easily in any manner (file locations/names/district numbers are 
hardcoded into the file for instance) but the code is simple and should be easy for anyone 
to modify and use for similar purposes anywhere in PA that they can get the voter export for their
county (costs $20 on PA's voter services web page).

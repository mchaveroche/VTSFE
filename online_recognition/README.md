# Online activity recognition

## Xsens module: sensor_processing.py

### Yarp port:

input: 
* /processing/xsens/"NameSignal":i

output:
* /processing/xsens/"NameSignal":o

## Eglove module: eglove_processing.py

### Yarp port:

input: 

output:

## Activity recognition module

### Yarp port:

input: 
* /activity_recognition/"NameSignal":i

output:
* /activity_recognition/state:o
* /activity_recognition/probabilities:o
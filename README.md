# Green Mountain Grill for Home Assistant

**WARNING** This compoment is still in development 


## Installation

Install via HACS 

Add below to configuration.yaml in home assistant

climate:
  - platform: gmg

## Requirements 

UDP port 8080 open between home assistant & GMG
Auto discovery will discover multiple GMG devices if on same network as home assistant 

## TODO 

Sensors for food probes (temperature monitor.. set temperature etc.)
Test cold smoke mode 
Ramp cooks

## Test

Power on - successful
Set temp - successful
Power off - successful 
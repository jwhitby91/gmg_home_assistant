# Green Mountain Grill for Home Assistant

**WARNING** This compoment is still in development 


## Installation

Install via HACS 

Add below to configuration.yaml in home assistant

[code]
climate:
  - platform: gmg
[/code]

## Requirements 

UDP port 8080 open between home assistant & GMG
Auto discovery will discover multiple GMG devices if on same network as home assistant 

## TODO 

Sensors for 
    [*] food probes (temperature monitor.. set temperature etc.) - in development.. Set them up as climate as you can set temp for them 
    [*] Warning states..
    [*] Fire States
Test cold smoke mode 
Ramp cooks

## Test

Power on - successful
Power off - successful 
Set temp - successful
Probes - successful 

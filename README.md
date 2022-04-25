# Green Mountain Grill for Home Assistant

**WARNING** This compoment is still in development 

## Installation

Install via HACS 

Add below to configuration.yaml in home assistant

<code>
climate:
  - platform: gmg
</code>

## Requirements 

UDP port 8080 open between home assistant & GMG
Auto discovery will discover multiple GMG devices if on same network as home assistant 

## TODO 

<ul>
    <li>Sensors for
        <ul>
            <li>food probes (temperature monitor.. set temperature etc.) - in development.. Set them up as climate as you can set temp for them </li>
            <li>Warning states..</li>
            <li>Fire States</li>
        </ul>
    </li>
    <li>Test cold smoke mode</li>
    <li>Ramp cooks</li>
</ul>

## Test

<ul>
    <li>Power on - successful</li>
    <li>Power off - successful</li>
    <li>Set temp - successful</li>
    </li>Probes - successful </li>
</ul>

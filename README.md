# Green Mountain Grill for Home Assistant

## **WARNING** This compoment is still in development. Use with caution!  

## Installation

Install via HACS (click 3 dots in top right > Custom Repositories > add this github as integration > press ok.. Then click Exlore & download repo bottom right then select Green Mountain Grill)

Add below to configuration.yaml in home assistant

```yaml
    climate:
        - platform: gmg
```

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
    <li>Change Home assistant to use config flow for easier set up</li>
</ul>

## Test list

<ul>
    <li>Power on - successful</li>
    <li>Power off - successful</li>
    <li>Set temp - successful </br><b>Notes:</b> as recommended in GMG manual you shouldn't change temp until it reaches 150 F so I put in check to only change temp once that has been reached</li> 
    <li>Probes - successful</li>
</ul>

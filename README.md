# Green Mountain Grill for Home Assistant

## **WARNING** This compoment is still in development. Use with caution!  

## Installation

Install via HACS 

<ul>
    <li>click 3 dots in top right</li>
    <li>Custom Repositories</li>
    <li>add this github URI as integration</li>
    <li>click add</li>
    </br>
    <li>click Exlore & download repo bottom right</li>
    <li>Search & select Green Mountain Grill</li>
    <li>Click install</li>
</ul>

Add below to configuration.yaml in home assistant

```yaml
    climate:
        - platform: gmg
```

## Requirements 

<ul>
    <li>UDP port 8080 open between home assistant & GMG</li>
    <li>Auto discovery will discover multiple GMG devices if on same network as home assistant</li>
</ul>

## TODO 

<ul>
    <li>Sensors for
        <ul>
            <li>food probes (temperature monitor.. set temperature etc.) - in development.. Set them up as climate as you can set temp for them </li>
            <li>
                <ul>
                    <li>Need to better detect when probes are unplugged</li>
                </ul>
            </li>
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

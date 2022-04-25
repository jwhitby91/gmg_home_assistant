"""Green Mountain Grill"""

from .gmg import grills, grill
#from gmg import grills,grill
import logging
from typing import List, Optional
from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVAC_MODE_OFF, HVAC_MODE_HEAT, SUPPORT_TARGET_TEMPERATURE, HVAC_MODE_HEAT, HVAC_MODE_OFF, HVAC_MODE_FAN_ONLY)
from homeassistant.const import (
    ATTR_TEMPERATURE,
    TEMP_FAHRENHEIT)

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    entities = []
    _LOGGER.debug("Looking for grills")

    # look for grills.. timeout = 2
    all_grills = grills(2)

    for my_grill in all_grills: 
        _LOGGER.debug(f"Found grill IP: {my_grill._ip} Serial: {my_grill._serial_number}")
        entities.append(GmgGrill(my_grill))

    async_add_entities(entities)

    return

class GmgGrill(ClimateEntity):
    """Representation of a Green Mountain Grill smoker"""

    def __init__(self, grill) -> None:
        """Initialize the Grill."""
        self._grill = grill
        self._unique_id = "{}".format(self._grill._serial_number)
        self.update()


    def set_temperature(self, **kwargs):
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)

        if temperature is None:
            return
        if temperature == self._state['grill_set_temp']:
            return
        
        # Add in section if grill is not on to error... 
        if self._state['on'] == 0:
            _LOGGER.error("Grill is not on, cannot set temperature")
            return

        # Add another section if grill not 150 F to not raise temp 
        if self._state['temp'] < 145:
            # GMG manual says need to wait until 150 F at least before changing temp 
            _LOGGER.error("Grill is not 150 F, cannot set temperature")
            return

        try:
            _LOGGER.debug(f"Setting temperature to {temperature}")
            self._grill.set_temp(int(temperature))
        except Exception as ex:
            _LOGGER.error("Error setting temperature: %s", temperature)

    def set_hvac_mode(self, hvac_mode: str) -> None:
        """Set the operation mode"""
        if hvac_mode == HVAC_MODE_HEAT:
            self._grill.power_on()
        elif hvac_mode == HVAC_MODE_OFF:
            self._grill.power_off()
        elif hvac_mode == HVAC_MODE_FAN_ONLY:
            self._grill.power_on_cool()
        else:
            _LOGGER.error("Unsupported hvac mode: %s", hvac_mode)

        self.update()

    def turn_off(self):
        """Turn device off."""
        return self._grill.power_off()
    
    @property
    def supported_features(self):
        """Return the list of supported features."""
        return (SUPPORT_TARGET_TEMPERATURE)
    
    @property
    def icon(self):
        return "mdi:grill"

    @property
    def hvac_modes(self) -> List[str]:
        """Return the supported operations."""
        return [HVAC_MODE_HEAT, HVAC_MODE_FAN_ONLY, HVAC_MODE_OFF]

    @property
    def hvac_mode(self):
        """Return current HVAC operation."""
        if self._state['on'] == 1:
            return HVAC_MODE_HEAT
        elif self._state['on'] == 2:
            return HVAC_MODE_FAN_ONLY

        return HVAC_MODE_OFF

    @property
    def name(self)  -> None:
        """Return unique ID of grill which is GMGSERIAL_NUMBER"""
        return self._unique_id

    # Climate Properties
    @property
    def temperature_unit(self) -> None:
        """Return the unit of measurement for the grill"""
        # intial tests look like raw value always in F not C even when set in the app. 
        return TEMP_FAHRENHEIT

    @property
    def current_temperature(self) -> None:
        """Return current temp of the grill"""
        return self._state.get('temp')

    @property
    def target_temperature_step(self) -> None:
        """Return the supported step of target temp"""
        
        return 1
        
    @property
    def target_temperature(self) -> None:
        """Return what the temp is set to go to"""
        return self._state.get('grill_set_temp')

    @property
    def max_temp(self) -> None:
        """Return the maximum temperature."""

        return self._grill.MAX_TEMP_F

    @property
    def min_temp(self) -> None:
        """Return the minimum temperature."""

        return self._grill.MIN_TEMP_F

    @property
    def unique_id(self) -> None:
        """Return a unique ID."""
        return self._unique_id

    def update(self) -> None:
        """Get latest data."""
        self._state = self._grill.status()

        print (self._state)

def testing(): 
    # testing PC has multiple adapters so binding to specific adapter IP required when testing. 
    all_grills = grills(timeout=2, ip_bind_address='10.100.111.141')

    for my_grill in all_grills:
        grill.status(my_grill)

        #grill.power_on(my_grill)

        # try setting temp... must send in F not C 
        #grill.set_temp(my_grill, 160)

        grill.status(my_grill)

        grill.power_off(my_grill)

        grill.status(my_grill)

    hass_grill = GmgGrill(my_grill)

    print(hass_grill.current_temperature)

    print(hass_grill)


# testing()



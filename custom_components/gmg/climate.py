"""Green Mountain Grill"""

from .gmg import gmg
import logging
from homeassistant.components.climate import ClimateEntity
from homeassistant.const import (
    ATTR_TEMPERATURE,
    TEMP_FAHRENHEIT,
)

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities,
                               discovery_info=None):
    entities = []
    _LOGGER.debug("Looking for grills")

    # look for grills.. timeout = 2
    grills = gmg.grills(2)

    for grill in grills: 
        _LOGGER.debug(f"Found grill IP: {grill._ip} Serial: {grill._serial_number}")
        entities.append(GmgGrill(grill))

    async_add_entities(entities)

    return

class GmgGrill(ClimateEntity):
    """Representation of a Green Mountain Grill smoker"""

    def __init__(self, grill):
        """Initialize the Grill."""
        self._grill = grill
        print(self._grill)
        self._unique_id = "gmg_{}".format(self._grill._serial_number)
        self.update()

    @property
    def name(self):
        """Return unique ID of grill which is gmg_SERIAL_NUMBER"""
        return self._unique_id

    # Climate Properties
    @property
    def temperature_unit(self):
        """Return the unit of measurement for the grill"""
        # intial tests look like raw value always in F not C even when set in the app. 
        return TEMP_FAHRENHEIT

    @property
    def current_temperature(self):
        """Return current temp of the grill"""
        return self._state.get('temp')

    @property
    def target_temperature_step(self):
        """Return the supported step of target temp"""
        return 5
    
    @property
    def target_temperature(self) -> float | None:
        """Return what the temp is set to go to"""
        return self._state.get('grill_set_temp')

    @property
    def max_temp(self):
        """Return the maximum temperature."""
        return self._grill.MAX_TEMP
    
    @property
    def min_temp(self):
        """Return the minimum temperature."""
        return self._grill.MIN_TEMP

    def update(self):
        """Get latest data."""
        self._state = self._grill.status()

        print (self._state)

def testing(): 
    # testing PC has multiple adapters so binding to specific adapter IP required when testing. 
    all_grills = gmg.grills(timeout=2, ip_bind_address='10.100.111.141')

    for my_grill in all_grills:
        gmg.grill.status(my_grill)

    hass_grill = GmgGrill(my_grill)

    print(hass_grill.current_temperature)


#testing()



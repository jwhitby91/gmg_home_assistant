


import gmg
from homeassistant.components.climate import ClimateEntity
from homeassistant.const import (
    ATTR_TEMPERATURE,
    TEMP_FAHRENHEIT,
)

class GmgGrill(ClimateEntity):
    """Representation of a Escea Fire."""

    def __init__(self, grill):
        """Initialize the fire."""
        self._grill = grill
        self._unique_id = "gmg_{}".format(grill.serial_number)

    @property
    def name(self):
        return self._unique_id

    # Climate Properties
    @property
    def temperature_unit(self):
        # intial tests look like raw value always in F not C even when set in the app. 
        return TEMP_FAHRENHEIT

    @property
    def current_temperature(self):
        return self._grill.state.get('temp')

    @property
    def target_temperature(self) -> float | None:
        return self._grill.state.get('grill_set_temp')

grill_ip = '10.100.111.152'

my_grill = gmg.grill(grill_ip)

gmg.grill.serial(my_grill)
gmg.grill.status(my_grill)

#my_grill = gmg.grill.discover_grill(ip = '10.100.111.152')

# my_grill = gmg.discover_grill(ip = '10.100.111.152')

print(my_grill)

hass_grill = GmgGrill(my_grill)

GmgGrill.current_temperature()


freeze("$(PORT_DIR)/modules")
# require("aioespnow")
require("bundle-networking")
require("dht")
require("ds18x20")
require("neopixel")
require("onewire")

# wsh/prometheus addons:
include('$(MPY_DIR)/../prometheus.micropython.manifest.py')

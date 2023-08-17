from pyper.viper_classes import PolhemusViper

viper = PolhemusViper()
viper.connect()

viper.get_units()

# The current position units are: cm
# The current orientation units are: euler_degrees

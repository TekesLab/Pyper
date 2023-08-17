from pyper.viper_classes import PolhemusViper

viper = PolhemusViper()
viper.connect()

viper.get_units()

# The current position units are: cm
# The current orientation units are: euler_degrees

viper.get_single_pno(pno_mode="standard")

# or for PNO frames that also contain acceleration info:
#viper.get_single_pno(pno_mode="acceleration")

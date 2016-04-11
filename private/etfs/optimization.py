from matplotlib.pyplot import show, title
from private.etfs.system import create_estimate_system

system = create_estimate_system()

system.combForecast.get_forecast_weights("GLD").plot()
title("GLD")
show()

system.portfolio.get_instrument_weights().plot()
show()

system.portfolio.get_instrument_diversification_multiplier().plot()
show()

system.accounts.portfolio().cumsum().plot()
show()

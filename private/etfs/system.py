from sysdata.csvdata import csvFuturesData
from sysdata.configdata import Config

from systems.forecasting import Rules
from systems.basesystem import System
from systems.forecast_combine import ForecastCombineFixed
from systems.forecast_scale_cap import ForecastScaleCap
from systems.positionsizing import PositionSizing
from systems.portfolio import PortfoliosFixed
from systems.account import Account


def create_system(log_level="on"):
    config = Config("private.etfs.config.yaml")
    data = csvFuturesData("private.data")

    sys = System([Account(), PortfoliosFixed(), PositionSizing(), ForecastCombineFixed(), ForecastScaleCap(), Rules()
                        ], data, config)

    sys.set_logging_level(log_level)

    return sys


def forecast_scalar_estimate():
    sys = create_system(log_level="off")
    instrument_list = sys.get_instrument_list()
    print(instrument_list)

    sys.config.forecast_scalar_estimate['pool_instruments'] = True

    results = []
    for instrument_code in instrument_list:
        results.append(
            round(float(sys.forecastScaleCap.get_forecast_scalar(instrument_code, "ewmac64_256").tail(1).values), 2))
    print(results)


if __name__ == '__main__':
    import private
    forecast_scalar_estimate()





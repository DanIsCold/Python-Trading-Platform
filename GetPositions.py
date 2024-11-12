from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest

trading_client = TradingClient('PK14CV687K30ALR8RMUG', 'Fh19ACB7Kb98LwPB3Wsiu7koQCaaEA08Rt5PiXsP', paper=True)

class getPositions():
    def __init__(self) -> None:
        pass

    def get_stock_position(self,symbol: str):
        return trading_client.get_open_position(symbol)
    
    def get_all_positions(self):
        portfolio = trading_client.get_all_positions()
        #just prints the positions - will be reworked to pass front end the data 
        for position in portfolio:
            print(f"{position.qty} shares of {position.symbol}")

    def portfolio_gain_loss(self):
        account = trading_client.get_account()
        balance_change = float(account.equity) - float(account.last_equity)
        print(f'Today\'s portfolio balance change: ${balance_change}')

joe = getPositions().get_all_positions()


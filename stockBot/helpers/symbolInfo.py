from jsonschema import validate

class SymbolInfo:
    symbolSchema = {
        "title": "schema",
        "type": "object",
        "required": [
            "symbol",
            "action"
        ],
        "properties": {
            "symbol":{
                "type": "string"
            },
            "action": {
                "type": "string",
                "enum": ["BUY", "SELL", "NONE"]
            },
            "totalQuantity": {
                "type": "integer"
            }
        }
    }

    def __init__(self):
        self.tickerInfo = {}


    def addSymbol(self, schema):
        validate(schema, SymbolInfo.symbolSchema)
        
        # self.tickerInfo[object.keys()] = {object.value()}

payload = {
        "symbol": "AAPL",
        "secType": "STK",
        "exchange": "SMART",
        "currency": "USD",
        "action": "BUY",
        "totalQuantity" : 0,
        "orderType": "MTK",
        "lmtPrice" : 1.10
    }


validator = SymbolInfo()
validator.addSymbol(payload)

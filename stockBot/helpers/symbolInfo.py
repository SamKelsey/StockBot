from jsonschema import validate

class SymbolInfo:

    # TODO - Required fields and schema structure needs confirmed.
    schema = {
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

    def __init__(self, values):
        validate(values, SymbolInfo.schema)
        self.__tickerInfo = values

    def getValue(self, key):
        return self.__tickerInfo[key]

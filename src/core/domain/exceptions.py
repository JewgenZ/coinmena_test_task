from typing import Optional


class AlphaVantageBadRequestError(Exception):
    def __init__(self, data: Optional[dict] = None, *args, **kwargs):
        self.data = data if data else {"error": "Bad request. Please check the payload"}
        super().__init__(*args, **kwargs)

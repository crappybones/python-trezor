# Automatically generated by pb2py
from .. import protobuf as p


class TxSize(p.MessageType):
    MESSAGE_WIRE_TYPE = 44
    FIELDS = {
        1: ('tx_size', p.UVarintType, 0),
    }

    def __init__(
        self,
        tx_size: int = None
    ) -> None:
        self.tx_size = tx_size

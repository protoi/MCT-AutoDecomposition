class Gate:
    target: int
    control: int
    target_state: int
    control_state: int
    inc_or_dec: str
    tq: str

    def __init__(self, target: int, control: int, target_state: int, control_state: int, inc_or_dec: str,
                 tq: str):
        self.target = target
        self.control = control
        self.target_state = target_state
        self.control_state = control_state
        self.inc_or_dec = inc_or_dec
        self.tq = tq

    def __str__(self) -> str:
        s = f"{self.tq} | target node: {self.target} state: {self.target_state} | control node: {self.control_state} state: {self.control_state} -> {self.inc_or_dec}"

        return s

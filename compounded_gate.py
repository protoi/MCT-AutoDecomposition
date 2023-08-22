from dataclasses import dataclass

from gate import Gate, Target, Control


@dataclass
class DecomposedGate:
    first: Gate
    second: Gate
    third: Gate


@dataclass
class OptimizedDecomposedGate:
    first: Gate
    second: Gate


class CompoundedGate:
    target: Target
    control_left: Control
    control_right: Control
    decom_gates: DecomposedGate
    opti_gates: OptimizedDecomposedGate

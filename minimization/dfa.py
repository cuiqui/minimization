from collections.abc import Hashable
from dataclasses import dataclass


@dataclass
class DFA:
    states: set[Hashable]
    alphabet: set[Hashable]
    transition: dict[tuple[Hashable, Hashable], Hashable]
    start_state: Hashable
    accept_states: set[Hashable]

    def delta(self, state: Hashable, symbol: Hashable) -> Hashable | None:
        return self.transition.get((state, symbol))

    def __or__(self, other):
        return DFA(
            states=self.states | other.states,
            alphabet=self.alphabet | other.alphabet,
            transition={**self.transition, **other.transition},
            start_state=self.start_state,  # we don't care
            accept_states=self.accept_states | other.accept_states
        )

class TestCase:
    def __init__(
        self,
        id: int,
        problem_id: int,
        input: str,
        expected_output: str,
        is_hidden: bool = True,
    ) -> None:
        self.id: int = id
        self.problem_id: int = problem_id
        self.input: str = input
        self.expected_output: str = expected_output
        self.is_hidden: bool = is_hidden

    @property
    def id(self) -> int:
        return self._id

    @property
    def problem_id(self) -> int:
        return self._problem_id

    @property
    def input(self) -> str:
        return self._input

    @property
    def expected_output(self) -> str:
        return self._expected_output

    @property
    def is_hidden(self) -> bool:
        return self._is_hidden

    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @problem_id.setter
    def problem_id(self, problem_id: int) -> None:
        self._problem_id = problem_id

    @input.setter
    def input(self, input: str) -> None:
        self._input = input

    @expected_output.setter
    def expected_output(self, expected_output: str) -> None:
        self._expected_output = expected_output

    @is_hidden.setter
    def is_hidden(self, is_hidden: bool) -> None:
        self._is_hidden = is_hidden

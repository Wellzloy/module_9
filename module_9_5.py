class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        
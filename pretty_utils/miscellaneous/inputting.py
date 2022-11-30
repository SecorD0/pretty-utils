import signal


def interrupted():
    raise InterruptedError


def timeout_input(prompt: str, timeout: int, default_value: str = '') -> str:
    signal.signal(signal.SIGALRM, interrupted)
    signal.alarm(timeout)
    action = default_value
    try:
        action = input(prompt)

    except InterruptedError:
        pass

    finally:
        print()
        signal.alarm(0)
        return action

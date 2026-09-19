import subprocess
import sys

# These are integration tests, not unit tests: each one spawns calculator_cli.py
# as a real subprocess (a separate Python process, real argv, real stdout/stderr/
# exit code) rather than importing and calling a function directly. That's what
# verifies argument parsing, the calculator module import, and process-level
# output are all correctly wired together — a unit test on calculator.py alone
# can't catch a bug in that wiring (e.g. a wrong OPERATIONS key or format string).
CLI_PATH = "calculator_cli.py"


def run_cli(*args):
    return subprocess.run(
        [sys.executable, CLI_PATH, *args],
        capture_output=True,
        text=True,
    )


def test_cli_add_success():
    result = run_cli("add", "2", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "5.0"


def test_cli_modulo_success():
    result = run_cli("modulo", "10", "3")
    assert result.returncode == 0
    assert result.stdout.strip() == "1.0"


def test_cli_divide_by_zero_reports_domain_error():
    result = run_cli("divide", "10", "0")
    assert result.returncode == 1
    assert "Cannot divide by zero" in result.stderr
    assert result.stdout == ""


def test_cli_invalid_operation_is_rejected_by_argparse():
    result = run_cli("foo", "1", "2")
    assert result.returncode == 2
    assert "invalid choice: 'foo'" in result.stderr

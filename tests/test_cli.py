import pytest

from logreport.cli import main as cli_main


def test_cli_success(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "main.py",
            "--files",
            "tests/data/example1.log",
            "tests/data/example2.log",
            "--report",
            "average",
            "--date",
            "2025-06-22",
        ],
    )
    exit_code = cli_main()
    assert exit_code == 0


def test_cli_invalid_report(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "main.py",
            "--files",
            "tests/data/example1.log",
            "tests/data/example2.log",
            "--report",
            "invalid",
        ],
    )

    with pytest.raises(SystemExit) as exc:
        cli_main()
    assert exc.value.code == 2


def test_cli_missing_file(monkeypatch):
    monkeypatch.setattr("sys.argv", ["main.py", "--report", "average"])

    with pytest.raises(SystemExit) as exc:
        cli_main()
    assert exc.value.code == 2


def test_output(monkeypatch, capsys):
    monkeypatch.setattr(
        "sys.argv",
        [
            "main.py",
            "--files",
            "tests/data/example1.log",
            "tests/data/example2.log",
            "--report",
            "average",
        ],
    )

    cli_main()
    out, err = capsys.readouterr()
    assert "handler" in out

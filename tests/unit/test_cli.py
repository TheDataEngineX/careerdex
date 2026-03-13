"""Tests for the CareerDEX CLI."""

from __future__ import annotations

from click.testing import CliRunner

from careerdex.cli import main


class TestCLI:
    """Verify all CLI commands are registered and invocable."""

    def setup_method(self) -> None:
        self.runner = CliRunner()

    def test_main_group_exists(self) -> None:
        result = self.runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "CareerDEX" in result.output

    def test_version_flag(self) -> None:
        result = self.runner.invoke(main, ["--version"])
        assert result.exit_code == 0
        assert "0.5.0" in result.output

    def test_serve_command_exists(self) -> None:
        result = self.runner.invoke(main, ["serve", "--help"])
        assert result.exit_code == 0
        assert "--port" in result.output

    def test_ingest_command_exists(self) -> None:
        result = self.runner.invoke(main, ["ingest", "--help"])
        assert result.exit_code == 0
        assert "--source" in result.output

    def test_match_command_exists(self) -> None:
        result = self.runner.invoke(main, ["match", "--help"])
        assert result.exit_code == 0
        assert "RESUME_PATH" in result.output

    def test_predict_salary_command_exists(self) -> None:
        result = self.runner.invoke(main, ["predict-salary", "--help"])
        assert result.exit_code == 0
        assert "RESUME_PATH" in result.output

    def test_career_path_command_exists(self) -> None:
        result = self.runner.invoke(main, ["career-path", "--help"])
        assert result.exit_code == 0
        assert "ROLE" in result.output

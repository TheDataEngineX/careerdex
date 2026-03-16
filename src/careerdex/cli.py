"""CareerDEX CLI — command-line interface for the career intelligence platform."""

from __future__ import annotations

import click
from rich.console import Console

console = Console()


@click.group()
@click.version_option(package_name="careerdex")
def main() -> None:
    """CareerDEX — AI career intelligence platform."""


@main.command()
@click.option("--port", default=8003, help="Port to serve on.")
@click.option("--host", default="0.0.0.0", help="Bind address.")
@click.option("--reload", is_flag=True, help="Enable auto-reload for development.")
def serve(port: int, host: str, reload: bool) -> None:
    """Start the CareerDEX API server."""
    import uvicorn

    console.print(f"[bold green]Starting CareerDEX API on {host}:{port}[/bold green]")
    uvicorn.run("careerdex.api.main:app", host=host, port=port, reload=reload)


@main.command()
@click.option("--source", type=click.Choice(["linkedin", "indeed", "glassdoor"]), required=True)
@click.option("--limit", default=100, help="Maximum jobs to ingest.")
def ingest(source: str, limit: int) -> None:
    """Ingest job data from external sources."""
    raise NotImplementedError("Job ingestion pipeline not yet connected — implement JobIngestionPipeline")


@main.command()
@click.argument("resume_path", type=click.Path(exists=True))
@click.option("--top-k", default=10, help="Number of top matches to return.")
def match(resume_path: str, top_k: int) -> None:
    """Match a resume against available jobs."""
    raise NotImplementedError("ResumeJobMatcher not yet implemented")


@main.command()
@click.argument("resume_path", type=click.Path(exists=True))
def predict_salary(resume_path: str) -> None:
    """Predict salary range from a resume."""
    raise NotImplementedError("SalaryPredictor not yet implemented")


@main.command()
@click.argument("role")
def career_path(role: str) -> None:
    """Show career path recommendations for a role."""
    raise NotImplementedError("CareerPathRecommender not yet implemented")


if __name__ == "__main__":
    main()

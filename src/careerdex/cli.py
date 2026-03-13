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
    # TODO: Wire up to phase2_job_ingestion pipeline
    console.print(f"[yellow]Ingesting up to {limit} jobs from {source}...[/yellow]")
    console.print("[dim]Not yet implemented — connect to JobIngestionPipeline[/dim]")


@main.command()
@click.argument("resume_path", type=click.Path(exists=True))
@click.option("--top-k", default=10, help="Number of top matches to return.")
def match(resume_path: str, top_k: int) -> None:
    """Match a resume against available jobs."""
    # TODO: Wire up to phase4_ml_models.ResumeJobMatcher
    console.print(f"[yellow]Matching {resume_path} (top {top_k})...[/yellow]")
    console.print("[dim]Not yet implemented — connect to ResumeJobMatcher[/dim]")


@main.command()
@click.argument("resume_path", type=click.Path(exists=True))
def predict_salary(resume_path: str) -> None:
    """Predict salary range from a resume."""
    # TODO: Wire up to phase4_ml_models.SalaryPredictor
    console.print(f"[yellow]Predicting salary for {resume_path}...[/yellow]")
    console.print("[dim]Not yet implemented — connect to SalaryPredictor[/dim]")


@main.command()
@click.argument("role")
def career_path(role: str) -> None:
    """Show career path recommendations for a role."""
    # TODO: Wire up to phase4_ml_models.CareerPathRecommender
    console.print(f"[yellow]Career path for: {role}[/yellow]")
    console.print("[dim]Not yet implemented — connect to CareerPathRecommender[/dim]")


if __name__ == "__main__":
    main()

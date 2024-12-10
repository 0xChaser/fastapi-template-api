from typing import Annotated, Union

import typer
from rich import print
from rich.padding import Padding
from rich.panel import Panel

from project_template.exceptions import ProjectTemplateCLIException
from project_template.settings import LogLevel, settings

try:
    import uvicorn
except ImportError:
    uvicorn = None

# helped from fastapi_cli -> https://github.com/fastapi/fastapi-cli/blob/e1cc513854e9fc9082962f3d79cb84d1429ffb4f/src/fastapi_cli/cli.py#L17
app = typer.Typer(rich_markup_mode="rich")


@app.command()
def run(
    host: Annotated[
        str,
        typer.Option(
            help="The host to serve on. For local development in localhost use [blue]127.0.0.1[/blue]. To enable public access, e.g. in a container, use all the IP addresses available with [blue]0.0.0.0[/blue]."
        ),
    ] = settings.host,
    port: Annotated[
        int,
        typer.Option(
            help="The port to serve on. You would normally have a termination proxy on top (another program) handling HTTPS on port [blue]443[/blue] and HTTP on port [blue]80[/blue], transferring the communication to your app."
        ),
    ] = settings.port,
    workers: Annotated[
        Union[int, None],  # noqa: UP007  # not supported by typer
        typer.Option(help="Number of workers processes to deploy with Uvicorn UWSGI server."),
    ] = settings.workers,
    proxy_headers: Annotated[
        bool,
        typer.Option(
            help="Enable/Disable X-Forwarded-Proto, X-Forwarded-For, X-Forwarded-Port to populate remote address info."
        ),
    ] = settings.proxy_headers,
    log_level: Annotated[
        LogLevel,
        typer.Option(help="Set the log level in UWSGI server and in the Project Template globally."),
    ] = settings.log_level,
):
    serving_str = f"[dim]Serving at:[/dim] [link]http://{host}:{port}[/link]\n\n[dim]API docs:[/dim] [link]http://{host}:{port}/docs[/link]"
    panel = Panel(
        f"{serving_str}\n\n[dim]Running in production mode, for development use:[/dim]\n\n[b]project_template dev[/b]",
        title="Project Template - Production mode",
        expand=False,
        padding=(1, 2),
        style="green",
    )
    _run(panel=panel, host=host, port=port, workers=workers, proxy_headers=proxy_headers, log_level=log_level)


@app.command()
def dev(
    host: Annotated[
        str,
        typer.Option(
            help="The host to serve on. For local development in localhost use [blue]127.0.0.1[/blue]. To enable public access, e.g. in a container, use all the IP addresses available with [blue]0.0.0.0[/blue]."
        ),
    ] = settings.host,
    port: Annotated[
        int,
        typer.Option(
            help="The port to serve on. You would normally have a termination proxy on top (another program) handling HTTPS on port [blue]443[/blue] and HTTP on port [blue]80[/blue], transferring the communication to your app."
        ),
    ] = settings.port,
    workers: Annotated[
        Union[int, None],  # noqa: UP007  # not supported by typer
        typer.Option(help="Number of workers processes to deploy with Uvicorn UWSGI server."),
    ] = settings.workers,
    proxy_headers: Annotated[
        bool,
        typer.Option(
            help="Enable/Disable X-Forwarded-Proto, X-Forwarded-For, X-Forwarded-Port to populate remote address info."
        ),
    ] = settings.proxy_headers,
    log_level: Annotated[
        LogLevel,
        typer.Option(help="Set the log level in UWSGI server and in the Project Template globally."),
    ] = settings.log_level,
) -> None:
    serving_str = f"[dim]Serving at:[/dim] [link]http://{host}:{port}[/link]\n\n[dim]API docs:[/dim] [link]http://{host}:{port}/docs[/link]"

    panel = Panel(
        f"{serving_str}\n\n[dim]Running in development mode, for production use:[/dim]\n\n[b]project_template run[/b]",
        title="Project Template - Development mode",
        expand=False,
        padding=(1, 2),
        style="black on yellow",
    )

    _run(
        panel=panel,
        host=host,
        port=port,
        workers=workers,
        proxy_headers=proxy_headers,
        log_level=log_level,
        dev_mode=True,
    )


def _run(
    panel: Panel,
    host: str = settings.host,
    port: int = settings.port,
    workers: int | None = settings.workers,
    proxy_headers: bool = settings.proxy_headers,
    log_level: str = settings.log_level,
    dev_mode: bool = False,
) -> None:
    print(Padding(panel, 1))
    if not uvicorn:
        raise ProjectTemplateCLIException("Could not import Uvicorn, try running 'pip install uvicorn'")
    uvicorn.run(
        app=f"{__package__}.main:app",  # required by uvicorn to enable reload and workers
        host=host,
        port=port,
        reload=dev_mode,
        workers=workers,
        proxy_headers=proxy_headers,
        log_level=log_level,
    )


def main() -> None:
    app()
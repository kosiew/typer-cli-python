from typing import Annotated

import typer

app = typer.Typer()


@app.command(name="mula")
def start2(
    name: Annotated[str, typer.Argument()] = "default name",
    number: Annotated[int, typer.Argument()] = 12,
    db_path2: Annotated[
        str,
        typer.Option(),
    ] = "default_db_path",
) -> None:
    """Initialize the to-do database."""
    typer.secho(f"starter2 {name=} {number=} db_path: {db_path2}")
    if name == "error":
        typer.secho(
            f"Error",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)


@app.command()
def start(
    # argument
    argument: str = typer.Argument(...),
    db_path: str = typer.Option(
        "db_path_string",
        "--db-path",
        "-db",
    ),
) -> None:
    """Initialize the to-do database."""
    typer.secho(f"init {argument=} db_path: {db_path}")
    if argument == "error":
        typer.secho(
            f"Error",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)


if __name__ == "__main__":
    print("Running typer app")
    app()

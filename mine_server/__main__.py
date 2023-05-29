from asyncio import sleep

import click

from mine import run

from . import serve


@click.command()
@click.option("--host", type=str, default="127.0.0.1")
@click.option("--port", type=int, required=True)
@run
async def main(
    host: str,
    port: int,
) -> None:
    with serve(host=host, port=port):
        while True:
            await sleep(1.0)


if __name__ == "__main__":
    main()

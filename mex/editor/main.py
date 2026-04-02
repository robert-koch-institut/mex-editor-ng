from contextlib import asynccontextmanager
from pathlib import Path
from typing import TYPE_CHECKING, Literal

from starlette.requests import Scope
from starlette.responses import Response

if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import AsyncGenerator

import click
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

from mex.common.logging import logger
from mex.editor.api.data import router as data_router
from mex.editor.api.system import router as system_router
from mex.editor.frontend import npm_watch


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope: Scope) -> Response:
        try:
            return await super().get_response(path, scope)
        except (HTTPException, StarletteHTTPException) as ex:
            if ex.status_code == 404:
                return await super().get_response("index.html", scope)
            raise ex


@asynccontextmanager
async def dev_lifespan(_: FastAPI) -> AsyncGenerator[None]:  # pragma: no cover
    """Run npm watch during dev mode."""
    logger.info("Starting npm run watch")
    with npm_watch():
        yield
    logger.info("Stopped npm run watch")


def create_fastapi(
    mode: Literal["dev"] | None = None,
    startup: Literal["api", "frontend", "both"] = "both",
    static_dir: Path | None = None,
    base_path: str = "",
) -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="mex-editor",
        lifespan=dev_lifespan if mode == "dev" else None,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    if startup in ["api", "both"]:
        app.include_router(data_router, prefix=f"{base_path}/api/v0")
        app.include_router(system_router, prefix=f"{base_path}/api/v0")
    if startup in ["frontend", "both"]:
        # TODO use CLIENT_DIST for local
        directory = static_dir
        app.mount(
            f"{base_path}/",
            SPAStaticFiles(directory=directory, html=True),
            name="spa-static-files",
        )
    return app


@click.command()
@click.option(
    "--startup",
    type=click.Choice(["api", "frontend", "both"]),
    default="both",
    help="Define what should start 'api', 'frontend' or 'both'.",
)
@click.option(
    "--dev",
    "-d",
    is_flag=True,
    default=False,
    help="Define if started in dev mode to watch angular src and rebuild on change.",
)
@click.option(
    "--static-dir",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Directory to serve static files from. Defaults to the client dist.",
)
@click.option(
    "--base-path",
    type=str,
    default="",
    help="Base path prefix for all routes, e.g. '/editor'.",
)
def main(
    *,
    startup: Literal["api", "frontend", "both"] = "both",
    dev: bool = False,
    static_dir: Path | None = None,
    base_path: str = "",
) -> None:  # pragma: no cover
    """Start the mex-editor api."""
    app = create_fastapi("dev" if dev else None, startup, static_dir, base_path)
    uvicorn.run(app, host="0.0.0.0", port=8000)

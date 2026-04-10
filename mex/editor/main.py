from typing import TYPE_CHECKING, Any, Literal

from mex.editor.debugpy import setup_debugpy

if TYPE_CHECKING:  # pragma: no cover
    from starlette.responses import Response

import click
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

from mex.editor.api.data import router as data_router
from mex.editor.api.system import router as system_router
from mex.editor.frontend import CLIENT_DIST


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope: Any) -> Response:
        try:
            return await super().get_response(path, scope)
        except (HTTPException, StarletteHTTPException) as ex:
            if ex.status_code == 404:
                return await super().get_response("index.html", scope)
            raise ex


def create_fastapi(
    startup: Literal["api", "frontend", "both"] = "both",
) -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="mex-editor",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    if startup in ["api", "both"]:
        app.include_router(data_router, prefix="/api/v0")
        app.include_router(system_router, prefix="/api/v0")
    if startup in ["frontend", "both"]:
        app.mount(
            "/",
            SPAStaticFiles(directory=CLIENT_DIST, html=True),
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
    "--debug",
    is_flag=True,
    default=False,
    help="Define if started in debug mode to be able to attach to debugpy (port: 5678).",
)
def main(
    *,
    startup: Literal["api", "frontend", "both"] = "both",
    debug: bool = False,
) -> None:  # pragma: no cover
    """Start the mex-editor api."""
    app = create_fastapi(startup)
    if debug:
        setup_debugpy()
    uvicorn.run(app, port=8000)


if __name__ == "__main__":
    main()

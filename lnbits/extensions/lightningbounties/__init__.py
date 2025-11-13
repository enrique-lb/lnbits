import asyncio
from fastapi import APIRouter
from .views import lightningbounties_ext_generic

# Main router for the extension, using the prefix /lightningbounties
lightningbounties_ext: APIRouter = APIRouter(prefix="/lightningbounties",
                                             tags=["lightningbounties"])
lightningbounties_ext.include_router(lightningbounties_ext_generic)

# Register the static files (like your logo.png)
lightningbounties_static_files = [{
    "path": "/lightningbounties/static",
    "name": "lightningbounties_static",
}]


# These are required by LNbits, we can leave them empty
def lightningbounties_stop():
    pass


def lightningbounties_start():
    pass

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from lnbits.core.models import User
from lnbits.decorators import check_user_exists
from lnbits.helpers import template_renderer

lightningbounties_ext_generic = APIRouter(tags=["lightningbounties"])


@lightningbounties_ext_generic.get("/",
                                   description="Lightning Bounties extension",
                                   response_class=HTMLResponse)
async def index(
        request: Request,
        user: User = Depends(check_user_exists),
):
    #
    # --- THIS IS THE FIX ---
    # We are changing the search path to be the root of your extension
    # and then specifying the full path to the template.
    #
    return template_renderer(["lightningbounties"]).TemplateResponse(
        request, "templates/lightningbounties/index.html",
        {"user": user.json()})

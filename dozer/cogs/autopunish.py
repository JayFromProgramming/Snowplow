"""Runs dozers autopunishments"""

from ._utils import *
from .. import db


class AutoPunish(Cog):
    """A cog to handle autopunishments."""

    def __init__(self, bot):
        super().__init__(bot)


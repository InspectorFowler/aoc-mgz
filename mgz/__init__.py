"""Entry point for reading MGZ."""

# pylint: disable=invalid-name,no-name-in-module

from construct import (Struct, CString, Const, Int32ul, Embedded, Float32l, Terminated, If, Computed, this, Peek)
from mgz.util import MgzPrefixed, ZlibCompressed, Version, get_version
from mgz.header.ai import ai
from mgz.header.replay import replay
from mgz.header.map_info import map_info
from mgz.header.initial import initial
from mgz.header.achievements import achievements
from mgz.header.scenario import scenario
from mgz.header.lobby import lobby
from mgz.header.de import de


compressed_header = Struct(
    "game_version"/CString(encoding='latin1'),
    "save_version"/Float32l,
    "version"/Computed(lambda ctx: get_version(ctx.game_version, ctx.save_version)),
    "de"/If(lambda ctx: ctx.version == Version.DE, de),
    ai,
    replay,
    map_info,
    initial,
    achievements,
    scenario,
    lobby,
    Terminated
)

subheader = Struct(
    "check"/Peek(Int32ul),
    "chapter_address"/If(lambda ctx: ctx.check == 0, # TODO: could be greater
        Int32ul
    ),
    Embedded(MgzPrefixed(lambda ctx: ctx._.header_length - 4 - (4 if ctx.check == 0 else 0), ZlibCompressed(compressed_header)))
)

"""Header is compressed"""
header = Struct(
    "header_length"/Int32ul,
    Embedded(subheader)
)

from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from . import __main__ as __main__
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="发电文学",
    description="被艾特或戳一戳时发送发电文学",
    usage="艾特bot或戳一戳bot即可触发",
    config=Config,
)

config = get_plugin_config(Config)


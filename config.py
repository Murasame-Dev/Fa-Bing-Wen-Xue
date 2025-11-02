from pydantic import BaseModel
from typing import Set


class Config(BaseModel):
    """Plugin Config Here"""
    
    # 黑名单群聊列表
    fabing_blacklist_groups: Set[int] = set()
    
    # 黑名单用户列表
    fabing_blacklist_users: Set[int] = set()
    
    # 触发冷却时间（秒），默认60秒
    fabing_cooldown: int = 60

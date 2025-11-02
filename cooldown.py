# -*- coding: utf-8 -*-
"""
冷却管理模块
负责管理用户触发冷却
"""
import time
from typing import Dict
from nonebot import get_plugin_config
from .config import Config

# 获取配置
plugin_config = get_plugin_config(Config)

# 冷却记录字典 {user_id: last_trigger_time}
cooldown_tracker: Dict[int, float] = {}


def check_cooldown(user_id: int) -> bool:
    """
    检查用户是否在冷却中
    返回 True 表示可以触发，False 表示还在冷却中
    
    Args:
        user_id: 用户QQ号
        
    Returns:
        bool: True=可以触发，False=冷却中
    """
    current_time = time.time()
    
    # 如果该用户没有触发记录，可以触发
    if user_id not in cooldown_tracker:
        cooldown_tracker[user_id] = current_time
        return True
    
    # 检查是否过了冷却时间
    last_trigger_time = cooldown_tracker[user_id]
    if current_time - last_trigger_time >= plugin_config.fabing_cooldown:
        cooldown_tracker[user_id] = current_time
        return True
    
    return False


def get_remaining_cooldown(user_id: int) -> int:
    """
    获取用户剩余冷却时间（秒）
    
    Args:
        user_id: 用户QQ号
        
    Returns:
        int: 剩余冷却时间（秒），0表示无冷却
    """
    if user_id not in cooldown_tracker:
        return 0
    
    current_time = time.time()
    last_trigger_time = cooldown_tracker[user_id]
    elapsed = current_time - last_trigger_time
    remaining = plugin_config.fabing_cooldown - elapsed
    
    return max(0, int(remaining))


def reset_cooldown(user_id: int) -> None:
    """
    重置用户冷却时间（管理功能）
    
    Args:
        user_id: 用户QQ号
    """
    if user_id in cooldown_tracker:
        del cooldown_tracker[user_id]

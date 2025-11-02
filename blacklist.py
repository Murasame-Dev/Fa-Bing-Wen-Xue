# -*- coding: utf-8 -*-
"""
黑名单管理模块
负责管理黑名单群聊和用户
"""
from nonebot import get_plugin_config
from .config import Config

# 获取配置
plugin_config = get_plugin_config(Config)


def is_blacklisted(group_id: int, user_id: int) -> bool:
    """
    检查群聊或用户是否在黑名单中
    
    Args:
        group_id: 群号
        user_id: 用户QQ号
        
    Returns:
        bool: True=在黑名单中，False=不在黑名单中
    """
    # 检查群聊黑名单
    if group_id in plugin_config.fabing_blacklist_groups:
        return True
    
    # 检查用户黑名单
    if user_id in plugin_config.fabing_blacklist_users:
        return True
    
    return False


def is_group_blacklisted(group_id: int) -> bool:
    """
    检查群聊是否在黑名单中
    
    Args:
        group_id: 群号
        
    Returns:
        bool: True=在黑名单中，False=不在黑名单中
    """
    return group_id in plugin_config.fabing_blacklist_groups


def is_user_blacklisted(user_id: int) -> bool:
    """
    检查用户是否在黑名单中
    
    Args:
        user_id: 用户QQ号
        
    Returns:
        bool: True=在黑名单中，False=不在黑名单中
    """
    return user_id in plugin_config.fabing_blacklist_users

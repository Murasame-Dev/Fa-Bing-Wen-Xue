import random
import re
from nonebot import on_notice, on_message, on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, GroupMessageEvent, MessageSegment
from nonebot.adapters.onebot.v11 import Message
from nonebot.rule import to_me

from .texts import fadian_text
from .cooldown import check_cooldown
from .blacklist import is_blacklisted

# 监听戳一戳事件
poke_event = on_notice(priority=10, block=False)

@poke_event.handle()
async def handle_poke(bot: Bot, event: PokeNotifyEvent):
    # 判断是否是戳bot
    if event.target_id == event.self_id:
        # 黑名单检查
        if is_blacklisted(event.group_id, event.user_id):
            return
        
        # 冷却检查（按用户）
        if not check_cooldown(event.user_id):
            return
        
        # 获取戳bot的用户信息
        user_info = await bot.get_group_member_info(
            group_id=event.group_id,
            user_id=event.user_id
        )
        # 获取用户昵称或群名片
        user_name = user_info.get("card") or user_info.get("nickname") or str(event.user_id)
        
        # 随机选择一条发电文学，并替换name
        text = random.choice(fadian_text).replace("name", user_name)
        
        # 发送消息
        await bot.send_group_msg(group_id=event.group_id, message=text)


# 监听艾特bot的消息
at_event = on_message(rule=to_me(), priority=10, block=False)

@at_event.handle()
async def handle_at(bot: Bot, event: GroupMessageEvent):
    # 黑名单检查
    if is_blacklisted(event.group_id, event.user_id):
        return
    
    # 冷却检查（按用户）
    if not check_cooldown(event.user_id):
        return
    
    # 获取发送消息的用户信息
    user_info = await bot.get_group_member_info(
        group_id=event.group_id,
        user_id=event.user_id
    )
    # 获取用户昵称或群名片
    user_name = user_info.get("card") or user_info.get("nickname") or str(event.user_id)
    
    # 随机选择一条发电文学，并替换name
    text = random.choice(fadian_text).replace("name", user_name)
    
    # 发送消息
    await bot.send_group_msg(group_id=event.group_id, message=text)


# 监听"发病"关键词
fabing_keyword = on_keyword({"发病"}, priority=10, block=False)

@fabing_keyword.handle()
async def handle_fabing(bot: Bot, event: GroupMessageEvent):
    # 黑名单检查
    if is_blacklisted(event.group_id, event.user_id):
        return
    
    # 冷却检查（按用户）
    if not check_cooldown(event.user_id):
        return
    
    # 获取消息内容
    message = event.get_message()
    
    # 查找消息中的at信息
    target_user_id = None
    for seg in message:
        if seg.type == "at":
            target_user_id = int(seg.data["qq"])
            break
    
    # 如果没有@任何人，则使用发送者自己
    if target_user_id is None:
        target_user_id = event.user_id
    
    # 获取目标用户信息
    user_info = await bot.get_group_member_info(
        group_id=event.group_id,
        user_id=target_user_id
    )
    # 获取用户昵称或群名片
    user_name = user_info.get("card") or user_info.get("nickname") or str(target_user_id)
    
    # 随机选择一条发电文学，并替换name
    text = random.choice(fadian_text).replace("name", user_name)
    
    # 发送消息
    await bot.send_group_msg(group_id=event.group_id, message=text)

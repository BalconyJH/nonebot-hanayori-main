import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot

nonebot.init()
app = nonebot.get_asgi()
driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)

# 优先加载定时任务插件
nonebot.load_plugin("nonebot_plugin_apscheduler")

nonebot.load_builtin_plugins()
nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
	nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
	nonebot.run(app="__mp_main__:app")
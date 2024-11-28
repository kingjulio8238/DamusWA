from browser_use.logging_config import setup_logging

setup_logging()

from browser_use.agent.prompts import SystemPrompt as SystemPrompt
from browser_use.agent.service import Agent as Agent
from browser_use.agent.views import ActionResult as ActionResult
from browser_use.browser.service import Browser as Browser
from browser_use.browser.service import BrowserConfig as BrowserConfig
from browser_use.controller.service import Controller as Controller
from browser_use.dom.service import DomService as DomService

__all__ = [
	'Agent',
	'Browser',
	'BrowserConfig',
	'Controller',
	'DomService',
	'SystemPrompt',
	'ActionResult',
]

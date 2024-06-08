import asyncio
import random

import requests
from pyrogram import *
from pyrogram import Client, filters
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *
from pyrogram.types import Message

from PBXMUSIC import app
from PBXMUSIC.utils.basic import edit_or_reply, get_text
from PBXMUSIC.utils.constants import MEMES


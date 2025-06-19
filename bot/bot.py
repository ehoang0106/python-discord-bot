import discord
from discord.ext import commands, tasks
from dotenv import dotenv_values
import time
from datetime import datetime


config = dotenv_values(".env")

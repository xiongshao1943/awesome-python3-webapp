#!/usr/bin/ptyon3
# _*_ coding: utf-8 _*_

__author__ = 'xiongshao'

import asyncio,os,inspect,logging,functools
from urllib import parse
from aiohttp import web
from apis import APIError

def get(path):
  '''
  Define decorator @get('/path')
  '''
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
      return func(*args,**kw)
    wrapper.__method__ = 'GET'
    wrapper.__route__ = path
    return warpper
  return decorator


def post(path):
  '''
  Define decorator @post('/path')
  '''
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
      return func(*args,**kw)
    wrapper.__method__ = 'POST'
    wrapper.__route__ = path
    return warpper
  return decorator

def get_required_kw_args(fn):
  args = []
  params = inspect.signature(fn).parameters
  for name,param in params.items():
    if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
      args.append(name)
  return tuple(args)

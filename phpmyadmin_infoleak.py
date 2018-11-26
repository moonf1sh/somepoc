#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = moonfish
#_PlugName_ = phpmyadmin_/setup/index.php_未授权访问漏洞
#__Refer___ = https://hackerone.com/reports/297339

def assign(service, arg):
    if service == fingerprint.phpmyadmin:
        return True, arg
def audit(arg):
    payload = 'setup/index.php'
    target = arg + payload
    code, head, res, final_url, log= hackhttp.http(target)
    if code == 200 and "phpMyAdmin" in res:
        security_info(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign(fingerprint.phpmyadmin, 'http://www.example.com/')[1])
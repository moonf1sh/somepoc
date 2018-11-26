#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = moonfish
#_PlugName_ = wordpress_wp-config.php_配置错误导致调试信息泄露
#__Refer___ = https://codex.wordpress.org/Debugging_in_WordPress
import re
def assign(service, arg):
    if service == fingerprint.wordpress:
        return True, arg
def audit(arg):
    payload = 'wp-content/debug.log'
    target = arg + payload

    code, head, res, final_url, log= hackhttp.http(target)
    if code == 200 and "Notice:" in res:
        security_info(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign(fingerprint.wordpress, 'http://www.example.com/')[1])
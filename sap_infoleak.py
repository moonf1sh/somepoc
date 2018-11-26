#!/usr/bin/env python
# -*- coding: utf-8 -*-
#__Author__ = moonfish
#_PlugName_ = SAP NetWeaver_tc~rtc~coll.appl.rtc~wd_chat/Chat_敏感信息泄露
#__Refer___ = https://mp.weixin.qq.com/s/hNNn8dzPG2PXAikxTB2RWw
#_Descripton : search all username
import re
def assign(service, arg):
    if service == fingerprint.sap_netweaver:
        return True, arg
def audit(arg):
    payload = 'webdynpro/resources/sap.com/tc~rtc~coll.appl.rtc~wd_chat/Chat#'
    target = arg + payload

    code, head, res, final_url, log= hackhttp.http(target)
    if code == 200 and "ENBI.ChatView.TextView2" in res:
        security_note(target)
if __name__ == '__main__':
    from dummy import *
    audit(assign(fingerprint.sap_netweaver, 'http://www.example.com/')[1])
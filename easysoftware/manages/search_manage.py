#!/usr/bin/python3
# ******************************************************************************
# Copyright (c) Huawei Technologies Co., Ltd. 2024-2024. All rights reserved.
# licensed under the Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#     http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN 'AS IS' BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v2 for more details.
# ******************************************************************************/
import json
from easysoftware.conf.constant import SEARCH_RPM,HEADERS,SEARCH_URL
from easysoftware.function.log import LOGGER
from easysoftware.util.http_util import HttpUtil
from easysoftware.model.search_vo import SearchVo


class Search: 
    """
    Provides functions to search software.
    """
    @staticmethod
    def search_rpm(pkg_name) -> json:
        res_json = HttpUtil.request_search_rpm(pkg_name)
        rpmpkg = res_json["data"]["rpmpkg"]

        if rpmpkg is None or not rpmpkg:
            print("not found")

        for item in res_json["data"]["rpmpkg"]:
            search_vo = SearchVo(item["name"], item["version"], item["os"], item["arch"],\
                                 item["srcRepo"], item["category"], item["rpmSize"])  
            search_vo.standard_out()



    @staticmethod
    def search_docker(pkg_name) -> json:
        res_json = HttpUtil.request_search_docker(pkg_name)
        appkg = res_json["data"]["apppkg"]

        if appkg is None or not appkg:
            print("not found")

        for item in res_json["data"]["apppkg"]:
            search_vo = SearchVo(item["name"], item["version"], item["os"], item["arch"],\
                                 item["srcRepo"], item["category"], 0)  
            search_vo.standard_out()

    
    @staticmethod
    def search_oepkg(pkg_name) -> json:
        res_json = HttpUtil.request_search_oepkg(pkg_name)
        oepkg = res_json["data"]["oepkg"]

        if oepkg is None or not oepkg:
            print("not found")

        for item in oepkg:
            search_vo = SearchVo(item["name"], item["version"], item["os"], item["arch"],\
                                 item["srcRepo"], item["category"], item["rpmSize"])  
            search_vo.standard_out()
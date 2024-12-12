#!/usr/bin/python3
# ******************************************************************************
# Copyright (c) openEuler. 2024. All rights reserved.
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
from easysoftware.model.info_vo import InfoVo


class Info: 
    """
    Provides functions to search software.
    """
    @staticmethod
    def info_name(pkg_name) -> json:
        res_json = HttpUtil.reqeust_info_pkg(pkg_name)
        pkg_list = res_json["data"]["list"]

        if pkg_list is None or not pkg_list:
            print("no package found by name:", pkg_name)

        info_vo_list = []
        for item in pkg_list:
            info_vo = InfoVo(item["os"], item["arch"], item["name"], item["version"],\
                    item["category"], item["tags"], item["description"], item["maintainers"])
            info_vo_list.append(info_vo)
        
        Info.std(info_vo_list)

    @staticmethod
    def std(info_vo_list):
        os_set = set()
        arch_set = set()
        name_set = set()
        version_set = set()
        category_set = set()
        tags_list = []
        description_set = set()
        maintainers_list = []

        for item in info_vo_list:
            os_set.add(item.os)
            arch_set.add(item.arch)
            name_set.add(item.name)
            version_set.add(item.version)
            category_set.add(item.category)
            description_set.add(item.description)
            tags_list.extend(Info.convert_str_to_list(item.tags))
            maintainers_list.extend(Info.convert_str_to_list(item.maintainers))

        print('name: ', name_set)
        print('os: ', os_set)
        print('arch: ', arch_set)
        print('version: ', version_set)
        print('category: ', category_set)
        print('tags: ', set(tags_list))
        print('description: ', description_set)
        print('maintianers: ', sorted(list(set(maintainers_list))))

    @staticmethod
    def convert_str_to_list(str_obj):
        res_list = str_obj.strip("[")
        res_list = res_list.strip("]")
        res_list = res_list.split(",")
        return res_list


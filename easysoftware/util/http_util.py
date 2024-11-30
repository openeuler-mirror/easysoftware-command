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

from easysoftware.conf.constant import SEARCH_RPM,SEARCH_DOCKER,SEARCH_OEPKG,HEADERS,SEARCH_URL
from easysoftware.function.log import LOGGER
import requests
import json

class HttpUtil:
    @staticmethod
    def request_search_rpm(pkg_name) -> json:

        SEARCH_RPM["keyword"] = pkg_name

        response = requests.post(SEARCH_URL, data=json.dumps(SEARCH_RPM), headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            LOGGER.error(f"error：{response.text}")
            return {"error": "check network", "status_code": response.status_code}

    @staticmethod
    def request_search_docker(pkg_name) -> json:
  
        SEARCH_DOCKER["keyword"] = pkg_name

        response = requests.post(SEARCH_URL, data=json.dumps(SEARCH_DOCKER), headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            LOGGER.error(f"error：{response.text}")
            return {"error": "check network", "status_code": response.status_code}
      
    
    @staticmethod
    def request_search_oepkg(pkg_name) -> json:

        SEARCH_OEPKG["keyword"] = pkg_name

        response = requests.post(SEARCH_URL, data=json.dumps(SEARCH_OEPKG), headers=HEADERS)
        if response.status_code == 200:
            return response.json()
        else:
            LOGGER.error(f"error：{response.text}")
            return {"error": "check network", "status_code": response.status_code}

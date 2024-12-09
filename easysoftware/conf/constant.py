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
import os

BASE_CONFIG_PATH = '/etc/easysoftware'
BASE_SERVICE_PATH = '/usr/lib/systemd/system'

CERES_CONFIG_PATH = os.path.join(BASE_CONFIG_PATH, 'easysoftware.conf')

SEARCH_RPM = {
    "dataType": "rpmpkg",
    "keyword": "redis",
    "keywordType": "name",
    "pageNum": 1,
    "pageSize": 12
}
SEARCH_DOCKER = {
    "dataType": "apppkg",
    "keywordType": "name",
    "pageNum": 1,
    "pageSize": 12
}
SEARCH_OEPKG = {
    "dataType": "oepkg",
    "keywordType": "name",
    "pageNum": 1,
    "pageSize": 12
}
HEADERS = {
    'Content-Type': 'application/json'
}

SEARCH_URL = "https://easysoftware.openeuler.org/api-search/software/docs"

class CommandExitCode:
    SUCCEED = 0
    FAIL = 255


class TaskExecuteRes:
    SUCCEED = "succeed"
    FAIL = "fail"


class CveFixTaskType:
    HOTPATCH = "hotpatch"
    COLDPATCH = "coldpatch"

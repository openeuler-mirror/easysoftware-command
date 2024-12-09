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

log = {
    "LOG_DIR": os.path.join('/', 'var', 'log', 'easysoftware'),
    "LOG_LEVEL": 'INFO',
    "MAX_BYTES": 31457280,
    "BACKUP_COUNT": 30,
}

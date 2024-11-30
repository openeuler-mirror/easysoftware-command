#!/usr/bin/python3
# ******************************************************************************
# Copyright (c) Huawei Technologies Co., Ltd. 2022-2022. All rights reserved.
# licensed under the Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#     http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN 'AS IS' BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v2 for more details.
# ******************************************************************************/

from dataclasses import dataclass
@dataclass
class SearchVo:
    name: str
    version: str
    os: str
    arch: str
    src_repo: str
    category: str
    size: str

    def standard_out(self) -> str:
        self.modify_field()
        std = f"{self.name}.{self.arch} {self.os} {self.category}"
        print(std)

    def modify_field(self):
        self.name = self.name.lstrip("<span>")
        self.name = self.name.replace("</span>","")

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
import sys

from easysoftware.cli.base import BaseCommand
from easysoftware.function.log import LOGGER
from easysoftware.manages.search_manage import Search


class SearchCommand(BaseCommand):
    """
    Plugin management command support
    """

    def __init__(self):
        super().__init__()
        self._sub_command = "search"
        self.parser = BaseCommand.subparsers.add_parser("search")
        self._add_arguments()
        self.command_handlers = {
            "oepkg": self.oepkg_search_handle,
            "docker": self.docker_search_handle,
            "rpm": self.rpm_search_handle,
        }

    def get_command_name(self):
        return self._sub_command

    def _add_arguments(self):
        self.parser.add_argument('--oepkg', type=str)
        self.parser.add_argument('--docker', type=str)
        self.parser.add_argument('--rpm', type=str)

    def execute(self, namespace):
        """
        Command execution entry
        """
        for option, arguments in vars(namespace).items():
            if option in self.command_handlers and arguments:
                self.command_handlers[option](arguments)

    @staticmethod
    def oepkg_search_handle(arguments):
        """
        oepkg search method
        """
        Search.search_oepkg(arguments)

    @staticmethod
    def docker_search_handle(arguments):
        """
        docker search method
        """
        Search.search_docker(arguments)

    def rpm_search_handle(self, arguments):
        """
        rpm search method
        """
        Search.search_rpm(arguments)


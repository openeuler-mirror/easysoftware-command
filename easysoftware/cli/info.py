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
import sys

from easysoftware.cli.base import BaseCommand
from easysoftware.function.log import LOGGER
from easysoftware.manages.info_manage import Info


class InfoCommand(BaseCommand):
    """
    Plugin management command support
    """

    def __init__(self):
        super().__init__()
        self._sub_command = "info"
        self.parser = BaseCommand.subparsers.add_parser("info")
        self._add_arguments()
        self.command_handlers = {
            "name": self.name_info_handle
        }

    def get_command_name(self):
        return self._sub_command

    def _add_arguments(self):
        self.parser.add_argument('--name', type=str, help="Specify the name you wish to query on openEuler.")

    def execute(self, namespace):
        """
        Command execution entry
        """
        for option, arguments in vars(namespace).items():
            if option in self.command_handlers and arguments:
                self.command_handlers[option](arguments)

    @staticmethod
    def name_info_handle(arguments):
        """
        name info method
        """
        Info.info_name(arguments)

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
import setuptools

NAME = "easysoftware"
INSTALL_REQUIRES=["requests", "concurrent_log_handler"]
VERSION = "1.0"

setuptools.setup(
    name = NAME,
    version = VERSION,
    description = "The easiest way to help every developer find what they want.",
    author = "",
    packages = setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'easysoftware = easysoftware.main:main'
        ]
    }
)

# openEuler easysoftware command 说明文档
# 做什么？
通过命令行搜索软件中心服务中管理的openEuler软件包，场景如下。
```bash
# 环境是 openeuler/openeuler:24.03-lts docker容器。
# 搜索软件中心中名称为`gcc`的类型是`rpm`的包，返回的是包`名称`和`架构`。
[root ]# easysoftware search --rpm gcc
gcc.arch:x86_64
gcc.arch:riscv64
gcc.arch:aarch64
```
# 怎么做？
将软件中心命令行工具打包为rpm包，用户安装rpm包即可使用。

# 案例
运行本仓库的`Dockerfile`生成容器，进入之后即可使用命令`easysoftware search --rpm gcc`。

# 实现步骤
## 1 软件中心命令行工具
软件中心命令行工具`easysoftware`本身由python编写。目录如下。
```
easysoftware/
├── cli
│   ├── base.py
│   ├── __init__.py
│   └── search.py
├── conf
│   ├── constant.py
│   ├── default_config.py
│   └── __init__.py
├── easysoftware.spec
├── function
│   ├── __init__.py
│   └── log.py
├── __init__.py
├── LICENSE
├── main.py
├── manages
│   ├── __init__.py
│   └── search_manage.py
├── model
│   ├── __init__.py
│   └── search_vo.py
└── util
    ├── http_util.py
    └── __init__.py
```
# 2 `setup.py`使python软件打包成rpm包
`setup.py`脚本如下。
```python
import setuptools

# 软件包名称
NAME = "easysoftware"
# 安装依赖
INSTALL_REQUIRES=["requests", "concurrent_log_handler"]
# 软件包版本
VERSION = "1.0"

setuptools.setup(
    name = NAME,
    version = VERSION,
    description = "The easiest way to help every developer find what they want.",
    author = "",
    packages = setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    zip_safe=False,
    # 'console_scripts'是控制台脚本。用户在控制台输入`easysoftware`，自动执行`easysoftware.main`文件下的`main`方法
    # 原理是rpm包会将`easysoftware`包安装在python三方包目录里，比如`/usr/lib/python3.11/site-packages/`。
    # 同时自动生成的`/usr/bin/easysoftware`可执行文件，对应用户在控制台的输入`easysoftware`。
    # 可执行文件是python文件，它从python目录里获取`easysoftware`包并且执行`main`方法。
    entry_points={
        'console_scripts': [
            'easysoftware = easysoftware.main:main'
        ]
    }
)
```
使用方法是命令行输入`python3 setup.py bdist_rpm`，生成的包在`./dist/easysoftware-1.0-1.noarch.rpm`
注意：`setup.py`要与`easysoftware`同目录，如下。如果在`easysoftware`目录里，会打包若干个`cli, conf, ..., util`包。
```
easysoftware-1.0
|-- easysoftware
|   |-- LICENSE
|   |-- __init__.py
|   |-- cli
|   |   |-- __init__.py
|   |   |-- base.py
|   |   `-- search.py
|   |-- conf
|   |   |-- __init__.py
|   |   |-- constant.py
|   |   `-- default_config.py
|   |-- easysoftware.spec
|   |-- function
|   |   |-- __init__.py
|   |   `-- log.py
|   |-- main.py
|   |-- manages
|   |   |-- __init__.py
|   |   `-- search_manage.py
|   |-- model
|   |   |-- __init__.py
|   |   `-- search_vo.py
|   |-- setup.py
|   `-- util
|       |-- __init__.py
|       `-- http_util.py
`-- setup.py

```

# 3 `easysoftware.spec`生成rpm包
## 1 目录结构
rpm包的目录要求是`~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}`。
其中`BUILD, BUILDROOT`是中间过程，构建完成后目录内容会被清空。
`SOURCES`目录是源码包目录，存放`easysoftware-1.0.tar.gz`。`easysoftware-1.0`目录是将`easysoftware-1.0.tar.gz`解压后的目录，仅仅为了展示，不是构建rpm包所必需的。
`SPECS`目录存放`easysoftware.spec`文件，控制台输入`rpmbuild -ba /root/rpmbuild/SPECS/easysoftware.spec`，rpm将根据`easysoftware.spec`文件的内容生成rpm包。
`RPMS, SRPMS`目录存放生成的rpm包，前者是安装包，控制台输入`rpm -ivh easysoftware-1.0-1.noarch.rpm`安装，后者是源码包。
```
~/rpmbuild/
|-- BUILD
|-- BUILDROOT
|-- RPMS
|   `-- noarch
|       `-- easysoftware-1.0-1.noarch.rpm
|-- SOURCES
|   |-- easysoftware-1.0
|   |   |-- Dockerfile
|   |   |-- easysoftware
|   |   |   |-- LICENSE
|   |   |   |-- __init__.py
|   |   |   |-- cli
|   |   |   |   |-- __init__.py
|   |   |   |   |-- base.py
|   |   |   |   `-- search.py
|   |   |   |-- conf
|   |   |   |   |-- __init__.py
|   |   |   |   |-- constant.py
|   |   |   |   `-- default_config.py
|   |   |   |-- easysoftware.spec
|   |   |   |-- function
|   |   |   |   |-- __init__.py
|   |   |   |   `-- log.py
|   |   |   |-- main.py
|   |   |   |-- manages
|   |   |   |   |-- __init__.py
|   |   |   |   `-- search_manage.py
|   |   |   |-- model
|   |   |   |   |-- __init__.py
|   |   |   |   `-- search_vo.py
|   |   |   |-- setup.py
|   |   |   `-- util
|   |   |       |-- __init__.py
|   |   |       `-- http_util.py
|   |   `-- setup.py
|   `-- easysoftware-1.0.tar.gz
|-- SPECS
|   `-- easysoftware.spec
`-- SRPMS
    `-- easysoftware-1.0-1.src.rpm
```
## 2 easysoftware.spec文件
` rpmbuild -ba /root/rpmbuild/SPECS/easysoftware.spec`的执行日志，会在控制台展示。
[关于宏的说明](https://docs.openeuler.org/zh/docs/20.03_LTS/docs/ApplicationDev/%E6%9E%84%E5%BB%BARPM%E5%8C%85.html)
```python
Name:           easysoftware
Version:        1.0
Release:        1
Summary:        The easiest way to help every developer find what they want.
License:        MulanPSL2
URL:            https://gitee.com/openeuler/easysoftware-command
# 以上信息是rpm包的元信息，可以通过命令`rpm -qi easysoftware`查询。

Source0:        %{name}-%{version}.tar.gz # easysoftware-1.0.tar.gz,源码包的名称
BuildArch:  noarch # 表示该rpm包不依赖特定架构
BuildRequires:  python3-setuptools # 构建rpm包的依赖，其实就是`setup.py`的依赖
Requires:  requests concurrent_log_handler # 提示用户在安装rpm包之前先安装这些依赖

%description # 描述
Easysoftware command tool.

%prep # 日志第一行就是 Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.AACinY，说明从本行开始执行。
%autosetup -n %{name}-%{version} # 解压源码包

%build # 构建
%py3_build # py3_build是rpm定义的宏，
# 控制台输入`rpm --eval %{py3_build}`可以得到如下结果
# /usr/bin/python3 setup.py  build --executable="/usr/bin/python3 -s"
# 可见，用的还是set.py命令

%install # 安装
%py3_install
# 控制台输入`rpm --eval %{py3_install}`可以得到如下结果
# /usr/bin/python3 setup.py  install -O1 --skip-build --root /root/rpmbuild/BUILDROOT/%{NAME}-%{VERSION}-%{RELEASE}.x86_64
# 表明将rpm包安装在BUILDROOT目录里

%files
%{python3_sitelib}/easysoftware*.egg-info
%{python3_sitelib}/easysoftware/*
%{_bindir}/easysoftware
# [root ]# rpm --eval %{python3_sitelib}
# /usr/lib/python3.11/site-packages
# 同理， %{_bindir}/easysoftware = /usr/bin/easysoftware
# %files目录表示安装包路径，如果注释掉`%files`下面三行，会报错：
# RPM build errors:
#     Installed (but unpackaged) file(s) found:
#    /usr/bin/easysoftware
#    /usr/lib/python3.11/site-packages/easysoftware-1.0-py3.11.egg-info/PKG-INFO
#    /usr/lib/python3.11/site-packages/easysoftware/main.py
# 即spec文件没有标明将要安装的文件/目录

# %changelog表示更改日志，每次更改脚本内容都应该记录日志
%changelog
* Tue Nov 30 2024 cc <cc@gmail.com> - 1.0-1
- Initial RPM release
```

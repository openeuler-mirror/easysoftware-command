FROM openeuler/openeuler:24.03-lts as BUILDER

RUN yum install -y rpm-build
RUN yum install -y rpmdevtools

ARG EASYSOFTWARE_VERSION=1.0


RUN yum install -y rpm-build rpmdevtools \
    && mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

COPY ./ /root/rpmbuild/SOURCES/easysoftware-$EASYSOFTWARE_VERSION
COPY ./easysoftware/easysoftware.spec /root/rpmbuild/SPECS/
COPY ./easysoftware/setup.py /root/rpmbuild/SOURCES/easysoftware-$EASYSOFTWARE_VERSION

RUN cd /root/rpmbuild/SOURCES/ \
    && tar zcf easysoftware-$EASYSOFTWARE_VERSION.tar.gz ./easysoftware-$EASYSOFTWARE_VERSION/


RUN rpmbuild -ba /root/rpmbuild/SPECS/easysoftware.spec

FROM openeuler/openeuler:24.03-lts
ARG EASYSOFTWARE_VERSION=1.0
COPY --from=Builder /root/rpmbuild/RPMS/noarch/easysoftware-$EASYSOFTWARE_VERSION-1.noarch.rpm /easysoftware-$EASYSOFTWARE_VERSION-1.noarch.rpm

RUN python3 -m ensurepip --upgrade \
    && python3 -m pip install requests \
    && python3 -m pip install concurrent_log_handler

RUN rpm -ivh easysoftware-$EASYSOFTWARE_VERSION-1.noarch.rpm --nodeps --force

# 进入容器试验：easysoftware search --rpm gcc
# 结果如下：
# gcc.arch:x86_64
# gcc.arch:x86_64
# gcc.arch:aarch64
# gcc.arch:aarch64
# gcc.arch:aarch64
# gcc.arch:aarch64
# gcc.arch:x86_64
# gcc.arch:x86_64
# gcc.arch:x86_64

Name:           easysoftware
Version:        1.0
Release:        1
Summary:        The easiest way to help every developer find what they want.
License:        MulanPSL2
URL:            https://gitee.com/openeuler/easysoftware-command
Source0:        %{name}-%{version}.tar.gz

BuildArch:  noarch
BuildRequires:  python3-setuptools
Requires:  requests concurrent_log_handler

%description
The easiest way to help every developer find what they want.

%prep
%autosetup -n %{name}-%{version}


%py3_build

%py3_install

%files
%{python3_sitelib}/%{name}*.egg-info
%{python3_sitelib}/%{name}/*
%{_bindir}/%{name}

%changelog
* Tue Nov 30 2024 cc <cc@gmail.com> - 1.0-1
- Initial RPM release

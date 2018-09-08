#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : CherryPy
Version  : 18.0.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/2d/42/00390197d077c4d147c77b2da48777c0243810000931a208b3ce30824d7c/CherryPy-18.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/2d/42/00390197d077c4d147c77b2da48777c0243810000931a208b3ce30824d7c/CherryPy-18.0.0.tar.gz
Summary  : Object-Oriented HTTP framework
Group    : Development/Tools
License  : BSD-3-Clause
Requires: CherryPy-bin
Requires: CherryPy-python3
Requires: CherryPy-license
Requires: CherryPy-python
Requires: alabaster
Requires: cheroot
Requires: contextlib2
Requires: docutils
Requires: portend
Requires: pyOpenSSL
Requires: pytest-sugar
Requires: python-memcached
Requires: simplejson
Requires: six
Requires: zc.lockfile
BuildRequires : buildreq-distutils3
BuildRequires : cheroot
BuildRequires : contextlib2
BuildRequires : more-itertools
BuildRequires : pluggy
BuildRequires : portend
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zc.lockfile

%description
.. image:: https://img.shields.io/pypi/v/cherrypy.svg
:target: https://pypi.org/project/cherrypy

%package bin
Summary: bin components for the CherryPy package.
Group: Binaries
Requires: CherryPy-license

%description bin
bin components for the CherryPy package.


%package license
Summary: license components for the CherryPy package.
Group: Default

%description license
license components for the CherryPy package.


%package python
Summary: python components for the CherryPy package.
Group: Default
Requires: CherryPy-python3
Provides: cherrypy-python

%description python
python components for the CherryPy package.


%package python3
Summary: python3 components for the CherryPy package.
Group: Default
Requires: python3-core

%description python3
python3 components for the CherryPy package.


%prep
%setup -q -n CherryPy-18.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536442733
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/CherryPy
cp LICENSE.md %{buildroot}/usr/share/doc/CherryPy/LICENSE.md
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cherryd

%files license
%defattr(-,root,root,-)
/usr/share/doc/CherryPy/LICENSE.md

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

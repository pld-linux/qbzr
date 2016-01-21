# TODO: Move %{py_sitescriptdir}/bzrlib/plugins to bzr package ?
Summary:	Plugin for Bazaar-NG (bzr)
Summary(pl.UTF-8):	Wtyczka do Bazaar-NG (bzr)
Name:		qbzr
Version:	0.23.1
Release:	1
License:	GPL v2+
Group:		Development/Version Control
Source0:	http://launchpad.net/qbzr/0.23/%{version}/+download/qbzr-%{version}.tar.gz
# Source0-md5:	594796b2cf9887d895545d7ed84e3879
URL:		http://wiki.bazaar.canonical.com/QBzr
BuildRequires:	python >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires(post,postun):	desktop-file-utils
%pyrequires_eq	python
Requires:	bzr
Requires:	python-PyQt4
# BuildArch:	noarch  # NOTE: In fact qbzr is noarch, but have to land in ../site-packages/bzrlib/plugins/ where bzr lands to work
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin for Bazaar-NG (bzr)

%prep
%setup -q -n qbzr

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--install-purelib %{py_sitedir} \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt NEWS.txt README.txt TODO.txt
%dir %{py_sitedir}/bzrlib/plugins
%{py_sitedir}/bzrlib/plugins/qbzr
%{py_sitedir}/qbzr*.egg-info

Summary:	BB - the portable demo
Summary(pl.UTF-8):	BB - przenośne demo
Name:		bb
Version:	1.3rc1
Release:	11
License:	GPL
Group:		Applications/Terminal
Source0:	http://dl.sourceforge.net/aa-project/%{name}-%{version}.tar.gz
# Source0-md5:	1ae5b742fbe654ba51c31832cf7e81fd
Patch0:		%{name}-typos.patch
Patch1:		%{name}-regparm.patch
Patch2:		segv64.patch
Patch3:		bb-1.3.0_rc1-disable-pulse.patch
URL:		http://aa-project.sourceforge.net/bb/
BuildRequires:	aalib-devel >= 1.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libmikmod-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BB is an high quality audio-visual demonstration for your text
terminal. It is portable demo, so you can run it on plenty of
operating systems.

%description -l pl.UTF-8
BB jest wysokiej jakości demem z grafiką i dźwiękiem, działającym na
terminalu tekstowym. Jest przenośne - działa na wielu systemach
operacyjnych.

%prep
%setup -q -n %{name}-1.3.0
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
rm -f missing
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/bb
%{_mandir}/man1/*

Summary:	BB - the portable demo
Summary(pl):	BB - przeno¶ne demo
Name:		bb
Version:	1.3rc1
Release:	2
License:	GPL
Group:		Applications/Terminal
Source0:	ftp://download.sourceforge.net/pub/sourceforge/aa-project/%{name}-%{version}.tar.gz
URL:		http://aa-project.sourceforge.net/bb/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	aalib-devel >= 1.4
BuildRequires:	libmikmod-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BB is an high quality audio-visual demonstration for your text
terminal. It is portable demo, so you can run it on plenty of
operating systems.

%description -l pl
BB jest wysokiej jako¶ci demem z grafik± i d¼wiêkiem, dzia³aj±cym na
terminalu tekstowym. Jest przeno¶ne - dzia³a na wielu systemach
operacyjnych.

%prep
%setup -q -n %{name}-1.3.0

%build
rm -f missing
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/bb
%{_mandir}/man1/*

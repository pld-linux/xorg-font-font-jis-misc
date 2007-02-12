Summary:	jis-misc font
Summary(pl.UTF-8):   Font jis-misc
Name:		xorg-font-font-jis-misc
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/font/font-jis-misc-%{version}.tar.bz2
# Source0-md5:	61febb49a71065723a1fba17cbf23c67
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jis-misc font.

%description -l pl.UTF-8
Font jis-misc.

%prep
%setup -q -n font-jis-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/misc/*.pcf.gz

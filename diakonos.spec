#
# TODO: custom user for config
#
Summary:	Customizable and usable console-based text editor
Name:		diakonos
Version:	0.9.0
Release:	0.1
License:	MIT
Group:		Applications
Source0:	http://diakonos.pist0s.ca/archives/%{name}-%{version}.tar.bz2
# Source0-md5:	237b86e00db10296e1beac3725516ae9
URL:		http://diakonos.pist0s.ca/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diakonos is a customizable, usable console-based text editor. It
features arbitrary language scripting, an interactive help system,
bookmarking, regular expression searching, parsed ("smart")
indentation, macro recording and playback, a multi-element clipboard,
multi-level undo, a customizable status line, completely customizable
keyboard mapping, and customizable syntax highlighting.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__ruby} install.rb \
	--lib-dir %{ruby_rubylibdir} \
	--dest-dir $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.rdoc
%attr(755,root,root) %{_bindir}/diakonos
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/diakonos.conf
%{ruby_rubylibdir}/diakonos.rb
%{ruby_rubylibdir}/diakonos
%{_datadir}/%{name}

Name:		guitoutils
Summary:	A set of utilities to help some tasks
Version:	1.5
Release:	1
Source0:	v%{version}.tar.gz
URL:		www.guitoalmeida.com.br
Group:		System/Base
License:	GPLv3+
BuildRequires:	help2man

%description
Guito Utils is a set of utilities that improve some tools
already available or a implement new tools that make easier some tasks.

%prep
%setup

%build
./configure --prefix=/usr
%make


%install
%makeinstall_std


%files
/usr/bin/backup-files
/usr/bin/clean-user-config
/usr/bin/dt
/usr/bin/gchmod
/usr/bin/hello
/usr/bin/known-hosts
/usr/bin/search-files
/usr/bin/sum-count
/usr/bin/tail
/usr/bin/userlist
/usr/share/man/man1/clean-user-config.1.xz
/usr/share/man/man1/dt.1.xz
/usr/share/man/man1/gchmod.1.xz
/usr/share/man/man1/hello.1.xz
/usr/share/man/man1/known-hosts.1.xz
/usr/share/man/man1/search-files.1.xz
/usr/share/man/man1/sum-count.1.xz
/usr/share/man/man1/tail.1.xz
/usr/share/man/man1/userlist.1.xz

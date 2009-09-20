%define name    snortsam
%define version 2.63
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    SnortSAM module
License:    GPL
Group:      Networking/Other
URL:        http://www.snortsam.net/
Source:     http://www.snortsam.net/files/snortsam/%{name}-src-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Snortsam is a daemon that interacts with snort to use a firewall.

%prep
%setup -q -n %{name}
cat > Makefile <<EOF
install:
EOF

%build
sh ./makesnortsam.sh
cd src
make samtool
#%make "CFLAGS=%optflags"

%install
install -d %{buildroot}%{_sbindir}
rm -rf %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_sysconfdir}
install snortsam %{buildroot}%{_sbindir}
install samtool %{buildroot}%{_sbindir}
install conf/snortsam.conf.sample %{buildroot}%{_sysconfdir}/snortsam.conf
%makeinstall
#%{__rm} -rf %{buildroot}

#mkdir %{buildroot}%_mandir/man1
#mv %{buildroot}%_mandir/*.1 %{buildroot}%_mandir/man1/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc docs/*
#%_bindir/*
%_sbindir/*
#%_mandir/man1/*
%{_sysconfdir}/snortsam.conf





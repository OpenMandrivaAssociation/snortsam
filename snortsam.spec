%define name    snortsam
%define version 2.70
%define release 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    SnortSAM module
License:    BSD
Group:      Networking/Other
URL:        https://www.snortsam.net/
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
%doc docs/{README*,LICENSE,INSTALL,FAQ,CREDITS,BUGS,AUTHORS}
%_sbindir/*
%{_sysconfdir}/snortsam.conf






%changelog
* Sun Mar 20 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.70-1mdv2011.0
+ Revision: 647105
- 2.70
  P0 is not necessary :-)

* Fri Aug 06 2010 Michael Scherer <misc@mandriva.org> 2.69-2mdv2011.0
+ Revision: 567142
- document the patch, increase the release
- fix License
- fix Doc to not include CVS directory
- clean spec by removing comment

* Fri Nov 27 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.69-1mdv2010.1
+ Revision: 470439
- P1 to fix an if
- New 2.69

* Mon Nov 09 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.68-1mdv2010.1
+ Revision: 463579
- New 2.68

* Sun Oct 18 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.66-0.1mdv2010.0
+ Revision: 458112
- New 2.66 with new cisco null route pluging, and speed improvements

* Sun Sep 20 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.63-1mdv2010.0
+ Revision: 445821
- New release 2.63

* Thu Sep 17 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.60-1mdv2010.0
+ Revision: 444191
- sh to let run makesnortsam.sh
- New version

* Fri Mar 20 2009 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.57-2mdv2009.1
+ Revision: 358237
- import snortsam


* Thu Feb 12 2009 Daniel Lucio <dlucio@okay.com.mx> 2.57-2mdv2009.0
- Adding samtool
* Sun Jan 18 2009 Daniel Lucio <dlucio@okay.com.mx> 2.57-1mdv2009.0
+ Revision: 243049
- rebuild
- rebuild


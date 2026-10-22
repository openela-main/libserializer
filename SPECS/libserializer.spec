Name: libserializer
Version: 1.1.2
Release: 20%{?dist}
Summary: JFreeReport General Serialization Framework
License: LGPLv2+
Group: System Environment/Libraries
#Original source: http://downloads.sourceforge.net/jfreereport/libserializer-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: libserializer-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org
BuildRequires: ant, ant-contrib, java-21-openjdk-devel, jpackage-utils, libbase >= 1.1.2
Requires: java-21-openjdk-headless >= 1:21, jpackage-utils, libbase >= 1.1.2
BuildArch: noarch

%global java_home /usr/lib/jvm/java-21-openjdk

Patch0: libserializer-1.1.2.build.patch
Patch1: libserializer-1.1.2.java11.patch
Patch2: libserializer-1.1.2-remove-commons-logging.patch

%description
Libserializer contains a general serialization framework that simplifies the
task of writing custom java serialization handlers.

%package javadoc
Summary: Javadoc for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
%patch1 -p1 -b .java11
%patch2 -p1 -b .no_commons_logging
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase
cd lib
ln -s /usr/share/java/ant ant-contrib

%build
export JAVA_HOME=%{java_home}
ant jar javadoc

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/libserializer-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%doc ChangeLog.txt licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Oct 19 2026 Tomas Popela <tpopela@redhat.com> - 1.1.2-20
- Remove commons logging dependency
- Related: RHEL-286491

* Tue Oct 06 2026 Tomas Popela <tpopela@redhat.com> - 1.1.2-19
- OpenJDK 8 won't be supported anymore on RHEL 8 starting from November 2026,
  move to OpenJDK 21
- Resolves: RHEL-275417

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Caolán McNamara <caolanm@redhat.com> - 1.1.2-12
- Resolves: rhbz#1068367 Switch to java-headless (build)requires

* Wed Oct 23 2013 Caolán McNamara <caolanm@redhat.com> - 1.1.2-11
- Resolves: rhbz#1022138 remove versioned jars

* Tue Aug 06 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.1.2-10
- ant-nodeps is dropped from ant-1.9.0-2 build in rawhide
- Drop buildroot, %%clean, %%defattr and removal of buildroot in %%install

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 02 2012 Caolán McNamara <caolanm@redhat.com> - 1.1.2-7
- repack source to remove bundled multi-license .jars

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> - 1.1.2-4
- Related: rhbz#749103 drop gcj aot

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 01 2010 Caolán McNamara <caolanm@redhat.com> 1.1.2-2
- fix up source-code download foo

* Fri Nov 20 2009 Caolán McNamara <caolanm@redhat.com> 1.1.2-1
- initial fedora import

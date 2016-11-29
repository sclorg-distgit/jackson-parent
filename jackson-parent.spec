%{?scl:%scl_package jackson-parent}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 2

Name:          %{?scl_prefix}jackson-parent
Version:       2.6.2
Release:       2.%{baserelease}%{?dist}
Summary:       Parent pom for all Jackson components
License:       ASL 2.0
URL:           https://github.com/FasterXML/jackson-parent
Source0:       https://github.com/FasterXML/jackson-parent/archive/%{pkg_name}-%{version}.tar.gz
# jackson-parent package don't include the license file
# reported @ https://github.com/FasterXML/jackson-parent/issues/1
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

Patch0: replace-replace-with-antrun.patch

BuildRequires: %{?scl_prefix_maven}maven-local
BuildRequires: %{?scl_prefix}mvn(com.fasterxml:oss-parent:pom:)
BuildRequires: %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires: %{?scl_prefix_java_common}mvn(junit:junit)

BuildArch:     noarch

%description
Project for parent pom for all Jackson components.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}

%patch0

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x

%mvn_build
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc README.md
%doc LICENSE

%changelog
* Mon Jul 25 2016 Mat Booth <mat.booth@redhat.com> - 2.6.2-2.2
- Use antrun instead of unavailable replace maven plugin

* Mon Jul 25 2016 Mat Booth <mat.booth@redhat.com> - 2.6.2-2.1
- Auto SCL-ise package for rh-eclipse46 collection

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Sep 28 2015 gil cattaneo <puntogil@libero.it> 2.6.2-1
- update to 2.6.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 gil cattaneo <puntogil@libero.it> 2.5-1
- update to 2.5

* Wed Jul 02 2014 gil cattaneo <puntogil@libero.it> 2.4.1-1
- initial rpm

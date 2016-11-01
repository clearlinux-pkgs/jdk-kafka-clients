Name     : jdk-kafka-clients
Version  : 0.10.0.0
Release  : 4
URL      : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.10.0.0/kafka-clients-0.10.0.0.jar
Source0  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.10.0.0/kafka-clients-0.10.0.0.jar
Source1  : https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.10.0.0/kafka-clients-0.10.0.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-kafka-clients-data
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%package data
Summary: data components for the jdk-kafka-clients package.
Group: Data

%description data
data components for the jdk-kafka-clients package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/kafka-clients.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/kafka-clients.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/kafka-clients.xml \
%{buildroot}/usr/share/maven-poms/kafka-clients.pom \
%{buildroot}/usr/share/java/kafka-clients.jar \

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/kafka-clients.jar
/usr/share/maven-metadata/kafka-clients.xml
/usr/share/maven-poms/kafka-clients.pom

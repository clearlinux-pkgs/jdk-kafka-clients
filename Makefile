PKG_NAME := jdk-kafka-clients
URL := https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.10.0.0/kafka-clients-0.10.0.0.jar
ARCHIVES := https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/0.10.0.0/kafka-clients-0.10.0.0.pom %{buildroot}

include ../common/Makefile.common

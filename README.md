# Steps to run

1. install and configure graalvm as default jdk with JAVA_HOME and PATH ( we tested with OpenJDK 64-Bit Server VM GraalVM CE 22.3.1 )
2. install graalpython ( `gu install python` )
3. install graalpython packages ( `graalpy -m ginstall pandas requests`, maybe also needed to install setuptools and wheel )
4. download the latest development branch assembly of rapiddweller-benerator-ce ( https://github.com/rapiddweller/rapiddweller-benerator-ce/releases/download/3.2.0/rapiddweller-benerator-ce-3.2.0-jdk-11-dist.tar.gz )
5. unzip the assembly and configure benerator with BENERATOR_HOME and PATH
6. test the installation with `benerator --version` in terminal
7. open the terminal enter the demo directory and run the demo with `benerator scriptfilePy.ben.xml`

cd /d C:\Kafka

if exist zookeeper (
    rmdir /s /q zookeeper
)

start "Zookeeper" .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
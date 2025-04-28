cd /d C:\Kafka

if exist "kafka-logs" (
    rmdir /s /q "kafka-logs"
)

start "Kafka" .\bin\windows\kafka-server-start.bat .\config\server.properties
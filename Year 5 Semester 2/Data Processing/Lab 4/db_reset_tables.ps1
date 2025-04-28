# --- CONFIG ---
$appVersion = "12"
$faustAppId = "lab4_t1-2_v$appVersion"              # Replace with your actual Faust app ID
$bootstrapServer = "localhost:9092"            # Kafka broker address
$changelogTopics = @(
    "$faustAppId-capacity_by_year_v$appVersion-changelog",
    "$faustAppId-low_entries_v$appVersion-changelog"
)                                              # List your changelog topics
$faustDataDir = ".\data\"                      # Faust state directory
$kafkaBinPath = "C:\Kafka\bin\windows"         # Update this to your Kafka `bin/windows` folder
# -------------

Write-Host "1. Stopping any running Faust worker..."
Get-Process | Where-Object { $_.Path -like "*faust*" } | ForEach-Object { Stop-Process -Id $_.Id -Force }

Write-Host "2. Deleting Faust local state directory..."
Remove-Item -Recurse -Force $faustDataDir -ErrorAction SilentlyContinue

Write-Host "3. Deleting Kafka changelog topics..."
foreach ($topic in $changelogTopics) {
    Start-Process -NoNewWindow -Wait "$kafkaBinPath\kafka-topics.bat" `
        -ArgumentList "--bootstrap-server $bootstrapServer --delete --topic $topic"
}

Write-Host "4. Resetting Kafka consumer group offsets..."
Start-Process -NoNewWindow -Wait "$kafkaBinPath\kafka-consumer-groups.bat" `
    -ArgumentList "--bootstrap-server $bootstrapServer --group $faustAppId --reset-offsets --to-earliest --all-topics --execute"

Write-Host "5. Faust reset completed successfully."

Write-Host "Press any key to continue..."
$Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
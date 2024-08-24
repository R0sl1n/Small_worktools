$Date = (Get-Date).ToString('ddMMyyyy-HHmmss')

Start-Transcript "C:\test\Logs\log-$Date.txt"

$MovedFiles = Move-Item c:\test\*.txt C:\test2 -Verbose -PassThru | Select -First 5
Write-Host "Number of files moved: [$(($MovedFiles | Measure).Count)]"

Stop-Transcript


# Days to keep c:\test\logs files.
$LogsRetention = 7

# Make the retention times negative.
$LogsRetention = $LogsRetention * -7

# Delete the old Logs files.
$Logs = (Get-ChildItem C:\test\Logs | `
    ?{$_.LastWriteTime -lt (Get-Date).AddDays($LogsRetention)})
$Logs | Remove-Item
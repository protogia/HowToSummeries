# How to check networkconnection with powershell

No telnet? Use .NET-core:

```ps1
$ipv4 = Read-Host -Prompt 'Type ipv4-address'
$port = Read-Host -Prompt 'Type port'

New-Object -TypeName System.Net.Sockets.TcpClient -ArgumentList $ipv4,$port # returns Object with Connection-attribute -eq $true if its established

# for udp
New-Object -TypeName System.Net.Sockets.UdpClient -ArgumentList $ipv4,$port 
```
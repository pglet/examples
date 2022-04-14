

param
(
	$destination=$PSScriptRoot,
	$token
)

New-Item -path "${destination}/pglet-node" -ItemType "directory" -Force

function Get-Files {
	
	param ($fl, $d)
	
	ForEach ($f in $fl) {
		
		if ($f.type -eq "blob") {
			$path = $f.path
			
			$outfilepath = "${destination}/pglet-node/"
			$response = Invoke-WebRequest -uri $f.url -OutFile "${d}/${path}" -Headers $fileRequestHeaders
			#Echo "response: $response"
		
		} elseif ($f.type -eq "tree") {
			$dirpath = $f.path
			New-Item -path "${destination}/pglet-node/${dirpath}" -ItemType "directory" -Force
			$innerfilelist = (Invoke-RestMethod -uri $f.url -ContentType "application/vnd.github.v3+json" -Headers $requestHeaders)
			
			Get-Files $innerfilelist.tree "${destination}/pglet-node/${dirpath}"
		}
	}		
}

$fileRequestHeaders = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$fileRequestHeaders.Add("Authorization", "token ${token}")
$fileRequestHeaders.Add("Accept", "application/vnd.github.v3.raw")
$requestHeaders = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
$requestHeaders.Add("Authorization", "token ${token}")
$requestHeaders.Add("Accept", "application/vnd.github.v3+json")
$mostRecentCommit = (Invoke-RestMethod -uri https://api.github.com/repos/OwenMcDonnell/pglet-node/branches/v1 -Headers $headers).commit.sha
Write-Output "the most recent commit is: $mostRecentCommit"
$filelist = Invoke-RestMethod -uri "https://api.github.com/repos/OwenMcDonnell/pglet-node/git/trees/${mostRecentCommit}" -Headers $headers
#Echo "returned file list: $filelist"
Get-Files $filelist.tree "${destination}/pglet-node"

Set-Location -Path "$PSScriptRoot\pglet-node"
$node_modules = "$PSScriptRoot\pglet-node\node_modules"
if (-Not (Test-path $node_modules)) {
	npm install
}
# $build_folder = "$PSScriptRoot\pglet-node\dist"
# if (-Not (Test-path $build_folder)) {
# 	tsc
# }
tsc





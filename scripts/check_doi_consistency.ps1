#Requires -Version 7.0
# Guard live cite targets. First mint: no superseded version IDs.
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$ConceptId = '21910874'
$CurrentVersionId = '21924075'
$SupersededIds = @('21910875')

$files = Get-ChildItem -LiteralPath $Root -Recurse -File -Include *.md,*.cff,*.html |
  Where-Object { $_.FullName -notmatch '\\.git\\' }

$bad = [System.Collections.Generic.List[string]]::new()
foreach ($f in $files) {
  $t = Get-Content -LiteralPath $f.FullName -Raw -ErrorAction SilentlyContinue
  if (-not $t) { continue }
  foreach ($id in $SupersededIds) {
    if ($t -match [regex]::Escape($id) -and $f.Name -ne 'ZENODO.md' -and $f.Name -ne 'CHANGELOG.md') {
      $bad.Add("$($f.Name): superseded id $id in live surface")
    }
  }
}
$readme = Get-Content -LiteralPath (Join-Path $Root 'README.md') -Raw
$zen = Get-Content -LiteralPath (Join-Path $Root 'ZENODO.md') -Raw
if ($readme -notmatch $ConceptId) { $bad.Add('README.md missing concept id') }
if ($readme -notmatch $CurrentVersionId) { $bad.Add('README.md missing current version id') }
if ($zen -notmatch $ConceptId -or $zen -notmatch $CurrentVersionId) { $bad.Add('ZENODO.md missing concept/version') }
if ($bad.Count) { $bad | ForEach-Object { Write-Host $_ }; exit 1 }
Write-Host "ok concept=$ConceptId current=$CurrentVersionId superseded=$($SupersededIds -join ',')"
exit 0

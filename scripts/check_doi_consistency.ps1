#Requires -Version 7.0
# Guard live cite targets. Scans tracked files only, so scratch files cannot trip it.
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
$ConceptId = '21910874'
$CurrentVersionId = '23262565'
$SupersededIds = @('21910875', '21924075')
# Earlier paper sources are archival: they correctly cite the version they were written for.
$HistoricalFiles = @('ZENODO.md', 'CHANGELOG.md', 'PAPER_PATCHGAP_DRAFT_v4-PRE.md', 'PAPER_PATCHGAP_DRAFT_v5-PRE.md')

$files = git -C $Root ls-files -- '*.md' '*.cff' '*.html' |
  ForEach-Object { Get-Item -LiteralPath (Join-Path $Root $_) }

$bad = [System.Collections.Generic.List[string]]::new()
foreach ($f in $files) {
  $t = Get-Content -LiteralPath $f.FullName -Raw -ErrorAction SilentlyContinue
  if (-not $t) { continue }
  foreach ($id in $SupersededIds) {
    if ($t -match [regex]::Escape($id) -and $HistoricalFiles -notcontains $f.Name) {
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

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

Write-Host "Configurando git core.hooksPath => .githooks"
git config core.hooksPath .githooks

if ($LASTEXITCODE -ne 0) {
    Write-Error "No se pudo configurar core.hooksPath."
    exit 1
}

Write-Host "Hooks configurados correctamente."
Write-Host "Proximo commit ejecutara la validacion del bootstrap automaticamente."

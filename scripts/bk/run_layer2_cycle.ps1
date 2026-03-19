param(
    [string]$ResponseDir = "reports",
    [int]$MaxIterations = 10,
    [string]$CycleResponseBasename = "validate_master_layer2_response",
    [string]$TaxonomyFile
)

$ErrorActionPreference = "Stop"

if ($MaxIterations -lt 1) {
    Write-Error "MaxIterations debe ser >= 1"
    exit 2
}

$repoRoot = Split-Path -Parent $PSScriptRoot
$validator = Join-Path $PSScriptRoot "validate_tree_layer2.py"

if (-not (Test-Path $validator)) {
    Write-Error "No existe el validador: $validator"
    exit 2
}

$responseDirPath = Join-Path $repoRoot $ResponseDir
if (-not (Test-Path $responseDirPath)) {
    Write-Error "No existe el directorio de respuestas: $responseDirPath"
    exit 2
}

$argsList = @(
    $validator,
    "--apply-cycle",
    $responseDirPath,
    "--max-iterations",
    "$MaxIterations",
    "--cycle-response-basename",
    $CycleResponseBasename
)

if ($TaxonomyFile) {
    $argsList += "--taxonomy-file"
    $argsList += $TaxonomyFile
}

Write-Host "Ejecutando ciclo L2..."
Write-Host "  ResponseDir: $responseDirPath"
Write-Host "  MaxIterations: $MaxIterations"
Write-Host "  Basename: $CycleResponseBasename"

& python @argsList
$exitCode = $LASTEXITCODE

Write-Host "ExitCode: $exitCode"
exit $exitCode
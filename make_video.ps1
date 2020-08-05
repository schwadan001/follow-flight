$proj_name=$args[0]
$trail=$args[1]

$valid_projects=( Get-ChildItem ./projects -directory | ForEach-Object -Process {$_.Name} )

if ( $proj_name -eq $null ) {
    Write-Output "Must specify project name as first positional argument"
    Write-Output "   - ex. restore_audio.ps1 my_project_name"
} elseif ( $valid_projects -contains $proj_name ) {
    Write-Output "Filling in coordinate gaps..."
    Start-Process python fill_gaps.py -Wait
    Write-Output "Processing images to add shot tracking..."
    if ( $trail -eq $null ) {
        Start-Process python process_images.py -Wait
    } else {
        Start-Process python -Wait -ArgumentList 'process_images.py', '--trail', "$trail"
    }
    Write-Output "Constructing AVI video from frames..."
    Start-Process python construct_video.py -Wait
    ./restore_audio.ps1 $proj_name
} else {
    Write-Output "'$proj_name' is not a valid project name"
}

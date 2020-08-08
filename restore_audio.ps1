$proj_name=$args[0]
$proj_path="./follow-flight-projects/$proj_name"

$silent_video_path="$proj_path/follow_flight_silent.avi"
$final_video_avi="$proj_path/follow_flight_final.avi"
$final_video_mp4="$proj_path/follow_flight_final.mp4"

if ( $proj_name -eq $null ) {
    Write-Output "Must specify project name as first positional argument"
    Write-Output "   - ex. restore_audio.ps1 my_project_name"
} elseif ( Test-Path $proj_path -PathType Container ) {
    Write-Output "Creating final video (with sound) for '$proj_name'"
    if ( Test-Path -Path $final_video_avi ) {
        Remove-Item $final_video_avi
    }
    ffmpeg -i $silent_video_path -i ./$proj_path/audio.wav -codec copy -shortest $final_video_avi
    Remove-Item $silent_video_path
    Write-Output "Converting from avi to mp4"
    if ( Test-Path -Path $final_video_mp4 ) {
        Remove-Item $final_video_mp4
    }
    ffmpeg -i $final_video_avi $final_video_mp4
    Remove-Item $final_video_avi
} else {
    Write-Output "'$proj_name' is not a valid project name"
}

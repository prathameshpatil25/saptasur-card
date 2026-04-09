# Hero Section Background Video

The hero section is now configured to display a background video.

## How to add your video

1. Place your video files in this directory:
   - `hero-background.mp4` (MP4 format for best browser compatibility)
   - `hero-background.webm` (WebM format as a fallback)

## Video Requirements

- **Recommended dimensions**: 1920x1080 or higher (Full HD minimum)
- **Recommended duration**: Loop seamlessly (5-30 seconds recommended)
- **Format**: MP4 (h264 codec) and WebM
- **File size**: Keep under 20MB for optimal loading performance
- **Properties**: 
  - Autoplay: Enabled (auto-starts)
  - Muted: Required (browsers mute autoplay videos by default)
  - Loop: Enabled (repeats continuously)
  - Playsinline: Enabled (plays inline on mobile)

## How to convert your video

If you have a video file in another format, use FFmpeg:

```bash
# Convert to MP4
ffmpeg -i input-video.mov -c:v libx264 -preset medium -crf 23 -c:a aac -b:a 128k hero-background.mp4

# Convert to WebM
ffmpeg -i input-video.mov -c:v libvpx-vp9 -b:v 1M -c:a libopus -b:a 128k hero-background.webm
```

## Fallback

If no video files are found, the hero section will display the original background image (`../images/68f8983186a14adafbf06104_img-1.webp`).

## CSS Properties

The video is styled with:
- `object-fit: cover` - Maintains aspect ratio while covering the entire container
- `position: absolute` - Positioned behind all content
- `z-index: 0` - Stays behind the inner hero content
- The `.inner-hero` content has `z-index: 3` to stay above the video

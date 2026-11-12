import subprocess
import os

print("--- Generating Banner 1 & Background 1 (Racing Velocity) ---")
# Banner 1: Left has alpine mountain sky + red racing chevrons, right has Philipp carving
subprocess.run("""
magick -size 1920x540 xc:"#0c1b33" \
  assets_gen/philipp_carv.jpg -geometry +720+0 -composite \
  \( -size 800x540 xc:none -fill "rgba(12,27,51,0.95)" -draw "polygon 0,0 750,0 550,540 0,540" \) -composite \
  \( -size 1920x540 xc:none -stroke "#C8102E" -strokewidth 6 -draw "line 750,0 550,540" -stroke "#FFFFFF" -strokewidth 2 -draw "line 740,0 540,540" \) -composite \
  \( -size 600x540 xc:none -stroke "rgba(255,255,255,0.15)" -strokewidth 1 -draw "line 0,100 600,100 line 0,200 600,200 line 0,300 600,300 line 0,400 600,400" \) -geometry +50+0 -composite \
  -quality 92 variation-1-racing-velocity/images/banner.jpg
""", shell=True, check=True)

# Background 1: High altitude slope with dark navy atmosphere
subprocess.run("""
magick images/carv.jpg -resize 1920x1080^ -gravity center -extent 1920x1080 \
  -modulate 90,80,100 \
  \( -size 1920x1080 radial-gradient:"rgba(10,20,38,0.7)-rgba(6,12,24,0.92)" \) -composite \
  -quality 85 variation-1-racing-velocity/images/background.jpg
""", shell=True, check=True)

print("--- Generating Banner 2 & Background 2 (Atomic Pro B&W) ---")
# Banner 2: Cinematic monochrome of Philipp Papst carving with stark lighting and crimson accent
subprocess.run("""
magick assets_gen/philipp_carv.jpg -colorspace Gray -level 10%,90%,1.15 \
  -resize 1920x540^ -gravity center -extent 1920x540 \
  \( -size 1920x540 radial-gradient:"rgba(0,0,0,0)-rgba(0,0,0,0.7)" \) -composite \
  \( -size 1920x540 xc:none -stroke "#E11D48" -strokewidth 4 -draw "line 0,536 1920,536" -stroke "rgba(225,29,72,0.4)" -strokewidth 1 -draw "line 0,4 1920,4" \) -composite \
  -quality 92 variation-2-atomic-pro/images/banner.jpg
""", shell=True, check=True)

# Background 2: Atomic style B&W slope action
subprocess.run("""
magick images/carv.jpg -colorspace Gray -level 12%,88%,1.1 \
  -resize 1920x1080^ -gravity center -extent 1920x1080 \
  \( -size 1920x1080 radial-gradient:"rgba(0,0,0,0.5)-rgba(0,0,0,0.85)" \) -composite \
  -quality 85 variation-2-atomic-pro/images/background.jpg
""", shell=True, check=True)

print("--- Generating Banner 3 & Background 3 (Van Deer Minimalist) ---")
# Banner 3: Van deer mountain landscape on left + Philipp Papst on right with seamless soft fade
subprocess.run("""
magick vandeer_banner.jpg -resize 1920x540^ -gravity north -extent 1920x540 \
  \( assets_gen/philipp_carv.jpg -resize 1200x540^ -gravity center -extent 1200x540 \) -geometry +750+0 -composite \
  \( -size 500x540 gradient:"rgba(220,230,240,1)-rgba(220,230,240,0)" -blur 0x15 \) -geometry +700+0 -compose blend -define compose:args=70,30 -composite \
  -modulate 100,85,100 \
  \( -size 1920x540 xc:none -stroke "#1E293B" -strokewidth 1 -draw "line 0,0 1920,0 line 0,539 1920,539" \) -composite \
  -quality 92 variation-3-vandeer-minimal/images/banner.jpg
""", shell=True, check=True)

# Background 3: Clean, subtle warm alabaster alpine slope texture
subprocess.run("""
magick images/carv.jpg -resize 1920x1080^ -gravity center -extent 1920x1080 \
  -modulate 110,25,100 -blur 0x15 \
  \( -size 1920x1080 xc:"#F4F5F7" -alpha set -channel A -evaluate set 85% \) -composite \
  -quality 85 variation-3-vandeer-minimal/images/background.jpg
""", shell=True, check=True)

print("--- Generating Banner 4 & Background 4 (Glacier Freeride) ---")
# Banner 4: Freestyle Jumper on left (Ride on) + Philipp carving on right (Race on)
subprocess.run("""
magick assets_gen/jumper_square.jpg -resize 900x540^ -gravity center -extent 900x540 assets_gen/jump_side.jpg
magick -size 1920x540 xc:"#03458c" \
  assets_gen/jump_side.jpg -geometry +0+0 -composite \
  assets_gen/philipp_carv.jpg -geometry +720+0 -composite \
  \( -size 300x540 gradient:"rgba(3,69,140,1)-rgba(3,69,140,0)" \) -geometry +700+0 -composite \
  \( -size 1920x540 xc:none -stroke "#00A3E0" -strokewidth 3 -draw "line 0,537 1920,537" \) -composite \
  -modulate 105,120,100 \
  -quality 92 variation-4-glacier-freeride/images/banner.jpg
""", shell=True, check=True)

# Background 4: Aerial jump cornice with deep blue sky
subprocess.run("""
magick images/jump.jpg -resize 1920x1080^ -gravity center -extent 1920x1080 \
  -modulate 95,110,100 \
  \( -size 1920x1080 radial-gradient:"rgba(5,20,45,0.65)-rgba(2,10,25,0.88)" \) -composite \
  -quality 85 variation-4-glacier-freeride/images/background.jpg
""", shell=True, check=True)

print("--- Generating Banner 5 & Background 5 (Summit Heritage) ---")
# Banner 5: Sunset Alpenglow golden hour
subprocess.run("""
magick assets_gen/philipp_carv.jpg -resize 1920x540^ -gravity center -extent 1920x540 \
  \( -size 1920x540 gradient:"#f59e0b-#b91c1c" -alpha set -channel A -evaluate set 28% \) -compose screen -composite \
  \( -size 1920x540 radial-gradient:"rgba(0,0,0,0)-rgba(30,10,20,0.55)" \) -composite \
  \( -size 1920x540 xc:none -stroke "#F59E0B" -strokewidth 4 -draw "line 0,536 1920,536" \) -composite \
  -quality 92 variation-5-summit-heritage/images/banner.jpg
""", shell=True, check=True)

# Background 5: Warm sunset alpine mountain backdrop
subprocess.run("""
magick images/carv.jpg -resize 1920x1080^ -gravity center -extent 1920x1080 \
  \( -size 1920x1080 gradient:"#fbbf24-#7c2d12" -alpha set -channel A -evaluate set 55% \) -compose overlay -composite \
  \( -size 1920x1080 xc:"#0f172a" -alpha set -channel A -evaluate set 55% \) -composite \
  -quality 85 variation-5-summit-heritage/images/background.jpg
""", shell=True, check=True)

print("All banner and background images successfully rendered!")

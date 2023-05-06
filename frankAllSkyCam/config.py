########################################
# frankAllSkyCam
# configuration file -  config.txt
# 
# please adjust according to your needs
# see comments and documentation
########################################

[system]
# Images main directory - DO NOT CHANGE IT
otuputFolder= img

# Log directory - DO NOT CHANGE IT
logFolder = log

# SQM-LE logs - DO NOT CHANGE IT
sqmFolder = sqm

# web folder where to save the skycam.jpg
outputLocalWebFile = /var/www/html/img/skycam.jpg

#how many days you want to keep jpgs
days_retention = 3

#watchdog will reboot if after 15 minutes no <home_path>/<log_path>/alive.txt has been generated 
rebootAfter = 15

[site]
#the following label will be printed on the image
inte = www.astrobrallo.com
latitude = 44.73
longitude = 9.31
time_zone = Europe/Rome

[resolution]
# may use  1024 x 768
horiz = 800
vert = 600
picture_rotation = 0

[libcamera]
# may personalize the libcamara params. 
# please DO NOT set --shutter, --gain, --awbgains --immediate
additional_params = ""

[timelapse]
# if True, timelapse from sunset to sunrise will be generated  Otherwise, not.
nightTL = True

# if True, 24h timelapse from 9am to 9am next day will be generated. Otherwise, not. 
fullTL = True
nightOnly = True

# following parameters are used by ffmpeg
tl_horiz = 800
tl_vert = 600
framerate = 10
ffmpeg1 = -c:v libx264 -crf 12 -preset slow -pix_fmt yuv420p 
# additional ffmpeg parameters may be added by experts!
ffmpeg2 = 
ffmpeg3 = 
 
[font]
#when 1024x768 you can increase it
font_size = 18

[exposure]
#night exposure in seconds
# urban sky:
#esp_secs = 4
# dark sky (i found 55 secs ok for sqm 21,3).
# adjust according to your sky
esp_secs =60
# max exposure during dawn and dusk:
esp_dawn_dusk = 40 

[moon]
#exposure reduction because of the moon
full_moon_reduc = 0.75

# minutes after moonset
ms_offset = -30

# minutes from moonset-start to no-moon
ms_duration = 50      

# minutes *before* the moon rises
mr_offset = -30 

# minutes from moon-rise to moon fully up
mr_duration = 60


[offset]
# minutes to offset dawn and dusk for optimal exposure 
dawn = 0
dusk = 0

[ftp]
# if True, allSkyCam image, timelapse and startrails 
#will be uploaded on your FTP Server 
isFTP=True

# ftp parameters allSkyCam image will be uploaded on a 
FTP_server = myftpserver.com
FTP_login = myuser
FTP_pass = mypass
FTP_uploadFolder =/public/frankAllSkyCam/

# allskycam.jpg will be generated on the FTP server
FTP_filenameAllSkyImgJPG = allskycam 

# allskycam_night.mp4 will be generated if nightTL = True
# allskycam_24h.mp4 will be generated if fullTL = True
FTP_fileNameTimelapseMP4 = /videos/frankAllSkycam

# starTrail.jpg will be generated 
FTP_fileNameStarTrailJPG = /startrails/starTrail.jpg

[sqm_le]
# if you want to use SQM LE then use_sqm = y Otherwise, not.
use_sqm = n
ip_address = 192.168.2.59
port = 10001
write_log = y


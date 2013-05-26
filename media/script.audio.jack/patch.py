import xbmcaddon
import xbmcgui
import subprocess

addon = xbmcaddon.Addon(id='addon.jack.aux')
name = addon.getAddonInfo('name')

line_ins = (
  "firewire_pcm:000a9200d8040896_LineIn L_in",
	"firewire_pcm:000a9200d8040896_LineIn R_in",
)
main_outs = (
	"firewire_pcm:000a9200d8040896_MainOut 1L_out",
	"firewire_pcm:000a9200d8040896_MainOut 2R_out",
)

for input, output in zip(line_ins, main_outs):
	subprocess.Popen(['jack_connect', input, output])

xbmcgui.Dialog().ok(name, 'Firebox Line-in (3/4) patched to Main Outs (1/2)')

for input, output in zip(line_ins, main_outs):
	subprocess.Popen(['jack_disconnect', input, output])

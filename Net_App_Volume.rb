require 'erb'
require 'yaml'

tmp=[]
begin
  f = File.open 'NetAppVolume.txt'
  while line = f.gets
    tmp.push(line)
  end
ensure
  f.close
end
#puts tmp[0]
netapp_url = tmp[0]
CVOMountPt = tmp[1]


# Change below

template = ERB.new File.read 'Net_App_Volume.erb'

File.open('netapp-nfs-pv.yaml', 'w') do |f|
  f.write template.result(binding)
end
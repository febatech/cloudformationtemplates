require 'erb'
require 'yaml'

tmp=[]
begin
  f = File.open 'VPCNetAppOutput.txt'
  while line = f.gets
    tmp.push(line)
  end
ensure
  f.close
end
#puts tmp[0]
vpcid = tmp[0]
pubsubnet1a = tmp[1]
pubsubnet1b = tmp[2]
prisubnet1a = tmp[3]
prisubnet1b = tmp[4]
serverip = tmp[5]
serverpath = tmp[6]

template = ERB.new File.read 'managedcluster.yaml.erb'


File.open('managedcluster.yaml', 'w') do |f|
  f.write template.result(binding)
end

template = ERB.new File.read 'netapp-nfs-pv.yaml.erb'

File.open('netapp-nfs-pv.yaml', 'w') do |f|
  f.write template.result(binding)
end


redis-cli -p 6383 monitor | grep "live/diy" | tee redis.log

while true; do cp MPD /home/v2pc/MPD.`date +%s`; sleep 2; done;

watch -n  1 'grep "d=\"360360" -A 5 -B 5  MPD'

tail -f squid.log | sed 's/http\:\/\/10\.16\.205\.35\:80/wgethttp\:\/\/live\.pep1\.v2p-a\.edm-cloud\.tv/' | stdbuf -o0 awk -F" " '{print $7}' | grep ts | grep hgtvhd | grep "812300/"

tail -f ../squid.log | awk '{print $7}' | grep "hgtvhd-east" | grep "812300_"

MPDs cleanup:
[root@mce-1 MPDs]# ls /home/v2pc/MPDs | grep -v MPD-capture.sh | xargs rm

mce-mpe-captures-cleanup:
[root@mpe-1 capture1-03-18-2017]# ls /home/v2pc/capture1-03-18-2017 | grep -v mce-mpe-captures.sh | xargs rm    

salt command references:
========================

salt-key
salt '*w2*' test.ping
salt '*w2*' grains.get ipv4
salt '*w2*' grains.ls
salt '*w2*' grains.get ip4_interfaces
salt '*w2*' cmd.run 'rpm -qa|grep -i mce'
salt '*w2[5,7]' cmd.run 'rpm -qa|grep -i mce'
salt '*w2[5,7]*' cmd.run 'rpm -qa|grep -i mce'
salt '*w2[5,7]*' cmd.run 'supervisorctl status'



salt 'STG-MPE-91.node.region-0.v2pc-staging.staging.cdvr.nowonline.com.br' cmd.retcode "sudo systemctl daemon-reload"

[root@v2p-master-0 conf.d]# salt 'worker22*' cmd.run 'curl -k https://localhost:7001/v1/assetworkflows/live1/assets'                                             

[root@v2p-master-0 conf.d]# salt 'worker22*' cmd.run 'tail /var/log/opt/cisco/v2pc/errorlog/am-error*'

salt '*' cmd.exec_code python 'import sys; print sys.version'

[root@v2p-master-0 conf.d]# salt 'worker22*' cmd.run 'rpm -qa | grep v2p'


[root@v2p-master-0 conf.d]# salt 'worker22*' cmd.run 'iostat'

[root@v2p-master-0 conf.d]# salt 'worker22*' cmd.run 'df -kh'

[root@v2p-master-0 conf.d]# salt 'worker22*' grains.get oscodename

[root@v2p-master-0 conf.d]# salt 'w19*' cmd.run 'tail /var/log/opt/cisco/mos/cts/squid.log'


[root@v2p-master-0 conf.d]# salt 'w19*' cmd.run 'cat /var/log/opt/cisco/mos/cts/squid.log' >> test1




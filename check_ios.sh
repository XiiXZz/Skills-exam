now=$(date)
echo "$now"
echo ""
echo "Starting ios check"
input="/Devasc_Skills/Task 7/ios_configs/running_config_csr101.txt"
Line=14
hostname1=sed 4p $input
echo "$hostname1"

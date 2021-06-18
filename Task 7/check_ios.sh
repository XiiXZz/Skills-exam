now=$(date)
echo "$now"
echo ""
echo "Starting ios check"
sed -n 15p ios_configs/running_config_csr101.txt
sed -n 8p ios_configs/running_config_csr101.txt
str=$(sed -n 8p ios_configs/running_config_csr101.txt)
substr=$(echo $str| cut -b 14-16)
if [ "$subst" == "101" ]
	then
		echo ios needs upgrading
fi
if [ "$subst" == "111" ] 
then 
        echo "ios is up to date"
fi
echo ""
sed -n 15p ios_configs/running_config_csr111.txt
sed -n 8p ios_configs/running_config_csr111.txt
str=$(sed -n 8p ios_configs/running_config_csr111.txt)
substr=$(echo $str| cut -b 14-16)
if [ "$subst" == "101" ]; then
        echo ios needs upgrading
fi
if [ "$subst" == "111" ] 
then 
        echo "ios is up to date"
fi
echo ""
echo "ENDING IOS CHECK"

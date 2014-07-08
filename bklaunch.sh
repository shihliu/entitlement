if [ $# != 1 ] ; then
	echo "PARAMETER ERROR !!!"
	echo " USAGE: $0 job_xml"
	echo " e.g.: $0 virtwhobeaker_rhel_7_kvm_job_sample.xml"
	exit 1;
fi 

job_xml=$1
basedir=`pwd`
bkr job-submit $basedir/data/beakerjobs/$job_xml

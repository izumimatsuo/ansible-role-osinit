#!/bin/sh

CMDNAME=`basename $0`

while getopts rdce: OPT
do
  case $OPT in
    "r" ) OPT_r="TRUE" ;;
    "c" ) OPT_c="TRUE" ;;
    "e" ) VALUE_e="-e $OPTARG" ;;
    "d" ) docker rm -f localhost
          exit $? ;;
      * ) echo "Usage: $CMDNAME [-r]" 1>&2
          exit 1 ;;
  esac
done

if [ "$OPT_c" == "TRUE" ]; then
  docker-compose run runner bash -lc "cd /root/build/tests &&\
                                      ansible-playbook test.yml --syntax-check &&\
                                      ansible-playbook test.yml --skip-tags "skip" &&\
                                      ansible-playbook test.yml $VALUE_e --check"
else
  docker-compose run runner bash -lc "cd /root/build/tests &&\
                                      ansible-playbook test.yml --syntax-check &&\
                                      ansible-playbook test.yml $VALUE_e &&\
                                      py.test -v test.py --hosts="docker://localhost""
fi

if [ "$OPT_r" != "TRUE" ]; then
  docker rm -f localhost
fi

exit 0
